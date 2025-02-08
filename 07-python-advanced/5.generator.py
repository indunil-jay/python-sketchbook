# A generator in Python is a special type of iterator that allows you to iterate over data lazily (i.e., one item at a time) without storing everything in memory. This makes them memory-efficient and useful for handling large datasets.

def generate_list(n: int):
    for i in range(n):
        yield i


generator = generate_list(10)
print(next(generator))


yield_comprehension = (i for i in range(10**10))

print(next(yield_comprehension))
print(next(yield_comprehension))
print(next(yield_comprehension))
print(next(yield_comprehension))
