import time
import timeit

# start_time: float = time.perf_counter()

# for i in range(10**9):
#     pass


# print('hello')

# end_time: float = time.process_time()

# print('total-time', end_time - start_time, 'seconds')

def make_calculation(a: int, b: int):
    for i in range(10 ** 3):
        pass

    return a+b


def do_something():
    for i in range(10):
        x: int = i ** i


def get_time(func: str, repeat: int, number: int) -> float:
    speed: float = min(timeit.repeat(func, repeat=repeat,
                       number=number, globals=globals()))
    print(f'{func}-> {round(speed, 4)} sec (ran {repeat * number:,} times)')
    return speed


a, b = 1, 2
get_time('do_something()', repeat=10, number=10**5)
get_time('make_calculation(a,b)', repeat=10, number=10**5)
