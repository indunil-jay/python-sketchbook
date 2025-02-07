name = 'Jw'


def hello():
    hello_str = "hello_str"
    hello_int = 10

    def inner():
        pass

    print(locals())


hello()


# these are locals for hello namespace
# {'hello_str': 'hello_str', 'hello_int': 10, 'inner': < function hello.<locals>.inner at 0x00000245F45F3D80>}
