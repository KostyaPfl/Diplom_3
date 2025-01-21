import allure

from data import URLS
from page.main_page import MainPage
from page.order_feed_page import OrderFeedPage
from page.account_page import AccountPage


class TestMainPage:

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        driver.get(URLS.BASE_URL)
        main_page.click_on_order_feed_button()
        main_page.click_on_constructor_button()
        assert main_page.find_constructor_header().is_displayed()

    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    def test_click_on_order_feed_button(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        driver.get(URLS.BASE_URL)
        main_page.click_on_order_feed_button()
        assert order_feed_page.find_order_feed_header().is_displayed()

    @allure.title('Проверка открытия окна с деталями об ингедиенте')
    def test_open_ingredient_info_window(self, driver):
        main_page = MainPage(driver)
        driver.get(URLS.BASE_URL)
        main_page.click_on_ingredient()
        assert main_page.find_ingredient_info_header().is_displayed()

    @allure.title('Проверка закрытия окна с деталями об ингедиенте')
    def test_close_ingredient_info_window(self, driver):
        main_page = MainPage(driver)
        driver.get(URLS.BASE_URL)
        main_page.click_on_ingredient()
        main_page.click_on_ingredient_info_close_button()
        assert main_page.find_ingredient_info_window() == True

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента')
    def test_increasing_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        driver.get(URLS.BASE_URL)
        main_page.add_bun()
        assert main_page.find_ingredient_counter().text == '2'

    @allure.title('Проверка что авторизованный пользователь может оформить заказ')
    def test_authorized_user_make_order(self, driver, user_with_order):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        driver.get(URLS.BASE_URL)
        main_page.click_on_personal_account_button()
        account_page.login_user(user_with_order)
        main_page.add_bun()
        main_page.click_on_place_an_order_button()
        assert main_page.find_order_id_header().is_displayed()
