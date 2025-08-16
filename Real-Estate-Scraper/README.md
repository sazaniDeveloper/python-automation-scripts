This python project scraps real-estate properties from a website. You can filter properties by type of property, city, zone, bedrooms, minimum size, maximum size, minimum price and maximum price. 

Features:
- Scrape either properties or a single property
- Filter properties with multiple parameters
- Provides data through a FastAPI Rest API

Libraries:
- FastAPI
- requests
- BeautifulSoup
- logging
- typing

Instructions:
1. git clone https://github.com/sazaniDeveloper/python-automation-scripts.git
2. cd python-automation-scripts
3. docker build -t real-estate .
4. docker run -p 8000:8000 real-estate-scraper
5. Run the API through localhost:8000

