import allure
from page.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordLocators

class ForgotPasswordPage(BasePage):
    @allure.step('Найти заголовок Восстановление пароля')
    def find_restore_header(self):
        return self.get_text_from_element(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step('Ввод адреса в поле Email')
    def enter_email(self, email):
        self.add_text_to_element(ForgotPasswordLocators.EMAIL_FIELD, email)

    @allure.step('Нажатие на кнопку "Востановить"')
    def restore_button_click(self):
        self.click_to_element(ForgotPasswordLocators.RESTORE_BUTTON)