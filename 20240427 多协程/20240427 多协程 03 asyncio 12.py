#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/4 01:58
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : 20240427 多协程 03 asyncio 12.py
# @Desc     :

from asyncio import Event, sleep
from dataclasses import dataclass
from time import perf_counter


@dataclass
class CalculationGame(object):
    """ Calculation Game """
    _name: str
    _AMOUNT: int
    _NUMBER: int = 0
    _start: float = 0
    _end: float = 0

    async def calculate(self, event: Event) -> None:
        """ Calculate """
        # Wait for the event to be set before starting the calculation
        await event.wait()

        self._start = perf_counter()
        for _ in range(self._AMOUNT):
            self._NUMBER += 1
            await sleep(0)
        self._end = perf_counter()

    def __str__(self) -> str:
        return (f"{self._name:>12}'s result is {self._NUMBER:>08d},"
                f"elapsed {self._end - self._start:.6f} seconds.")

def main() -> None:
    """ Main Function """
    pass


if __name__ == "__main__":
    main()
