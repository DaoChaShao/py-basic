#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 18:55
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 04 迭代器 01.py
# @Desc     :

from asyncio import run, sleep


class Generator(object):
    """ Reader Class """

    def __init__(self, max: int) -> None:
        self._count: int = 0
        self._max: int = max

    async def _lines_reader(self) -> None | int:
        await sleep(1)
        self._count += 1
        if self._count == self._max:
            return None

        return self._count

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self._lines_reader()
        if value is None:
            raise StopAsyncIteration
        return value


async def main() -> None:
    """ Main Function """
    MAX: int = 10

    async for line in Generator(MAX):
        print(line)


if __name__ == "__main__":
    run(main())
