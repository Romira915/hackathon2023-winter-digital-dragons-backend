import datetime
from .data_access_object import data_access_object


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
            category_id: int = None, pr_type: str = None,
            start_date: str = None, end_date: str = None,
            prefecture: str = None, industry: str = None, ipo_type: str = None,
        ):
        query = f"SELECT r.*, c.address, c.industry, c.ipo_type FROM releases AS r LEFT JOIN companies AS c ON r.company_id = c.company_id"
        criteria = []

        if category_id is not None:
            criteria.append(f"main_category_id = {category_id} AND sub_category_id = {category_id}")
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
        query += f" LIMIT {limit}"

        with data_access_object.get_cursor() as cursor:
            cursor.execute(query)
            keys = cursor.column_names
            rows = cursor.fetchall()
        results = [dict(zip(keys, row)) for row in rows]

        return results