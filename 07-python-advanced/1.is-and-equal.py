class Fruit:
    def __init__(self, name: str, calories: float) -> None:
        self.name = name
        self.calories = calories

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__


fruit_a = Fruit('Banana', 10)
fruit_b = Fruit('Banana', 10)

print(f"a: {id(fruit_a)}, b: {id(fruit_b)}")

print(f"fruit a is fruit b={fruit_a is fruit_b}")
# False beacuse there are not same object

print(f"fruit a = fruit b={fruit_a == fruit_b}")
# True beacuse  objects are same


##########################################

a = 10
b = 10


print(f"a: {id(a)}, b: {id(b)}")

print(f"a is b={a is b}")
# True

print(f"a = b {a == b}")
# True


##########################################
_ = 10
x = _ + 5
z = 15


print(f"x: {id(x)}, z: {id(z)}")

print(f"x is z={x is z}")
# True

print(f"x = z {z == x}")
# True


# == (Equality Operator)

# Checks value equality.
# Returns True if the values of the two objects are the same.
# Does not check whether the objects are the same in memory.

# is (Identity Operator)

# Checks object identity.
# Returns True if both variables reference the same object in memory.
# Even if two objects have the same value, is will return False if they are stored in different memory locations.
