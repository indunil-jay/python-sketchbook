class Fruit:
    def __init__(self, name: str) -> None:
        self.name = name


apple = Fruit('Apple')
banana = Fruit('Banana')


print(isinstance(apple, Fruit))


print(isinstance('string', str))

print(isinstance('string', int))
