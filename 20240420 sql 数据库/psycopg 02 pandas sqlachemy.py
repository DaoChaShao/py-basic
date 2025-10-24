from sqlalchemy import create_engine, text

import pandas as pd
import urllib.parse


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


def sql_reader(engine, schema_name, table_name):
    with engine.connect() as connection:
        result = connection.execute(
            text(f"SELECT * FROM {schema_name}.{table_name}")
        )
        # get sql column names
        column_names = [row[0] for row in result.cursor.description]
        # print("Data's column names: ", column_names)
        # get sql data
        data = result.fetchall()
        # print("Data's content: ", data)
        return column_names, data


def sql_pandas_transformer(column_names, sql_data):
    dataframe = pd.DataFrame(sql_data, columns=column_names)
    return dataframe


def main():
    # create engine
    engine = engine_creator()

    # read data from table
    schema_name = "public"
    table_name = "students"
    cols, data = sql_reader(engine, schema_name, table_name)

    # transform data to pandas dataframe
    df = pd.DataFrame(data, columns=cols)
    # set index starting from 1
    df.index = df.index + 1
    print("Dataframe:\n", df)


if __name__ == "__main__":
    main()
