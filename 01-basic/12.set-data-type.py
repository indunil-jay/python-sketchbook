### sets
# Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.
fruits = {'apple', 'banana', 'grape'}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

fruits = {'apple', 'banana', 'grape'}
fruits.add('pear')
print(fruits)
# Prints: {'banana', 'grape', 'pear', 'apple'}

#  Empty set

#Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.
fruits = set()
fruits.add('pear')
print(fruits)
# Prints: {'pear'}


# order is not guranteed
fruits = {'apple', 'banana', 'grape'}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple
