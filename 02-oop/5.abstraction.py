# Abstraction
# Abstraction helps us handle complexity by hiding unnecessary details.
# Sounds like encapsulation, right? They're so similar that it's almost not worth worrying about the difference...almost.


#  Abstraction vs encapsulation

#     Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed.
#     Encapsulation is about hiding internal state. It focuses on tucking implementation details away so no one depends on them

# Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.


#  Are we encapsulating or abstracting?

# Both. Almost always we are doing both. Here's an example of using the random library to generate a random number:
import random

attack_damage = random.randrange(5)

# Generating random numbers is a really hard problem. The operating system uses the physical hardware of the computer to create a seed for the randomness.
# However, the developers of the random library have abstracted that complexity away and encapsulated it within the simple randrange function.
# We just say "I want a random number from 0 to 4" and the library does it.

# When writing libraries for use by other developers, getting the abstractions right is crucial because changing them later can be disastrous.
#  Imagine if the maintainers of the random module changed the input parameters to the randrange function! It would break code all over the world.



# Abstraction is about reducing complexity. Creating good abstractions is particularly crucial when you're developing libraries for other developers to use. For example, the built-in pow function in Python is an abstraction that hides the complexity of calculating exponents.

# pow isn't magic. Somewhere, code that does something like this exists and is called when you use pow:

def pow(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result







# How OOP developers think

# Classes in object-oriented programming are all about grouping data and behavior together in one place: an object. Object-oriented programmers tend to think about programming as a modeling problem. They think:

#     "How can I write a Human class that holds the data and simulates the behavior of a real human?"

# To provide some contrast, functional programmers tend to think of their code as inputs and outputs, and how those inputs and outputs transition the world from one state to the next:

#     "When a human takes a step, what's the new state of the game?"

# oop vs fp
# Both paradigms are valuable

# OOP isn't the only pattern for organizing code, but it's one of the more popular ones. If you understand multiple ways of thinking about code, you'll be a much better developer overall.
