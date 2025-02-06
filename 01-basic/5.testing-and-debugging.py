#  A unit test is just an automated program that tests a small "unit" of code. Usually just a function or two.
# These new unit-test-style lessons will test your code's functionality rather than its output.
#  Our tests will call functions in your code with different arguments, and expect certain return values.
# If your code returns the correct values, you pass. If it doesn't, you fail.


def total_xp(level,xp_to_add):
     level_xp = level * 100;
     total_xp  = level_xp +xp_to_add
     return total_xp


run_cases = [
    (1, 200, 300),
    (2, 50, 250),
]

submit_cases = run_cases + [
    (0, 0, 0),
    (0, 200, 200),
    (176, 350, 17950),
    (250, 100, 25100),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    print(f"Expecting: {expected_output}")
    result = total_xp(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
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








# Debugging

# When you're working as a professional developer, you'll typically write code on your computer and test it by yourself before it's deployed to users.

# That first part of the process is called debugging. You write some code, run it, and if it doesn't work, you fix the bugs. You repeat this process until you're confident that your code works as expected.



# Stack Trace

# A stack trace (or "traceback") is a scary-looking error message that the Python interpreter prints to the
# console when it encounters certain problems. Stack traces are most common (at least for you right now) when you're trying to run invalid Python code.
