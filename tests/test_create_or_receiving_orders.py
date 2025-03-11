import allure
import pytest
import credentials

from helper import Helper


@allure.feature('Сценарии создания заказа или получения писка заказов')
class TestCreateOrReceivingOrders:
    @pytest.mark.create_order
    @allure.story('Создание заказа с различными значениями ключа color. Ожидаемый результат: 201')
    @pytest.mark.parametrize('value', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_create_order_complete_data_success_201(self, value):
        # Arrange
        data = Helper.get_json(credentials.create_order_json_path)
        data['color'] = value
        # Act
        response_by_create_order = Helper.api_post(url=credentials.ORDER_API, data=data)
        # Assert
        assert response_by_create_order.status_code == 201
        assert response_by_create_order.json()['track'] and isinstance(response_by_create_order.json()['track'], int)

    @pytest.mark.get_orders
    @allure.story('Получение всего списка заказов. Ожидаемый результат: 200')
    def test_get_orders_complete_data_success_200(self):
        # Arrange
        # Act
        response_by_get_orders = Helper.api_get(url=credentials.ORDER_API, params=None)
        print(len(response_by_get_orders.json()['orders']))
        # Assert
        assert response_by_get_orders.status_code == 200
        assert (isinstance(response_by_get_orders.json()['orders'], list) and
                len(response_by_get_orders.json()['orders']) > 0)
