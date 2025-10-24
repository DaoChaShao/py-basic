from sqlalchemy import (
    create_engine,
    MetaData,
    Table, Column,
    Date, String, Text, Numeric,
    inspect
)

import faker
import random
import urllib.parse

data_maker = faker.Faker()
metadata = MetaData()


def engine_creator():
    db_name = "postgres"
    db_host = "localhost"
    db_port = "9527"
    db_user = "postgres"
    db_password = urllib.parse.quote("123@")  # password with special character
    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    # print(engine)
    return engine


def table_builder(table_name):
    table = Table(
        table_name,
        metadata,
        Column("id", String(10), primary_key=True),
        Column("name", String(50)),
        Column("birthday", Date),
        Column("gender", String(10)),
        Column("class", Text),
        Column("chinese", Numeric(5, 2)),
        Column("math", Numeric(5, 2)),
        Column("english", Numeric(5, 2)),
    )
    return table


def data_inserter(engine, table, data_volume):
    # insert data
    with engine.connect() as connection:
        for i in range(data_volume):
            student = {
                "id": "s" + "".join(random.choices("0123456789", k=8)),
                "name": data_maker.last_name(),
                "birthday": data_maker.date_of_birth(minimum_age=6, maximum_age=22),
                "gender": random.choice(["Male", "Female"]),
                "class": random.choice(["A", "B", "C"]),
                "chinese": round(random.uniform(30, 100), 2),
                "math": round(random.uniform(30, 100), 2),
                "english": round(random.uniform(30, 100), 2)
            }
            connection.execute(table.insert().values(student))
            print(f"Inserted data {i + 1} / {data_volume}")
        connection.commit()
    print("Data insertion completed.")


def existing_table_checker(engine, table_name, mode="append"):
    inspector = inspect(engine)
    if table_name not in inspector.get_table_names():
        print(f"Table {table_name} does not exist, creating new one!")
        metadata.create_all(engine)
        print(f"Table {table_name} created.")
    else:
        match mode:
            case "overwrite":
                print(f"Table {table_name} already exists, overwriting...")
                metadata.drop_all(engine)
                metadata.create_all(engine)
            case "append":
                print(f"Table {table_name} already exists, appending...")
                pass
            case _:
                print(f"Invalid mode: {mode}. Please use 'overwrite' or 'append'.")


def mian():
    # create engine
    engine = engine_creator()
    # build table
    table_name = "students"
    table = table_builder(table_name)
    # check table
    existing_table_checker(engine, table_name, mode="overwrite")
    # insert data
    data_volume = 10
    data_inserter(engine, table, data_volume)


if __name__ == "__main__":
    mian()
