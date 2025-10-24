#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 14:59
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 thread 12 类线程 02.py
# @Desc     :

from faker import Faker
from threading import Thread
from typing import Callable, override


class Threader(Thread):
    """ Threader Class """

    def __init__(self, func: Callable[[int, str], None], amount: int, thread_name: str) -> None:
        super().__init__()
        self._func = func
        self._amount = amount
        self._name = thread_name

    @override
    def run(self):
        self._func(self._amount, self._name)

    @classmethod
    def executor(cls, func: Callable[[int, str], None], amount: int, thread_names: list[str]) -> None:
        _threads: list[Threader] = []
        for _name in thread_names:
            _thread = cls(func, amount, _name)
            _threads.append(_thread)
            _thread.start()

        for _thread in _threads:
            _thread.join()


def addition(amount: int, thread_name: str) -> None:
    """ Addition Function """
    _sum = 0
    for _ in range(amount):
        _sum += 1
        print(f"{thread_name} : {_sum}")


def main() -> None:
    """ Main Function """
    AMOUNT_DATA: int = 100

    data_faker: Faker = Faker()

    AMOUNT_NAME: int = 2
    names: list[str] = [data_faker.first_name() for _ in range(AMOUNT_NAME)]

    Threader.executor(addition, AMOUNT_DATA, names)


if __name__ == "__main__":
    main()
