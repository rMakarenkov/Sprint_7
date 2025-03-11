import json
import allure
import pytest
import credentials

from helper import Helper


@allure.feature('Сценарии авторизации курьера')
@pytest.mark.login_courier
class TestLoginCourier:
    @allure.story('Авторизация курьера. Ожидаемый результат: 200')
    def test_login_courier_complete_data_success_200(self, create_new_user_and_return_login_password):
        # Arrange
        response_by_create_courier = create_new_user_and_return_login_password
        login_data = json.loads(response_by_create_courier.request.body)
        login_data.pop('firstName')
        # Act
        response_by_login_courier = Helper.api_post(url=credentials.COURIER_API + '/login', data=login_data)
        # Assert
        assert response_by_login_courier.status_code == 200
        assert response_by_login_courier.json()['id'] and isinstance(response_by_login_courier.json()['id'], int)

    @allure.story('Авторизация курьера с ошибкой в поле - {key}')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_login_courier_with_error_in_data_not_found_404(self, create_new_user_and_return_login_password, key):
        # Arrange
        response_by_create_courier = create_new_user_and_return_login_password
        login_data = json.loads(response_by_create_courier.request.body)
        login_data[key] = login_data.setdefault(key, ' ') + '_'
        login_data.pop('firstName')
        # Act
        response_by_login_courier = Helper.api_post(url=credentials.COURIER_API + '/login', data=login_data)
        # Assert
        assert response_by_login_courier.status_code == 404
        assert response_by_login_courier.json()['message'] == 'Учетная запись не найдена'

    @allure.story('Авторизация курьера без одного из обязательных ключей - {key}. Ожидаемый результат: 400')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_login_courier_without_required_key_bad_request_400(self, key):
        # Arrange
        login_data = Helper.get_json(credentials.create_courier_json_path)
        login_data.pop('firstName')
        login_data.pop(key)
        # Act
        response_by_login_courier = Helper.api_post(url=credentials.COURIER_API + '/login', data=login_data)
        # Assert
        assert response_by_login_courier.status_code == 400
        assert response_by_login_courier.json()['message'] == 'Недостаточно данных для входа'
