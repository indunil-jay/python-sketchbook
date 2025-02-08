class File:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        print(f'opening {self.name}...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        print(f'closing {self.name}...')


with File('10.context-manager.py') as file:
    print(file.name)

print('done!')
