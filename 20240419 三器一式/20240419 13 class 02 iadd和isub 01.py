from random import randint


class Counter(object):
    def __init__(self, num: int) -> None:
        self._number: int = num

    def __iadd__(self, other: int) -> "Counter":
        self._number += other
        return self

    def __isub__(self, other: int) -> "Counter":
        self._number -= other
        return self

    def __str__(self):
        return str(self._number)


def main() -> None:
    num = randint(1, 10)
    print(f"The original number is {num}.")
    cal = Counter(num)

    step: int = 1
    cal += step
    print(f"The {num} is increased by {step} is {cal}.")

    cal -= step
    print(f"The {num} is decreased by {step} is {cal}.")


if __name__ == "__main__":
    main()
