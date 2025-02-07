# What is object-oriented programming?

# Object-Oriented Programming, or "OOP", is a pattern for writing clean and maintainable code.
# Not everyone agrees that object-oriented principles are the best way to write code, but, to be a good engineer,
# you should at least understand them.

# Clean code

# Paradigms like object-oriented programming and functional programming are all about making code easier to work with and
# understand as the feeble humans we are. Code that's easy for humans to understand is called "clean code".


# Clean code does not

#     Make your programs run faster
#     Make your programs function correctly
#     Only occur in object-oriented programming

# Clean code does

#     Make code easier to work with
#     Make it easier to find and fix bugs
#     Make the development process faster
#     Help us retain our sanity


# DRY code

# Another "rule of thumb" for writing maintainable code is "Don't Repeat Yourself" (DRY). It just means that, when possible,
# you should avoid writing the same code in multiple places. Repeating code can be bad because:

#     If you need to change it, you have to change it in multiple places
#     If you forget to change it in one place, you'll have a bug
#     It's more work to write it over and over again


# Example:
# Take a look at the code we wrote. We started with this:

# soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
# soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

# And refactored the code to look like this:

def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]

soldier_one_dps = get_soldier_dps(soldier_one)
soldier_two_dps = get_soldier_dps(soldier_two)


# Don't repeat yourself (DRY)

# We don't want too much of our code doing the same thing. When code is duplicated, it leads to many potential problems. In our example, let's pretend the soldier dictionary changed, and now the key that stores the "damage" value is called dmg.
# In the first example, we would need to update two lines of code. In the second example, we only need to make the change in one place.
# It's not a big deal when two lines are the same and exist right next to each other. However, imagine if we had done this several hundred times in
# ten or twenty different code files! All of a sudden, it makes a lot of sense to stop repeating yourself and write more reusable functions. We call that DRY code.
