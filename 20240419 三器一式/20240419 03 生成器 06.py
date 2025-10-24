#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/25 19:21
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 03 生成器 06.py
# @Desc     : 
from faker import Faker
from logging import basicConfig, StreamHandler, info, warning


class Logger(object):
    """ Log Recorder """

    def __init__(self, level: str) -> None:
        self._log_recorder(level)

    @staticmethod
    def _log_recorder(level: str) -> None:
        basicConfig(
            level=level,
            format="%(asctime)s - %(levelname)-7s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                StreamHandler(),
            ],
        )

    @staticmethod
    def info(message_info: str) -> None:
        info(message_info)

    @staticmethod
    def warning(message_warning: str) -> None:
        warning(message_warning)


class NameGenerator(object):
    """ Generate a name """

    def __init__(self, faker: Faker, amount: int) -> None:
        self._faker: Faker = faker
        self._amount: int = amount
        self._names = (self._faker.first_name() for _ in range(self._amount))

    def __iter__(self) -> iter:
        return self

    def __next__(self):
        return next(self._names)

    def __str__(self):
        return next(self)


def main() -> None:
    """ Main Function """
    en_faker = Faker()
    AMOUNT = 3
    gen = NameGenerator(en_faker, AMOUNT)

    LEVEL: str = "INFO"
    logger = Logger(LEVEL)

    for _ in range(AMOUNT + 1):
        try:
            logger.info(f"Generated name: {gen}")
        except StopIteration:
            logger.warning("No more name to generate")


if __name__ == "__main__":
    main()
