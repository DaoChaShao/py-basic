#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 16:09
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 thread 13 lock 05 死锁 01 lock.py
# @Desc     :

from faker import Faker
from random import uniform
from threading import Thread, Lock, current_thread
from time import sleep


def data_set(faker: Faker, amount: int) -> list[str]:
    """ Data Set Function """
    _names = [faker.first_name() for _ in range(amount)]
    return _names


def seeker(lock: Lock, index: int, names: list[str]) -> None:
    """ Seeker Function """
    lock.acquire()
    print(f"Current thread: {current_thread().ident} {current_thread().name}")

    if index >= len(names):
        print(f"End, the {index} does not exist.")
        # If the lock is not released here,
        # - the main thread will be deadlocked
        # - the program will not stop automatically
        lock.release()
        return
    print(f"{names[index]:^12} is seeked.")

    SLEEP_MIN: int = 0
    SLEEP_MAX: int = 1
    sleep(uniform(SLEEP_MIN, SLEEP_MAX))

    lock.release()


def main() -> None:
    """ Main Function """
    AMOUNT_DATA: int = 10
    data_faker: Faker = Faker()

    names: list[str] = data_set(data_faker, AMOUNT_DATA)

    lock: Lock = Lock()

    AMOUNT_THREAD: int = 20
    for j in range(AMOUNT_THREAD):
        thread = Thread(target=seeker, args=(lock, j, names), name=f"Thread-{j}")
        thread.start()


if __name__ == "__main__":
    main()
