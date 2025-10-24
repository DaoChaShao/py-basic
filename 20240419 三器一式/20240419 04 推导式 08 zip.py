from faker import Faker
from random import randint, uniform

data_faker = Faker()


def lst_gen() -> tuple[list[str], list[int], list[float]]:
    _amount: int = 3
    _age_min: int = 6
    _age_max: int = 24
    _score_min: int = 0
    _score_max: int = 100
    names: list = [data_faker.first_name() for _ in range(_amount)]
    ages: list = [randint(_age_min, _age_max) for _ in range(len(names))]
    scores: list = [round(uniform(_score_min, _score_max), 2) for _ in range(len(names))]
    return names, ages, scores


def without_for(x: list[str], y: list[int], z: list[float]) -> zip:
    return zip(x, y, z)


def main() -> None:
    names, ages, scores = lst_gen()
    print("Without for loop: ", list(without_for(names, ages, scores)))

    for i, item in enumerate(without_for(names, ages, scores)):
        print(f"The {i + 1:<02d} person is {item[0]:<12}, "
              f"who is {item[1]:<02d} years old, "
              f"and has a score of {item[2]:>05.2f}.")


if __name__ == "__main__":
    main()
