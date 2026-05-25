import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np

with open("data.csv",'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Price","Link"])

data = requests.get("https://books.toscrape.com")

soup = BeautifulSoup(data.content,'html.parser')

article = soup.find_all('article',class_="product_pod")

for articles in article:
    name = (articles.find('h3').text)
    price = (articles.find('p',class_="price_color").text)
    link = (articles.find('img')['src'])

    with open('data.csv','a',encoding="UTF-8") as f:
              writer = csv.writer(f)
              writer.writerow([name,price,link])

call = pd.read_csv("data.csv")

dirty_rows = pd.DataFrame({
    "Name": [
        "Check this book!! 😍 https://spam.com",
        "<b>Great Novel</b> must read!!",
        "hi",
        "Buy now!!! Visit http://buy.com 🔥",
        "<p>Amazing story about life</p>",
        "😂😂😂",
        "ok",
        "The best book ever!! 😊❤️ https://t.co/abc",
        "<h1>Science Fiction</h1> great read",
        "lol",
    ],
    "Price": [
        "£10.00", "£20.00", "£5.00", "£15.00",
        "£25.00", "£8.00",  "£3.00", "£18.00",
        "£22.00", "£7.00"
    ],
    "Link": ["https://books.toscrape.com"] * 10
})

for i in range(1,11,2):
    call.loc[i,'Name'] = dirty_rows.iloc[i,0]

call["Name"] = call["Name"].str.replace(r'http\S+|www\S+','',regex=True)
call["Name"] = call["Name"].str.replace(r'[^\x00-\x7F]+','',regex=True)
call["Name"] = call["Name"].str.replace(r'<[^>]+>','',regex=True)
call["Name"] = call["Name"].replace('',np.nan)
call = call[call['Name'].str.len() >= 3]
call = call[call['Name'].str.split().str.len() >= 2]

spam_keywords = ['buy now', 'visit', 'click here', 'subscribe', 'follow us', 'shop now']
pattern = '|'.join(spam_keywords)
call = call[~call['Name'].str.lower().str.contains(pattern, regex=True)]

call["Price"] = call["Price"].str.replace('£','$')
call["Link"] = "https://books.toscrape.com/"+call["Link"]

print(call.iloc[1,2])
call