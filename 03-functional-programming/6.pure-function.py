
# Pure Functions
#     They always return the same value given the same arguments.
#     Running them causes no side effects

# In short: pure functions don't do anything with anything that exists outside of their scope


# Example of a pure function
def find_max(nums):
    max_val = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val

# Example of an impure function
# instead of returning a value
# this function modifies a global variable
global_max = float("-inf")

def find_max(nums):
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num



# Pure Function Review

# Pure functions have a lot of benefits. Whenever possible, good developers try to use pure functions instead of impure functions. Remember, pure functions:

#     Return the same result if given the same arguments. They are deterministic.
#     Do not change the external state of the program. For example, they do not change any variables outside of their scope.
#     Do not perform any I/O operations (like reading from disk, accessing the internet, or writing from the console).

# These properties result in pure functions being easier to test, debug, and think about.

# Refer to the following examples and answer the questions.

################################################################################
# Reference vs. Value

# When you pass a value into a function as an argument, one of two things can happen:

#     It's passed by reference: The function has access to the original value and can change it
#     It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original

# There is a bit more nuance, but this explanation mostly works.

# These types are passed by reference:

#     Lists
#     Dictionaries
#     Sets

# These types are passed by value:

#     Integers
#     Floats
#     Strings
#     Booleans
#     Tuples

# Most collection types are passed by reference (except for tuples) and most primitive types are passed by value.

# Example of Pass by Reference (mutable)
def modify_list(inner_lst):
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]



# Example of Pass by Value (immutable)
def attempt_to_modify(inner_num):
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num = 1
attempt_to_modify(outer_num)
# outer_num = 1

# Pass by Reference Impurity

# Because certain types in Python are passed by reference, we can mutate values that we didn't intend to. This is a form of function impurity.

# Remember, a pure function should have no side effects. It shouldn't modify anything outside of its scope, including its inputs.
# It should return new copies of inputs instead of changing them.
#pure
def remove_format(default_formats, old_format):
    new_formats = default_formats.copy()
    new_formats[old_format] = False
    return new_formats

#impure
def remove_format(default_formats, old_format):
    default_formats[old_format] = False
    return default_formats





# Why do we care?

# One of the biggest differences between good and great developers is how often they incorporate pure functions into their code.
#  Pure functions are easier to read, easier to reason about, easier to test, and easier to combine.
# Even if you're working in an imperative language like Python, you can (and should) write pure functions whenever reasonable.

# There's nothing worse than trying to debug a program where the order functions are
#  called needs to be juuuuust right because they all read and modify the same global variable.


################################################################################



# The term "i/o" stands for input/output. In the context of writing programs, i/o refers to anything in our code that interacts with the "outside world". "Outside world" just means anything that's not stored in our application's memory (like variables).
# Examples of i/o

#     Reading from or writing to a file on the hard drive
#     Accessing the internet
#     Reading from or writing to a database
#     Even simply printing to the console is considered i/o!

# All i/o is a form of "side effect".

def convert_case(text, target_format):

    if not text or not target_format:
        raise ValueError(f"No text or target format provided")

    if target_format == "uppercase":
      return text.upper()

    if target_format == "lowercase":
      return  text.lower()

    if target_format == "titlecase":
      return  text.title()

    raise ValueError(f"Unsupported format: {target_format}")

# Should I i/o?

# A program that doesn't do any i/o is pretty useless. What's the point of computing something if you can't see the results?

# In functional programming, i/o is viewed as dirty but necessary. We know we can't eliminate i/o from our code, so we just contain it as much as possible. There should be a clear place in your project that does nasty i/o stuff, and the rest of your code can be pure.

# For example, a Python program might:

#     Read a file from the hard drive as the program starts
#     Run a bunch of pure functions to analyze the data
#     Write the results of the analysis to a file on the hard drive at the end



################################################################################


# No-Op

# A no-op is an operation that does... nothing.

# If a function doesn't return anything, it's probably impure. If it doesn't return anything, the only reason for it to exist is to perform a side effect.

#  Example no-op

# This function performs a useless computation because it doesn't return anything or perform a side-effect. It's a no-op.
def square(x):
    x * x


# Example side-effect
# This function performs a side effect. It changes the value of the y variable that is outside of its scope. It's impure.
y = 5
def add_to_y(x):
    global y
    y += x

add_to_y(3)
# y = 8

# The global keyword just tells Python to allow access to the outer-scoped y variable.

# Even the print() function (technically) has an impure side effect! It doesn't return anything, but it does print text to the console, which is a form of i/o.


################################################################################


# Memoization

# At its core, memoization is just caching (storing a copy of) the result of a computation so that we don't have to compute it again in the future
def add(x, y):
    return x + y



# A call to add(5, 7) will always evaluate to 12. So, if you think about it, once we know that add(5, 7) can be replaced with 12, we can just store the value 12 somewhere in memory so that we don't have to do the addition operation again in the future. Then, if we need to add(5, 7) again, we can just look up the value 12 instead of doing a (potentially expensive) CPU operation.

# The slower and more complex the function, the more memoization can help speed things up.

# Note: It's pronounced "memOization", not "memORization". This confused me for quite a while in college, I thought my professor just didn't speak goodly...

# example of memoziatons

def word_count_memo(document,memos):
    memos_copy = memos.copy()

    if(document in memos_copy):
      return memos_copy[document],memos_copy
    else:
       count =  word_count(document)
       memos_copy[document] =count
       return count, memos_copy



def word_count(document):
    count = len(document.split())
    return count

################################################################################

# Referential transparency

# Pure functions are always referentially transparent.

# "Referential transparency" is a fancy way of saying that a function call can be replaced by its would-be return value because it's the same every time. Referentially transparent functions can be safely memoized. For example add(2, 3) can be smartly replaced by the value 5.

# The great thing about pure functions is that they can always be safely memoized. Impure functions can't be because they might do something in addition to returning a static value, or they might return different values given the same arguments.
# Should I always memoize?

# No! Memoization is a tradeoff between memory and speed. If your function is fast to execute, it's probably not worth memoizing, because the amount of RAM (memory) your program will need to store the results will go way up.

# It's also a bunch of extra code to write, so you should only do it if you have a good reason to.

################################################################################

# sort()  use to sort list


################################################################################

# Index Keywords

# By indexing keywords, documents are better organized, enabling users to navigate through their documents more efficiently. It also reduces the computational overhead of repeatedly searching for the same terms, improving the performance and responsiveness of Doc2Doc. This is useful for notebooking, research and project management.
