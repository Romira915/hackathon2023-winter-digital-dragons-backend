import mysql.connector
import datetime

import settings

from .data_access_object import data_access_object


class Release_DB(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Release_DB, cls).__new__(cls)
        return cls._instance


    def __init__(self):
        self.table = 'releases'
        

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance


    def to_dict(
            self,
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
        cursor = data_access_object.get_cursor()
        query = f"SELECT * FROM {self.table} LIMIT {limit}"
        cursor.execute(query)

        releases = [self.to_dict(*c) for c in cursor]

        cursor.close()
        return releases


    def search(self, limit=100, category_id: int = None, pr_type: str = None, start_date: str = None, end_date: str = None):
        criteria = []

        if category_id is not None:
            criteria.append(f"main_category_id = {category_id} AND sub_category_id = {category_id}")
        if pr_type is not None:
            criteria.append(f"pr_type = '{pr_type}'")

        if start_date is not None:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            if end_date is None:
                end_date = datetime.datetime.now()
            else:
                end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            criteria.append(f"created_at >= '{start_date}' AND created_at <= '{end_date}'")
        # start_dateがなく、end_dateだけある場合
        elif end_date is not None:
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            criteria.append(f"created_at <= '{end_date}'")

        query = f"SELECT * FROM {self.table}"
        if len(criteria) != 0:
            query += f" WHERE {' AND '.join(criteria)}"
        query += f" LIMIT {limit}"

        cursor = data_access_object.get_cursor()
        cursor.execute(query)
        
        results = [self.to_dict(*c) for c in cursor]

        cursor.close()

        return results