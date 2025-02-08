from functools import wraps
from time import perf_counter, sleep


def get_time(func):
    """times any functions"""

# wrap important for make behviour correct when checking class name and doc string
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time: float = perf_counter()
        func(*args, **kwargs)
        end_time: float = perf_counter()

        total_time: float = round(end_time-start_time, 3)
        print('Time:', total_time, 'seconds.')

    return wrapper


@get_time
def do_something(param):
    """Do something important"""
    sleep(1)
    print(param)


do_something('hello world')
