#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/25 03:34
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 13 class 04 魔术方法 01.py
# @Desc     :

from faker import Faker
from random import choice, randrange
from typing import Callable, Any


class Group(object):
    def __init__(self, team: list[str], squad: list[str]) -> None:
        self._team: list[str] = team
        self.__add__(squad)

    def __add__(self, squad: list[str]):
        self._team.extend(squad)
        return self

    def __str__(self) -> str:
        return ", ".join(self._team)

    def __repr__(self):
        return f"{self.__class__.__name__}(team={self._team})"

    def __len__(self):
        return len(self._team)

    def __call__(self, name: str) -> None:
        self._team.append(name)

    def __getitem__(self, index: int) -> str:
        return self._team[index]

    def __setitem__(self, key: int, value: str) -> None:
        self._team[key] = value

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper():
            print("*" * 50)
            print(f"Function {func.__name__} is running:")
            print("-" * 50)
            result = func()
            print("-" * 50)
            print(f"Function {func.__name__} is completed")
            print("*" * 50)
            return result

        return wrapper

    decorator = staticmethod(decorator)


@Group.decorator
def main() -> None:
    """ Main Function """
    data_faker = Faker()

    amount: int = 3
    team: list[str] = [data_faker.first_name() for _ in range(amount)]
    squad: list[str] = [data_faker.first_name() for _ in range(amount)]

    group = Group(team, squad)
    print(group)

    print(f"The length of the team is {len(group)}.")
    print(repr(group))

    names = [data_faker.first_name() for _ in range(amount)]
    name = choice(names)
    group(name)
    print(group)
    print(f"The length of the team is {len(group)}.")

    index = randrange(0, len(group))
    print(group[index])

    group[index] = "Shawn"
    print(group)


if __name__ == "__main__":
    main()
