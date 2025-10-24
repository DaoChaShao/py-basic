#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/2 02:56
# @Author   : Shawn
# @Version  : Version 1.0
# @Fime     : 20240427 多协程 03 asyncio 08.py
# @Desc     : 

from asyncio import run, sleep, gather, create_task
from dataclasses import dataclass
from faker import Faker
from time import perf_counter


@dataclass
class CalculationGame(object):
    """ Calculation Game """
    _name: str
    _AMOUNT: int
    _NUMBER: int = 0
    _start: float = 0
    _end: float = 0

    async def calculate(self) -> None:
        """ Calculate """
        self._start = perf_counter()
        for _ in range(self._AMOUNT):
            self._NUMBER += 1
            await sleep(0)
        self._end = perf_counter()

    def __str__(self) -> str:
        return (f"{self._name:>12}'s result is {self._NUMBER:>08d},"
                f"elapsed {self._end - self._start:.6f} seconds.")


async def main() -> None:
    """ Main Function """
    data_faker = Faker()
    AMOUNT_NAME: int = 10
    names: list[str] = [data_faker.first_name() for _ in range(AMOUNT_NAME)]

    AMOUNT_DATA: int = 100_000

    async def game_runner(name: str) -> None:
        game = CalculationGame(name, AMOUNT_DATA)
        print(f"{name:>12} is starting...")
        await game.calculate()
        print(game)

    await gather(*(game_runner(name) for name in names))


if __name__ == "__main__":
    run(main())
