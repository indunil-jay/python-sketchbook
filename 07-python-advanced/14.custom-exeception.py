from typing import Any


class NegetiveExeception(Exception):
    """Raise if a  value is below zero (0)"""

    def __init__(self, number: float, error_code: int) -> None:
        self.number = number
        self.error_code = error_code
        super().__init__(
            f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})', self.number, self.error_code)

    def __str__(self) -> str:
        return f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})'

    def __reduce__(self) -> str | tuple[Any, ...]:
        return NegetiveExeception, (self.number, self.error_code)


try:
    raise NegetiveExeception(error_code=400, number=-5)

except NegetiveExeception as e:
    print(e.args)
    print(e)
