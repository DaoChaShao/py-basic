#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/2 01:50
# @Author   : Shawn
# @Version  : Version 1.0
# @Fime     : 20240419 21 loop 02.py
# @Desc     : 

from dataclasses import dataclass


@dataclass
class Loop():
    _x: int
    _y: int
    _amount: int

    def __post_init__(self):
        while self._amount:
            self._x += 1
            self._amount -= 1
        else:
            self._y += 1

    def __str__(self):
        return f"{self._x}, {self._y}"


def main() -> None:
    """ Main Function """
    X: int = 1
    Y: int = 1
    AMOUNT: int = 10
    loop = Loop(X, Y, AMOUNT)
    print(loop)


if __name__ == "__main__":
    main()
