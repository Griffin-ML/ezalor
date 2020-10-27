import time

MAX_RETRIES = 10


def retry(func, MAX_RETRIES):
    for i in range(max_tries):
        try:
            time.sleep(0.3)
            func()
            break
        except Exception:
            continue
