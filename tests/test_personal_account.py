import allure


from data import URLS
from page.account_page import AccountPage
from page.main_page import MainPage



class TestPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет нажатием на кнопку «личный кабинет» на главной странице')
    def test_go_to_personal_account_page(self, driver, user_with_order):
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        driver.get(URLS.LOGIN_PAGE_URL)
        account_page.login_user(user_with_order)
        main_page.click_on_personal_account_button()
        assert account_page.find_profile_link().is_displayed()

    @allure.title('Проверка перехода в историю заказов')
    def test_go_to_order_history(self, driver, user_with_order):
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        driver.get(URLS.LOGIN_PAGE_URL)
        account_page.login_user(user_with_order)
        main_page.click_on_personal_account_button()
        account_page.click_on_order_history_link()
        assert account_page.find_order_history_list().is_displayed()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_user(self, driver, user_with_order):
        account_page = AccountPage(driver)
        main_page = MainPage(driver)
        driver.get(URLS.LOGIN_PAGE_URL)
        account_page.login_user(user_with_order)
        main_page.click_on_personal_account_button()
        account_page.click_on_logout_link()
        assert account_page.personal_area_enter_header().is_displayed()
