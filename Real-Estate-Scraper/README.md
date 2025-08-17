## Real-Estate Scraper API 🏠

A FastAPI web scraper for real-estate properties from a website. You can filter properties by type of property, city, zone, bedrooms, etc.

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

## Install
1. git clone https://github.com/sazaniDeveloper/python-automation-scripts.git
2. cd python-automation-scripts
3. docker build -t real-estate-scraper .
4. docker run -p 8000:8000 real-estate-scraper
5. Run the API through localhost:8000

## Requirements
- Python 3.0 required
- Docker installed
- Git installed

Run Without Docker:
pip install -r requirements.txt

## Instructions

**/properties**

Scrape multiple properties with filters.  

**Parameters:** 
- type: `rent` or `sale`  
- city: e.g., `Tirana`  
- zone: e.g., `Ali+Demi` (use `+` for multiple words)  
- bedrooms: integer  
- price_min / price_max: integers  
- size_min / size_max: integers  
Example:
/properties/type:rent/city:Tirana/zone:Ali+Demi/bedrooms:2/price_min:500/price_max:800/size_min:50/size_max:90

**/property**

Scrape details of a single property by URL.  
Example:
property_ = Scrap_Estate("https://www.century21albania.com/property/4836239/japim-me-qira-apartament-2-1-post-parkimi-gold120722.html")

