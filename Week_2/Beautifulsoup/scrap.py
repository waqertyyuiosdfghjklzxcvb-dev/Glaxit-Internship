from bs4 import BeautifulSoup
import requests


try:
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    #     "Accept-Language": "en-US,en;q=0.9",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept": "text/html,application/xhtml+xml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #     "Connection": "keep-alive",
    # }

    # session = requests.Session()
    # session.headers.update(headers)

    # response = session.get('https://daraz.com/', timeout=10)
    # response.raise_for_status()  
    # print(response.status_code)
    # # print(response.content)



    
    # soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup.title.text)
    # print(soup.find('script'))


    session = requests.Session()

    response = session.get('https://books.toscrape.com/',timeout=10)

    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.title.text)
    print(soup.h1.text)

    print(soup.find_all('img'))

    print("Solo")
    print(soup.find('div',class_ ="col-sm-8 col-md-9"))


    all = soup.find_all('article',class_='product_pod')

    print(f"Length : {len(all)}")

    print(all[0])
    print("Name of All Books")
    for i in all:
        print(i.find('img')['alt'])
        print(i.find('p',class_='price_color').text)
















except TimeoutError:
    print("Server Not reached or Taking more time to respond")


