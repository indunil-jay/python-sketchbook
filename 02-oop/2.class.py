#Classes
   #  A class is a special type of value in an object-oriented programming language like Python.
   # It's similar to a dictionary in that it usually stores other types inside itself.

# class Soldier:
#     health=5
#     armor=5
#     damage=2

# Just like a string, integer or float, a class is a type, but instead of being a built-in type, your classes are custom types that you define.
# An object is just an instance of a class type.

# mark  = Soldier()
# print(mark.damage)

# Method
# One thing that makes classes cool is that we can define methods on them. A method is a function that's tied directly to a class and has access to all its properties.

class Soldier:
    health=5

    def take_damage(self, damage):
        self.health -=damage


soldierOne = Soldier()
soldierOne.take_damage(3)
print(soldierOne.health)


#self In Python, self is a convention used inside class methods to refer to the instance of the class itself. It allows access to instance attributes and methods within the class.

# Methods are nested within the class declaration. Their first parameter is always the instance of the class that the method is being called on.
# By convention, it's called "self". Because self is a reference to the object, you can use it to read and update the properties of the object.

# Methods return values

# If a normal function doesn't return anything, it's typically not a very useful function. In contrast,
# methods often don't return anything explicitly because they can mutate the properties of the object instead

class Soldier2:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier2()
print(soldier_one.get_speed())
# prints "6"

# Methods vs Functions

# You know what a function is. A method has all the same properties as a function, but it is tied directly to a class and has access to all its properties.
# A method automatically receives the object it was called on as its first parameter

class Soldier3:
    health = 5

    def take_damage(self, damage, multiplier):
        damage = damage * multiplier
        self.health -= damage

dalinar = Soldier3()
damage, multiplier = 30, 3

# Only "damage" and "multiplier" are passed as arguments
# "dalinar" is passed implicitly as the first argument, "self"
dalinar.take_damage(damage, multiplier)

# A method can operate on data that is contained within the class. In other words, you won't always see all
#  the "outputs" in the return statement because the method might just mutate the object's properties directly



# The OOP debate

# Because functions are more explicit, some developers argue that functional programming is better than object-oriented programming.
# In reality, neither paradigm is "better", and the best developers learn and understand both styles and use them as they see fit.

# For example, while methods are more implicit and often make code more difficult to read,
# they also make it easier to group a program's data and behavior in one place, which can lead to a more organized codebase.
