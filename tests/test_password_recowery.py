import allure

from data import URLS
from page.account_page import AccountPage
from page.forgot_password_page import ForgotPasswordPage
from page.reset_password_page import ResetPasswordPage


class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_restore_page_from_login_page(self, driver):
        account_page = AccountPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        driver.get(URLS.LOGIN_PAGE_URL)
        account_page.personal_area_click_on_restore_link()
        assert forgot_password_page.find_restore_header() == 'Восстановить'

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_restore_password_enter_email_and_click_restore(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        driver.get(URLS.FORGOT_PASSWORD_PAGE_URL)
        forgot_password_page.enter_email('test@mail.ru')
        forgot_password_page.restore_button_click()
        assert reset_password_page.find_restore_password_header().text == 'Восстановление пароля'

    @allure.title('Проверка клика по кнопке показать/скрыть пароль делает поле активным')
    def test_click_on_password_button_makes_field_active(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        driver.get(URLS.FORGOT_PASSWORD_PAGE_URL)
        forgot_password_page.enter_email('test@mail.ru')
        forgot_password_page.restore_button_click()
        reset_password_page.visible_element_click()
        assert reset_password_page.check_active_field_password().is_displayed()
