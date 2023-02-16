import os

from dotenv import load_dotenv

load_dotenv()

MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
FRONTEND_ORIGIN = os.getenv('FRONTEND_ORIGIN')
