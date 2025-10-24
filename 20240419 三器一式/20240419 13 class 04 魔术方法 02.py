#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 13:31
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 13 class 04 魔术方法 02.py
# @Desc     :

from random import randint


class Addition(object):
    def __init__(self, x: int, y: int):
        self._m: int = x
        self._n: int = y

    def __add__(self):
        return self._m + self._n

    def __str__(self):
        return f"{self._m} + {self._n} = {self.__add__()}"

    # def __repr__(self):
    #     return f"Addition({self._m}, {self._n})"

    __repr__ = __str__


def main() -> None:
    """ Main Function """
    x: int = randint(1, 10)
    y: int = randint(1, 10)

    addition = Addition(x, y)
    print(addition)
    # print(repr(addition))


if __name__ == "__main__":
    main()
