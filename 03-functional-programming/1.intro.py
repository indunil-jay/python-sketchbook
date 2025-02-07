#  What is Functional Programming?

# Functional programming is a style (or "paradigm" if you're pretentious) of programming where we compose functions instead of mutating state (updating the value of variables).

#     Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
#     Imperative (or procedural) programming declares both the what and the how

# Example of imperative code:

# car = create_car()
# car.add_gas(10)
# car.clean_windows()

# Example of functional code:

# return clean_windows(add_gas(create_car()))
# The important distinction is that in the functional example, we never change the value of the car variable,
#  we just compose functions that return new values, with the outermost function, clean_windows in this case, returning the final result.

################################################################################

# Why Python?

# Frankly, Python is not the best language for functional programming. Reasons include:

#     No static typing.
#     Everything is mutable.
#     No tail call optimization.
#     Side effects are common.
#     Imperative and OOP styles abound in popular libraries.
#     Purity is not enforced (and sometimes not even encouraged).
#     Sum Types are hard to define.
#     Pattern matching is weak at best.

# So seriously, why are we using Python? One reason trumps all others: you already know Python. Python is a great choice for learning coding basics, OOP, Algorithms, and Data Structures, and the tradeoff of learning a new language at this point in the curriculum isn't worth it.

# We can still cover the most important concepts of functional programming in Python, even if we have to jump through a hoop or two to do it. Functional programming is a paradigm of useful techniques for writing better code, and they apply to all languages, not just purely functional ones.

# Note: We also plan to release a "Functional Programming 2" course in a more functional language. Likely one of these:


################################################################################


# Immutability

# In FP, we strive to make data immutable. Once a value is created, it cannot be changed. Mutable data, on the other hand, can be changed after it's created.
# Who cares?

# Immutable data is easier to think about and work with. When 10 different functions have access to the same variable, and you're debugging a problem with that variable, you have to consider the possibility that any of those functions could have changed the value.

# When a variable is immutable, you can be sure that it hasn't changed since it was created. It's a helluva lot easier to work with.

# Generally speaking, immutability means fewer bugs and more maintainable code

################################################################################

#  Tuples vs Lists

# Tuples and lists are both ordered collections of values, but tuples are immutable and lists are mutable.

# You can append to a list, but you can not append to a tuple. You can create a new copy of a tuple using values from an existing tuple, but you can't change the existing tuple.
# Lists are mutable

ages = [16, 21, 30]
# 'ages' is being changed in place
ages.append(80)
# [16, 21, 30, 80]

# Tuples are immutable

ages = (16, 21, 30)
more_ages = (80,) # note the comma! It's required for a single-element tuple
# 'all_ages' is a brand new tuple
all_ages = ages + more_ages
# (16, 21, 30, 80)


# Declarative Programming
# Functional programming aims to be declarative. We prefer to declare what we want the computer to do, rather than muck around with the details of how to do it.

# Let's take an extreme example and pretend we wanted to style a webpage with CSS (Obviously a hypothetical because, well, why would anyone want to work on the frontend???)
# Declarative styling

# The following CSS changes all button elements to have red text:

# button {
#     color: red;
# }

# It does not execute line-by-line like an imperative language.0Instead, it simply declares the desired style, and it's up to a web browser to figure out how to apply and display it.
# Imperative styling

# Unlike functional programming (and CSS), a lot of code is imperative. We write out the exact step-by-step implementation details. This Python script draws a red button on a
# screen using the Tkinter library:

# from tkinter import * # first, import the library
# master = Tk() # create a window
# master.geometry("200x100") # set the window size
# button = Button(master, text="Submit", fg="red").pack() # create a button
# master.mainloop() # start the event loop



# It's Math

# Functional programming tends to be popular amongst developers with a strong mathematical background. After all, a math equation isn't procedural: it's declarative. Take the following math equation:

# avg = Σx/N

# To put this calculation in plain English:

#     Σ is just the Greek letter Sigma, and it represents "the sum of a collection".
#     x is the collection of numbers we're averaging.
#     N is the number of elements in the collection.
#     avg is equal to the sum of all the numbers in collection "x" divided by the number of elements in collection "x".

