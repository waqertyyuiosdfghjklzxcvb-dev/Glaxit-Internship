import requests
from bs4 import BeautifulSoup
import csv


for i in range(1,5):

    session = requests.Session()
    response = session.get(f"https://books.toscrape.com/catalogue/page-{i}.html")

    # print(response.content)

    soup = BeautifulSoup(response.content,'html.parser')

    print(f"Page {i}")

    products = soup.find_all('article',class_='product_pod')
    for product in products:
        name = product.find('h3').text
        price = product.find('p',class_="price_color").text
        with open('scrap_data.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name,price])



