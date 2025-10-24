"""
brew link postgresql@17
如果psql 命令仍然显示为旧版本（14），
是因为 PostgresSQL 17 版本被安装为 keg-only（独立安装），
并没有自动加入到你的系统 PATH 中
运行以下命令将 PostgresSQL 17 添加到你的 PATH 中：
echo 'export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
"""

import psycopg2
import pandas as pd


def db_connector():
    connection = psycopg2.connect(
        database="postgres",
        host="localhost",
        port="9527",
        user="postgres",
        password="123@",
    )
    return connection


def db_query(table_name, schema_name, connection):
    """
    cursor.description:
    这是一个包含元组的列表，每个元组描述了查询结果中的一列。
    每个元组的结构如下：
    (name, type_code, display_size, internal_size, precision, scale, null_ok)
    这些字段是由 psycopg2 用于描述每一列的属性：
    name：列名
    type_code：数据类型的代码
    display_size：显示的大小
    internal_size：内部存储大小
    precision：精度
    scale：小数位数
    null_ok：是否允许 NULL 值
    """
    # bash：psql -U postgres -h localhost -p 9527 -d postgres
    # bash：\l  # 查看数据库列表
    # bash：\dt  # 查看表列表
    # bash：\dn  # 查看模式列表
    # 创建一个游标对象
    cursor = connection.cursor()
    # 执行 SQL 查询
    cursor.execute(f"Select * From {schema_name}.{table_name};")
    # 获取查询结果
    content = cursor.fetchall()
    # 获取列结果
    cols_index = [desc[0] for desc in cursor.description]
    return cursor, content, cols_index


def db_transfer(content, cols_index):
    df = pd.DataFrame(content, columns=cols_index)
    print(df)


def query_terminator(connection, cursor):
    # 关闭游标和连接
    cursor.close()
    connection.close()


def main():
    # create connection
    connection = db_connector()
    # query data and get rows and cols
    table_name = "tab_test"
    schema_name = "public"
    cursor, content, cols = db_query(table_name, schema_name, connection)
    # transfer data to pandas dataframe
    db_transfer(content, cols)

    # terminate connection
    query_terminator(connection, cursor)


if __name__ == "__main__":
    main()
