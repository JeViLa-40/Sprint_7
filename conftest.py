import random
import string
import pytest
import requests
from data import Url


@pytest.fixture
def generate_courier_data():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    login_pass = {
        "login": login,
        "password": password,
        "firstName": first_name
    } 

    return login_pass

@pytest.fixture
def generate_courier_data_with_delete(generate_courier_data):
    courier_data = generate_courier_data
    yield courier_data

    response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
                             json={
                                 "login": courier_data['login'],
                                 "password": courier_data['password']
                             }
    )
    id = response.json()['id']

    requests.delete(f'{Url.MAIN_URL}{Url.DELETE_COURIER}{id}')

@pytest.fixture
def create_courier_with_delete(generate_courier_data):
    courier_data = generate_courier_data
    requests.post(
        f'{Url.MAIN_URL}{Url.CREATE_COURIER}',
        json=courier_data
    )   

    yield courier_data

    response = requests.post(f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
                             json={
                                 "login": courier_data["login"],
                                 "password": courier_data["password"]
                             }
    )
    id = response.json()['id']

    requests.delete(f'{Url.MAIN_URL}{Url.DELETE_COURIER}{id}')
