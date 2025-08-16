from fastapi import FastAPI
from scraper import Scrap_Estate

app = FastAPI()


@app.get("/properties/type:{type}/city:{city}/zone:{zone}/bedrooms:{bedrooms}/price_min:{price_min}/price_max:{price_max}/size_min:{size_min}/size_max:{size_max}")
def properties(type: str, city: str, zone: str, bedrooms: str, price_min: int, price_max: int, size_min: int, size_max: int):
    properties = Scrap_Estate(f"https://www.century21albania.com/properties?q={zone}&business_type={type}&city={city}&bedrooms={bedrooms}&price%5Bmin%5D={price_min}&price%5Bmax%5D={price_max}&area%5Bmin%5D={size_min}&area%5Bmax%5D={size_max}&extra%5Belevator%5D=&property_status=&")
    result = properties.scrap_properties()
    return result


@app.get("/property")
def property():
    property_ = Scrap_Estate("https://www.century21albania.com/property/4836239/japim-me-qira-apartament-2-1-post-parkimi-gold120722.html")
    result = property_.scrap_property()
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)