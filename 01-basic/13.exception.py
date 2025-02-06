# Errors and exceptions in Python
#You've probably encountered some errors in your code from time to time i. In Python, there are two main kinds of distinguishable errors.

    # syntax errors : . A syntax error is just the Python interpreter telling you that your code isn't adhering to proper Python syntax.
    # exceptions : Even if your code has the right syntax, however, it may still cause an error when an attempt is made to execute it.
                   # Errors detected during execution are called "exceptions" and can be handled gracefully by your code. You can even raise your own exceptions when bad things happen in your code.


# try:
#   10 / 0
# except Exception:
#   print("can't divide by zero")

#   The try block is executed until an exception is raised or it completes, whichever happens first.
#  In this case, an exception is raised because division by zero is impossible. The except block is only executed if an exception is raised in the try block.

try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"
# Wrapping potential errors in try/except blocks allows the program to handle the exception gracefully without crashing.


# Raising your own exceptions

# Errors are not something to be scared of. Every program that runs in production is expected to manage errors on a constant basis.
#  Our job as developers is to handle the errors gracefully and in a way that aligns with our user's expectations.


#########Raising exceptions review###########

#Software applications aren't perfect, and user input and network connectivity are far from predictable. Despite intensive debugging and unit testing, applications will still have failure cases.

# Loss of network connectivity, missing database rows, out of memory issues, and unexpected user inputs can all prevent an application from performing "normally". It is your job to catch and handle any and all exceptions gracefully so that your app keeps working.
# When you are able to detect that something is amiss, you should be raising the errors yourself, in addition to the "default" exceptions that the Python interpreter will raise.\

raise Exception("something bad happened")





# Different types of exceptions

# We haven't covered classes and objects yet, which is what an Exception really is at its core. We'll go more into that in the course on object-oriented programming.

# For now, what is important to understand is that there are different types of exceptions and we can handle them differently depending on the situation. Some exceptions are more specific,
# like ZeroDivisionError or IndexError, and some are more general, like the base Exception.

try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)


    # When handling exceptions, it’s important to catch the most specific ones first, because Python stops checking once
    #  it finds a matching exception handler. If you catch a more general Exception first, any specific errors will never get handled individually.
