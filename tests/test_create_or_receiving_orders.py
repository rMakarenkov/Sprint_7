import allure
import pytest
import urls
import copy

from api_client import ApiClient
from data.test_data import OrderData


@allure.feature('Сценарии создания заказа или получения списка заказов')
class TestCreateOrReceivingOrders:
    @pytest.mark.create_order
    @allure.title('Создание заказа с различными значениями ключа color. Ожидаемый результат: 201')
    @pytest.mark.parametrize('value', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_complete_data_success_201(self, value):
        # Arrange
        data = copy.deepcopy(OrderData.valid_order)
        data['color'] = value
        # Act
        response_by_create_order = ApiClient.post(url=urls.ORDER_URL, data=data)
        # Assert
        assert response_by_create_order.status_code == 201
        assert response_by_create_order.json()['track'] and isinstance(response_by_create_order.json()['track'], int)

    @pytest.mark.get_orders
    @allure.title('Получение всего списка заказов. Ожидаемый результат: 200')
    def test_get_orders_complete_data_success_200(self):
        # Arrange
        # Act
        response_by_get_orders = ApiClient.get(url=urls.ORDER_URL, params=None)
        # Assert
        assert response_by_get_orders.status_code == 200
        assert (isinstance(response_by_get_orders.json()['orders'], list) and
                len(response_by_get_orders.json()['orders']) > 0)
