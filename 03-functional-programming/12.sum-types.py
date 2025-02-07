# Sum Types

# Remember when I said, "Pure functions are my favorite part of functional programming"? Well, sum types are a close second.

# A "sum" type is the opposite of a "product" type. This Python object is an example of a product type:

# man.studies_finance = True
# man.has_trust_fund = False

# The total number of combinations a man can have is 4, the product of 2 * 2:
# studies_finance 	has_trust_fund
# True 	True
# True 	False
# False 	True
# False 	False

# If we add a third attribute, perhaps a has_blue_eyes boolean, the total number of possibilities multiplies again, to 8!
# studies_finance 	has_trust_fund 	has_blue_eyes
# True 	True 	True
# True 	True 	False
# True 	False 	True
# True 	False 	False
# False 	True 	True
# False 	True 	False
# False 	False 	True
# False 	False 	False

# But let's pretend that we live in a world where there are really only three types of people that our program cares about:

#     Dateable
#     Undateable
#     Maybe dateable

# We can reduce the number of cases our code needs to handle by using a (admittedly fake Pythonic) sum type with only 3 possible types:

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Dateable(Person):
#     pass

# class MaybeDateable(Person):
#     pass

# class Undateable(Person):
#     pass

# Then we can use the isinstance built-in function to check if a Person is an instance of one of the subclasses. It's a clunky way to represent sum types, but hey, it's Python.

# def respond_to_text(guy_at_bar):
#     if isinstance(guy_at_bar, Dateable):
#         return f"Hey {guy_at_bar.name}, I'd love to go out with you!"
#     elif isinstance(guy_at_bar, MaybeDateable):
#         return f"Hey {guy_at_bar.name}, I'm busy but let's hang out sometime later."
#     elif isinstance(guy_at_bar, Undateable):
#         return "Have you tried being rich?"
#     else:
#         raise ValueError("invalid Person type")

# Sum Types

# As opposed to product types, which can have many (often infinite) combinations, sum types have a fixed number of possible values.
# To be clear: Python doesn't really support sum types. We have to use a workaround and invent our own little system and enforce it ourselves.









class Parsed:
    def __init__(self, doc_name, text):
        self.doc_name = doc_name  # Store the document name
        self.text = text          # Store the parsed text

class ParseError:
    def __init__(self, doc_name, err):
        self.doc_name = doc_name  # Store the document name
        self.err = err            # Store the error message






# Explanation:

#     Parsed class:
#         When an instance of Parsed is created, it takes the doc_name (the name of the document) and text (the successfully parsed text) as arguments.
#         These values are stored as instance variables, which means we can later access the document name and the parsed text through the instance.

#     ParseError class:
#         When an instance of ParseError is created, it takes doc_name (the name of the document that failed to parse) and err (the error message) as arguments.
#         These values are stored as instance variables, which can be accessed to understand the failure reason.

# Successful parsing
parsed_doc = Parsed("document1", "This is the parsed text.")
print(parsed_doc.doc_name)  # Output: document1
print(parsed_doc.text)      # Output: This is the parsed text.

# Failed parsing
parse_error = ParseError("document2", "Parsing failed due to invalid format.")
print(parse_error.doc_name)  # Output: document2
print(parse_error.err)       # Output: Parsing failed due to invalid format.

# Example of checking success or failure
doc1 = Parsed("document1", "Valid content")
doc2 = ParseError("document2", "Invalid content format")

# Check if parsing succeeded for doc1
if isinstance(doc1, Parsed):
    print(f"Document '{doc1.doc_name}' parsed successfully with text: {doc1.text}")
else:
    print(f"Document '{doc1.doc_name}' failed with error: {doc1.err}")

# Check if parsing failed for doc2
if isinstance(doc2, ParseError):
    print(f"Document '{doc2.doc_name}' failed with error: {doc2.err}")
else:
    print(f"Document '{doc2.doc_name}' parsed successfully with text: {doc2.text}")





# Enums

# Doing the admittedly weird class and isinstance() thing works, but it turns out, there's a better way in some cases.
#  If you're trying to represent a fixed set of values (but not store additional data within them) enums are the way to go.

# Let's say we have a Color variable that we want to restrict to only three possible values:

#     RED
#     GREEN
#     BLUE

# We could use a plain-old string to represent these values, but that's annoying because we have to remember all the "valid" values and defensively check for invalid ones all over our codebase. Instead, we can use an Enum:

from enum import Enum

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL) # this raises an exception



# Now Color is a sum type! At least, as close as we can get in Python.

# There are a few benefits:

#     A "Color" can only be RED, GREEN, or BLUE. If you try to use Color.TEAL, Python raises an exception.
#     There is a central place to see the "valid" values for a Color.
#     Each "Color" has a "name" (e.g. Color.RED) and a "value" (e.g. 1). The value is an integer and is used under the hood instead of the name.
# Integers take up less memory than strings, which helps with performance.


# Sum Types

# Unfortunately, Python does not support sum types as well as some of the other statically typed languages.
# Python does not enforce your types before your code runs. That's why we need this line here to raise an Exception if a color is invalid:

def color_to_hex(color):
    if color == Color.GREEN:
        return '#00FF00'
    elif color == Color.BLUE:
        return '#0000FF'
    elif color == Color.RED:
        return '#FF0000'
    # handle the case where the color is invalid
    raise Exception('Unknown color')


#  Working with enums

# Python has a match statement that tends to be a lot cleaner than a series of if/else/elif statements when we're working with a fixed set of possible values (like a sum type, or more specifically an enum):

