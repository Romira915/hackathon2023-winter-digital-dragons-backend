import datetime
from .data_access_object import data_access_object
from typing import Tuple, Union


class Release_DB(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Release_DB, cls).__new__(cls)
        return cls._instance


    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance


    def get_n_releases(self, limit=100):
        query = f"SELECT * FROM releases LIMIT {limit}"
        with data_access_object.get_cursor() as cursor:
            cursor.execute(query)
            keys = cursor.column_names
            rows = cursor.fetchall()
        releases = [dict(zip(keys, row)) for row in rows]
        return releases


    def search(
            self, 
            limit=100, 
            category_ids: Union[int, Tuple] = None, pr_type: str = None,
            start_date: str = None, end_date: str = None,
            prefecture: str = None, industry: str = None, ipo_type: str = None,
            sort_field: str = None, sort_order: str = None
        ):
        query = f"SELECT r.*, c.address, c.industry, c.ipo_type FROM releases AS r LEFT JOIN companies AS c ON r.company_id = c.company_id"
        criteria = []

        if category_ids is not None:
            if isinstance(category_ids, tuple) and len(category_ids) > 0:
                criteria.append(f"main_category_id in {category_ids} OR sub_category_id in {category_ids}")
            elif isinstance(category_ids, int):
                criteria.append(f"main_category_id = {category_ids} OR sub_category_id = {category_ids}")
        if pr_type is not None:
            criteria.append(f"pr_type = '{pr_type}'")
        if prefecture is not None:
            # addressの先頭にある都道府県名が含まれるか
            criteria.append(f"address LIKE '{prefecture}%'")
        if industry is not None:
            criteria.append(f"industry LIKE '{industry}'")
        if ipo_type is not None:
            criteria.append(f"ipo_type LIKE '{ipo_type}'")
        if start_date is not None:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date =  datetime.datetime.now() if end_date is None else datetime.datetime.strptime(end_date, '%Y-%m-%d')
            criteria.append(f"created_at >= '{start_date}' AND created_at <= '{end_date}'")
        # start_dateがなく、end_dateだけある場合
        elif end_date is not None:
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            criteria.append(f"created_at <= '{end_date}'")

        if len(criteria) != 0:
            query += f" WHERE {' AND '.join(criteria)}"
        
        if sort_field is not None:
            query += f" ORDER BY {sort_field}"
            if sort_order is not None and sort_order in ['ASC', 'DESC']:
                query += f" {sort_order}"
                
        query += f" LIMIT {limit}"
        
        with data_access_object.get_cursor() as cursor:
            cursor.execute(query)
            keys = cursor.column_names
            rows = cursor.fetchall()
        results = [dict(zip(keys, row)) for row in rows]
        return results
        #return [query] + [f'main:{row["main_category_id"]}, sub:{row["sub_category_id"]}' for row in results]