# Pickling in Python(pickle Module)

# Pickling is a process in Python that allows you to serialize(convert to bytes) and deserialize(convert back to objects) Python objects. This is useful for saving and loading data efficiently.

#  Use Cases:

#     Saving machine learning models
#     Storing program state
#     Caching data for faster access

# exL01
# text: str = 'something'
# number: int = 10


# with open('08-file-management/pickling.txt', 'w') as file:
#     file.write(text + '\n')
#     file.write(str(number) + '\n')


import pickle


class Fruit:
    def __init__(self, name: str, calories: float) -> None:
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, ":", self.calories)


friut: Fruit = Fruit('banana', 10.5)

friut.calories = 150


with open('08-file-management/save.pickling.txt', 'wb') as file:
    pickle.dump(friut, file)


with open('08-file-management/save.pickling.txt', 'rb') as file:
    fruit1: Fruit = pickle.load(file)
    print(fruit1.calories)
    fruit1.describe_fruit()
