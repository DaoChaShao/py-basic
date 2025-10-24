#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     : 2024/12/27 19:42
# @Author   : Shawn
# @Version  : V 1.0
# @Fime     : 20240427 多协程 07 sql 01.py
# @Desc     :
# 1. Need to install psycopg2 and sqlalchemy
# 2. As the psycopg2 is not support the async, so we need to use the asyncpg
# 3. pip install asyncpg

from asyncio import set_event_loop_policy, run
from dataclasses import dataclass
from logging import basicConfig, StreamHandler, info, warning
from pandas import DataFrame
from sqlalchemy import MetaData, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from tqdm import tqdm
from urllib import parse
from uvloop import EventLoopPolicy

# Global Variables
# Set the event loop policy to uvloop to speed up the asyncio
set_event_loop_policy(EventLoopPolicy())
meta = MetaData()


@dataclass
class Looger(object):
    """ Logger Function """
    level: str

    def __init__(self, level: str) -> None:
        basicConfig(
            level=level,
            format="%(asctime)s - %(name)s - %(levelname)-7s - %(message)s",
            handlers=[StreamHandler(), ],
        )

    @staticmethod
    def info(message: str) -> None:
        info(message)

    @staticmethod
    def warning(message: str) -> None:
        warning(message)


async def engine_creator(logger: Looger) -> create_async_engine:
    DB_NAME: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: str = "9527"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = parse.quote("123@")  # password with special character

    # asyncpg is used under the async engine
    # psycopg2 is used under the sync engine
    RUN_STYLE: str = "asyncpg"
    engine: AsyncEngine = create_async_engine(
        f"postgresql+{RUN_STYLE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    logger.info("SQL Engine Created")
    return engine


async def selector(engine: AsyncEngine, schema_name: str, table_name: str):
    async with engine.connect() as connection:
        select = await connection.execute(
            text(f"SELECT * FROM {schema_name}.{table_name}")
        )
        lines = select.fetchall()
        with tqdm(total=len(lines), desc="Data generating: ", unit="lines") as pbar:
            dataframe = DataFrame(lines)
            pbar.update(len(lines))
            print(dataframe)


async def main():
    # create logger
    LEVEL: str = "WARNING"
    logger = Looger(LEVEL)

    # create sql engine
    engine = await engine_creator(logger)

    # check foreign keys of the table
    SCHEMA = "public"
    TABLE = "students"
    await selector(engine, SCHEMA, TABLE)


if __name__ == "__main__":
    run(main())
