#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/25 02:10
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 13 class 10 dataclass 01.py
# @Desc     :

from dataclasses import dataclass, field
from faker import Faker
from random import randint, choice
from typing import Literal, ClassVar

data_faker = Faker()
AGE_MIN = 6
AGE_MAX = 24
GENDER = ["Female", "Male"]
GenderType = Literal["Female", "Male"]


@dataclass(order=True)
class Person(object):
    name: str = field(default_factory=lambda: data_faker.first_name())
    gender: GenderType = field(default_factory=lambda: choice(GENDER))
    age: int = field(default_factory=lambda: randint(AGE_MIN, AGE_MAX))
    amount: ClassVar[int] = 0

    @staticmethod
    def __post_init__():
        Person.amount += 1

    def decorator(func):
        def wrapper():
            print("*" * 50)
            print(f"Function {func.__name__} is running")
            print("-" * 50)
            result = func()
            print("-" * 50)
            print(f"Function {func.__name__} is completed")
            print("*" * 50)
            return result

        return wrapper

    decorator = staticmethod(decorator)


@Person.decorator
def main() -> None:
    x = Person()
    y = Person()
    print(
        f"{x.name.upper():>12} is {x.age:>02d} years old.\n"
        f"{y.name.upper():>12} is {y.age:>02d} years old."
    )

    # If the order parameter is not set to True, the comparison will fail
    print("Comparison result: ", x > y)

    print(f"The amount of Person is {Person.amount}.")


if __name__ == "__main__":
    main()
