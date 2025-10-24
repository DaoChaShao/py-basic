#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 17:14
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 03 asyncio 01.py
# @Desc     :

from asyncio import ensure_future, get_event_loop, sleep, wait
from random import uniform


async def indicator(delay: float) -> None:
    """ Indicator Function """
    print(1)
    await sleep(delay)
    print(2)


async def demonstrator(delay: float) -> None:
    """ Demonstrator Function """
    print(3)
    await sleep(delay)
    print(4)


def main() -> None:
    """ Main Function """
    DELAY_DEFAULT: int = 2
    tasks = [
        ensure_future(indicator(DELAY_DEFAULT)),
        ensure_future(demonstrator(DELAY_DEFAULT)),
    ]

    loop = get_event_loop()
    loop.run_until_complete(wait(tasks))


if __name__ == "__main__":
    main()
