# News Scraper (Flask-based) 📰
A Flask-based API that is designed to scrap headlines from a news website based on a keyword provided in the endpoint. It returns all of the titles of the articles in a JSON response.

Libraries used:
- Flask
- requests
- BeautifulSoup4
- re

## Install
1. git clone https://github.com/sazaniDeveloper/python-automation-scripts.git
2. cd python-automation-scripts/news-scraper
3. docker build -t news-scraper .
4. docker run -p 8080:8080 news-scraper
5. Run the API through localhost:8080

### Requirements
- Python 3.x
- Docker installed
- Git installed
Run locally:
- pip install -r requirements.txt
- python web_scraping.py
   
## Instructions
1. Open in the browser or API client localhost:8080
2. Replace the `<keyword>` in the endpoint

## Example
```
[ 'Mero Baze: ‘Ndjellësi i fatkeqësive’ që i ngre topin për ‘fitore të rreme’ Edi Ramës',
  'Në ditën e 15 vjetorit të ndarjes nga jeta të albanologut Peter Prifti'
]
```
