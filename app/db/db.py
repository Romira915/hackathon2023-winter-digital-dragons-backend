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

table = 'test_table1'

def connect_to_mysql():
    return mysql.connector.connect(**db_config)

# 記事を全件取得
def get_articles(limit=100):
    cnx = connect_to_mysql()
    cursor = cnx.cursor()
    query = f"SELECT * FROM {table} LIMIT {limit}"
    cursor.execute(query)
    articles = []
    
    for (body, company_id, company_name, created_at, lead_paragraph, main_category_id, main_category_name, main_image, main_image_fastly, pr_type, release_id, sub_category_id, sub_category_name, subtitle, title, url) in cursor:
        article = {
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
        articles.append(article)
    cursor.close()
    cnx.close()
    return articles

    
if __name__ == "__main__":
    print((get_articles()))
    
