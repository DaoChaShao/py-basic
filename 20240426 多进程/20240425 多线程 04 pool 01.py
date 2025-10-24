#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 21:27
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 多线程 04 pool 01.py
# @Desc     :

from dataclasses import dataclass
from faker import Faker
from multiprocessing import Pool
from random import randint, uniform
from time import sleep


@dataclass
class Calculation(object):
    amount: int

    NUM_MIN: int = 1
    NUM_MAX: int = 100
    SECOND_MIN: float = 0
    SECOND_MAX: float = 1

    def __init__(self, amount: int) -> None:
        self._amount = amount
        self._x: list[int] = []
        self._y: list[int] = []
        self._t: list[float] = []

    def __call__(self, participant: str) -> None:
        _X, _Y, _T = self._data_generator()
        for i, (m, n, delay) in enumerate(zip(_X, _Y, _T)):
            result: int = m + n
            print(
                f"{participant:^12} is running: "
                f"{i + 1:>02d} cal result: {result:>03d}."
            )
            sleep(delay)

        print(f"The {participant} calculation is done.")

    def _data_generator(self) -> tuple[list[int], list[int], list[float]]:
        self._x = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._y = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._t = [uniform(self.SECOND_MIN, self.SECOND_MAX) for _ in range(self._amount)]
        return self._x, self._y, self._t


def main() -> None:
    """ Main Function """
    data_faker = Faker()

    AMOUNT_PERSON = 3
    names = [data_faker.first_name() for _ in range(AMOUNT_PERSON)]

    AMOUNT_DATA = 10
    with Pool() as pool:
        for name in names:
            calculation = Calculation(AMOUNT_DATA)
            pool.apply_async(calculation, args=(name,))

        pool.close()
        pool.join()


if __name__ == "__main__":
    main()
