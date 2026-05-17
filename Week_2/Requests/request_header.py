import requests


headers={  # Header is a extra information that we send to the server with the reqeust.
    'content-Type': 'application/json',  # sent data type
    'Authorization': 'Api_key',    # Authntication if needed
    'Accept': 'application/json'   # Accept type of data that you want from the server
}


response = requests.get('https://httpbin.org/get',headers=headers)
print(response.json())