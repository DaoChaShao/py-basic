#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 22:39
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 多线程 04 pool 04.py
# @Desc     :

from dataclasses import dataclass
from faker import Faker
from multiprocessing import Pool
from os import getpid
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
                f"{participant:^12} {getpid()} is running: "
                f"{i + 1:>02d} cal result: {result:>03d}."
            )
            sleep(delay)

        print(f"The {participant} calculation is done.")

    def _data_generator(self) -> tuple[list[int], list[int], list[float]]:
        self._x = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._y = [randint(self.NUM_MIN, self.NUM_MAX) for _ in range(self._amount)]
        self._t = [uniform(self.SECOND_MIN, self.SECOND_MAX) for _ in range(self._amount)]
        return self._x, self._y, self._t


class ProcessPool(object):
    def __init__(self, process: int, lifespan: int) -> None:
        self._process = process
        self._lifespan = lifespan
        self._pool = None

    def __enter__(self) -> Pool:
        self._pool = Pool(processes=self._process, maxtasksperchild=self._lifespan)
        return self._pool

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._pool:
            self._pool.close()
            self._pool.join()


def main() -> None:
    """ Main Function """
    data_faker = Faker()

    AMOUNT_PERSON = 10
    names = [data_faker.first_name() for _ in range(AMOUNT_PERSON)]

    AMOUNT_DATA = 3
    POOL_SIZE = 3
    LIFESPAN = 2
    with ProcessPool(process=POOL_SIZE, lifespan=LIFESPAN) as pool:
        for i, name in enumerate(names):
            calculation = Calculation(AMOUNT_DATA)
            pool.apply_async(calculation, args=(name,))


if __name__ == "__main__":
    main()
