import time
from functools import cache


@cache
def process_input(n):
    time.sleep(2)
    return n ** 2


print(process_input(5))
print(process_input(5))
print(process_input(5))
print(process_input(5))
