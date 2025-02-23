import requests

header = {
    'Accept':'text/plain',
    'Content_Type':'application/json'
}

body = {
  "id": 546,
  "idBook": 546,
  "firstName": "hina",
  "lastName": "shekar"
}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Authors/5", headers=header, json=body)

print(response.status_code)
print(response.json())

assert response.status_code == 200
response_body = response.json()
assert response_body['id'] == 546
assert response_body['idBook'] == 546