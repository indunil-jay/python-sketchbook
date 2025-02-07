# Function currying is a specific kind of function transformation where we translate a single
# function that accepts multiple arguments into multiple functions that each accept a single argument.
# This is a "normal" 3-argument function:
# box_volume(3, 4, 5)
# This is a "curried" series of functions that does the same thing:
# box_volume(3)(4)(5)

def sum(a, b):
  return a + b

print(sum(1, 2))
# prints 3

def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3


# The sum function only takes a single input, a. It returns a new function that takes a single input, b. This new function when called with a value for b will return the sum of a and b. We'll talk later about why this is useful.


# Why Curry?
# So why would we ever want to do the more complicated thing? Well, currying is often used to change a function's signature to make it conform to a specific shape. For example:



def colorize(converter, doc):
  # ...
  converter(doc)
  # ...

# The colorize function accepts a function called converter as input, and at some point during its execution,
# it calls converter with a single argument. That means that it expects converter to accept exactly one argument. So, if I have a conversion function like this:

def markdown_to_html(doc, asterisk_style):
  pass

# I can't pass markdown_to_html to colorize because markdown_to_html wants two arguments. To solve this problem, I can curry markdown_to_html into a function that takes a single argument:

def markdown_to_html(asterisk_style):
  def asterisk_md_to_html(doc):
    pass

  return asterisk_md_to_html

markdown_to_html_italic = markdown_to_html('italic')
# colorize(markdown_to_html_italic, doc)



# Remember, currying is when we take a function that accepts multiple arguments:
# And convert it into a series of functions that each accept a single argument:

def box_volume(length):
  def box_volume_with_len(width):
    def box_volume_with_len_width(height):
      return length * width * height
    return box_volume_with_len_width
  return box_volume_with_len

def create_html_table(data_rows):
    rows = ""

    # Helper function to create the header row
    def create_table_headers(headers):
        nonlocal rows  # Access the outer 'rows' variable

        # Convert the headers into <th> tags inside a <tr> tag
        header_row = "<tr>" + "".join(map(lambda header: f"<th>{header}</th>", headers)) + "</tr>"
        # Add the header row to the beginning of the rows string
        rows = header_row + rows

        # Convert the data rows into <tr><td></td></tr> format
        for data_row in data_rows:
            rows += "<tr>" + "".join(map(lambda data: f"<td>{data}</td>", data_row)) + "</tr>"

        # Wrap the entire table content in <table> tags
        return f"<table>{rows}</table>"

    return create_table_headers

def create_html_table(data_rows):
    # First step: Accepts headers and adds them to the table
    def create_table_headers(headers):
        rows = "<tr>" + "".join(map(lambda header: f"<th>{header}</th>", headers)) + "</tr>"

        # Second step: Adds data rows to the table
        def add_data_rows():
            nonlocal rows  # Access the outer 'rows' variable
            for data_row in data_rows:
                rows += "<tr>" + "".join(map(lambda data: f"<td>{data}</td>", data_row)) + "</tr>"

            # Third step: Wrap everything inside <table> tags and return the full HTML table
            return f"<table>{rows}</table>"

        return add_data_rows  # Return the next curried function

    return create_table_headers  # Return the first curried function

# Example usage:
data_rows = [
    ["Row 2, Cell 1", "Row 2, Cell 2"],
    ["Row 3, Cell 1", "Row 3, Cell 2"]
]
headers = ["Row 1, Header 1", "Row 1, Header 2"]

create_table = create_html_table(data_rows)  # First curried function
create_data_rows = create_table(headers)    # Second curried function
html_table = create_data_rows()              # Third curried function that returns the final HTML table
print(html_table)






def create_markdown_image(alt_text):
    def inner_function(url):
        # Escape parentheses in the URL
        escaped_url = url.replace('(', '%28').replace(')', '%29')
        # Basic markdown syntax: ![alt_text](url)
        markdown = f"![{alt_text}]({escaped_url})"

        def innermost_function(title=None):
            if title:
                # Add the title in quotes if provided
                markdown_with_title = markdown.rstrip(')') + f' "{title}")'
                return markdown_with_title
            return markdown

        return innermost_function

    return inner_function

# Example usage:
image = create_markdown_image("Example Image")("http://example.com/image (with spaces).jpg")("Image Title")
print(image)
