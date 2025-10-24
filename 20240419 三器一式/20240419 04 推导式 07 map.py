from random import randint


def lst_gen() -> tuple[list[int], list[int]]:
    _num_min = 1
    _num_max = 100
    _amount = 10
    lst_x = [randint(_num_min, _num_max) for _ in range(_amount)]
    lst_y = [randint(_num_min, _num_max) for _ in range(_amount)]
    return lst_x, lst_y


def good(num: int) -> int:
    return num * 2


def nice(m: int, n: int) -> int:
    return m + n if m > 50 and n > 50 else 0


def without_for_single(lst: list) -> map:
    return map(good, lst)


def without_for_double(x: list, y: list) -> map:
    return map(nice, x, y)


def main() -> None:
    x, y = lst_gen()
    # for item in without_for_single(x):
    #     print(item)

    for i, item in enumerate(without_for_double(x, y)):
        print(f"The {i + 1:>02d} number is {item:>3d}.")


if __name__ == "__main__":
    main()
