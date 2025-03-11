import json
import allure
import pytest
import credentials

from helper import Helper


@allure.feature('Сценарии создания курьера')
@pytest.mark.create_courier
class TestCreateCourier:
    @allure.story('Создание курьера с валидными для регистрации данными. Ожидаемый результат: 201')
    def test_create_courier_complete_data_success_201(self, create_new_user_and_return_login_password):
        # Arrange
        # Act
        response_by_create_courier = create_new_user_and_return_login_password
        # Assert
        assert response_by_create_courier.status_code == 201
        assert response_by_create_courier.json() == {'ok': True}

    @allure.story('Создание дублирующей сущности курьера. Ожидаемый результат: 409')
    def test_create_courier_already_created_conflict_409(self, create_new_user_and_return_login_password):
        # Arrange
        response_by_create_courier = create_new_user_and_return_login_password
        data = json.loads(response_by_create_courier.request.body)
        # Act
        repeated_response = Helper.api_post(url=credentials.COURIER_API, data=data)
        # Assert
        assert repeated_response.status_code == 409
        assert repeated_response.json()['message'] == 'Этот логин уже используется'

    @allure.story('Создание курьера без одного из обязательных ключей - {key}. Ожидаемый результат: 400')
    @pytest.mark.parametrize('key', ['login', 'password'])
    def test_create_courier_without_required_key_bad_request_400(self, key):
        # Arrange
        data = Helper.get_json(credentials.create_courier_json_path)
        data.pop(key)
        # Act
        response_by_create_courier = Helper.api_post(url=credentials.COURIER_API, data=data)
        # Assert
        assert response_by_create_courier.status_code == 400
        assert response_by_create_courier.json()['message'] == 'Недостаточно данных для создания учетной записи'
