from typing import cast

people: list[str | int] = ['Maria', 12, 'jessi', 'tot', 99]


def is_str(element) -> bool:
    return isinstance(element, str)


# Explicitly converting to a list
filtered_people = cast(list[str], list(filter(is_str, people)))

print(filtered_people)  # Output: ['Maria', 'jessi', 'tot']
