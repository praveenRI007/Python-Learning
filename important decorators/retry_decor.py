import random
import time


def retry(retries=3, exception=Exception,delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    attempts += 1
                    print(f"failed : {attempts}/{retries}")
                    time.sleep(delay)
            raise exception

        return wrapper

    return decorator


@retry(retries=5, exception=ValueError,delay=1)
def error_prone_function():
    if random.random() < 0.8:
        raise ValueError('Error !')
    else:
        print('Success!')


error_prone_function()
