#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 14:33
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 thread 11 守护线程.py
# @Desc     :

from faker import Faker
from threading import Thread
from typing import Callable


def addition(amount: int, thread_name: str) -> None:
    """ Addition Function """
    _sum = 0
    for _ in range(amount):
        _sum += 1
        print(f"{thread_name} : {_sum}")


def threader(func: Callable[[int, str], None], amount: int, thread_names: list[str]) -> None:
    """ Threader Function """
    _threads: list[Thread] = []
    for _name in thread_names:
        _name = Thread(target=func, args=(amount, _name), daemon=True)
        _threads.append(_name)
        _name.start()

    for _thread in _threads:
        _thread.join()


def main() -> None:
    """ Main Function """
    AMOUNT_DATA: int = 100

    data_faker: Faker = Faker()
    AMOUNT_NAME: int = 2
    names: list[str] = [data_faker.first_name() for _ in range(AMOUNT_NAME)]

    threader(addition, AMOUNT_DATA, names)


if __name__ == "__main__":
    main()
