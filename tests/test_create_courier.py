import requests
import allure
from data import Url

class TestCourier:

    @allure.title('Проверка успешного создания курьера')
    def test_courier_creation_successful(self, generate_courier_data):
        courier_data = generate_courier_data
        response = requests.post(
            f'{Url.MAIN_URL}{Url.CREATE_COURIER}',
            json=courier_data
        )

        assert response.status_code == 201
        assert response.json()['ok'] is True

    @allure.title('Проверка ошибки при создании существующего курьера')
    def test_cannot_create_duplicate_courier(self, generate_courier_data):
        courier_data = generate_courier_data
        requests.post(
            f'{Url.MAIN_URL}{Url.CREATE_COURIER}',
            json=courier_data
        )
        response = requests.post(
            f'{Url.MAIN_URL}{Url.CREATE_COURIER}',
            json=courier_data
        )

        assert response.status_code == 409
        assert response.json()['message'] == "Этот логин уже используется"

    @allure.title('Проверка ошибки, если не передан пароль')
    def test_create_courier_missing_field_error(self, generate_courier_data):
        courier_data = generate_courier_data
        del courier_data["password"]
        response = requests.post(
            f'{Url.MAIN_URL}{Url.CREATE_COURIER}',
            json=courier_data
        )
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"