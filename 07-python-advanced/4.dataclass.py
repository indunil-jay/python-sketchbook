from dataclasses import asdict
from dataclasses import dataclass, field
from dataclasses import dataclass


class Fruit:
    def __init__(self, name: str, calories: float) -> None:
        self.name = name
        self.calories = calories

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__


apple1 = Fruit('apple', 10)
apple2 = Fruit('apple', 10)


print(apple1 == apple2)


# A dataclass in Python is a decorator (@dataclass) introduced in Python 3.7 to simplify the creation of classes that store data. It automatically generates methods like __init__, __repr__, and __eq__ so you don't have to write them manually.

@dataclass
class Fruit2:
    name: str
    calories: float


apple3 = Fruit2('apple', 10)
apple4 = Fruit2('apple', 10)
print(apple3 == apple4)

# Make a dataclass read-only(immutable):


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(1, 2)
p.x = 5  # ❌ Error: Cannot assign to field 'x'


# Use field() to:

#     Exclude attributes from __init__
#     Define default values dynamically
#     Make attributes private

@dataclass
class User:
    username: str
    password: str = field(repr=False)  # Excludes `password` from `repr`
    age: int = field(default=18)


user = User("john_doe", "secret123")
print(user)  # User(username='john_doe', age=18)


# You can still define methods inside a dataclass:

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height


rect = Rectangle(10, 5)
print(rect.area())  # 50

# You can easily convert a dataclass to a dictionary:

p = Person("Charlie", 30)
print(asdict(p))  # {'name': 'Charlie', 'age': 30}

# You can reconstruct an object from a dictionary using ** kwargs:
data = {'name': 'Emma', 'age': 22}
p = Person(**data)
print(p)  # Person(name='Emma', age=22)
