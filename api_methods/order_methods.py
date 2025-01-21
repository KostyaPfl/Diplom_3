import allure

from data import URLS
import requests


class OrderMethods:
    @allure.step('создание заказа')
    def create_order(self, payload, access_token):
        return requests.post(URLS.ORDERS_API_URL, data=payload, headers=access_token)
