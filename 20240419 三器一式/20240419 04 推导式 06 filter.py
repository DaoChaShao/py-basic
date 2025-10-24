from typing import Iterator


def lst_gen() -> list:
    _amount = 100
    return [i for i in range(_amount)]


def good(num: int) -> bool:
    return num % 2 == 0


def without_for(lst: list) -> Iterator[int]:
    return filter(good, lst)


def main() -> None:
    lst = lst_gen()
    object_ = without_for(lst)
    print(next(object_))


if __name__ == "__main__":
    main()
