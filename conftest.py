import allure
import pytest
import urls
import copy

from helper import Helper
from api_client import ApiClient
from data.test_data import CourierData



@allure.step('Вызываем фикстуру создания нового курьера с последующим удалением сущности курьера')
@pytest.fixture(scope='function')
def create_new_user_and_return_login_password():
    courier_data = copy.deepcopy(CourierData.valid_courier)

    for key in courier_data.keys():
        courier_data[key] = Helper.generate_random_string(10)

    response = ApiClient.post(url=urls.COURIER_URL, data=courier_data)

    yield response

    login_data = copy.deepcopy(courier_data)
    login_data.pop('firstName')
    login_courier_response = ApiClient.post(url=urls.LOGIN_URL, data=login_data)
    courier_id = login_courier_response.json()['id']
    ApiClient.delete(url=urls.COURIER_URL + f'/{courier_id}')
