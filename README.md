
# AI News Aggregator

## Overview
AI News Aggregator is a web application built with Django that scrapes AI-related news articles from various sources and displays them on a user-friendly interface. Users can search for specific articles and view detailed information about each article.

## Features
- Scrapes AI news articles from VentureBeat
- Displays articles with titles, summaries, and publication dates
- Search functionality to find articles by keywords
- Detailed view for each article with a link to the original source
- Pagination for easy navigation through articles

## Installation

### Prerequisites
- Python 3.6+
- Django 3.0+
- Django REST Framework

### Setup
1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/ai-news-aggregator.git
    cd ai-news-aggregator
    ```

2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin site
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server
    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`

## Usage

### Scraping News Articles
To scrape AI news articles from VentureBeat, run the following command:
    ```bash
    python manage.py scrape_venturebeat
    ```
Accessing Articles
Navigate to http://127.0.0.1:8000/news/articles/ to view the list of articles.
Use the search bar to find articles by keywords.
Click on an article title to view the detailed information and visit the original source.
Project Structure
    ```
    .
    ├── db.sqlite3
    ├── manage.py
    ├── news
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── management
    │   │   └── commands
    │   │       └── scrape_venturebeat.py
    │   ├── migrations
    │   ├── models.py
    │   ├── scripts
    │   │   └── scrape_VentureBeatAI_news.py
    │   ├── serializers.py
    │   ├── templates
    │   │   └── news
    │   │       └── article_list.html
    │   │       └── article_detail.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── news_aggregator
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── templates
        └── rest_framework
            └── api.html
    ```
    
Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, enhancements, or bug fixes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For any inquiries or feedback, please contact your-email@example.com.



### 追加情報

- これはポートフォリオです


