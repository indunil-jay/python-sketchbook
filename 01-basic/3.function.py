# Functions allows  us to reuse and organize code.
# functiions are th building blocks when making real world applications
# when passing argument to a function,the value is only pass and then assign that value whatever variable name inside the function call (signature, if there is multiple it assigned by pass order.)

def area_of_circle(radius):
    pi = 3.14
    area  = pi * radius * radius
    return area


print("circle area is: ",area_of_circle(5))



# multiple parameters
def subtract (a,b):
    return a-b

print("subtract result is: ",subtract(10,3))

#we can have any number of arguments
"""
print() vs return

print():

    A function that prints a value to the console.
    It does NOT return a value.

return:

    A keyword that ends the function execution.
    It gives the specified value back to the caller of the function.
    It does NOT print anything to the console
"""

# You've probably noticed that a variable needs to be declared before it's used

#not working like this
# print(my_name)
# my_name = 'Lane Wagner'

# #it should like below
# my_name = 'Lane Wagner'
# print(my_name)

#NOTE;
# Lines of code execute in order from top to bottom, so a variable needs to be created before it can be used.
# That means that if you define a function, you can not call that function until after the definition.

# All functions must be defined before they're used.

# Most Python developers solve this problem by defining all the functions in their program first, then finally calling the
#  "entry point" function last. Conventionally this "entry point" function is usually called main to keep things simple and consistent

def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# call entrypoint last
main()


# NONE RETURNS
# When no return value is specified in a function, it will automatically return None.
# For example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value. The following code snippets all return the same value, None:

def my_func():
    print("I do nothing")
    return None

def my_func():
    print("I do nothing")
    return

def my_func():
    print("I do nothing")


# multiple returns
# in python has this cool feature.A function can return more than one value by separating them with commas.
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # Return two values

#receiving multiple values
# When calling a function that returns multiple values, you can assign them to multiple variables.
dmg, mana = cast_iceblast(5, 100)
print(f"Damage: {dmg}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90

# When cast_iceblast is called, it returns two values. The first value is assigned to dmg, and the second value is assigned to mana.
# This happens because that's the order they were returned in, not because of their variable names.


#Parameters vs arguments

# Parameters are the names used for inputs when defining a function. Arguments are the values of the inputs supplied when a function is called.
# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)


#default value for function arguments
# Python has a way to specify a default value for function arguments. This can be convenient if a function has arguments that are essentially "optional",
#  and you as the function creator want to use a specific default value in case the caller doesn't provide one.

def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)

get_greeting("lane@example.com", "Lane")
# Hello Lane welcome! You've registered your email: lane@example.com

get_greeting("lane@example.com")
# Hello there welcome! You've registered your email: lane@example.com

# If the second parameter is omitted, the default "there" value will be used in its place.
#  As you may have guessed, for this structure to work, optional arguments that have defaults specified come after all the required arguments
