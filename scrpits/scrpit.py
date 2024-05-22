# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database configuration
db_config = {
    'host': 'localhost',
    'port': '5432',
    'name': 'tickvah_banks_ads',
    'user': 'postgres',
    'password': 'ocho'
}

# Function to create database engine
def create_db_engine(db_config):
    db_url = f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["name"]}'
    engine = create_engine(db_url)
    return engine

# Function to load data from the database
def load_data(engine):
    ads_data = pd.read_sql('SELECT * FROM tikvah_ads', engine)
    reviews_data = pd.read_sql('SELECT * FROM google_play_reviews', engine)
    return ads_data, reviews_data

# Function for data summarization and quality assessment
def data_summary(ads_data, reviews_data):
    print("Ads Data Summary:")
    print(ads_data.describe())
    print("\nReviews Data Summary:")
    print(reviews_data.describe())

# Function for univariate analysis
def univariate_analysis(ads_data):
    plt.figure(figsize=(10, 6))
    sns.histplot(ads_data['view_count'], bins=30, kde=True)
    plt.title('Distribution of Ad View Counts')
    plt.xlabel('View Count')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=ads_data, x='view_count')
    plt.title('Box Plot of Ad View Counts')
    plt.xlabel('View Count')
    plt.show()

# Function for bivariate/multivariate analysis
def bivariate_analysis(ads_data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=ads_data, x='post_date', y='view_count', hue='time_of_day')
    plt.title('Ad View Counts by Post Date and Time of Day')
    plt.xlabel('Post Date')
    plt.ylabel('View Count')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.heatmap(ads_data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Ads Data')
    plt.show()

# Function to enrich data by merging datasets
def merge_data(ads_data, reviews_data):
    merged_data = ads_data.merge(reviews_data, left_on='post_date', right_on='at', how='inner')
    return merged_data

# Function for trend analysis
def trend_analysis(ads_data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=ads_data, x='post_date', y='view_count')
    plt.title('Trend of Ad View Counts Over Time')
    plt.xlabel('Post Date')
    plt.ylabel('View Count')
    plt.show()

# Function to visualize key insights
def visualize_key_insights(ads_data):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=ads_data, x='time_of_day', y='view_count')
    plt.title('Ad View Counts by Time of Day')
    plt.xlabel('Time of Day')
    plt.ylabel('View Count')
    plt.show()

# Function for outlier detection and visualization
def outlier_detection(ads_data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=ads_data, x='view_count')
    plt.title('Box Plot of Ad View Counts')
    plt.xlabel('View Count')
    plt.show()

# Function for additional creative visualizations
def additional_visualizations(ads_data, reviews_data):
    ads_data['day_of_week'] = ads_data['post_date'].dt.day_name()
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=ads_data, x='day_of_week', y='view_count')
    plt.title('Ad View Counts by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('View Count')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(reviews_data['score'], bins=5, kde=True)
    plt.title('Distribution of Review Scores')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=reviews_data, x='score', y='thumbsUp')
    plt.title('Review Score vs. Thumbs Up')
    plt.xlabel('Score')
    plt.ylabel('Thumbs Up')
    plt.show()

# Main function to run the analysis
def run_analysis():
    engine = create_db_engine(db_config)
    ads_data, reviews_data = load_data(engine)
    
    data_summary(ads_data, reviews_data)
    univariate_analysis(ads_data)
    bivariate_analysis(ads_data)
    
    merged_data = merge_data(ads_data, reviews_data)
    
    trend_analysis(ads_data)
    visualize_key_insights(ads_data)
    outlier_detection(ads_data)
    additional_visualizations(ads_data, reviews_data)

# Run the analysis
if __name__ == "__main__":
    run_analysis()
