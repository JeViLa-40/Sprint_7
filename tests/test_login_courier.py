import requests
import allure
from data import Url, CourierAccount

class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    def test_login_courier_successful(self):
        response = requests.post(
            f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
            json= {
                "login": CourierAccount.exist_login,
                "password": CourierAccount.exist_password
            }
        )
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Проверка ошибки при передаче неверного логина')
    def test_(self):
        response = requests.post(
            f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
            json= {
                "login": 'anonasik',
                "password": CourierAccount.exist_password
            }
        )
        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка ошибки, если не передан логин')
    def test_login_courier_missing_field_error(self):
        response = requests.post(
            f'{Url.MAIN_URL}{Url.LOGIN_COURIER}',
            json= {
                "password": CourierAccount.exist_password
            }
        )
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для входа"
