from random import randint


class Calculation(object):
    def __init__(self, x: int, y: int) -> None:
        self._m: int = x
        self._n: int = y
        self.__call__()

    def __call__(self) -> int:
        return self._m + self._n

    def __str__(self) -> str:
        return f"{self._m} + {self._n} = {self.__call__()}"


class Addition(object):
    def __init__(self, num: int) -> None:
        self._number: int = num

    def __call__(self, other: int) -> int:
        return self._number + other

    def __str__(self) -> str:
        return str(self._number)


def main() -> None:
    x: int = randint(1, 10)
    y: int = randint(1, 10)
    cal: Calculation = Calculation(x, y)
    print(cal)

    m: int = randint(1, 10)
    n: int = randint(1, 10)
    call: Addition = Addition(m)
    print(f"The result of {m} + {n} is {call(n)}.")


if __name__ == "__main__":
    main()
