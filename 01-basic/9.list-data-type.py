## list #######
# A natural way to organize and store data is in a List. Some languages call them "arrays", but in Python we just call them lists.
inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]


# we can use multiple line for create one list for better readability.
flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum"
]

player_ages = [
    23,
    18,
    31,
    42
]

#Lists can contain items of any data type, in our example above we have a List of strings.

# index
# Each item in a list has an index that refers to its spot in the list.
names = ["Bob", "Lane", "Alice", "Breanna"]
# index 0 = "bob"


########### access specific item in a list. ###################  list[position]
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
# print(best_languages[1])
# prints "Go", because index 1 was provided

###########  len() ###################
fruits = ["apple", "banana", "pear"]
length = len(fruits)
# print(length)

###########  list item mutate ###################
inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Iron Ore', 'Healing Potion']

###########  append() - add element to end of list ###################
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']

###########  pop() - remove element from end of list ###################
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'

#NOTE While .pop() typically removes the last item of a list, it can also be used to remove an item at a specific index. For example,
# vegetables.pop(1) would remove 'cabbage' from the list. This can be useful when you need to remove items from other positions in your list.


########### iterate items in a list ###################
sports = ['cricket',"score","tennis","rugby"]

for index in range(0,len(sports)):
    #  print(sports[index])
    pass

# other elegent way that provides by python
for sport in sports :
    #  print(sport)
    pass


#  Infinity

# The built-in float() function can create a numeric floating point value of negative infinity.
# Because every value will be greater than negative infinity, we can use it to help us accomplish our goal of finding the max value
negative_infinity = float("-inf")
positive_infinity = float("inf")

######## modulo operator % ##############
# the modulo operator can be used to find a remainder

remainder = 8 % 3
# remainder = 2



########### slicing list   ###################
# Python makes it easy to slice and dice lists to work only with the section you care about. One way to do this is to use the simple slicing operator, which is just a colon :.
# my_list[ start : stop : step ]

my_list  = [0,1,2,3,4,5,6,7,8,9]

list1 = my_list[1:5:2]
# print("list-1",list1)   #list-1 [1, 3]
# print("list-2",my_list[1:]) #list-2 [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("list-3",my_list[: : 2]) #list-3 [0, 2, 4, 6, 8]
# print("list-4",my_list[:5]) #list-4 [0, 1, 2, 3, 4]
# print("list-5",my_list[-2:]) #list-5 [8, 9]
# print("list-6",my_list[:-2]) #list-5 [0, 1, 2, 3, 4, 5, 6, 7]

# concatenated lists
first =[1,3,4]
two =[2,4,6]
# print("concatated_list",first+two) #concatated_list [1, 3, 4, 2, 4, 6]

# check item in a list "in"
fruits = ["apple", "orange", "banana"]
#print("banana" in fruits)# Prints: True

# delete items from a list
nums  =[0,1,2,3,4,5,6,7]
# nums.pop(3)
# print(nums)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []


# Feature	             del	                                  pop()
# Works on	            Lists, dictionaries, variables	          Lists, dictionaries
# Returns value?	    ❌ No (only deletes)	                    ✅ Yes (returns the removed value)
# Usage on lists	    Deletes by index or slice	              Removes by index (default last)
# Usage on dicts	     Deletes by key	                           Removes by key and returns value
# Deletes entire variable?	✅ Yes	                             ❌ No
