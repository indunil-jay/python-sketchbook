# tuples
# Tuples are collections of data that are ordered and unchangeable. You can think of a tuple as a List with a fixed size. Tuples are created with round brackets:

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True


# works as lists
# len()
# my_tuple[start:end:step] (slicient)


# not works
# my_tuple.append("new")
# my_tuple.pop(1)
# del my_tuple[1]

# Because Tuples hold their data, multiple tuples can be stored within a list. Similar to storing other data in lists, each tuple within the list is separated by a comma.
#  When accessing a list of tuples, the first index selects which tuple you want to access, the second selects a value within that tuple.

my_tuples = [("this is the first tuple in the list", 45, True),("this is the second tuple in the list", 21, False)]
print(my_tuples[0][0]) # this is the first tuple in the list
print(my_tuples[0][1]) # 45
print(my_tuples[1][0]) # this is the second tuple in the list
print(my_tuples[1][2]) # False4


# tuple unpacking
dog = ("Fido", 4)
dog_name, dog_age = dog
print(dog_name)
# Fido
print(dog_age)
# 4

# When you return multiple values from a function, you're actually returning a tuple.

#list unpacking is also very similar
a  = [23, 56]
b,c = a
print(b)
print(c)


#reverse a list we can use for loop or  list slicing
string = "hello world"
for character in string:
    pass
    # process individual characters here


def double_string(sentence):
    # Use a list comprehension to double each character and then join them back into a string
    return ''.join([char * 2 for char in sentence])

# Test the function
sentence = "LF3M BRD full clear"
print(double_string(sentence))  # Output: "LLFF33MM  BBRRDD  ffuullll  cclleeaarr"
