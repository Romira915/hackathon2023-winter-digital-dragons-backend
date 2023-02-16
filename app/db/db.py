from flask import Flask, jsonify
import mysql.connector
import os, json
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

db_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE'),
    'host': 'hackathon2023-winter-digital-dragons-backend-mysql-1',
    'port': 3306,
}

    
class DB():
    def __init__(self, ):
        self.table = 'test_table1'

    def connect_to_mysql(self):
        return mysql.connector.connect(**db_config)
    
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
        cnx = self.connect_to_mysql()
        cursor = cnx.cursor()
        query = f"SELECT * FROM {self.table} LIMIT {limit}"
        cursor.execute(query)
        
        releases = [self.to_dict(*c) for c in cursor]
        
        cursor.close()
        cnx.close()
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

        cnx = self.connect_to_mysql()
        cursor = cnx.cursor()
        cursor.execute(query)
        resulst = [self.to_dict(*c) for c in cursor]
        
        cursor.close()
        cnx.close()
        
        return results

def main():
    db = DB()
    print(db.get_all())

if __name__ == "__main__":
    main()