#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 14:48
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 thread 12 类线程 01.py
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

    threads: list[Threader] = []
    for name in names:
        name = Threader(addition, AMOUNT_DATA, name)
        threads.append(name)
        name.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
