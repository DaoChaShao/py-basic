#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 19:46
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 多线程 03 进程类 01.py
# @Desc     :

from faker import Faker
from multiprocessing import Process, current_process
from random import randint, uniform
from time import sleep
from typing import override


class CalculationProcess(Process):
    NUM_MIN: int = 1
    NUM_MAX: int = 100
    SECOND_MIN: float = 0
    SECOND_MAX: float = 1

    def __init__(self, amount: int, process_name: str) -> None:
        super().__init__(name=process_name)
        self._amount = amount
        self._x: list[int] = []
        self._y: list[int] = []
        self._s: list[float] = []

    def __call__(self, *args, **kwargs):
        self._data_generator()
        self.start()

    def _data_generator(self) -> None:
        self._x = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._y = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._s = [uniform(self.SECOND_MIN, self.SECOND_MAX) for _ in range(self._amount)]

    @override
    def run(self) -> None:
        current = current_process()

        for i, (m, n, delay) in enumerate(zip(self._x, self._y, self._s)):
            result: int = m + n
            print(
                f"{current.pid} {current.name:^12} is running: "
                f"{i + 1:>02d} cal result: {result:>03d}."
            )
            sleep(delay)

        print("The calculation is done.")


def main() -> None:
    """ Main Function """
    data_faker = Faker()

    AMOUNT_PERSON = 2
    names = [data_faker.first_name() for _ in range(AMOUNT_PERSON)]

    AMOUNT_DATA = 10
    for name in names:
        globals()[name] = CalculationProcess(AMOUNT_DATA, name)
        globals()[name]()


if __name__ == "__main__":
    main()
