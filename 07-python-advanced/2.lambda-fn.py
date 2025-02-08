def square(a: float) -> float:
    return a ** 2

 # type : ignore
# sq =lambda a: a ** 2


print("function: ", square(4))
# print("lambda: ", square(4))


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]

even: list[int] = list(filter(lambda a: a % 2 == 0, numbers))
