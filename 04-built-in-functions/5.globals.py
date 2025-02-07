variable = 'GLOBAL'


def hello():
    return "GLOBAL"


class Fruit:
    def __init__(self) -> None:
        print('GLOBAL')


print(globals())
