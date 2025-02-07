
# Reduce

# The built-in functools.reduce() function takes a function and a list of values, and applies the function to each value in the list, accumulating a single result as it goes

# import functools from the standard library
import functools

def add(sum_so_far, x):
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10


# Higher-order functions like map, filter, and reduce, allow us to avoid stateful iteration and mutations of variables.
def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

import functools

def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))


# In the functional example, we're just combining functions to get the result we want. There's no need to reassign variables or keep track of the program's state in a loop.

# A loop is inherently stateful. Depending on which iteration you're on, the i variable has a different value.
