import requests
import re
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

class printResponse:

    def __init__(self, url):
        self.url = url

    def response(self):
        res = requests.get(self.url)
        return res.text
    
    def scrap_headers(self, keyword):
        self.keyword = keyword
        soup = BeautifulSoup(self.response(), "html.parser")
        results = soup.find_all("h3")
        h3 = []
        for result in results:
            cleaned_string = re.sub(r'\r\n', "", result.text.strip())
            cleaned_string_1 = re.sub(r'\s+', ' ', cleaned_string)
            if self.keyword in cleaned_string_1:
                h3.append(cleaned_string_1)
        return list(set(h3))
    



@app.route("/<keyword>")
def index(keyword):
   shqip = printResponse("https://shqiptarja.com/home")
   shqip.response()
   return jsonify(shqip.scrap_headers(keyword))

if __name__=="__main__":
    app.run()