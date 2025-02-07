
# Closures

# A closure is a function that references variables from outside its own function body. The function definition and its environment are bundled together into a single entity.

# Put simply, a closure is just a function that keeps track of some values from the place where it was defined, no matter where it is executed later on.

def concatter():
	doc = ""
	def doc_builder(word):
		# "nonlocal" tells Python to use the 'doc'
		# variable from the enclosing scope
		nonlocal doc
		doc += word + " "
		return doc
	return doc_builder

# save the returned 'doc_builder' function
# to the new function 'harry_potter_aggregator'
harry_potter_aggregator = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive



# Closure Review

# The whole point of a closure is that it's stateful. It's a function that "remembers" the values from the enclosing scope even after the enclosing scope has finished executing.

# It's as if you're saving the state of a function at a particular point in time, and then you can use and update that state later on.


# Closure Practice

# Remember, a closure is a function that retains the state of its environment. That makes it useful for tracking data as it changes over time, but it can come at the cost of understandability.

# When not to use the nonlocal keyword: when the variable is mutable (such as a list, dictionary or set), and you are modifying its contents rather than reassigning the variable.
#  You only need the nonlocal keyword if you are reassigning a variable instead of modifying its contents (which you must do to change immutable values such as strings and integers).


def new_collection(initial_docs):
    # Create a copy of initial_docs to avoid modifying the original
    docs = initial_docs[:]

    # Define the inner function that appends to the copy
    def add_to_collection(new_doc):
        docs.append(new_doc)  # Append the new document to the list
        return docs  # Return the updated list

    return add_to_collection  # Return the inner function

# Example usage
new_collection_func = new_collection(["doc1", "doc2", "doc3"])
print(new_collection_func("doc4"))  # ['doc1', 'doc2', 'doc3', 'doc4']
print(new_collection_func("doc5"))  # ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']






# Doc2Doc has a simple clipboard for copying to and pasting from a cache. Initialize the clipboard to set and get strings

def new_clipboard(initial_dict):
    # Create a copy of the input dictionary to avoid modifying the original
    clipboard = initial_dict.copy()

    # Function to add a key-value pair to the clipboard
    def copy_to_clipboard(key, value):
        clipboard[key] = value  # Add or update the key-value pair

    # Function to retrieve a value by key from the clipboard
    def paste_from_clipboard(key):
        return clipboard.get(key, "")  # Return the value or an empty string if key is missing

    # Return both functions
    return copy_to_clipboard, paste_from_clipboard

# Example usage
copy_to_clipboard, paste_from_clipboard = new_clipboard({"a": "apple", "b": "banana"})

# Copy a new key-value pair to the clipboard
copy_to_clipboard("c", "cherry")

# Paste values from the clipboard
print(paste_from_clipboard("a"))  # Output: "apple"
print(paste_from_clipboard("c"))  # Output: "cherry"
print(paste_from_clipboard("d"))  # Output: ""

# Doc2Doc has a spellchecker, but users often use slang words that aren't recognized. Create a feature to allow users to add their own words to the spellchecker.
def user_words(initial_words):
    # Define the function to add a word
    def add_word(new_word):
        nonlocal initial_words  # Use the enclosed initial_words
        initial_words += (new_word,)  # Create a new tuple with the added word
        return initial_words  # Return the updated tuple

    return add_word  # Return the add_word function

# Example usage
add_word = user_words(("hello", "world"))
print(add_word("python"))  # Output: ('hello', 'world', 'python')
print(add_word("code"))    # Output: ('hello', 'world', 'python', 'code')



def css_styles(initial_styles):
    # Make a copy of the initial styles dictionary
    styles = initial_styles.copy()

    # Define the add_style inner function
    def add_style(selector, property, value):
        # If the selector doesn't exist, create an empty dictionary for it
        if selector not in styles:
            styles[selector] = {}
        # Add or update the property in the selector's dictionary
        styles[selector][property] = value
        # Return the modified styles dictionary
        return styles

    return add_style

# Example usage
initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)

# Add a new style
new_styles = add_style("p", "color", "grey")
print(new_styles)
# Output:
# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }

# Update an existing style
updated_styles = add_style("body", "font-size", "14px")
print(updated_styles)
# Output:
# {
#    "body": {
#        "background-color": "white",
#        "color": "black",
#        "font-size": "14px"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }


# Users should be able to paginate lengthy documents to make them manageable. Pagination is simply dividing a document into pages.
# This idea can also be applied to other data besides raw text, such as a list of search results or API responses

def add_word_to_pages(pages, word, page_length):
    # If pages is empty, start with the word as the only page
    if not pages:
        return [word]

    # Assign the last page in pages to current_page
    current_page = pages[-1]

    # Check if adding the word exceeds the page length
    if len(current_page) + len(word) + 1 > page_length:  # +1 for the space
        # Start a new page with the word
        pages.append(word)
    else:
        # Add the word to the current page with a space
        pages[-1] = current_page + " " + word

    # Return the updated pages
    return pages

def paginator(page_length):
    def paginate(text):
        # Split the text into words
        words = text.split()

        # Initialize pages as an empty list
        pages = []

        # Add each word to pages using add_word_to_pages function
        for word in words:
            pages = add_word_to_pages(pages, word, page_length)

        return pages

    return paginate

# Example usage
paginate = paginator(11)
pages = paginate("Boots loves salmon because he is a bear.")
print(pages)
