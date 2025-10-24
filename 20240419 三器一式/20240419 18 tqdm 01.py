#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/31 02:11
# @Author   : Shawn
# @Version  : Version 1.0
# @Fime     : 20240419 18 tqdm 01.py
# @Desc     : 

from dataclasses import dataclass, field
from urllib.parse import quote

from sqlalchemy import Engine, create_engine, text, CursorResult
from tqdm import tqdm


@dataclass
class SQLReader(object):
    """
    Read the data from postgresql
    1. pip3 install psycopg2-binary
    """
    _SCHEMA: str
    _TABLE: str

    _DB_NAME: str = "postgres"
    _DB_HOST: str = "localhost"
    _DB_PORT: str = "9527"
    _DB_USER: str = "postgres"
    _DB_PASSWORD: str = field(default_factory=lambda: quote("123@"))
    _RUNNING_TYPE: str = "psycopg2"
    _engine: Engine = field(init=False)

    def __post_init__(self) -> None:
        """Initialize the SQLAlchemy engine."""
        self._engine = create_engine(
            f"postgresql+{self._RUNNING_TYPE}://"
            f"{self._DB_USER}:{self._DB_PASSWORD}@"
            f"{self._DB_HOST}:{self._DB_PORT}/"
            f"{self._DB_NAME}"
        )

    @property
    def _data_length(self) -> int:
        """ Get the length of the data """
        _query = text(f"SELECT COUNT(*) AS total FROM {self._SCHEMA}.{self._TABLE}")
        with self._engine.connect() as connection:
            return connection.execute(_query).scalar()

    def read(self, col_x: str, col_y: str, col_z: str) -> list:
        """ Read the data from SQL """
        _query = text(f"SELECT {col_x}, {col_y}, {col_z} FROM {self._SCHEMA}.{self._TABLE}")
        _chunks = []

        with self._engine.connect() as connection:
            # Using a cursor to fetch rows in chunks
            result: CursorResult = connection.execution_options(stream_results=True).execute(_query)
            _total = self._data_length

            with tqdm(total=_total, desc="Data reading: ", unit="rows") as pbar:
                for row in result:
                    _chunks.append(row)
                    pbar.update(1)

        # Convert rows to a DataFrame
        return _chunks


def main() -> None:
    """ Main Function """
    SCHEMA = "public"
    TABLE = "porto_trajectory_dataset"
    COLUMN_X = "taxi_id"
    COLUMN_Y = "timestamp"
    COLUMN_Z = "polyline"
    sql = SQLReader(SCHEMA, TABLE)
    data = sql.read(COLUMN_X, COLUMN_Y, COLUMN_Z)
    # print(data)


if __name__ == "__main__":
    main()
