#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/31 01:03
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 17 enum 02 flag.py
# @Desc     : 

from enum import unique, Flag, auto
from random import choice


@unique
class Gender(Flag):
    """ Color Enum """
    MALE = auto()
    FEMALE = auto()
    WALMART_BAG = auto()


def main() -> None:
    """ Main Function """
    # print(Gender.MALE.value)
    # print(Gender.FEMALE.value)
    # print(Gender.WALMART_BAG.value)

    # | is the symbol for combining (按位或)
    PHYS: Gender = Gender.MALE | Gender.FEMALE

    option: Gender = choice([Gender.MALE, Gender.FEMALE, Gender.WALMART_BAG])
    match option:
        # & is the symbol for checking (按位与)
        case option if option & PHYS:
            print(f"You should enter the bathroom for {option}.")
        case _:
            print("Invalid physical gender")


if __name__ == "__main__":
    main()
