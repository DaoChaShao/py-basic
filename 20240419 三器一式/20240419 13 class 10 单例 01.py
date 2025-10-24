#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2025/1/4 18:05
# @Author   : Shawn
# @Version  : Version 1.0
# @File     : 20240419 13 class 10 单例 01.py
# @Desc     :

from dataclasses import dataclass, field
from typing import Final, final
from pandas import DataFrame
from urllib.parse import quote

from sqlalchemy import create_engine, Engine, text, Sequence, Row


@dataclass
class SQLConnection(object):
    _DB_NAME: Final[str] = "postgres"
    _DB_HOST: Final[str] = "localhost"
    _DB_PORT: Final[str] = "9527"
    _DB_USER: Final[str] = "postgres"
    _DB_PASSWORD: Final[str] = quote("123@")
    _ENGINE_TYPE: Final[str] = "psycopg2"

    _engine: Engine = field(init=False, repr=False)

    _INSTANCE = None

    def __new__(cls, *args, **kwargs) -> "SQLConnection":
        if not cls._INSTANCE:
            cls._INSTANCE = super(SQLConnection, cls).__new__(cls)
        return cls._INSTANCE

    def __post_init__(self) -> None:
        self._engine = create_engine(
            f"postgresql+{self._ENGINE_TYPE}://"
            f"{self._DB_USER}:{self._DB_PASSWORD}@"
            f"{self._DB_HOST}:{self._DB_PORT}/"
            f"{self._DB_NAME}")

    @final
    def query(self, schema_name: str, table_name: str, col_x: str, col_y: str) -> Sequence[Row]:
        """ Read the data from SQL """
        _query = text(f"SELECT {col_x}, {col_y} FROM {schema_name}.{table_name}")

        with self._engine.connect() as connection:
            return connection.execute(_query).fetchall()

    @final
    def to_dict(self, query_data) -> dict:
        """ Convert the result to dict """
        return {word: level for word, level in query_data}

    @final
    def to_df(self, query_data) -> DataFrame:
        """ Convert the result to dict """
        return DataFrame(query_data)


def main() -> None:
    """ Main Function """
    SCHEMA: str = "english"
    TABLE: str = "words"
    COLUMN_X: str = "word"
    COLUMN_Y: str = "level"

    sql = SQLConnection()

    query = sql.query(SCHEMA, TABLE, COLUMN_X, COLUMN_Y)
    print(query)

    print(sql.to_dict(query))
    print(len(sql.to_dict(query)))

    print(sql.to_df(query))


if __name__ == "__main__":
    main()
