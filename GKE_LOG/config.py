import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv('GCP_PROJECT_ID')

CLUSTER_NAME = os.getenv('GKE_CLUSTER_NAME')
CLUSTER_LOCATION = os.getenv('GKE_CLUSTER_LOCATION')
NAMESPACE = os.getenv("GKE_NAMESPACE")

DEPLOYMENTS = [
    x.strip()
    for x in os.getenv('DEPLOYMENTS','').split(',')
    if x.strip()
]

LOOKBACK_MINUTES = int (
    os.getenv('LOG_LOOKBACK_MINUTES','60')
)

DATABASE = 'data/logs.db'