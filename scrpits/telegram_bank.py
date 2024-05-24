import pandas as pd
import os
from google_play_scraper import Sort, reviews

def collect_all_reviews(app_id):
    all_reviews = []
    batch_size = 100
    next_token = None
    lang = 'en'
    country = 'us'
    sort = Sort.NEWEST

    while True:
        result, next_token = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=sort,
            count=batch_size,
            continuation_token=next_token
        )
        all_reviews.extend(result)
        if not next_token or len(result) == 0:
            break

    return all_reviews

def save_reviews_to_csv(reviews_list, csv_filename):
    # Define the column names based on the PostgreSQL table schema
    reviews_data = [{
        'review_id': review['reviewId'],
        'username': review['userName'],
        'user_image': review['userImage'],
        'likes': review['thumbsUpCount'],
        'review_created_version': review.get('reviewCreatedVersion', None),
        'created_at': review['at'],
        'reply_content': review.get('replyContent', None),
        'replied_at': review.get('repliedAt', None),
        'app_version': review.get('reviewCreatedVersion', None),  # Assuming app version is the same as review created version
        'score': review['score'],
        'comments': review['content'],
        'keywords': None,  # Placeholder for future data
        'lda_category': None,  # Placeholder for future data
        'sentiment': None,  # Placeholder for future data
        'insight': None  # Placeholder for future data
    } for review in reviews_list]

    df = pd.DataFrame(reviews_data)

    # Construct the path to save the CSV file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    data_directory = os.path.join(parent_directory, 'data')

    # Create the 'data' directory if it doesn't exist
    os.makedirs(data_directory, exist_ok=True)

    # Full path for the CSV file
    full_csv_path = os.path.join(data_directory, csv_filename)

    # Save the DataFrame to CSV
    df.to_csv(full_csv_path, index=False, encoding='utf-8')

    print(f"Collected {len(reviews_list)} reviews and saved to {full_csv_path}")

def main(app_id, csv_filename):
    reviews_list = collect_all_reviews(app_id)
    save_reviews_to_csv(reviews_list, csv_filename)

if __name__ == '__main__':
    app_id = 'com.boa.apollo'
    csv_filename = 'app_reviews.csv'
    main(app_id, csv_filename)