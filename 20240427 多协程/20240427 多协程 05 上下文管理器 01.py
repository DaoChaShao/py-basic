#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 19:29
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 05 上下文管理器 01.py
# @Desc     :

from asyncio import run, sleep


class Opener(object):
    """ Opener Class """

    def __init__(self, filename: str) -> None:
        self._filename: str = filename
        self._connection: None

    async def __aenter__(self):
        print(f"Open {self._filename}")
        self._connection = await sleep(1)
        return self

    async def executor(self):
        print(f"Execute {self._filename}")
        return "RETURN"

    async def __aexit__(self, exc_type, exc, tb):
        print(f"Close {self._filename}")
        self._connection = None
        await sleep(1)


async def main() -> None:
    """ Main Function """
    FILENAME: str = "test.txt"

    async with Opener(FILENAME) as opener:
        result = await opener.executor()
        print(result)


if __name__ == "__main__":
    run(main())
