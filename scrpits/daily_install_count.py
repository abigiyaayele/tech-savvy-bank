import pandas as pd
from sqlalchemy import create_engine
from google_play_scraper import app, reviews_all
import os
from datetime import datetime, timedelta
import csv
import time
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Script for counting install count using CSV file

CSV_FILE = 'data/installations.csv'

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as csvfile:
            fieldnames = ['date', 'installation_count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

def fetch_installation_count(date):
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['date'] == date.isoformat():
                return int(row['installation_count'])
    return 0  # Return 0 if the count for the given date is not found

def save_installation_count_for_date(date, count):
    # Read all rows into memory to modify specific ones
    rows = []
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    
    # Check if date already exists
    found = False
    for row in rows:
        if row['date'] == date.isoformat():
            row['installation_count'] = str(int(row['installation_count']) + count)
            found = True
            break
    
    # If date not found, add a new row
    if not found:
        rows.append({'date': date.isoformat(), 'installation_count': count})

    # Write all rows back to the CSV
    with open(CSV_FILE, 'w', newline='') as csvfile:
        fieldnames = ['date', 'installation_count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Installation count saved successfully for", date)

if __name__ == '__main__':
    init_csv()
    app_id = 'com.boa.boaMobileBanking'  
    start_date = datetime(2020, 1, 12).date()
    current_date = start_date
    while current_date <= datetime.today().date():
        try:
            playstore_data = app(app_id)
            installs = playstore_data['realInstalls']
        except Exception as e:
            print(f"Failed to fetch data for {app_id}: {e}")
            installs = 0
        count = fetch_installation_count(current_date) + installs
        save_installation_count_for_date(current_date, count)
        current_date += timedelta(days=1)