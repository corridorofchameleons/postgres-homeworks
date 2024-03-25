"""Скрипт для заполнения данными таблиц в БД Postgres."""

import os
from dotenv import load_dotenv
import psycopg2

from utils.compose_stmt import insert_data
from utils.read_csv import read_data

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')


def main():
    customers = read_data('north_data/customers_data.csv')
    employees = read_data('north_data/employees_data.csv')
    orders = read_data('north_data/orders_data.csv')

    insert_customers_stmt = insert_data(customers, 'customers_data')
    insert_employees_stmt = insert_data(employees, 'employees_data')
    insert_orders_stmt = insert_data(orders, 'orders_data')

    with psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    ) as conn:

        with conn.cursor() as cur:
            cur.execute(insert_customers_stmt)
            cur.execute(insert_employees_stmt)
            cur.execute(insert_orders_stmt)


if __name__ == '__main__':
    main()
