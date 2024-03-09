import pytest
import requests
import json

from data import Data

@pytest.fixture()
def generate_courier_data():
    payload = {
        "login": Data.login,
        "password": Data.password,
        "firstName": Data.firstName
    }
    yield payload


@pytest.fixture()
def generate_courier_data_and_delete_after_test():
    payload = {
        "login": Data.login,
        "password": Data.password,
        "firstName": Data.firstName
    }
    yield payload
    response = requests.post(f'{Data.main_url}/api/v1/courier/login',
                                data={"login": payload['login'], "password": payload['password']})
    id_courier = response.json()
    requests.delete(f'{Data.main_url}/api/v1/courier/{id_courier["id"]}')

@pytest.fixture()
def generate_required_order_data():
    order_data = {
        "firstName": Data.firstName,
        "lastName": Data.lastName,
        "adress": Data.address,
        "metroStation": Data.metroStation,
        "phone": Data.phone,
        "rentTime": Data.rentTime,
        "deliveryDate": Data.deliveryDate,
        "comment": Data.comment
    }
    yield order_data

