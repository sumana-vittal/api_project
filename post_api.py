import requests

header = {
    'Accept':'text/plain',
    'Content_Type':'application/json'
}

request_payload = {
  "id": 2,
  "idBook": 2,
  "firstName": "sdsds",
  "lastName": "vvv"
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Authors",
                         headers=header,
                         json=request_payload)
print(response.status_code)
print(response.json())