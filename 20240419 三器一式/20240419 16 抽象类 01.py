#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/26 16:06
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 16 抽象类 01.py
# @Desc     :

from abc import ABC, abstractmethod
from dataclasses import dataclass
from faker import Faker
from functools import wraps
from random import choice, randrange, randint
from time import perf_counter
from typing import override


class Timer(object):
    """ Decorator for timing the function """

    def __init__(self, func):
        self._func = func
        self._start: int = 0
        self._end: int = 0

        # Ensure the function signature is preserved
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        print("*" * 50)
        print(f"The function {self._func.__name__} is running:")
        print("-" * 50)
        self._start = perf_counter()
        result = self._func(*args, **kwargs)
        self._end = perf_counter()
        print("-" * 50)
        print(f"Function: {self._func.__name__} is finished with {self._elapsed():.6f} s")
        print("*" * 50)

        return result

    def _elapsed(self):
        return self._end - self._start


@dataclass
class Person(ABC):
    """ Define the parent and abstract class """
    AMOUNT = 3
    GENDER = ["Female", "male"]
    AGE_MIN = 6
    AGE_MAX = 24

    names: list[str]
    genders: list[str]
    ages: list[int]

    def __init__(self, faker: Faker) -> None:
        self.names = [faker.first_name() for _ in range(self.AMOUNT)]
        self.genders = [choice(self.GENDER) for _ in range(self.AMOUNT)]
        self.ages = [faker.random_int(min=self.AGE_MIN, max=self.AGE_MAX) for _ in range(self.AMOUNT)]

    @abstractmethod
    def greet(self) -> None:
        pass


class Pupil(Person):
    """ Define the child class of Person """
    INDEX = randrange(Person.AMOUNT)

    def __init__(self, faker: Faker) -> None:
        super().__init__(faker)
        self._name = self.names[self.INDEX]
        self._gender = self.genders[self.INDEX]
        self._age = self.ages[self.INDEX]

    @override
    def greet(self) -> None:
        print(
            f"{self._name} is talking to a teacher: \n"
            f"I am a {self._age}-years-old {self._gender} pupil."
        )


class Tutors(Person):
    """ Define the child class of Person """

    def __init__(self, faker: Faker) -> None:
        super().__init__(faker)

    def __getitem__(self, index: int):
        """ Access a specific tutor's information by index """
        return self.names[index], self.genders[index], self.ages[index]

    def __setitem__(self, index: int, value: tuple):
        """ Modify a specific tutor's information by index """
        self.names[index], self.genders[index], self.ages[index] = value
        print(f"Modified Tutor at {index}: "
              f"{self.names[index]}, {self.genders[index]} and {self.ages[index]} years old.")

    def __str__(self):
        """ Return the tutor information """
        return (
            f"Tutors: {self.names}\n"
            f"Genders: {self.genders}\n"
            f"Ages: {self.ages}"
        )

    def __repr__(self):
        """ Return the tutor information """
        return self.__str__()

    def __len__(self):
        """ Return the amount of tutors """
        return len(self.names)

    def _generator(self):
        """ A generator to iterate through the tutor information """
        return zip(self.names, self.genders, self.ages)

    @override
    def greet(self) -> None:
        """ Print greeting for each tutor using the generator """
        gen = self._generator()
        for name, gender, age in gen:
            print(f"{name}: {gender} and {age} years old.")


@Timer
def main() -> None:
    """ Main Function """
    data_faker = Faker()

    pupil = Pupil(data_faker)
    pupil.greet()

    tutors = Tutors(data_faker)
    tutors.greet()

    print(tutors)

    NEW_INDEX = randint(0, Person.AMOUNT - 1)
    NEW_NAME = "Jack"
    NEW_GENDER = "BAG"
    NEW_AGE = 12
    tutors[NEW_INDEX] = (NEW_NAME, NEW_GENDER, NEW_AGE)

    print(tutors)


if __name__ == "__main__":
    main()
