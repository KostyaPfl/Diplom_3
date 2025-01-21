import allure

from data import URLS
import requests
from helpers import generate_random_string


class UserMethods:
    @allure.step('Генерируем данные для регистрации пользователя')
    def user_data_generation(self):
        email = f'{generate_random_string(10)}@yandex.ru'
        password = generate_random_string(10)
        name = generate_random_string(10)
        return {
            "email": email,
            "password": password,
            "name": name
        }

    @allure.step('Регистрируем нового пользователя')
    def registration_new_user(self, payload):
        return requests.post(URLS.REGISTER_USER_API_URL, data=payload)

    @allure.step('Удаляем пользователя')
    def delete_user(self, access_token):
        payload = {'Authorization': access_token}
        return requests.delete(URLS.DELETE_USER_API_URL, headers=payload)