# So, the equation really just says that avg is the average of all the numbers in collection "x". This math equation is
# a declarative way of writing "calculate the average of a list of numbers". Here's some imperative Python code that does the same thing:

def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

# However, with functional programming, we would write code that's a bit more declarative:

def get_average(nums):
    return sum(nums) / len(nums)

# Here we're not keeping track of state (the total variable in the first example is "stateful"). We're simply composing functions together to get the result we want


# Classes vs Functions

# I run into new developers who, after learning about classes, want to use them everywhere. They assume that because they learned about functions first, functions are somehow inferior.

# Nope. They're just different.
# Should I use functions or classes?

# Here's my rule of thumb:

# If you're unsure, default to functions. I find myself reaching for classes when I need something long-lived and stateful that would be easier to model if I could share behavior and data structure via inheritance. This is often the case for:

#     Video games
#     Simulations
#     GUIs

# The difference is:

#     Classes encourage you to think about the world as a hierarchical collection of objects. Objects bundle behavior, data, and state together in a way that draws boundaries between instances of things, like chess pieces on a board.

#     Functions encourage you to think about the world as a series of data transformations. Functions take data as input and return a transformed output. For example, a function might take the entire state of a chess board and a move as inputs, and return the new state of the board as output.

# Use what feels right to you in your projects, and adjust and refactor as you improve your skills.




# Debugging FP

# It's nearly impossible, even for tenured senior developers, to write perfect code the first time. That's why debugging is such an important skill. The trouble is, sometimes you have these "elegant" (sarcasm intended) one-liners that are tricky to debug:

# def get_player_position(position, velocity, friction, gravity):
#     return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)

# If the output of get_player_position is incorrect, it's hard to know what's going on inside that black box. Break it up! Then you can inspect the moved, slowed, and final variables more easily:

# def get_player_position(position, velocity, friction, gravity):
#     moved = calc_move(position, velocity)
#     slowed = calc_friction(moved, friction)
#     final = calc_gravity(slowed, gravity)
#     print("Given:")
#     print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
#     print("Results:")
#     print(f"moved: {moved}, slowed: {slowed}, final: {final}")
#     return final

# Once you've run it, found the issue, and solved it, you can remove the print statements.


# Functional vs OOP

# Functional programming and object-oriented programming are styles for writing code. One isn't inherently superior to the other,
#    but to be a well-rounded developer you should understand both well and use ideas from each when appropriate.

# You'll encounter developers who love functional programming and others who love object-oriented programming. However,
# contrary to popular opinion, FP and OOP are not always at odds with one another. They aren't opposites.
# Of the four pillars of OOP, inheritance is the only one that doesn't fit with functional programming.


# Inheritance isn't seen in functional code due to the mutable classes that come along with it. Encapsulation,
# polymorphism and abstraction are still used all the time in functional programming.

# When working in a language that supports ideas from both FP and OOP (like Python, JavaScript, or Go) the
# best developers are the ones who can use the best ideas from both paradigms effectively and appropriately.



# Functions as Values
# In Python, functions are just values, like strings, integers, or objects. For example, we can assign an existing function to a variable:

def add(x, y):
    return x + y

# assign the function to a new variable
# called "addition". It behaves the same
# as the original "add" function
addition = add
print(addition(2, 5))
# 7


# Anonymous Functions

#Anonymous functions have no name, and in Python, they're called lambda functions after lambda calculus. Here's a lambda function that takes a single argument x and returns the result of x + 1:

lambda x: x + 1

# Notice that the expression x + 1 is returned automatically, no need for a return statement. And because functions are just values, we can assign the function to a variable named add_one:

add_one = lambda x: x + 1
print(add_one(2))
# 3

# Lambda functions might look scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small,
# simple evaluations. Here's an example that uses a lambda to get a value from a dictionary:

get_age = lambda name: {
    'lane': 29,
    'hunter': 69,
    'allan': 17
}.get(name, 'not found')
print(get_age('lane'))
# 29


# First Class and Higher Order Functions

# A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

#     First-class function: A function that is treated like any other value
#     Higher-order function: A function that accepts another function as an argument or returns a function

# Python supports first-class and higher-order functions.

# First-class example
def square(x):
    return x * x

# Assign function to a variable
f = square

print(f(5))
# 25

# Higher-order example
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]
