import allure
from page.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data import URLS


class AccountPage(BasePage):
    @allure.step('Нажатие на ссылку "Восстановить пароль"')
    def personal_area_click_on_restore_link(self):
        self.click_to_element(AccountPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step('Нахождение заголовка "Вход"')
    def personal_area_enter_header(self):
        return self.find_element_with_wait(AccountPageLocators.ENTER_HEADER)

    @allure.step('Авторизация зарегистрированного пользователя')
    def login_user(self, user):
        email = user[0]['email']
        password = user[0]['password']
        self.add_text_to_element(AccountPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_FIELD, password)
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)



    @allure.step('нажатие на строчку "История заказов"')
    def click_on_order_history_link(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_LINK)

    @allure.step('поиск списка заказов')
    def find_order_history_list(self):
        return self.find_element_with_wait(AccountPageLocators.ORDER_HISTORY_LIST)

    @allure.step('нажатие на строчку "Выход"')
    def click_on_logout_link(self):
        self.find_element_with_wait(AccountPageLocators.LOGOUT_BUTTON)
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('поиск ID заказа')
    def find_order_id(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_NUMBER)

    @allure.step('поиск ссылки "Профиль"')
    def find_profile_link(self):
        return self.find_element_with_wait(AccountPageLocators.PROFILE_LINK)

    @allure.step('Открыть страницу авторизации')
    def open_account_page(self):
        self.go_to_url(URLS.LOGIN_PAGE_URL)

