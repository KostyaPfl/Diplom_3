import allure
from page.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step('Полечение текста заголовка "Восстановление пароля"')
    def find_restore_password_header(self):
        return self.find_element_with_wait(ResetPasswordLocators.RESTORE_PASSWORD_HEADER)

    @allure.step('Нажатие на кнопку показать/скрыть пароль')
    def visible_element_click(self):
        self.click_to_element(ResetPasswordLocators.VISIBILITY_ELEM)



    @allure.step('Проверка что поле "Пароль" активно')
    def check_active_field_password(self):
        return self.find_element_with_wait(ResetPasswordLocators.FIELD_ACTIVE_PASSWORD)

