people = ('mario', 'lugi', 'toad')
numbers = (10, 20, 30)


zipped = zip(people, numbers)

print(zipped)
print(tuple(zipped))


# both tupples must be equal and it created a nested tuple structure,
# if there is exceeding one it will automatically discarded

# then error throws
zipped = zip(people, numbers, strict=True)


# you can add as many tuples as needed
