# Loops
############# for #################
# Loops are a programmer's best friend. Loops allow us to do the same operation multiple times without having to write it explicitly each time.
for i in range(0, 10):
    print(i)

    # The body of a for-loop must be indented, otherwise you'll get a syntax error. Not only that, but every line in the body of
    # the loop must be indented in the same way - we use the "4 spaces" convention. Pressing the <tab> key should automatically insert 4 spaces.



# Range Continued

# The range() function we've been using in our for loops actually has an optional 3rd parameter: the "step".
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1


############# while #################
# Python has another type of loop, the while loop. It's a loop that continues while a condition remains True.
while 1:
    print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)

# The example above is hardcoded to continue forever, creating an infinite loop. Typically, a while loop condition is a comparison or variable, and it determines when the loop ends:
num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)
