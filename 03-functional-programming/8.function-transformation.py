# Function Transformations

# "Function transformation" is just a more concise way to describe a specific type of higher order function.
# It's when a function takes a function (or functions) as input and returns a new function. Let's look at an example:'

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# self_math is a higher order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10



# Why Transform?

# You might be wondering:

#     "When would I use function transformations in the real world?"
#     "Isn't it simpler to just define functions at the top level of the code, and call them as needed?"

# Good questions. To be clear, we don't just transform functions at runtime for the fun of it! We only use advanced techniques like function transformations when they make our code simpler than it would otherwise be.

#  Code Reusability

# Creating variations of the same function dynamically can make it a lot easier to share common functionality. Take a look at this formatter function. It accepts a "pattern" and returns a new function that formats text according to that pattern

def formatter(pattern):
    def inner_func(text):
        result = ""
        i = 0
        while i < len(pattern):
            if pattern[i:i+2] == '{}':
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result
    return inner_func

bold_formatter = formatter("**{}**")
italic_formatter = formatter("*{}*")
bullet_point_formatter = formatter("* {}")

print(bold_formatter("Hello"))
# **Hello**
print(italic_formatter("Hello"))
# *Hello*
print(bullet_point_formatter("Hello"))
# * Hello
