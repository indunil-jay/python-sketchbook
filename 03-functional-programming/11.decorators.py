# Python decorators are just syntactic sugar for higher-order functions.

def vowel_counter(func_to_decorate):
    vowel_count = 0
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiou"
        for char in doc:
            if char in vowels:
                vowel_count += 1
        print(f"Vowel count: {vowel_count}")
        return func_to_decorate(doc)
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("What")
# Vowel count: 1
# Document: What

process_doc("a wonderful")
# Vowel count: 5
# Document: a wonderful

process_doc("world")
# Vowel count: 6
# Document: world
# The @vowel_counter line is "decorating" the process_doc function with the vowel_counter function. vowel_counter is called once when process_doc is defined with the @ syntax,
# but the wrapper function that it returns is called every time process_doc is called. That's why vowel_count is preserved and printed after each time.



# Python decorators are just another (sometimes simpler) way of writing a higher-order function. These two pieces of code are identical:



# Args and kwargs

# In Python, *args and **kwargs allow a function to accept and deal with a variable number of arguments.

    # *args collects positional arguments into a tuple
    # **kwargs collects keyword (named) arguments into a dictionary

def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}

#  Positional arguments

# Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:
def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1

#  Keyword arguments

# Keyword arguments are passed in by name. Order does not matter. Like this:

def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1

# Any positional arguments must come before keyword arguments.



# Decorators

# The *args and **kwargs syntax is great for decorators that are intended to work on functions with different signatures.


# The log_call_count function below doesn't care about the number or type of the decorated function's (func_to_decorate) arguments. It just wants to count how many times the function is called. However, it still needs to pass any arguments through to the wrapped function.
def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # The * and ** syntax unpacks the arguments
        # and passes them to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper

# Decorators Review

# A Python decorator is just syntactic sugar for higher-order functions. "Syntactic sugar" just means "a more convenient syntax".

# Not all programming languages have built-in decorators, but most do support higher-order functions and closures.

# Some of the famous functional languages like:

#     Haskell
#     Erlang
#     Clojure
#     Lisp

# do not have special syntax decorators, but they do have higher-order functions and closures, meaning the decorator pattern can still be used.
# So, if you understand those concepts, they will serve you well in many different languages.













import re

def convert_md_to_txt(md_string):
    """
    Converts Markdown heading to plain text by removing the Markdown heading symbols.
    """
    # Regex to remove Markdown headings (e.g., # Heading 1 -> Heading 1)
    return re.sub(r"^#+\s*", "", md_string)

def markdown_to_text_decorator(func):
    """
    A decorator that strips Markdown headings from the input arguments before passing them to the decorated function.
    """
    def wrapper(*args, **kwargs):
        # Map *args to strip Markdown headings
        new_args = [convert_md_to_txt(arg) if isinstance(arg, str) else arg for arg in args]

        # Map **kwargs to strip Markdown headings
        new_kwargs = {key: convert_md_to_txt(value) if isinstance(value, str) else value
                      for key, value in kwargs.items()}

        # Call the original function with the new arguments
        return func(*new_args, **new_kwargs)

    return wrapper

# Example usage:
@markdown_to_text_decorator
def display_content(title, content):
    print(f"Title: {title}")
    print(f"Content: {content}")

# Test the decorator
display_content("# Heading 1", "## Subheading 2\nThis is some content.")
