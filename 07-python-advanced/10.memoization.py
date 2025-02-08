from functools import wraps, cache
from textwrap import wrap
from time import perf_counter
import sys


def memoize(func):
    cache: dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key: str = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper


@cache
# @memoize
def fibonacci(n: int) -> int:
    if (n < 2):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


start: float = perf_counter()
f: int = fibonacci(30)
end: float = perf_counter()

print(f)
print(f"Time : {end - start} seconds")
