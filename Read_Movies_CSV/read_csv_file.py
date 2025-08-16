import pandas as pd
import imdb
from tqdm import tqdm

ia = imdb.IMDb()

dataframe1 = pd.read_excel("C:/Users/jcesu/Desktop/Python Projects/practice/Movies I have seen.xlsx", usecols=["Title"])
dataframe2 = pd.read_excel("C:/Users/jcesu/Desktop/Python Projects/practice/Movies I have seen.xlsx")


years = []
for movie in tqdm(dataframe1["Title"]):
   years.append(ia.search_movie(str(movie))[0]["year"])

dataframe2["Year"] = years
print(dataframe2["Year"])
dataframe2.to_excel("C:/Users/jcesu/Desktop/Python Projects/practice/Movies I have seen.xlsx", index=True, header=True)


