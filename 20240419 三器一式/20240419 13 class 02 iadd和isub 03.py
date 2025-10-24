#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/25 17:23
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 13 class 02 iadd和isub 03.py
# @Desc     :

from random import randint


class Counter(object):
    def __init__(self, num: int, step: int) -> None:
        self._original_num: int = num
        self._increased_num: int = num
        self._decreased_num: int = num
        self.__iadd__(step)
        self.__isub__(step)
        self._step: int = step

    def __iadd__(self, other: int) -> "Counter":
        self._increased_num += other
        return self

    def __isub__(self, other: int) -> "Counter":
        self._decreased_num -= other
        return self

    def __str__(self):
        return (f"{self._original_num} is incremented by {self._step} is {self._increased_num}\n"
                f"{self._original_num} is decremented by {self._step} is {self._decreased_num}")


def main() -> None:
    num = randint(10, 100)
    step = randint(1, 10)
    cal = Counter(num, step)
    print(cal)


if __name__ == "__main__":
    main()
