from sqlalchemy import (create_engine, MetaData,
                        text)

import urllib.parse

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


def foreign_key_checker(engine, table_name):
    with engine.connect() as connection:
        foreign_keys = connection.execute(
            text(f"select conname from pg_constraint where conrelid = '{table_name}'::regclass;")
        )
        # foreign_keys is a list of tuples, where each tuple contains only one element,
        # which is the name of the foreign key
        for i, key in enumerate(foreign_keys):
            print(f"Foreign key {i + 1}: {key[0]}")


def foreign_key_dropper(engine, table_name, foreign_key_name):
    with engine.connect() as connection:
        connection.execute(
            text(f"alter table {table_name} drop constraint if exists {foreign_key_name}")
        )
        connection.commit()
        print(f"Foreign key {foreign_key_name} dropped from table {table_name}")


def main():
    # create sql engine
    engine = engine_creator()

    # check foreign keys of the table
    table_name = "db_student"
    foreign_key_checker(engine, table_name)

    # drop foreign key from the table
    table_name = "db_student"
    foreign_key_name = "db_student_class_id_fkey"
    foreign_key_dropper(engine, table_name, foreign_key_name)


if __name__ == "__main__":
    main()
