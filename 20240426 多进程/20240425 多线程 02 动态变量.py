#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 18:08
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 多线程 02 动态变量.py
# @Desc     :

from dataclasses import dataclass
from faker import Faker
from multiprocessing import Process, current_process
from random import randint, uniform
from time import sleep


class Calculation(object):
    def __init__(self, x: list[int], y: list[int], s: list[float]) -> None:
        self._x: list[int] = x
        self._y: list[int] = y
        self._s: list[float] = s

    def __call__(self, *args, **kwargs):
        current = current_process()

        for i, (m, n, delay) in enumerate(zip(self._x, self._y, self._s)):
            result: int = m + n
            print(
                f"{current.pid} {current.name:^12} is running: "
                f"{i + 1:>02d} cal result: {result:>03d}."
            )
            sleep(delay)

        print("The calculation is done.")


@dataclass
class Person(object):
    amount: int
    name: str

    NUM_MIN: int = 1
    NUM_MAX: int = 100
    SECOND_MIN: float = 0
    SECOND_MAX: float = 1

    def __init__(self, amount: int, name: str) -> None:
        self._amount: int = amount
        self._name: str = name
        self._x: list[int] = []
        self._y: list[int] = []
        self._t: list[float] = []

    def __call__(self, *args, **kwargs):
        self._x = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._y = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._t = [uniform(self.SECOND_MIN, self.SECOND_MAX) for _ in range(self._amount)]
        self._process_starter()

    def _process_starter(self):
        calc = Calculation(self._x, self._y, self._t)
        process = Process(target=calc, name=self._name)
        process.start()

        print(f"{self._name} start to calculate:")


def main() -> None:
    """ Main Function """
    AMOUNT_CALC = 10
    AMOUNT_NAME = 3

    data_faker = Faker()

    names = [data_faker.first_name() for _ in range(AMOUNT_NAME)]
    for name in names:
        globals()[name] = Person(AMOUNT_CALC, name)
        globals()[name]()


if __name__ == "__main__":
    main()
