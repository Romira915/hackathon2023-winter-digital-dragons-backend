import mysql.connector

import settings


class DataAccessObject():
    def __init__(self) -> None:
        self.connection = None

        db_config = {
            'user': settings.MYSQL_USER,
            'password': settings.MYSQL_PASSWORD,
            'database': settings.MYSQL_DATABASE,
            'host': settings.MYSQL_HOST,
            'port': settings.MYSQL_PORT,
        }
        try:
            self.connection = mysql.connector.connect(**db_config)
        except mysql.connector.Error as err:
            raise Exception(f"Failed to connect to MySQL: {err}")

    def get_cursor(self):
        return self.connection.cursor()


data_access_object = DataAccessObject()
