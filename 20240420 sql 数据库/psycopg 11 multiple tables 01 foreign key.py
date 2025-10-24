from sqlalchemy import (
    create_engine,
    MetaData,
    Table, Column,
    SmallInteger, Text, Date, Numeric,
    ForeignKey,
    inspect,
    CheckConstraint
)

import faker
import random
import urllib.parse

data_faker = faker.Faker()
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


def parent_table_builder(table_name):
    table = Table(
        table_name,
        metadata,
        Column("id", SmallInteger, autoincrement=True, primary_key=True),
        Column("name", Text, nullable=False, unique=True),
    )
    return table


def parent_data_inserter(engine, table, parent_category):
    # insert data
    with engine.connect() as connection:
        for i, name in enumerate(parent_category):
            student = {
                "name": parent_category[i],
            }
            connection.execute(table.insert().values(student))
            print(f"Inserted data {i + 1:02d} / {len(parent_category)}")
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


def child_table_builder(table_name, foreign_key_name=None):
    table = Table(
        table_name,
        metadata,
        Column("id", SmallInteger, autoincrement=True, primary_key=True, ),
        Column("name", Text, unique=True),
        Column("birthday", Date),
        Column("gender", Text),
        Column("age", SmallInteger, CheckConstraint("age between 1 and 120"), nullable=False),
        Column("class_id", SmallInteger, ForeignKey(f"{foreign_key_name}.id")),
        Column("chinese", Numeric(5, 2)),
        Column("math", Numeric(5, 2)),
        Column("english", Numeric(5, 2)),
    )
    return table


def child_data_inserter(engine, table, data_amount, parent_category):
    age_min = 6
    age_max = 22
    # insert data
    with engine.connect() as connection:
        for i in range(data_amount):
            student = {
                "name": data_faker.last_name(),
                "birthday": data_faker.date_of_birth(minimum_age=age_min, maximum_age=age_max),
                "gender": random.choice(["Male", "Female"]),
                "age": random.randint(age_min, age_max),
                "class_id": random.randint(1, len(parent_category)),
                "chinese": round(random.uniform(0, 100), 2),
                "math": round(random.uniform(0, 100), 2),
                "english": round(random.uniform(0, 100), 2)
            }
            connection.execute(table.insert().values(student))
            print(f"Inserted data {i + 1} / {data_amount}")
        connection.commit()
    print("Data insertion completed.")


def main():
    # create engine
    engine = engine_creator()

    # build parent table
    parent_table_name = "db_class"
    # parent_table = parent_table_builder(parent_table_name)
    # check table
    # existing_table_checker(engine, parent_table_name, mode="overwrite")

    # # insert data
    parent_category = ["A", "B", "C", "D", "E"]
    # parent_data_inserter(engine, parent_table, parent_category)

    # build child table
    child_table_name = "db_student"
    child_table = child_table_builder(child_table_name, parent_table_name)
    # check table
    # existing_table_checker(engine, child_table_name, mode="overwrite")

    # # insert data
    data_amount = 20
    child_data_inserter(engine, child_table, data_amount, parent_category)


if __name__ == "__main__":
    main()
