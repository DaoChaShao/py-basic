#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/2 23:41
# @Author   : Shawn
# @Version  : Version 1.0
# @Fime     : 20240419 01 装饰器 04了类的装饰器.py
# @Desc     : 

from dataclasses import dataclass
from random import randint


class Timer(object):
    """ Timer """

    def __init__(self, precision: int = 6):
        self._precision = precision

    def __call__(self, func):
        from time import perf_counter
        def wrapper(*args, **kwargs):
            print("*" * 50)
            print(f"Function {func.__name__} is starting...")
            print("-" * 50)
            _start = perf_counter()
            result = func(*args, **kwargs)
            _end = perf_counter()
            print(result)
            print("-" * 50)
            print(f"Function {func.__name__} has ended.")
            print("-" * 50)
            print(f"Time elapsed: {(_end - _start):.{self._precision}f} seconds")
            print("*" * 50)
            return result

        return wrapper


@Timer(8)
@dataclass
class Addition(object):
    """ Addition """
    _X: int
    _Y: int
    _result: int = 0

    def __post_init__(self):
        self._result = self._X + self._Y

    def __str__(self) -> str:
        return f"{self._X} + {self._Y} = {self._result}"


def main() -> None:
    """ Main Function """
    X: int = randint(1, 10)
    Y: int = randint(1, 10)

    Addition(X, Y)


if __name__ == "__main__":
    main()
