import json


# load and loads (use with stream of reads write)

# with open('08-file-management/sample.json', 'r') as file:
#     content: dict = json.load(file)
#     print(content)
#     print(content)


# write

sample = {"name": "Elon", "age": 10, 'has_married': False}
sample_json = json.dumps(sample)
print(sample_json)


with open('08-file-management/sample1.json', 'w') as file:
    json.dump(sample, file)
