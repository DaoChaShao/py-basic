from sqlalchemy import create_engine

import faker
import pandas as pd
import random
import urllib.parse

fake_maker = faker.Faker()


def datamaker():
    data = {
        "Name": [fake_maker.last_name() for _ in range(10)],
        "Age": [random.randint(18, 65) for _ in range(10)],
        "City": [fake_maker.city() for _ in range(10)],
    }
    # print(data)
    return data


def data_transfer(data):
    df = pd.DataFrame(data)
    # print(df)
    return df


def db_engine_creator():
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


def db_writer(df, engine, table_name, schema_name):
    df.to_sql(table_name, engine, schema=schema_name, if_exists="replace", index=False)
    print(f"Data has been written to {table_name} table in database.")


def db_reader(engine, table_name, schema_name):
    # console: psql -U postgres -h localhost -p 9527 -d postgres
    df = pd.read_sql(f"Select * from {schema_name}.{table_name}", engine)
    print(df)


def main():
    # making fake data
    faker_data = datamaker()
    # transferring data to database
    df_data = data_transfer(faker_data)
    # creating database engine
    engine = db_engine_creator()

    # writing data to database
    table_name = "users"
    schema_name = "public"
    db_writer(df_data, engine, table_name, schema_name)

    # reading data from database
    db_reader(engine, table_name, schema_name)


if __name__ == "__main__":
    main()
