#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/25 02:47
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 13 class 10 dataclass 02.py
# @Desc     :

from dataclasses import dataclass, field
from random import randint


@dataclass
class Counter(object):
    _num: int = field(default_factory=lambda: randint(1, 10))
    _step: int = field(default=1)

    def __post_init__(self):
        self._current = self._num
        self._num += self._step

    def __repr__(self):
        return f"{self._current} is increased by {self._step} is {self._num}."

    def decorator(func):
        def wrapper():
            print("*" * 50)
            print(f"Function {func.__name__} is running: ")
            print("-" * 50)
            result = func()
            print("-" * 50)
            print(f"Function {func.__name__} is completed.")
            print("*" * 50)
            return result

        return wrapper

    decorator = staticmethod(decorator)


@Counter.decorator
def main() -> None:
    step: int = randint(1, 10)
    print(f"The step is {step}.")
    result = Counter(_step=step)
    print(
        # f"The {result.num} is increased by {step} is {result}."
        result
    )


if __name__ == "__main__":
    main()
