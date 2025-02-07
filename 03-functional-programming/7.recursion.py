# Recursion

# Recursion is a famously tricky concept to grasp, but it's honestly quite simple - don't let it intimidate you! A recursive function is just a function that calls itself
# Recursion is the process of defining something in terms of itself.


# If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:

def sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum(nums[1:])

print(sum([1, 2, 3, 4, 5]))
# 15


def print_chars(word, i):
    if i == len(word):
        return
    print(word[i])
    print_chars(word, i + 1)

print_chars("Hello", 0)
# H
# e
# l
# l
# o

def zipmap(keys, values):
    # Base case: if keys or values is empty, return an empty dictionary
    if not keys or not values:
        return {}

    # Recursive case: take the first key-value pair and combine with the result of the recursive call
    return {keys[0]: values[0], **zipmap(keys[1:], values[1:])}

# Example usage
zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)



def sum_nested_list(root):
    total = 0
    for element in root:
        if isinstance(element, list):  # If the element is a list, recurse into it
            total += sum_nested_list(element)
        else:  # If it's not a list, add the value to the total
            total += element
    return total

# Example usage
root = [
    5,
    [6, 7],
    [[8, 9], 10]
]
print(sum_nested_list(root))  # Output: 45


# Recursion Review

# Recursion is so dang useful with tree-like structures because we don't always know how deep they're nested. Stop and think about how you would write nested loops to traverse a tree of arbitrary depth... it's not easy, is it?

# for item in tree:
#     for nested_item in item:
#         for nested_nested_item in nested_item:
#             for nested_nested_nested_item in nested_nested_item:
#                 # ... WHEN DOES IT END???

# I most often use recursion on tree-like problems (file systems, nested dictionaries, etc). If I'm just iterating over a one-dimensional list then a loop (gasp...) is typically simpler, even if it's not as "pure" in the academic sense.

# Remember: The rules of functional programming are just philosophies to help you write better code, but it's not always the right tool for the job. The same goes for any programming paradigm.



# Recursion on a tree

# Recursion is often used in "tree-like" structures. For example:

#     Nested dictionaries
#     File systems
#     HTML documents
#     JSON objects

# That's because trees can have unknown depth. It's hard to write a series of loops because you don't know how many levels deep the tree goes



# Dangers of Recursion

# Recursion is great because it's simple and elegant, often being the most straightforward way to solve a problem. But there are some things to watch out for:

#     Stack Overflow: Each function call requires a bit of memory. So, if you recurse too deeply, you can run out of "stack" memory which will crash your program. (This is what the famous website is named after)
#     If you don't have a solid base case, you can end up in an infinite loop (which will likely lead to a stack overflow).
#     Recursion (especially in a language like Python) is often slower than a for loop because each function call requires some memory. Tail call optimization can help with this, but Python doesn't support it.












zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
