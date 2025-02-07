# Intersect

# The .intersection() method calculates the intersection of two sets
# The intersection of two sets is a new set that contains all of the elements that are in both original sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.intersection(b)
print(c)
# {3, 4}


# Zip

# The zip function takes two iterables (in this case lists), and returns a new iterable where each element is a tuple containing one element from each of the original iterables.
a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
