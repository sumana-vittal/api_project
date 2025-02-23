import pytest
import requests


def test_get_request_validation():
    header = {
        'Content-Type':'application/json'
    }

    base_url = 'https://reqres.in'

    response = requests.get(url=str(base_url+"/api/users/2"), headers=header)

    print(response.status_code)
    print(response.json())