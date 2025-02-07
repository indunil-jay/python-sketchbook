# file = open('1.read.txt')
# text: str = file.read()
# file.close()

# print(text)


with open('1.read.txt') as file:
    text: str = file.read()
    print(text)
