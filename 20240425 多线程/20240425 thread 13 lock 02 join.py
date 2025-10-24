#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 15:56
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 thread 13 lock 02 join.py
# @Desc     :

from faker import Faker
from threading import Thread


def addition(amount: int, num: int, thread_name: str) -> None:
    """ Addition Function """
    for _ in range(amount):
        num += 1
    print(f"{thread_name} : {num}")


def main() -> None:
    """ Main Function """
    NUMBER: int = 0
    AMOUNT_DATA: int = 1_000

    data_faker: Faker = Faker()
    AMOUNT_NAME: int = 2
    names: list[str] = [data_faker.first_name() for _ in range(AMOUNT_NAME)]

    threads: list[Thread] = []
    for name in names:
        name = Thread(target=addition, args=(AMOUNT_DATA, NUMBER, name), daemon=True)
        threads.append(name)
        name.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
