import json
import allure
import pytest
import urls
import copy

from api_client import ApiClient
from data.test_data import CourierData


@allure.feature('Сценарии создания курьера')
@pytest.mark.create_courier
class TestCreateCourier:
    @allure.title('Создание курьера с валидными для регистрации данными. Ожидаемый результат: 201')
    def test_create_courier_complete_data_success_201(self, create_new_user_and_return_login_password):
        # Arrange
        # Act
        response_by_create_courier = create_new_user_and_return_login_password
        # Assert
        assert response_by_create_courier.status_code == 201
        assert response_by_create_courier.json() == CourierData.valid_response

    @allure.title('Создание дублирующей сущности курьера. Ожидаемый результат: 409')
    def test_create_courier_already_created_conflict_409(self, create_new_user_and_return_login_password):
        # Arrange
        response_by_create_courier = create_new_user_and_return_login_password
        data = json.loads(response_by_create_courier.request.body)
        # Act
        repeated_response = ApiClient.post(url=urls.COURIER_URL, data=data)
        # Assert
        assert repeated_response.status_code == 409
        assert repeated_response.json()['message'] == CourierData.login_taken_response

    @allure.title('Создание курьера без одного из обязательных ключей. Ожидаемый результат: 400')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_create_courier_without_required_key_bad_request_400(self, key):
        # Arrange
        data = copy.deepcopy(CourierData.valid_courier)
        data.pop(key)
        # Act
        response_by_create_courier = ApiClient.post(url=urls.COURIER_URL, data=data)
        # Assert
        assert response_by_create_courier.status_code == 400
        assert response_by_create_courier.json()['message'] == CourierData.missing_data_create_response
