numbers: list[int] = [1, 2, 3, 4]


def to_string(element: int):

    return str(element)


converted_list: list[str] = list(map(to_string, numbers))

print(converted_list)
