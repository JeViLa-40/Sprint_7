import requests
import allure
from data import Url

class TestGetOrdersList:

    @allure.title('Проверка успешного получения списка заказов')
    def test_get_orders_list(self):
        response = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDERS_LIST}')
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
