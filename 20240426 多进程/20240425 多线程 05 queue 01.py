#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 22:56
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240425 多线程 05 queue 01.py
# @Desc     :

from faker import Faker
from random import uniform
from multiprocessing import Queue, Process
from time import sleep
from typing import override


def producer(faker: Faker, q: Queue, amount: int, delays: list[float]) -> None:
    for i in range(amount):
        phone_number = faker.phone_number()
        q.put(phone_number)
        print(f"Producing {i + 1:>02d}: {phone_number}.")
        sleep(delays[i])


def consumer(q: Queue, amount: int, delays: list[float]) -> None:
    for i in range(amount):
        phone_number = q.get()
        print(f"{phone_number} is consumed.")
        sleep(delays[i])


class MultipleProcessor(Process):
    def __init__(self, target, args) -> None:
        super().__init__()
        self._target = target
        self._args = args

    @override
    def run(self) -> None:
        self._target(*self._args)


def main() -> None:
    """ Main Function """
    # PHONE_NUMBERS: list[str] = []

    AMOUNT_DATA = 10
    SECOND_MIN = 0
    SECOND_MAX = 1
    DELAYS: list[float] = [uniform(SECOND_MIN, SECOND_MAX) for _ in range(AMOUNT_DATA)]

    data_faker = Faker()
    q = Queue()

    maker = MultipleProcessor(target=producer, args=(data_faker, q, AMOUNT_DATA, DELAYS))
    reader = MultipleProcessor(target=consumer, args=(q, AMOUNT_DATA, DELAYS))

    maker.start()
    reader.start()

    maker.join()
    reader.join()

    maker.terminate()
    reader.terminate()


if __name__ == "__main__":
    main()
