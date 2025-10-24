from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

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


def session_initializer(engine):
    session_init = sessionmaker(bind=engine)
    return session_init


def view_querier(view_name, session_init):
    with session_init() as session:
        lines = session.execute(text(f"SELECT * FROM {view_name};")).fetchall()

        cols_name = ["Name", "Chinese", "Math", "English"]
        df = pd.DataFrame(lines, columns=cols_name)
        df.index = df.index + 1
        print(df)


def main():
    # create engine
    engine = engine_creator()
    # initialize session
    session_init = session_initializer(engine)
    # query the view data
    view_name = "view_score"
    view_querier(view_name, session_init)


if __name__ == "__main__":
    main()
