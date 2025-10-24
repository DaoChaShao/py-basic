#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/31 00:48
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 17 enum 01 enum.py
# @Desc     :

from enum import Enum, unique
from random import choice


@unique
class Gender(Enum):
    MALE = 0
    FEMALE = 1


def main() -> None:
    """ Main Function """
    # print(Gender.MALE)
    # print(Gender.MALE.value)

    gender: int = choice([Gender.MALE.value, Gender.FEMALE.value, 2])

    match gender:
        case 0:
            print("You should enter the bathroom for MALE.")
        case 1:
            print("You should enter the bathroom for FEMALE.")
        case _:
            print("Invalid physical gender.")


if __name__ == "__main__":
    main()
