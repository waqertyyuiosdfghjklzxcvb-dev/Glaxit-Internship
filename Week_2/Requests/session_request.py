import requests

session = requests.session()

# if one time session creates so no need to again send haeader and parametersin everey request because session auto send all 
response = session.post('http://127.0.0.1:8000/login', json={
    "username": "waleed",
    "password": "123456"
})
print(response.status_code)



# now simply send request to the srever without any other information simply using session obj(that stores all the things (server-side session also have (so two types)))
response2 = session.get('http://127.0.0.1:8000/profile')
print(response2.status_code)