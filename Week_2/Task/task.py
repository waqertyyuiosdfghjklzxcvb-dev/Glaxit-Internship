import requests
from bs4 import BeautifulSoup
import csv

try:
    # creating file
    with open('task_scrap.csv','w', newline="",encoding="utf-8") as f:
        write = csv.writer(f)
        write.writerow(['Name','Price','Stock','Image'])

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    base_url = input("Enter the URL of the website to scrape(https://books.toscrape.com): ")

    session = requests.Session()

    page = 1
    save = set()
    while True:
        print(f"Page : {page}")
        response = session.get(base_url+f"/catalogue/page-{page}.html",headers=headers,timeout=10)

        soup = BeautifulSoup(response.content,'html.parser')

        data = soup.find_all('article',class_='product_pod')

        for i in data:
            name_tag = (i.find('h3'))
            price_tag = (i.find('p',class_='price_color'))
            stock_tag = (i.find('p',class_='instock availability')) 
            image_tag = (i.find('img')['src'])      
            
            name = name_tag.text if name_tag else "N/A"
            price = price_tag.text.replace('£','$') if price_tag else "N/A"
            stock = stock_tag.text.split()[0]+" Stock" if stock_tag else "N/A"
            image = image_tag.replace("../","https://books.toscrape.com/") if image_tag else "N/A"

            
            if (name,price,stock,image) in save:
                print("Data Already Exsists")

            else:
                with open('task_scrap.csv','a',newline="", encoding="utf-8") as f:
                    write = csv.writer(f)
                    write.writerow([name,price,stock,image])
                    save.add((name,price,stock,image))
                     
        page += 1

        if soup.find('li',class_='next') == None:
            print("Pages ended")
            break

        print("Data Saved !")

            
except Exception as e:
    print(f"Error Occured : {e}")