names: list[str] = ['robert', 'mario', 'sofia', 'james']


# for name in names:
#     print(names.index(name)+1, ":", name)

# instead of above we can use
# loopthrought and unpacking both same at time
#  i default start number is 0, we can specify number for start
for i, name in enumerate(names, start=1):
    print(i, ":", name)
