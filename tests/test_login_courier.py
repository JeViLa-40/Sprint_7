import requests
import allure
from data import Url

class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    def test_login_courier_successful(self, create_courier_with_delete):
        login_data = create_courier_with_delete
        response = requests.post(
            f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
            json={
                "login": login_data["login"],
                "password": login_data["password"]
            }
        )
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Проверка ошибки при передаче несуществующего логина')
    def test_(self, create_courier_with_delete):
        login_data = create_courier_with_delete
        response = requests.post(
            f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
            json= {
                "login": 'anonasik',
                "password": login_data["password"]
            }
        )
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка ошибки, если не передан логин')
    def test_login_courier_missing_field_error(self, create_courier_with_delete):
        login_data = create_courier_with_delete
        response = requests.post(
            f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
            json= {
                "password": login_data["password"]
            }
        )
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"
