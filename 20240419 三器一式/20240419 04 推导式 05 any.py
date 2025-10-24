from random import randint


def lst_gen(amount: int) -> list:
    return [i for i in range(amount)]


def good(number: int) -> bool:
    return number % 2 == 0


def with_for(lst: list) -> list:
    result = []
    for i in lst:
        if good(i):
            result.append(i)
    return result


def without_for(lst: list) -> list:
    return [i for i in lst if good(i)]


def without_for_any(lst: list) -> bool:
    return any(good(i) for i in lst)


def main() -> None:
    lst = lst_gen(100)

    num_lst = [randint(0, 100) for _ in range(1)]

    print("Time duration with for: ", with_for(lst))
    print("Time duration without for: ", without_for(lst))

    print(without_for_any(num_lst))


if __name__ == "__main__":
    main()
