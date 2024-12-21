import time


def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print('Time Taken: ', f"{end - start:.4f}")
        return result

    return wrapper


@time_logger
def process_input(n):
    time.sleep(2)
    return n ** 2


print(process_input(5))
