from random import randint


class Calculator(object):
    def __init__(self, x: int, y: int) -> None:
        self.m: int = x  # 使用属性赋值，触发 x 的 setter 方法
        self.n: int = y

    @property
    def m(self) -> int:
        return self._m

    @m.setter
    def m(self, value: int) -> None:
        if value < 0:
            raise ValueError("m must be positive")
        self._m = value  # 使用 _m 作为内部存储变量

    @property
    def n(self) -> int:
        return self._n  # 这是一个 getter

    @n.setter
    def n(self, value: int) -> None:
        if value < 0:
            raise ValueError("n must be positive")
        self._n = value  # 使用 _n 作为内部存储变量，这是一个 getter

    @property
    def sum(self) -> int:
        return self._m + self._n

    def __str__(self) -> str:
        return f"{self._m} + {self._n} = {self.sum}"


def main() -> None:
    x = randint(-10, 10)
    y = randint(-10, 10)

    cal = Calculator(x, y)

    print(cal)
    print(cal.sum)


if __name__ == "__main__":
    main()
