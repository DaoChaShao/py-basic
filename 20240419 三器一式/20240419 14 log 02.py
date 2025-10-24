#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/25 18:23
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240419 14 log 02.py
# @Desc     :

from faker import Faker
from logging import basicConfig, StreamHandler, info, warning
from random import choice

import re


def name_generator(faker: Faker) -> str:
    """ Generate a name """
    AMOUNT = 3
    names = [faker.name() for _ in range(AMOUNT)]
    return choice(names)


def log_indicator(file_name: str) -> None:
    """ Record the log """
    LEVEL = "INFO"
    basicConfig(
        level=LEVEL,
        format="%(asctime)s - %(levelname)-7s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            StreamHandler(),
        ],
    )


def main() -> None:
    """ Main Function """
    en_faker = Faker()
    en_name = name_generator(en_faker)
    cn_faker = Faker("zh_CN")
    cn_name = name_generator(cn_faker)

    match name := choice([en_name, cn_name]):
        case name if re.match(r"^[\u4e00-\u9fa5]+$", name):
            print(f"Chinese name is {name}")
            info(f"The checking result: Chinese. The Chinese name is {name}")
        case _:
            print(f"English name is {name}")
            warning(f"The checking result: English. The English name is {name}")


if __name__ == "__main__":
    main()
