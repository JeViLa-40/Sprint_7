import requests
import allure
from data import Url
import pytest

class TestMakeOrder:
    @allure.title('Проверка успешного создания заказа')
    @pytest.mark.parametrize('colour', [['BLACK'],['GREY'],['BLACK','GREY'],[]])
    def test_make_order_successful(self, colour):
        response = requests.post(
            f'{Url.MAIN_URL}{Url.MAKE_ORDER}',
            json={
                "firstName": "Naruto",
                "lastName": "Uchiha",
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha",
                "color": colour
            }
        )
        assert response.status_code == 201
        assert 'track' in response.json()
