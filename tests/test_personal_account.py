import allure


class TestPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет нажатием на кнопку «личный кабинет» на главной странице')
    def test_go_to_personal_account_page(self, account_page, main_page, user_with_order):
        account_page.open_account_page()
        account_page.login_user(user_with_order)
        main_page.click_on_personal_account_button()
        assert account_page.find_profile_link().is_displayed()

    @allure.title('Проверка перехода в историю заказов')
    def test_go_to_order_history(self, account_page, main_page, user_with_order):
        account_page.open_account_page()
        account_page.login_user(user_with_order)
        main_page.click_on_personal_account_button()
        account_page.click_on_order_history_link()
        assert account_page.find_order_history_list().is_displayed()

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_user(self, account_page, main_page, user_with_order):
        account_page.open_account_page()
        account_page.login_user(user_with_order)
        main_page.click_on_personal_account_button()
        account_page.click_on_logout_link()
        assert account_page.personal_area_enter_header().is_displayed()
