#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/3 23:07
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : 20240419 23 parquet 02.py
# @Desc     : 

from dataclasses import dataclass, field
from enum import Enum, auto, unique
from faker import Faker
from random import choice
from pandas import DataFrame, read_parquet


@unique
class Gender(Enum):
    MALE = auto()
    FEMALE = auto()


@dataclass
class Students(object):
    _AGE_MIN: int = 6
    _AGE_MAX: int = 24
    _data_faker: Faker = Faker()

    name: str = field(init=False)
    gender: Gender = field(init=False)
    age: int = field(init=False)

    def __post_init__(self):
        self.name = self._data_faker.first_name()
        self.gender = choice([Gender.MALE, Gender.FEMALE])
        self.age = self._data_faker.random_int(min=self._AGE_MIN, max=self._AGE_MAX)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "gender": self.gender.value,
            "age": self.age
        }


@dataclass
class ParquetHandler(object):
    def __init__(self, filepath: str) -> None:
        self._filepath = filepath

    def parquet_saver(self, dataframe: DataFrame) -> None:
        """ This function is used to save DataFrame to Parquet file """
        dataframe.to_parquet(self._filepath, engine="pyarrow", index=False)
        print(f"DataFrame has been saved to {self._filepath}")

    def parquet_loader(self) -> DataFrame:
        """ This function is used to load DataFrame from Parquet file """
        return read_parquet(self._filepath)


def main() -> None:
    """ Main Function """
    students = [Students() for _ in range(100)]
    df = DataFrame([student.to_dict() for student in students])

    FILEPATH: str = "students.parquet"
    parquet = ParquetHandler(FILEPATH)
    parquet.parquet_saver(df)

    df_load = parquet.parquet_loader()
    print(df_load)


if __name__ == "__main__":
    main()
