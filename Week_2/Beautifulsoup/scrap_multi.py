# Scrap the fixed number of Pages 
import requests
from bs4 import BeautifulSoup


for i in range(1,5):

    session = requests.Session()
    response = session.get(f"https://books.toscrape.com/catalogue/page-{i}.html")

    # print(response.content)

    soup = BeautifulSoup(response.content,'html.parser')

    print(f"Page {i}")

    products = soup.find_all('article',class_='product_pod')
    for product in products:
        print(product.find('h3').text)
        print(product.find('p',class_="price_color").text)

    



# Scrap the all Pages (when the all pages end so stop)
import requests
from bs4 import BeautifulSoup


page = 1
while True:
    try:
        session = requests.Session()
        response = session.get(f"https://books.toscrape.com/catalogue/page-{page}.html")

        if response.status_code != 200:
            print("No more pages to scrape.")
            break


        soup = BeautifulSoup(response.content,'html.parser')

        print(f"Page {page}")

        products = soup.find_all('article',class_='product_pod')
        for product in products:
            print(product.find('h3').text)
            print(product.find('p',class_="price_color").text)
        
        page += 1
    
    except Exception as e:
        print("Something Wrong")
