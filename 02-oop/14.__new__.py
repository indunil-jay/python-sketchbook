
# The __new__() method in Python is a special method responsible for creating a new instance of a class. It is called before __init__() and is mainly used for controlling object creation.

# When to Use __new__()?

# When you want to customize instance creation.
# When implementing singleton patterns(ensuring only one instance is created).
# When working with immutable classes like tuple or str.

class Connection:
    __instance = None

    def __init__(self) -> None:
        print('connected to database')

    def __new__(cls):
        if cls.__instance is None:
            print('connecting...')
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


connection1 = Connection()
connection2 = Connection()
# only one connection is established


class Car:
    def __init__(self) -> None:
        print('Car is initialized')


class MotoBike:
    def __init__(self) -> None:
        print('MotoBike is initialized')


class Vehical:
    def __init__(self, wheel: int) -> None:
        self.wheel = wheel

    def __new__(cls, wheel: int):
        if (wheel == 2):
            return MotoBike()
        if (wheel == 4):
            return Car()
        return super().__new__(cls)
