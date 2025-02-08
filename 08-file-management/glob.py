import os
import glob

# The glob module in Python is used for finding file paths that match a specified pattern, similar to shell-style wildcard matching.

# 📌 Use Case:

#     Searching for specific files in a directory
#     Filtering files by extension(e.g., .txt, .csv)
#     Recursively finding files in subdirectories

# Match Specific Files in Current Directory
files = glob.glob("*.txt")  # Find all `.txt` files in the current directory
print(files)  # ['file1.txt', 'notes.txt']


# Wildcard Patterns

# * → Matches everything
# ? → Matches a single character
# [abc] → Matches any character inside brackets
print(glob.glob("data_*.csv"))   # Matches 'data_1.csv', 'data_2.csv'
print(glob.glob("report_?.pdf"))  # Matches 'report_1.pdf', 'report_2.pdf'

# Searching in a Specific Directory
print(glob.glob("/home/user/documents/*.pdf"))


# Recursive Search(**)
# Use ** to search recursively through subdirectories(requires recursive=True).
print(glob.glob("**/*.txt", recursive=True))
# This will return all .txt files in the current folder and subfolders.


# Using iglob() for Memory Efficiency
# iglob() works like glob() but returns an iterator instead of a list(useful for large directories).

for file in glob.iglob("**/*.jpg", recursive=True):
    print(file)  # Prints file paths one by one


# 5️⃣ Example: Deleting Files Matching a Pattern

for file in glob.glob("temp_*.log"):
    # Delete all files starting with 'temp_' and ending in '.log'
    os.remove(file)


# 🔹 When to Use glob?

# ✅ Finding and listing files based on patterns
# ✅ Searching files recursively in directories
# ✅ Efficient file processing with iglob()
