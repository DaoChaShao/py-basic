#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 13:59
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 15 文件管理器 01.py
# @Desc     :

from logging import basicConfig, StreamHandler, info, warning
from time import perf_counter, sleep
from random import randint


class Logger(object):
    def __init__(self, level: str = "INFO") -> None:
        self._log_recorder(level)

    @staticmethod
    def _log_recorder(level: str) -> None:
        basicConfig(
            level=level,
            format="%(asctime)s - %(name)s - %(levelname)-7s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                StreamHandler(),
            ],
        )

    @staticmethod
    def info(msg: str) -> None:
        info(msg)

    @staticmethod
    def warning(error: str) -> None:
        warning(error)


class Timer(object):
    def __init__(self):
        self._start: int = 0
        self._end: int = 0
        self._elapsed()

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, *args):
        self._end = perf_counter()

    def _elapsed(self):
        return self._end - self._start

    def __str__(self):
        return f"Elapsed Time: {self._elapsed():.6f} s"

    def __repr__(self):
        return self.__str__()


def func(logger: Logger) -> None:
    seconds: int = randint(1, 3)
    logger.info(f"The random seconds is {seconds}")

    sleep(seconds)


def main() -> None:
    """ Main Function """
    LEVEL: str = "INFO"
    logger = Logger(LEVEL)

    with Timer() as timer:
        print("Start")
        func(logger)
        print("End")

    print(timer)


if __name__ == "__main__":
    main()
