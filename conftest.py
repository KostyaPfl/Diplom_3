import pytest
from data import OrderInfo
from selenium import webdriver
from api_methods.user_methods import UserMethods
from api_methods.order_methods import OrderMethods
from page.main_page import MainPage
from page.account_page import AccountPage
from page.forgot_password_page import ForgotPasswordPage
from page.reset_password_page import ResetPasswordPage
from page.order_feed_page import OrderFeedPage


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


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture()
def reset_password_page(driver):
    return ResetPasswordPage(driver)
