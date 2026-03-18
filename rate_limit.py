import time
from fastapi import HTTPException

request_log = {}

LIMIT = 5
WINDOW = 600  # seconds

def check_rate_limit(user: str):
    now = time.time()

    if user not in request_log:
        request_log[user] = []

    # remove old requests (older than 600 sec)
    request_log[user] = [
        t for t in request_log[user] if now - t < WINDOW
    ]

    if len(request_log[user]) >= LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later."
        )

    request_log[user].append(now)