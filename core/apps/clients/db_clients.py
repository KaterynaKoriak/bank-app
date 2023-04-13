from collections import namedtuple

import mariadb

from config.env import DbCredentials
from core.testlib.logger import LOGGER


def create_record(obj, fields):
    Record = namedtuple("Record", fields)
    mappings = dict(zip(fields, obj))
    return Record(**mappings)


class DbClient:
    def __init__(self, db_credentials: DbCredentials = DbCredentials) -> None:
        self.credentials = db_credentials

    def __enter__(self):
        self.connection = mariadb.connect(
            user=self.credentials.DB_USER,
            password=self.credentials.DB_PASS,
            host=self.credentials.DB_HOST,
            port=self.credentials.DB_PORT,
            database=self.credentials.DB_NAME
        )
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()


def execute_db_query(query: str) -> namedtuple:
    with DbClient() as client:
        client.cursor.execute(query)
        LOGGER.info(f'Query executed - {query}')
        try:
            column_names = [desc[0] for desc in client.cursor.description]
            rows = client.cursor.fetchall()
            result = [create_record(row, column_names) for row in rows]
            LOGGER.info(f'Query result  - {result}')
        except TypeError:
            pass
        client.connection.commit()
        return result


if __name__ == '__main__':
    execute_db_query('Select * from country')