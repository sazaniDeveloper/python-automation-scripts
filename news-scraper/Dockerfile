FROM python:3.10-slim
WORKDIR /news-scraper
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=web_scraping.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
