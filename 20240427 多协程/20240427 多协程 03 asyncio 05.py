#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 18:42
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 03 asyncio 05.py
# @Desc     :

from asyncio import create_task, sleep, wait, run
from faker import Faker
from random import uniform


async def names(faker: Faker, amount: int, wait_min: float, wait_max: float, delay_default: int) -> None:
    """ Seeker Function """
    _names = [faker.name() for _ in range(amount)]

    for i, _name in enumerate(_names):
        # Simulate the time it takes to get the data via the network
        await sleep(uniform(wait_min, wait_max))
        # Simulate the time it takes to process the data
        await sleep(delay_default)
        print(f"Names {i + 1:>02d}: {_name}")


async def numbers(faker: Faker, amount: int, wait_min: float, wait_max: float, delay_default: int) -> None:
    """ Demonstrator Function """
    _numbers = [faker.phone_number() for _ in range(amount)]

    for j, _number in enumerate(_numbers):
        # Simulate the time it takes to get the data via the network
        await sleep(uniform(wait_min, wait_max))
        # Simulate the time it takes to process the data
        await sleep(delay_default)
        print(f"Telephones {j + 1:>02d}: {_number}")


async def main() -> None:
    """ Main Function """
    data_faker = Faker()

    WAIT_MIN: float = 0.5
    WAIT_MAX: float = 1.5
    DELAY_DEFAULT: int = 1
    AMOUNT_DATA: int = 10

    tasks = [
        create_task(names(data_faker, AMOUNT_DATA, WAIT_MIN, WAIT_MAX, DELAY_DEFAULT)),
        create_task(numbers(data_faker, AMOUNT_DATA, WAIT_MIN, WAIT_MAX, DELAY_DEFAULT)),
    ]

    await wait(tasks)


if __name__ == "__main__":
    run(main())
