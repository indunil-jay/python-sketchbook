# Inheritance

# We've made it to the holy grail of object-oriented programming: inheritance.
# Non-OOP languages like Go and Rust allow for encapsulation and abstraction features as nearly every language does.
# Inheritance, on the other hand, tends to be unique to class-based languages like Python, Java, and Ruby.


#  What is inheritance?
# Inheritance allows one class, the "child" class, to inherit the properties and methods of another class, the "parent" class.

# This powerful language feature helps us avoid writing a lot of the same code twice. It allows us to DRY (don't repeat yourself) up our code.\

class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

class Cow(Animal):
    def __init__(self):
        # call the parent constructor to
        # give the cow some legs
        super().__init__(4)


# When should I use inheritance?

# Inheritance is a powerful tool, but it is a really bad idea to try to overuse it.
# Inheritance should only be used when all instances of a child class are also instances of the parent class.

# When a child class inherits from a parent, it inherits everything. If you only want to share some functionality,
# inheritance is probably not the best answer. Better to simply share some functions, or maybe make a new parent class that both classes can inherit from.




# Inheritance Hierarchy

# There is no limit to how deeply we can nest an inheritance tree. For example, a Cat can inherit from an Animal that inherits from LivingThing. That said, be careful! New programmers often get carried away.
# You should never think to yourself:
#     "Well most wizards are elves... so I'll just have wizard inherit from elf"
# A good child class is a strict subset of its parent class.

class Wall:
    def __init__(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

class Castle(Wall):
    def __init__(self, height, towers):
        super().__init__(height)
        self.towers = towers

    def get_tower_height(self):
        return self.get_height() * 2


#Example:02

class RealEstate:
    def __init__(self, location):
        self.__location = location


class Residential(RealEstate):
    def __init__(self, location, bedrooms):
        super().__init__(location)
        self.__bedrooms = bedrooms


class House(Residential):
    def __init__(self, location, bedrooms, yard_size):
        super().__init__(location, bedrooms)
        self.__yard_size = yard_size


# Multiple children
# So far we've worked with linear class inheritance, but usually, inheritance hierarchies form trees, not lines. A parent class can have multiple children.

'''

character
├── elf
│   ├── noldor
│   │__ sindar
│__ human
|   |__ humenorean
|   |__ Gondorian
|__ Dwarf
'''



# Why are inheritance trees often wide instead of deep?

# As we talked about earlier, in good software a child class is a strict subset of its parent class.
# In a deep tree, that means the children need to be perfect members of all the parent class "types".
# That simply doesn't happen very often in the real world. It's much more likely that
# you'll have a base class that simply has many sibling classes that are slightly different variations of the base.


# Method Overloading (Polymorphism at Compile Time)

# Method overloading in Python allows a class to define multiple methods with the same name but with different arguments.
# However, Python does not support traditional method overloading as seen in languages like Java or C++. Instead, you can achieve similar functionality by:

#     Using default arguments in a method.
#     Checking the number or type of arguments inside the method.

# Example:

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))          # Output: 5
print(calc.add(5, 10))      # Output: 15
print(calc.add(5, 10, 15))  # Output: 30

# Here, add works with different numbers of arguments by using default values. Python doesn’t create separate methods based on argument numbers; instead, the logic is handled inside the method.
# Method Overriding (Polymorphism at Runtime)

# Method overriding occurs when a subclass defines a method that already exists in its superclass.
# The subclass's method overrides the behavior of the superclass's method when called on an instance of the subclass.
# Example:

class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    def greet(self):
        return "Hello from Child!"

# Demonstration
p = Parent()
c = Child()

print(p.greet())  # Output: Hello from Parent!
print(c.greet())  # Output: Hello from Child!

# When greet is called on the Child instance, the method defined in Child overrides the one in Parent.
