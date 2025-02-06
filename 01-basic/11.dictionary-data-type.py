# Dictionaries

# Dictionaries in Python are used to store data values in key -> value pairs. Dictionaries are a great way to store groups of information.

# use curly braces
# add key-value pairs
car = {
  "brand": "Tesla",
  "model": "3",
  "year": 2019
}

# Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. If you try to use the same key twice, the first value will simply be overwritten.

#########Accessing Dictionary Values ###############

# Dictionary elements must be accessible somehow in code, otherwise they wouldn't be very useful.
# A value is retrieved from a dictionary by specifying its corresponding key in square brackets. The square brackets look similar to indexing into a list.

car["model"]

names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_list = name.split() #  "jack bronson" => ["jack","bronson"]

    # here we update the dictionary
    names_dict[name_list[0]] = name_list[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}

# mutating object dictionaries

car["year"] = 2025

print(car)

#  Deleting Dictionary

Valuesnames_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["joe"]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

# Notice that if you try to delete a key that doesn't exist, you'll get an error.

names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["unknown"]
# ERROR HERE, key doesn't exist

# Checking for existence

cars = {
    "ford": "f150",
    "tesla": "3"
}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False


# Iterating over a dictionary in Python

# We can iterate over a dictionary's keys using the same no-index syntax we used to iterate over the values in a list.
# With access to the dictionary's keys, we also have access to their corresponding values.

fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny

# Ordered or Unordered?

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries were unordered.

# Because dictionaries are ordered, the items have a defined order, and that order will not change.

# Unordered means that the items do not have a defined order, so you couldn't refer to an item by using an index.

# The takeaway is that if you're on Python 3.7 or later, you'll be able to iterate over dictionaries in the same order every time



progress = {
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        }
    }
}

for quest_name, quest_data in progress["entity"]['character']["quests"]:
    status = quest_data["status"]
    print(f"key {quest_name}: status {status}")


# Loop through each quest in the 'quests' dictionary using the keys
for quest_name in progress["entity"]['character']["quests"]:
    status = progress["entity"]['character']["quests"][quest_name]["status"]
    print(status)
