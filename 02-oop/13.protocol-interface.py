from typing import Protocol


class Printable(Protocol):

    page: int = 0

    def prints(self):
        pass

    def recylce(self):
        pass


class Book:
    page: int = 0

    def __init__(self, title: str) -> None:
        self.title = title

    def prints(self):
        print(f'printing {self.title} ...')

    def recylce(self):
        print(f'recylcing {self.title} ...')


class Magazine:
    page: int = 0

    def __init__(self, title: str) -> None:
        self.title = title

    def prints(self):
        print(f'printing Magazine {self.title} ...')

    def recylce(self):
        print(f'recylcing Magazine {self.title} ...')

    def other(self):
        ...


def print_item(printable: Printable):
    printable.prints()


book: Printable = Book('self motivation')

print_item(book)


magazine: Printable = Magazine('lora')
print_item(magazine)


# here we have followed a  interface or contract for our object, util all methods are compatibale with interface
# it is not complaing to the compiler, but, in child classes we can use any other extra methods, maintaining
# the shep of the interface or contract.
