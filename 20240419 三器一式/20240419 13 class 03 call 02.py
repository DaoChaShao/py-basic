from random import randint


class Calculation(object):
    def __init__(self, x: int, y: int) -> None:
        self._m: int = x
        self._n: int = y

    def __call__(self) -> int:
        return self._m + self._n

    def __str__(self) -> str:
        return f"{self._m} + {self._n} = {self.__call__()}"


def main() -> None:
    x = randint(1, 10)
    y = randint(1, 10)
    cal = Calculation(x, y)
    print(cal)


if __name__ == "__main__":
    main()
