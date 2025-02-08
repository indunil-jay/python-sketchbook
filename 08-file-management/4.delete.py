import os


if os.path.exists('08-file-management/sample1.text'):
    os.remove('08-file-management/sample1.text')
else:
    print('no file found')


# os.listdir(folderName) , get all files in a folder
# os.rmdir()
