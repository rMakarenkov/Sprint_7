import allure
import pytest
import credentials

from helper import Helper


@allure.feature('Сценарии получения списка заказов')
@pytest.mark.get_orders
class TestGetOrders:
    @allure.story('Получение всего списка заказов. Ожидаемый результат: 200')
    def test_get_orders_complete_data_success_200(self):
        # Arrange
        # Act
        response_by_get_orders = Helper.api_get(url=credentials.ORDER_API, params=None)
        # Assert
        assert response_by_get_orders.status_code == 200
        assert (isinstance(response_by_get_orders.json()['orders'], list) and
                len(response_by_get_orders.json()['orders']) > 0)
