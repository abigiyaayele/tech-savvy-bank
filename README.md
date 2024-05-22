# tech-savvy-bank
 Marketing Analytics Dashboard:  Monitoring and evaluating  Ads efficiency 


#### objectives
This project aims to enhance the marketing strategy of a tech-savvy bank in Ethiopia by tracking the efficiency of their marketing campaigns and providing actionable insights. 

### Task 1: Git and GitHub Setup

#### Steps:
1. Create a new GitHub repository named "MarketingAnalytics".
2. Initialize the repository with a README file.
3. Create a branch named "task-1" for day-to-day analysis.
4. Commit work at least three times a day with descriptive messages.
5. Set up GitHub Actions for automated workflows.
6. Merge "task-1" branch into the main branch using Pull Requests (PR).

### Task 2: Design Database Schema

#### Title: Designing and Implementing the Database Schema

#### Methodology:
1. **Schema Design:** Develop a schema to store datasets in PostgreSQL, including time series data for Telegram posts, Google Play Store reviews and downloads, and Telegram subscription growth.
2. **ETL Process:** Extract, Transform, and Load (ETL) data into the database, ensuring time of day classification.

#### Steps:
1. Design database schema:
    - `tikvah_ads` table for advertisement data.
    - `play_store_reviews` table for reviews.
    - `play_store_downloads` table for download counts.
    - `telegram_subscriptions` table for subscription data.
2. Write SQL scripts to create tables in PostgreSQL.
3. Implement ETL scripts to classify and insert data into the respective tables.

### Task 3: Exploratory Data Analysis (EDA) and Statistical Analysis

#### Title: Conducting Exploratory Data Analysis and Statistical Analysis

#### Methodology:
1. **Data Understanding:** Summarize data and assess quality.
2. **Univariate Analysis:** Analyze single variables.
3. **Bivariate/Multivariate Analysis:** Explore relationships between variables.
4. **Data Enrichment:** Merge datasets for deeper insights.
5. **Trend Analysis:** Analyze data trends over time.
6. **Visualization:** Create visual representations of data insights.

#### Steps:
1. Perform data summarization and quality assessment.
2. Conduct univariate analysis using histograms and box plots.
3. Explore bivariate relationships with scatter plots and heatmaps.
4. Enrich data by merging relevant datasets.
5. Analyze trends over time with line charts.
6. Identify outliers and visualize findings with 10 creative plots.
7. Commit changes to the repository and merge with the main branch.

### Task 4: Dashboard Setup with Docker and Open Source Tools

#### Title: Setting Up a Scalable Dashboard System

#### Methodology:
1. **Dashboard Selection:** Review open-source dashboard tools (Redash, Superset, Metabase) and select the most suitable.
2. **Automation Scripts:** Develop bash/python scripts for setting up the dashboard system using Docker.

#### Steps:
1. Create a branch named "task-2" for dashboard setup.
2. Review and select a dashboard tool based on comparison metrics.
3. Write Docker Compose scripts to automate the setup.
4. Implement bash/python scripts for system setup and scalability.
5. Commit and merge changes into the main branch.

### Task 5: Data Loading and Kedro Framework Integration

#### Title: Loading Data and Setting Up Kedro Framework

#### Methodology:
1. **Kedro Integration:** Utilize Kedro framework to manage data layers and pipelines.
2. **Data Layering:** Organize data into raw, intermediate, and primary layers.
3. **Dashboard Creation:** Develop dashboards using the loaded data.

#### Steps:
1. Create a branch named "task-3".
2. Set up raw and intermediate layers in Kedro.
3. Load processed data into PostgreSQL as the primary layer.
4. Create dashboards to analyze:
    - Ad performance comparisons.
    - Impact of ad timing.
    - Play Store review sentiment.
    - Impact on app downloads and Telegram subscriptions.
5. Commit and merge changes into the main branch.

### Task 6: Database and Dashboard Migration Tools

#### Title: Developing Database and Dashboard Migration Tools

#### Methodology:
1. **Migration Scripts:** Write scripts to migrate database tables and dashboards to remote instances.
2. **Automation:** Ensure automated migration to facilitate seamless transitions.

#### Steps:
1. Create a branch named "task-4".
2. Develop scripts to migrate database tables to remote instances.
3. Write scripts to migrate SQL queries and dashboards.
4. Commit and merge changes into the main branch.

By following these tasks and methodologies, I aim to establish a robust system for tracking and improving the bank's marketing efficiency, providing valuable insights through dynamic and interactive dashboards.