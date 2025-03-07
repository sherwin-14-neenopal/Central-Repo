import os
import pandas as pd
import psycopg2

from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('DB_USER')
password= os.getenv('DB_PASSWORD')
host= os.getenv('DB_HOST')
port= os.getenv('DB_PORT')

def create_postgres_connection(user, password, host, port, db_name=None):
    try:
        conn = psycopg2.connect(
            dbname=db_name if db_name else 'postgres',
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def create_postgres_database(user, password, host, port, db_name):
    conn = create_postgres_connection(user, password, host, port)
    if conn is not None:
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
                print(f"PostgreSQL Database '{db_name}' created successfully.")
        conn.close()

def create_postgres_table_from_dataframe(conn, df, table_name):
    with conn.cursor() as cur:
        create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({});").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(sql.Identifier(col) + sql.SQL(' TEXT') for col in df.columns)
        )
        cur.execute(create_table_query)

        for index, row in df.iterrows():
            insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
                sql.Identifier(table_name),
                sql.SQL(', ').join(sql.Identifier(col) for col in df.columns),
                sql.SQL(', ').join(sql.Placeholder() * len(row))
            )
            cur.execute(insert_query, tuple(row))



