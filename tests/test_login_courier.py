import copy
import json
import allure
import pytest
import urls

from helper import Helper
from api_client import ApiClient
from data.test_data import CourierData


@allure.feature('Сценарии авторизации курьера')
@pytest.mark.login_courier
class TestLoginCourier:
    @allure.title('Авторизация курьера. Ожидаемый результат: 200')
    def test_login_courier_complete_data_success_200(self, create_new_user_and_return_login_password):
        # Arrange
        response_by_create_courier = create_new_user_and_return_login_password
        login_data = json.loads(response_by_create_courier.request.body)
        login_data.pop('firstName')
        # Act
        response_by_login_courier = ApiClient.post(url=urls.LOGIN_URL, data=login_data)
        # Assert
        assert response_by_login_courier.status_code == 200
        assert response_by_login_courier.json()['id'] and isinstance(response_by_login_courier.json()['id'], int)

    @allure.title('Авторизация курьера с ошибкой в значении ключа login или password. Ожидаемый результат: 404')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_login_courier_with_error_in_data_not_found_404(self, create_new_user_and_return_login_password, key):
        # Arrange
        response_by_create_courier = create_new_user_and_return_login_password
        login_data = json.loads(response_by_create_courier.request.body)
        login_data[key] = login_data.setdefault(key, ' ') + '_'
        login_data.pop('firstName')
        # Act
        response_by_login_courier = ApiClient.post(url=urls.LOGIN_URL, data=login_data)
        # Assert
        assert response_by_login_courier.status_code == 404
        assert response_by_login_courier.json()['message'] == CourierData.courier_not_found_response

    @allure.title('Авторизация курьера без одного из обязательных ключей. Ожидаемый результат: 400')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_login_courier_without_required_key_bad_request_400(self, key):
        # Arrange
        login_data = copy.deepcopy(CourierData.valid_courier)
        login_data.pop('firstName')
        login_data.pop(key)
        # Act
        response_by_login_courier = ApiClient.post(url=urls.LOGIN_URL, data=login_data)
        # Assert
        assert response_by_login_courier.status_code == 400
        assert response_by_login_courier.json()['message'] == CourierData.missing_data_login_response
