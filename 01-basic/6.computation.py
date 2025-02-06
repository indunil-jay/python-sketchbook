# Numbers
 # in python numbers  without a decimal point are called Integers. just like they are in mathematics. integers are simply whole numbers, positive or negetive, ofr example 3 and -3 are bothh examples of integers..

################### arithmatic operations##################
  # addition  ex: 2 + 3 = 5
  # subtraction ex: 4 - 1 = 3
  # multiplication ex: 2 * 2 = 4
  # division ex: 3 /2  = 1.5   #  division on two integers will actually produce a float. A float is, as you may have guessed, the number type that allows for decimal values.


 # A float is, as you may have guessed, the number type that allows for decimal values. ex 5.75  -9.32

##################floor division##################
     # Floor division is like normal division except the result is floored afterward, which means the result is rounded down to the nearest integer. The // operator is used for floor division.

7 // 3
# 2 (an integer, rounded down from 2.333)
-7 // 3
# -3 (an integer, rounded down from -2.333)


################### exponents##################
      # Python has built-in support for exponents - something most languages require a math library for.

# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9

################### Changing In Place It's fairly common to want to change the value of a variable based on its current value.##################
player_score = 4
player_score = player_score + 1
# player_score now equals 5

# Plus Equals
star_rating = 4
star_rating += 1
# star_rating is now 5

star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0



################### Scientific Notation##################
# As we covered earlier, a float is a positive or negative number with a fractional part.
# You can add the letter e or E followed by a positive or negative integer to specify that you're using scientific notation.
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

# If you're not familiar with scientific notation, it's a way of expressing numbers that are too large or too small to conveniently write normally
# In a nutshell, the number following the e specifies how many places to move the decimal to the right for a positive number, or to the left for a negative number.


################### Underscores for readability##################
# Python also allows you to represent large numbers in the decimal format using underscores as the delimiter instead of commas to make it easier to read.
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

################### Logical Operators   (and , or)##################
# Logical operators deal with boolean values, True and False.
# The logical and operator requires that both inputs are True to return True. The logical or operator only requires that at least one input is True to return True

True and True == True
True and False == False
False and False == False

True or True == True
True or False == True
False or False == False


################### Binary numbers##################

# Binary numbers are just "base 2" numbers. They work the same way as "normal" base 10 numbers, but with two symbols instead of ten.

    # Base-2 (binary) symbols: 0 and 1
    # Base-10 (decimal) symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


################### Bitwise opertors {&} ##################
# Bitwise operators are similar to logical operators, but instead of operating on boolean values, they apply the same logic to all the bits in a value by column.
  # 5 = 0101
  # 7 = 0111
  #---------- &
  #   = 0101 = 5
  # 1 in Binary form means TRUE
  # 0 in binary form means FALSE
  # & in binary form means AND
print(5 & 7)

# binary  notation
# When writing a number in binary, the prefix 0b is used to indicate that what follows is a binary number. 0b10 is two in binary, but 10 without the 0b prefix is simply ten.


# user  permision mechanism with bitwise operators
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def get_create_bits(user_permissions):
    return can_create_guild & user_permissions


def get_review_bits(user_permissions):
    return can_review_guild & user_permissions


def get_delete_bits(user_permissions):
   return can_delete_guild & user_permissions


def get_edit_bits(user_permissions):
   return get_edit_bits & user_permissions



run_cases = [
    (0b0110, False, True, True, False),
    (0b1111, True, True, True, True),
    (0b0000, False, False, False, False),
]

submit_cases = run_cases + [
    (0b1001, True, False, False, True),
    (0b1000, True, False, False, False),
    (0b0100, False, True, False, False),
    (0b0010, False, False, True, False),
    (0b0001, False, False, False, True),
]


def test(
    input1, expected_output1, expected_output2, expected_output3, expected_output4
):
    print("---------------------------------")
    print(f"Inputs: {input1:04b}")
    print(f"Expecting can_create: {expected_output1}")
    print(f"Expecting can_review: {expected_output2}")
    print(f"Expecting can_delete: {expected_output3}")
    print(f"Expecting can_edit: {expected_output4}")

    result1 = get_create_bits(input1) == can_create_guild
    result2 = get_review_bits(input1) == can_review_guild
    result3 = get_delete_bits(input1) == can_delete_guild
    result4 = get_edit_bits(input1) == can_edit_guild

    print(f"Actual can_create: {result1}")
    print(f"Actual can_review: {result2}")
    print(f"Actual can_delete: {result3}")
    print(f"Actual can_edit: {result4}")
    if (
        result1 == expected_output1
        and result2 == expected_output2
        and result3 == expected_output3
        and result4 == expected_output4
    ):
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()




################### Bitwise "|" Operator##################
# As you may have guessed, the bitwise "or" operator is similar to the bitwise "and" operator in that it works on binary rather than boolean values. However, the bitwise "or" operator "or"s the bits together.
# 5  = 0101
# 7 = 0111
# -------------  |
#    0111  = 7

# A 1 in binary is the same as True, while 0 is False. So a bitwise operation is just a bunch of logical operations that are completed in tandem. When two binary numbers are "or"ed together, the result has a 1 in any place where either of the input numbers has a 1 in that place.



########### NOT operator ##################
#The not operator reverses the result. It returns False if the input was True and vice-versa.
print(not True)
# Prints: False

print(not False)
# Prints: True

# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)



########### comparison operators ##############
# When coding it's necessary to be able to compare two values. Boolean logic is the name for these kinds of comparison operations that always result in True or False.

    # < "less than"
    # > "greater than"
    # <= "less than or equal to"
    # >= "greater than or equal to"
    # == "equal to"
    # != "not equal to"

# When a comparison happens, the result of the comparison is just a boolean value, it's either True or False.
