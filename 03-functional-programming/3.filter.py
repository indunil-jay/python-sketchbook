#Filter

# The built-in filter function takes a function and an iterable (in this case a list) and returns a new iterable that only contains elements
#  from the original iterable where the result of the function on that item returned True.

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
