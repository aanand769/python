import re

ERROR_PATTERNS = {
    "ERROR":r"\berror\b",
    "EXPECTATION":r"\b{exception|traceback}\b",
    "OOM":r"\b{outofmemory|oom|oomkilled}\b",
    "CRASH":r"\b{crash|crashed|crashloop}\b",
    "TIMEOUT":r"\b{timeout|timed out}\b",
    "CONNECTION":r"\b{connection refused|connection reset}\b",
    "FATAL":r"\bfatal\b"
}

def detect_error(message):
    message_lower = message.lower()

    for error_type, pattern in ERROR_PATTERNS.items():
        if re.search(pattern, message_lower):
            return error_type

    return None

