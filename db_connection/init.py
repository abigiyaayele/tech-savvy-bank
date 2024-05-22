# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from google_play_scraper import app, reviews_all
import psycopg2
import time
from urllib.error import URLError
from requests.exceptions import RequestException

# Define a custom NotFoundError in case the google_play_scraper package doesn't have it
class NotFoundError(Exception):
    pass

# Function to fetch app info and reviews with retry mechanism
def fetch_app_data(app_id, retries=3, delay=5):
    for i in range(retries):
        try:
            app_info = app(app_id)
            reviews = reviews_all(app_id)
            return app_info, reviews
        except (URLError, RequestException) as e:
            print(f"Attempt {i+1} failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
        except Exception as e:
            if "404" in str(e):
                raise NotFoundError(f"App not found with ID: {app_id}")
            else:
                raise
    raise Exception("Failed to fetch data after multiple attempts.")

# Function to classify time of day
def classify_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 24:
        return 'Evening'
    else:
        return 'Night'

# Function to load and transform ads data
def load_and_transform_ads_data(filepath):
    ads_data = pd.read_excel(filepath)
    ads_data['post_date'] = pd.to_datetime(ads_data['Date'])
    ads_data['time_of_day'] = ads_data['post_date'].dt.hour.apply(classify_time_of_day)
    return ads_data

# Function to load reviews data
def load_reviews_data(filepath):
    reviews_df = pd.read_excel(filepath)
    return reviews_df

# Function to save data to SQL tables
def save_to_sql(engine, ads_data, reviews_df, app_data_df):
    ads_data.to_sql('tikvah_ads', engine, if_exists='append', index=False)
    reviews_df.to_sql('google_play_reviews', engine, if_exists='replace', index=False)
    app_data_df.to_sql('google_play_app_data', engine, if_exists='replace', index=False)
    print("Data saved successfully.")

# Function to load data from the database
def load_data_from_db(engine):
    ads_data = pd.read_sql('SELECT * FROM tikvah_ads', engine)
    reviews_df = pd.read_sql('SELECT * FROM google_play_reviews', engine)
    return ads_data, reviews_df

# Main ETL process
def etl_process(app_id, ads_filepath, reviews_filepath, db_config):
    # Load and transform data
    ads_data = load_and_transform_ads_data(ads_filepath)
    reviews_df = load_reviews_data(reviews_filepath)

    # Fetch app information and reviews
    app_info, reviews = fetch_app_data(app_id)

    if app_info and reviews:
        # Construct DataFrames
        app_data = {
            'date': pd.Timestamp.now(),
            'total_reviews': app_info['reviews'],
            'rating': app_info['score'],
            'installs': app_info['installs']
        }
        app_data_df = pd.DataFrame([app_data])

        # Create reviews DataFrame with specified column names
        reviews_df = pd.DataFrame(reviews, columns=[
            'reviewId', 'userName', 'userImage', 'thumbsUp', 'reviewCreatedVersion',
            'at', 'replyContent', 'repliedAt', 'appVersion', 'score', 'Comments',
            'Keywords', 'LDA_Category', 'Sentiment', 'Insight'])

        # Construct the database URL
        db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["name"]}'

        # Create the SQLAlchemy engine
        engine = create_engine(db_url)

        # Save data to SQL tables
        save_to_sql(engine, ads_data, reviews_df, app_data_df)

        # Load data from the database
        ads_data, reviews_df = load_data_from_db(engine)
    else:
        print("No data to save.")

# Execution
if __name__ == "__main__":
    # Database configuration
    db_config = {
        'host': 'localhost',
        'port': '5432',
        'name': 'tickvah_banks_ads',
        'user': 'postgres',
        'password': 'ocho'
    }

    # Filepaths
    ads_filepath = 'data/BANKS AD DATA.xlsx'
    reviews_filepath = 'data/Apollo android review data.xlsx'

    # App ID
    app_id = 'com.boa.boaMobileBanking'  # Modify as per actual app ID

    # Run the ETL process
    etl_process(app_id, ads_filepath, reviews_filepath, db_config)
