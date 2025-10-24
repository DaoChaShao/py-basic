#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/25 17:31
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 11 海象赋值 02.py
# @Desc     :

from faker import Faker
from random import choice
from typing import Literal

GenderType = Literal["Female", "Male"]


def main() -> None:
    """ Main Function """
    data_faker = Faker()

    AMOUNT: int = 5
    AGE_MIN: int = 16
    AGE_MAX: int = 20
    ages = [data_faker.random_int(AGE_MIN, AGE_MAX) for _ in range(AMOUNT)]

    AGE_RESTRICTION = 18
    match age := choice(ages):
        case age if age >= AGE_RESTRICTION:
            print("You are allowed to enter the bar.")
        case _:
            print("You are not allowed to enter the bar.")


if __name__ == "__main__":
    main()
