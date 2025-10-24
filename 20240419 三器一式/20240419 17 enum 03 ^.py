#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/31 01:35
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 17 enum 03 ^.py
# @Desc     : 
from enum import unique, Flag, auto
from random import choice


@unique
class Switch(Flag):
    """ Switch Enum """
    ON = auto()
    OFF = auto()
    PAUSE = auto()


def main() -> None:
    """ Main Function """
    # | is the symbol for combining
    status = Switch.ON | Switch.OFF

    option: Switch = choice([Switch.ON, Switch.OFF, Switch.PAUSE])
    print(option)
    # print(option ^ status)

    # ^ is the symbol for changing (按位异)
    match switch := option ^ status:
        case Switch.ON:
            print(f"Switch is {switch}.")
        case Switch.OFF:
            print(f"Switch is {switch}.")
        case _:
            print(f"The machine is fucked.")


if __name__ == "__main__":
    main()
