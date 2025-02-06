# Scope refers to where a variable or function name is available to be used

#  For example, when we create variables in a function (such as by giving names to our parameters), that data is not available outside of that function.

def subtract(x, y):
    return x - y
result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"


# python variable has function scope.
