import json
import string
import random
import allure

import requests


class Helper:
    @staticmethod
    @allure.step('Вызываем метод генерации рандомной строки. Длина - {lenth}')
    def generate_random_string(lenth: int) -> str:
        charasters = string.digits + string.ascii_letters
        random_string = ''.join(random.choice(charasters) for _ in range(lenth))
        return random_string

    @staticmethod
    @allure.step('Вызываем метод получения данных из файла - {path}')
    def get_json(path: str) -> dict:
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    @allure.step('Вызываем метод GET c параметрами - {params}, эндпоинт - {url}')
    def api_get(url: str, params: dict | None):
        return requests.get(url=url, params=params)

    @staticmethod
    @allure.step('Вызываем метод POST c данными - {data}, эндпоинт - {url}')
    def api_post(url: str, data: dict):
        return requests.post(url=url, json=data)

    @staticmethod
    @allure.step('Вызываем метод DELETE, эндпоинт - {url}')
    def api_delete(url: str):
        return requests.delete(url=url)
