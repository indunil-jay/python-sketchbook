# A variable is a named storage location in memory that holds a value, which can change during the execution of a program. Variables are fundamental in programming because they allow developers to store, retrieve, and manipulate data dynamically.


# 1. String Type =>Strings are raw text in coding speak. They are called "strings" because they are a list of characters combined together. Strings are declared in Python by using single quotes or double quotes. That said, for consistency's sake, we prefer double quotes.
name_with_single_quotes = 'boot.dev'
name_with_double_quotes = "boot.dev"

# 2. Numeric Type => Numbers aren't surrounded by quotes when created, but they can have decimals and negative signs.
# integers
x = 5
y = -5

# floats
x = 5.2
y = -5.2

# 3. Boolean Type : A "Boolean" (or "bool") is a type that can only have one of two values: True or False. As you may have heard, computers really only use 1's and 0's. These 1's and 0's are just Boolean values.
is_tall = True
is_short = False


# F-STRING in python
# You can create a string with dynamic values by using f-strings in Python.
    # The opening quotes must be preceded by an f.
    # Any variables within curly brackets have their values "interpolated" (injected) into the string.


num_bananas  = 10
print(f"you have {num_bananas} banans.")


# 4. None Type : Not all variables have a value. We can declare an "empty" variable by setting it to None.

# what is None in python ?
# None is a special value in Python that represents the absence of a value or a null value. It is not the same as zero, False, or an empty string.

this_is_absence_or_null_varible = None

    # the None keyword is used to define an empty (or null value) variable or object.
    # In Python, the None keyword is an object and it is a data type of the class NoneType.

if num_bananas is None:
    print(this_is_absence_or_null_varible)

if num_bananas is not None:
    print(num_bananas)


# Remember, it's crucial to recognize that None is not the same as the string "None". They look the same when printed to the console, but they are different data types. If you use "None"
# instead of None, you will end up trying to debug code that looks right when it's printed but is failing the tests.



#type() is used for check variable type, it return the variable belong class

print(type(num_bananas))

#Dynamic Typing
#Python is dynamically typed. All this means is that a variable can store any type, and that type can change.

#For example, if I make a number variable, I can later change that variable to a string:
speed = 5
speed = "five"


# In almost all circumstances, it's a bad idea to change the type of a variable. The "proper" thing to do is to just create a new one.

# Math with String

# Most of the math operators we went over earlier don't work with strings, aside from the * and addition operators. When working with strings the + operator performs a "concatenation".
# "Concatenation" is a fancy word that means the joining of two strings. You should prefer string interpolation with f-strings over concatenation.

first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"


#Multi-Variable Declaration

sword_name, sword_damage, sword_length = "Excalibur", 10, 200

#above line same as this
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200






#NOTE:
"""
what is a variable ?
    ANS : In programming, a variable is a symbolic name associated with a value. This value can be modified and used during the execution of a program. The variable acts as a container that holds data, and you can perform operations on this data, such as mathematical calculations or logical comparisons


Naming variale in python rules:
    ANS : 1. Variable names can't have spaces, they're continuous strings of characters.
          2. In Python you should use "snake_case" when creating variable names with two words or more.


what is a comment in python?
    ANs : Comments don't run like code, they are ignored by the computer. Comments are useful for adding reminders or explaining what a piece of code does in plain English.

"""

# this is a single line comments

""" this is a
         mutltiline comments """
