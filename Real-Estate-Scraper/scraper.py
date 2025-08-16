from bs4 import BeautifulSoup
from typing import List, Dict
import requests
import logging


def safe_text(element, default: str = "N/A") -> str:
    return element.text.strip() if element else default

class Scrap_Estate():

    def __init__(self, link):
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }
        self.link = link
        try:
            self.response = requests.get(self.link, headers=headers)
        except requests.RequestException as e:
            logging.error(f"Error fetching property: {e}")
            self.response = None

    def scrap_properties(self) -> List[Dict[str, str]]:
        if not self.response:
            return {"error": "Failed to fetch properties"}
        soup = BeautifulSoup(self.response.text, "html.parser")
        text_gold = soup.find_all(class_="text-gold-shade-55 uppercase font-semibold font-barlow")
        price = soup.find_all('span', class_="heading-5 text-black-custom font-semibold font-barlow")
        size = soup.find_all('p', class_="paragraph-3 text-black-custom font-urbanist")
        size_all = [safe_text(element) for element in size]
        sale_or_rent = soup.find_all('span', class_="text-white text-[20px] leading-[21px] font-urbanist font-medium")
        h6 = soup.find_all('h6', class_="text-black-custom font-semibold font-barlow line-clamp-1")
        ID = [safe_text(element) for element in text_gold] 
        prices = [safe_text(element) for element in price]
        types = [safe_text(element) for element in sale_or_rent]
        headers = [safe_text(element) for element in h6]
        sizes = size_all[0:35:3]
        bedrooms = size_all[1:35:3]
        property_type = size_all[2:35:3]

        data = [
            {"ID": i,
            "Header": h,
            "Type": t,
            "Price": p,
            "Size": s,
            "Bedrooms": b,
            "Property Type": pt} for i, h, t, p, s, b, pt in zip(ID, headers, types, prices, sizes, bedrooms, property_type)
        ]

        return data

    def scrap_property(self) -> Dict[str, Dict[str, str]]:
        soup = BeautifulSoup(self.response.text, "html.parser")
        ID = safe_text(soup.find("span", class_="text-gold-shade-55"))
        h1 = safe_text(soup.find("h1", class_="font-extrabold text-black-custom heading-4 font-barlow"))
        h2 = safe_text(soup.find("h2", class_="font-bold text-gold-shade-55 whitespace-nowrap font-barlow s:text-[32px] s:font-extrabold"))
        h6 = safe_text(soup.find("h6", class_="font-semibold text-black-custom font-barlow"))
        spans = soup.find_all("span", class_="font-bold")
        floor = safe_text(spans[3] if len(spans) > 3 else None)
        size = safe_text(spans[0] if len(spans) > 0 else None)
        bedrooms = safe_text(spans[2] if len(spans) > 2 else None)

        return {
            "property": {
                "ID": ID,
                "Title": h1,
                "Price": h2.replace(" ", "").replace("\n", ""),
                "Location": h6,
                "Floor": floor,
                "Size": size,
                "Bedrooms": bedrooms
            }
}