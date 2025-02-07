#  In Python, if you name a method __init__, that's the constructor and it is called when a new object is created.

class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier("Legolas", 5, 10)
print(soldier.name)
# prints "Legolas"
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"

# In object-oriented programming, an instance is a concrete occurrence of any object...
# "Instance" is synonymous with "object" as they are each a particular value...
# "Instance" emphasizes the distinct identity of the object. The creation of an instance is called instantiation.



# Class variables vs instance variables

# So far we've worked with both class variables and instance variables, but we haven't talked about the difference.

# Instance variables vary from object to object and are declared in the constructor
# Class variables remain the same between instances of the same class and are declared at the top level of a class definition.
