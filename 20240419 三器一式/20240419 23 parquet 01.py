#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/3 22:54
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : 20240419 23 parquet 01.py
# @Desc     : pip3 install pandas pyarrow

from faker import Faker
from pandas import DataFrame, read_parquet
from random import choice


def parquet_saver(dataframe: DataFrame, filepath: str) -> None:
    """ This function is used to save DataFrame to Parquet file """
    dataframe.to_parquet(filepath, engine="pyarrow", index=False)
    print(f"DataFrame has been saved to {filepath}")


def parquet_loader(filepath: str) -> DataFrame:
    """ This function is used to load DataFrame from Parquet file """
    return read_parquet(filepath)


def main() -> None:
    """ Main Function """
    data_faker = Faker()

    AMOUNT: int = 10
    AGE_MIN: int = 6
    AGE_MAX: int = 24
    data = {
        "name": [data_faker.first_name() for _ in range(AMOUNT)],
        "gender": [choice(["Female", "Male"]) for _ in range(AMOUNT)],
        "age": [data_faker.random_int(min=AGE_MIN, max=AGE_MAX) for _ in range(AMOUNT)]
    }

    df = DataFrame(data)
    # print(df)

    # parquet_saver(df, "students.parquet")

    FILEPATH: str = "students.parquet"
    de_load = parquet_loader(FILEPATH)
    print(de_load)


if __name__ == "__main__":
    main()
