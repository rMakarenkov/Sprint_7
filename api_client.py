import requests
import allure


class ApiClient:
    @staticmethod
    @allure.step('Вызываем метод GET c параметрами - {params}, эндпоинт - {url}')
    def get(url: str, params: dict | None) -> requests.Response:
        return requests.get(url=url, params=params)

    @staticmethod
    @allure.step('Вызываем метод POST c данными - {data}, эндпоинт - {url}')
    def post(url: str, data: dict) -> requests.Response:
        return requests.post(url=url, json=data)

    @staticmethod
    @allure.step('Вызываем метод DELETE, эндпоинт - {url}')
    def delete(url: str) -> requests.Response:
        return requests.delete(url=url)
