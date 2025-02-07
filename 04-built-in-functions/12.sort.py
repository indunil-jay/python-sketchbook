numbers: list[int] = [2, 53, 7, 1, 24, 13]

# nothing return, mutate existing array
# print(numbers.sort())
# numbers.sort()
# print(numbers)


# sorted() returns a new list rather than mutating existing
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)


strings: list[str] = ['A', 'b', "B", "a", "C", "D", "E"]

# ascii order
print(sorted(strings))

# key
print(sorted(strings, key=str.lower))


class Fruit:
    def __init__(self, name: str, calories: int) -> None:
        self.name = name
        self.calories = calories

    def __repr__(self) -> str:
        return f'{self.name} : {self.calories}'


fruits: list[Fruit] = [Fruit('apple', 500), Fruit(
    'banana', 200), Fruit('mango', 700)]


def sort_by_calories(fruit: Fruit):
    return fruit.calories


print(sorted(fruits, key=sort_by_calories))
