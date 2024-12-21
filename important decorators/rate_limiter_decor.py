import random
import time


def rate_limiter(calls, period):
    def decorator(func):
        last_calls = []

        def wrapper(*args, **kwargs):
            nonlocal last_calls

            now = time.time()

            last_calls = [call_time for call_time in last_calls if now - call_time < period]

            if len(last_calls) > calls:
                raise RuntimeError("Rate limit exceeded . Try again later !")

            last_calls.append(now)

            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limiter(calls=2,period=5)
def fetch_data():
    print("Fetching data ... ")
    time.sleep(1)
    print("Received data ... ")


fetch_data()
fetch_data()
fetch_data()
fetch_data()
fetch_data()
fetch_data()
fetch_data()
fetch_data()