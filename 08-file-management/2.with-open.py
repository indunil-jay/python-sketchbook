# file = open('08-file-management/sample.text','rt')
# file.read()
# file.close()


with open('08-file-management/sample.text', 'r') as text:
    print(text.read())
