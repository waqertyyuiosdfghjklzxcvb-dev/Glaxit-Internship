import requests


# Get Request
# response = requests.get('http://api.weatherapi.com/v1/current.json?key=1c4f42d71cf245f3a6a55200261505&q=Rawalpindi')

# print(response.json())



# post_data = {
#     "name": "Waleed Ahmed",
#     "email": "wa4299448@gmail.com",
#     "phone": "03183704036",
#     "password": "987543"
# }


# Post request
# request2 = requests.post('http://127.0.0.1:8000/post',json=post_data)
# print(request2.status_code)


put_data = {
    "name": "Waleed Ahmed",
    "email": "wa4299448@gmail.com",
    "phone": "03183704036",
    "password": "password changed"
}

# Put/Replace Request
requests3 = requests.put('http://127.0.0.1:8000/put/6a06be5a1142a00345b4c6fe',json=put_data)
print(requests3.status_code)


# Delete Request
responses4 = requests.delete('http://127.0.0.1:8000/delete/6a0481acddaaac6e3719c9f5',)
print(responses4.status_code)
