

#  a -> append to the end
# a+ -> append and read
# w+ -> overwrite
# x+ -> create file and read write

with open('08-file-management/sample1.text', 'x+') as text:
    text.write('\n New text added!!!')
    # start of line-01 otherwise it will stay in end of the file so there is no data add the bottom
    text.seek(0)
    print(text.read())
