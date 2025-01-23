import allure


class TestMainPage:

    @allure.title('Проверка перехода по кнопке "Конструктор"')
    def test_click_on_constructor_button(self, main_page):
        main_page.open_main_page()
        main_page.click_on_order_feed_button()
        main_page.click_on_constructor_button()
        assert main_page.find_constructor_header().is_displayed()

    @allure.title('Проверка перехода по кнопке "Лента заказов"')
    def test_click_on_order_feed_button(self, main_page, order_feed_page):
        main_page.open_main_page()
        main_page.click_on_order_feed_button()
        assert order_feed_page.find_order_feed_header().is_displayed()

    @allure.title('Проверка открытия окна с деталями об ингедиенте')
    def test_open_ingredient_info_window(self, main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient()
        assert main_page.find_ingredient_info_header().is_displayed()

    @allure.title('Проверка закрытия окна с деталями об ингедиенте')
    def test_close_ingredient_info_window(self, main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient()
        main_page.click_on_ingredient_info_close_button()
        assert main_page.find_ingredient_info_window() == True

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента')
    def test_increasing_counter_ingredient(self, main_page):
        main_page.open_main_page()
        main_page.add_bun()
        assert main_page.find_ingredient_counter().text == '2'

    @allure.title('Проверка что авторизованный пользователь может оформить заказ')
    def test_authorized_user_make_order(self, user_with_order, main_page, account_page):
        main_page.open_main_page()
        main_page.click_on_personal_account_button()
        account_page.login_user(user_with_order)
        main_page.add_bun()
        main_page.click_on_place_an_order_button()
        assert main_page.find_order_id_header().is_displayed()
