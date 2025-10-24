"""
先安装 PostgresSQL 的客户端工具，以便包含 pg_config 工具
brew install postgresql
然后安装 psycopg2 库
pip install psycopg2
"""

import psycopg2


def db_connector():
    # 连接到数据库
    connection = psycopg2.connect(
        host="localhost",
        port="9527",
        database="postgres",  # 你的数据库名称
        user="postgres",  # 你的数据库用户名
        password="123@"  # 你的数据库密码
    )
    return connection


def db_query(table_name, schema_name, connection):
    # 创建一个游标对象
    cursor = connection.cursor()
    # 执行 SQL 查询
    cursor.execute(f"Select * from {schema_name}.{table_name};")
    # 获取查询结果
    content = cursor.fetchall()
    return cursor, content


def query_terminator(connection, cursor):
    # 关闭游标和连接
    cursor.close()
    connection.close()


def main():
    # connect to database
    connection = db_connector()
    # query data from table
    table_name = "tab_test"
    schema_name = "public"
    cursor, content = db_query(table_name, schema_name, connection)
    # print query result
    for row in content:
        print(row)

    # terminate connection
    query_terminator(connection, cursor)


if __name__ == "__main__":
    main()
