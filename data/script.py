import json
import csv
import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()
token = os.environ["API_TOKEN"]
base_url = os.environ["API_BASE_URL"]
headers = { "Authorization": f"Bearer {token}" }

def fetch_releases(page):
    time.sleep(0.1)
    res = requests.get(f"{base_url}/releases?page={page}", headers=headers)
    return json.loads(res.content.decode())

def fetch_company_info(company_id):
    time.sleep(0.1)
    res = requests.get(f"{base_url}/companies/{company_id}", headers=headers)
    return json.loads(res.content.decode())

def convert_to_csv(page):
    release_file = open(f"releasetest_{page}.csv", 'w')
    csv_writer_release = csv.writer(release_file)
    company_file = open(f"company/company_{page}.csv", 'w')
    csv_writer_company = csv.writer(company_file)

    releases = fetch_releases(page)

    count = 0
    for release in releases:
        company_id = release["company_id"]
        company = fetch_company_info(company_id)
        if count == 0:
            release_header = release.keys()
            company_header = company.keys()
            csv_writer_release.writerow(release_header)
            csv_writer_company.writerow(company_header)
            count += 1
        csv_writer_release.writerow(release.values())
        csv_writer_company.writerow(company.values())

for page in list(range(1, 11)):
    convert_to_csv(page)