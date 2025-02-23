import requests

header = {
    'Accept':'text/plain',
    'Content_Type':'application/json',
    'Authorization':'Bearer 612cb12ba9aaa034102e694db22d5dbddaca26261b2458c5c0f4e7a604018c53'
}

request_payload = {
    "name": "Adhrit Pothuvaal",
    "email": "adhrit_pothuv77aa12334l@rolfson.test",
    "gender": "female",
    "status": "active"
}

response = requests.post("https://gorest.co.in/public/v2/users", headers=header, json=request_payload)

print(response.status_code)
print(response.json())

response = requests.get("https://gorest.co.in/public/v2/users/7716315", headers=header)
print(response.status_code)
print(response.json())
