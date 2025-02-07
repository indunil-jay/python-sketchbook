# Encapsulation
# Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.

# The most basic example of encapsulation is a function.
# The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.

# acceleration = calc_acceleration(initial_speed, final_speed, time)

# To use the calc_acceleration function, we don't need to think about every individual line of code inside the function. We just need to know that if we give it the inputs:

#     initial_speed
#     final_speed
#     time

# Then it will give us the correct acceleration as an output.


# public and private
# By default, all properties and methods in a class are public. That means that you can access them with the . operator:

# Private data members are how we encapsulate logic and data within a class.
# To make a property or method private, you just need to prefix it with two underscores.

class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor   #private property or variable
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
# print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30


# Encapsulation is the practice of hiding code complexity inside a "black box" so that other developers working with the code don't have to worry about it.
# To be clear, it does not make the code more secure in a cryptographic or cyber-security sense. That's a point I was personally confused about when I was first learning about private and public class members.
# Encapsulation is about organization, not security.
# Encapsulation is like folders in an unlocked filing cabinet. They don't stop someone from peeking inside, but they do keep everything tidy and easy to find.


# Python is a dynamic language, and that makes it difficult for the interpreter to enforce some of the safeguards that languages like Go do.
#  That's why encapsulation in Python is achieved mostly by convention rather than by force

# Prefixing methods and properties with a double underscore is a strong suggestion to the users of your class that they shouldn't be touching that stuff.
#  If a developer wants to break convention, there are ways to get around the double underscore rule.
