import requests

try : 
    response = requests.get('https://httpbin.org/delay/15',timeout=10)
except requests.exceptions.Timeout:
    print("Request TimeOut")

except requests.exceptions.ConnectionError:
    print("Url Wrong or Internet Connection Error")

