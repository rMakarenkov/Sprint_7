import allure
import pytest
import credentials
import copy

from helper import Helper


@allure.step('Вызываем фикстуру создания нового курьера с последующим удалением сущности курьера')
@pytest.fixture(scope='function')
def create_new_user_and_return_login_password():
    try:
        courier_data = Helper.get_json(credentials.create_courier_json_path)

        for key in courier_data.keys():
            courier_data[key] = Helper.generate_random_string(10)

        response = Helper.api_post(url=credentials.COURIER_API, data=courier_data)
        if not response.ok:
            raise Exception(f'Failed to create courier: {response.text}')

        yield response

        login_data = copy.deepcopy(courier_data)
        login_data.pop('firstName')
        login_courier_response = Helper.api_post(url=credentials.COURIER_API + '/login', data=login_data)
        courier_id = login_courier_response.json()['id']
        if not courier_id:
            raise Exception('Failed to extract courier ID from login response')

        delete_courier_response = Helper.api_delete(url=credentials.COURIER_API + f'/{courier_id}')
        if not delete_courier_response.ok:
            raise Exception(f'Failed to delete courier with ID {courier_id}: {delete_courier_response.text}')

    except Exception as e:
        raise Exception(f'Error name: {type(e).__name__}, error message: {e}')
