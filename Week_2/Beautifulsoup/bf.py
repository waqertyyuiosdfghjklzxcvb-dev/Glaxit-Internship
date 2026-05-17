from bs4 import BeautifulSoup
import requests


html = """ 
    <!DOCTYPE html>
    <html>
    <head>
        <title>Title of the document</title>
    </head>

    <body>
        The content of the document......
    </body>

    </html>
"""


soup = BeautifulSoup(html,'html.parser')
print(soup.title.text)


response = requests.get('https://books.toscrape.com/')

soups = BeautifulSoup(response.content,'html.parser')
print(soups.h1.text)