def get_hex(color):
    match color:
        case Color.RED:
            return "#FF0000"
        case Color.GREEN:
            return "#00FF00"
        case Color.BLUE:
            return "#0000FF"

        # default case
        # (invalid Color)
        case _:
            return "#FFFFFF"

# If you have two values to match, you can use a tuple:
def get_hex(color, shade):
    match (color, shade):
        case (Color.RED, Shade.LIGHT):
            return "#FFAAAA"
        case (Color.RED, Shade.DARK):
            return "#AA0000"
        case (Color.GREEN, Shade.LIGHT):
            return "#AAFFAA"
        case (Color.GREEN, Shade.DARK):
            return "#00AA00"
        case (Color.BLUE, Shade.LIGHT):
            return "#AAAAFF"
        case (Color.BLUE, Shade.DARK):
            return "#0000AA"

        # default case
        # (invalid combination)
        case _:
            return "#FFFFFF"

# The value we want to compare is set after match keyword, which is then compared against different cases/patterns. If a match is found, the code in the block is executed.











def get_csv_status(status, data):
    match status:
        case "PENDING":
            # Convert each item in data to a string and return as a list of lists of strings
            data_converted = [list(map(str, row)) for row in data]
            return ("Pending...", data_converted)

        case "PROCESSING":
            # Convert data to a CSV string (joining each row by commas and all rows by newlines)
            data_csv = "\n".join([",".join(row) for row in data])
            return ("Processing...", data_csv)

        case "SUCCESS":
            # Return the data as is
            return ("Success!", data)

        case "FAILURE":
            # First, convert the data to a list of lists of strings (like PENDING)
            data_converted = [list(map(str, row)) for row in data]
            # Then, convert to CSV string (like PROCESSING)
            data_csv = "\n".join([",".join(row) for row in data_converted])
            return ("Unknown error, retrying...", data_csv)

        case _:
            # Raise an exception for unknown status
            raise Exception("Unknown export status")


# Example data
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"]
]

# Example calls
print(get_csv_status("PENDING", data))
print(get_csv_status("PROCESSING", data))
print(get_csv_status("SUCCESS", data))
print(get_csv_status("FAILURE", data))

# Example of raising an exception for an unknown status
try:
    print(get_csv_status("INVALID_STATUS", data))
except Exception as e:
    print(e)

















from enum import Enum

# Enum for EditType
class EditType(Enum):
    NEWLINE = "NEWLINE"
    SUBSTITUTE = "SUBSTITUTE"
    INSERT = "INSERT"
    DELETE = "DELETE"

def handle_edit(document, edit_type, edit):
    # Split the document into lines for easier manipulation
    lines = document.split("\n")

    # Handle each edit type using a match case statement
    match edit_type:
        case EditType.NEWLINE:
            # Ensure the line number is valid
            line_number = edit.get('line_number')
            if line_number >= len(lines):
                raise Exception("Invalid line number")

            # Add a newline at the end of the specified line
            lines[line_number] += "\n"
            return "\n".join(lines)

        case EditType.SUBSTITUTE:
            # Ensure valid edit dictionary keys are present
            line_number = edit.get('line_number')
            start = edit.get('start')
            end = edit.get('end')
            insert_text = edit.get('insert_text')

            # Check line_number validity
            if line_number >= len(lines):
                raise Exception("Invalid line number")

            # Check start and end index validity
            line = lines[line_number]
            if start > len(line):
                raise Exception("Invalid start index")
            if end > len(line) or end < start:
                raise Exception("Invalid end index")

            # Perform substitution
            lines[line_number] = line[:start] + insert_text + line[end:]
            return "\n".join(lines)

        case EditType.INSERT:
            # Ensure valid edit dictionary keys are present
            line_number = edit.get('line_number')
            start = edit.get('start')
            insert_text = edit.get('insert_text')

            # Check line_number validity
            if line_number >= len(lines):
                raise Exception("Invalid line number")

            # Check start index validity
            line = lines[line_number]
            if start > len(line):
                raise Exception("Invalid start index")

            # Perform insert
            lines[line_number] = line[:start] + insert_text + line[start:]
            return "\n".join(lines)

        case EditType.DELETE:
            # Ensure valid edit dictionary keys are present
            line_number = edit.get('line_number')
            start = edit.get('start')
            end = edit.get('end')

            # Check line_number validity
            if line_number >= len(lines):
                raise Exception("Invalid line number")

            # Check start and end index validity
            line = lines[line_number]
            if start > len(line):
                raise Exception("Invalid start index")
            if end > len(line) or end < start:
                raise Exception("Invalid end index")

            # Perform delete
            lines[line_number] = line[:start] + line[end:]
            return "\n".join(lines)

        case _:
            raise Exception("Unknown edit type")




document = """This is the first line.
This is the second line.
This is the third line."""

# Example 1: Add a newline to the second line
edit = {'line_number': 1}
print(handle_edit(document, EditType.NEWLINE, edit))

# Example 2: Substitute text in the first line
edit = {'line_number': 0, 'start': 5, 'end': 9, 'insert_text': "modified"}
print(handle_edit(document, EditType.SUBSTITUTE, edit))

# Example 3: Insert text in the second line at position 5
edit = {'line_number': 1, 'start': 5, 'insert_text': " inserted"}
print(handle_edit(document, EditType.INSERT, edit))

# Example 4: Delete a portion of the third line
edit = {'line_number': 2, 'start': 5, 'end': 15}
print(handle_edit(document, EditType.DELETE, edit))

# Example 5: Invalid edit type
try:
    print(handle_edit(document, "INVALID", edit))
except Exception as e:
    print(e)
