import json
import os

import mysql.connector

import settings


class Release_DB(object):
    _instance = None
    _cnx = None

    def __new__(cls, *args, **kwars):
        if not cls._instance:
            cls._instance = super(Release_DB, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.table = 'releases'
        self.db_config = {
<<<<<<< Updated upstream
            'user': os.getenv('MYSQL_USER'),
            'password': os.getenv('MYSQL_PASSWORD'),
            'database': os.getenv('MYSQL_DATABASE'),
            'host': os.getenv('MYSQL_HOST'),
            'port': os.getenv('MYSQL_PORT'),
||||||| Stash base
            'user': os.getenv('MYSQL_USER'),
            'password': os.getenv('MYSQL_PASSWORD'),
            'database': os.getenv('MYSQL_DATABASE'),
            'host': 'hackathon2023-winter-digital-dragons-backend-mysql-1',
            'port': 3306,
=======
            'user': settings.MYSQL_USER,
            'password': settings.MYSQL_PASSWORD,
            'database': settings.MYSQL_DATABASE,
            'host': settings.MYSQL_HOST,
            'port': settings.MYSQL_PORT,
>>>>>>> Stashed changes
        }
        self._cnx = self.connect_to_mysql()

    def connect_to_mysql(self):
<<<<<<< Updated upstream
        try:
            return mysql.connector.connect(**self.db_config)        
        except mysql.connector.Error as err:
            raise Exception(f"Failed to connect to MySQL: {err}")
    
||||||| Stash base
        return mysql.connector.connect(**self.db_config)
    
=======
        return mysql.connector.connect(**self.db_config)

>>>>>>> Stashed changes
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def to_dict(self,
                body,
                company_id,
                company_name,
                created_at,
                lead_paragraph,
                main_category_id,
                main_category_name,
                main_image,
                main_image_fastly,
                pr_type,
                release_id,
                sub_category_id,
                sub_category_name,
                subtitle,
                title,
                url
                ):

        release = {
            'company_name': company_name,
            'company_id': company_id,
            'release_id': release_id,
            'title': title,
            'subtitle': subtitle,
            'url': url,
            'lead_paragraph': lead_paragraph,
            'body': body,
            'main_image': main_image,
            'main_image_fastly': main_image_fastly,
            'main_category_id': main_category_id,
            'main_category_name': main_category_name,
            'sub_category_id': sub_category_id,
            'sub_category_name': sub_category_name,
            'pr_type': pr_type,
            'created_at': created_at
        }
        return release

    # 記事を全件取得

    def get_all(self, limit=100):
        cursor = self._cnx.cursor()
        query = f"SELECT * FROM {self.table} LIMIT {limit}"
        cursor.execute(query)

        releases = [self.to_dict(*c) for c in cursor]

        cursor.close()
        self._cnx.close()
        return releases

    def search(self, limit=100, main_category_id: int = None, sub_category_id: int = None, pr_type: str = None):
        criteria = ""

        if main_category_id is not None:
            criteria += f"main_category_id = {main_category_id}"
        if sub_category_id is not None:
            criteria += f" AND sub_category_id = {sub_category_id}"
        if pr_type is not None:
            criteria += f" AND pr_type = '{pr_type}'"

        query = f"SELECT * FROM {self.table}"
        if criteria != "":
            query += f" WHERE {criteria}"
        query += f" LIMIT {limit}"

        cursor = self._cnx.cursor()
        cursor.execute(query)
<<<<<<< Updated upstream
        results = [self.to_dict(*c) for c in cursor]
        
||||||| Stash base
        resulst = [self.to_dict(*c) for c in cursor]
        
=======
        results = [self.to_dict(*c) for c in cursor]

>>>>>>> Stashed changes
        cursor.close()
        self._cnx.close()
<<<<<<< Updated upstream
        
        return results
||||||| Stash base
        
        return results
=======

        return results
>>>>>>> Stashed changes
