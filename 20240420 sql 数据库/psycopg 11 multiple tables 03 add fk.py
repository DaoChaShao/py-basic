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


def foreign_key_adder(
        engine,
        child_table_name, foreign_key_name, child_column_name,
        parent_table_name, parent_column_name
):
    with engine.connect() as connection:
        connection.execute(
            text(
                f"alter table {child_table_name} "
                f"add constraint {foreign_key_name} "
                f"foreign key ({child_column_name}) "
                f"references {parent_table_name}({parent_column_name}) "
                # cascade can be subsituted with "set null", "restrict" or "no action"
                f"on delete cascade on update cascade"
            )
        )
        connection.commit()
        print(f"Foreign key {foreign_key_name} added to table {child_table_name}, column {child_column_name}")


def main():
    # create sql engine
    engine = engine_creator()

    # check foreign keys of the table
    table_name = "db_student"
    foreign_key_checker(engine, table_name)

    # add foreign key to the table
    child_table_name = "db_student"
    foreign_key_name = "db_student_class_id_fkey"
    child_column_name = "class_id"
    parent_table_name = "db_class"
    parent_column_name = "id"
    foreign_key_adder(
        engine,
        child_table_name, foreign_key_name, child_column_name,
        parent_table_name, parent_column_name
    )


if __name__ == "__main__":
    main()
