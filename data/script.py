import json
import csv
import requests
import os
from dotenv import load_dotenv

def fetch_data(page):
    token = os.environ["API_TOKEN"]
    base_url = os.environ["API_BASE_URL"]
    headers = { "Authorization": f"Bearer {token}" }
    res = requests.get(f"{base_url}/releases?page={page}", headers=headers)
    return res.content.decode()

def convert_to_csv(page):
    res = fetch_data(page)
    data = json.loads(res)
    data_file = open(f"release_{page}.csv", 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for emp in data:
        if count == 0:
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(emp.values())
    return

load_dotenv()
for page in list(range(1, 11)):
    convert_to_csv(page)