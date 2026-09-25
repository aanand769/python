from google.cloud import logging
from datetime import datetime, timedelta, timezone

from config import PROJECT_ID, DEPLOYMENTS,LOOKBACK_MINUTES
from analyzer import detect_error
from database import insert_log

client = logging.Client(project=PROJECT_ID)

def get_message(entry):
    payload = entry.payload

    if isinstance(payload, dict):
        if "message" in payload:
            return str(payload["message"])
        return str(payload)
    return str(payload)

def extract_kubernetes_data(entry):
    resource = entry.resource
    labels = resource.labels

    namespace = labels.get(
        "namespace_name",
        "unknown"
    )

    pod = labels.get(
        "pod_name",
        "unknown"
    )

    return namespace, pod

def collect_logs():

    start_time = (
        datetime.now(timezone.utc)
        - timedelta(minutes=LOOKBACK_MINUTES)
    )

    timestamp = start_time.strftime(
        "%Y-%M-%DT%H:%M:%SZ"
    )

    filter_string = f'''
        resource.type="k8s_container"
        timestamp >= "{timestamp}"
        '''

    print("Collecting logs... .. .")

    entries = client.list_entries(
        filter_=filter_string,
        page_size=1000
    )

    count = 0

    for entry in entries:
        message = get_message(entry)
        namespace, pod= extract_kubernetes_data(entry)
        deployment = find_deployment(pod)

        if deployment is None:
            continue

        error_type = detect_error(message)

        if error_type is None:
            continue

        insert_log(
            timestamp=str(entry.timestamp),
            deployment=deployment,
            pod=pod,
            namespace=namespace,
            severity=str(entry.severity),
            message=message,
            error_type=error_type
        )

        count += 1

    print(
        f"Collected {count} error logs"
    )

def find_deployment(pod):
    for deployment in DEPLOYMENTS:
        if pod.startswith(deployment + "-"):
            return deployment

    return None

if __name__=="__main__":

    collect_logs()