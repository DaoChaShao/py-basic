#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 14:08
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 thread 10.py
# @Desc     :

from faker import Faker
from threading import Thread


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

    threads: list[Thread] = []
    for name in names:
        name = Thread(target=addition, args=(AMOUNT_DATA, name))
        threads.append(name)
        name.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
