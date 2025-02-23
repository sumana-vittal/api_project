import requests
import json

base_url = 'https://reqres.in/api/users'

header = {
    'Content_Type':'application/json'

}

# payload ={
#     "name": "morpheus",
#     "job": "leader"
# }

# response = requests.post(base_url, headers=header, json=payload)

# as json file
json_file = open("./payload.json")
json_payload = json.load(json_file)

# to use data use dumps

# response = requests.post(base_url, headers=header, json=json_payload)

response = requests.post(base_url, headers=header, data=json.dumps(json_payload))

print(response.status_code)
print(response.json())