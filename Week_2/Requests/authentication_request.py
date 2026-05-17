import requests


#1. Authentication using API Key
parameter = {
    'key': '1c4f42d71cf245f3a6a55200261505',
    'q': 'Rawalpindi'
}

response = requests.get('https://api.weatherapi.com/v1/current.json', params=parameter)
print(response.status_code)
print(response.json())



#2. Authentication using Basic Auth (UserName and Password) 
# request automaticaaly take username and password from auth parameter and send it to the server from authentication

response2 = requests.get('https://httpbin.org/get', auth=('Waleed Ahmed', 'password'))
print(response2.status_code)
                         

# print(response2.json())


#3. Authentication using Bearer Token (when you login so it gives you a token so then no login, every request send with bearer token so get data easily )

# this attempts to login and take a token  from the response
login = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
response3 = requests.post('https://reqres.in/api/login', json=login)
print(response3.json()['token'])


# give bearer token to server and access the data from the server
header = {
    'Authorization': f"Bearer {response3.json()['token']}"
}

response4= requests.get('https://httpbin.org/get',headers=header)
print(response4.status_code)
print(response4.json())




#4.  OAUTH (when you login with google or facebook so it gives you a token and then you can access the data from the server without login again and again)