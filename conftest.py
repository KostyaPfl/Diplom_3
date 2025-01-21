import pytest
from data import OrderInfo
from selenium import webdriver
from api_methods.user_methods import UserMethods
from api_methods.order_methods import OrderMethods


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    else:
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture()
def user_with_order():
    payload = UserMethods().user_data_generation()
    creation_response = UserMethods().registration_new_user(payload)
    token = creation_response.json()['accessToken']
    token_for_order = {'Authorization': token}
    OrderMethods().create_order(OrderInfo.CORRECT_INGREDIENTS, token_for_order)
    yield payload, creation_response, token
    UserMethods().delete_user(token)
