import allure


class TestOrderFeedPage:
    @allure.title('Проверка открытия окна с деталями заказа')
    def test_open_order_detail_window(self, order_feed_page):
        order_feed_page.open_order_feed_page()
        order_feed_page.click_on_order_card()
        assert order_feed_page.find_order_detail_window().is_displayed()

    @allure.title('Проверка появления ID заказа в ленте заказов')
    def test_order_id_in_order_feed(self, account_page, main_page, order_feed_page, user_with_order):
        account_page.open_account_page()
        account_page.login_user(user_with_order)
        main_page.click_on_personal_account_button()
        account_page.click_on_order_history_link()
        order_id = account_page.find_order_id()
        main_page.click_on_order_feed_button()
        assert order_feed_page.search_element_by_order_number(order_id).text == order_id

    @allure.title('Проверка увеличения счетчика заказов за все время')
    def test_order_counter_for_all_time(self, account_page, main_page, order_feed_page, user_with_order):
        account_page.open_account_page()
        account_page.login_user(user_with_order)
        main_page.find_flurescent_bun()
        main_page.click_on_order_feed_button()
        count_before_order = order_feed_page.get_total_order_count()
        main_page.click_on_constructor_button()
        main_page.add_bun()
        main_page.click_on_place_an_order_button()
        main_page.get_order_number()
        main_page.click_on_close_button_on_order_modal_form()
        main_page.click_on_order_feed_button()
        count_after_order = order_feed_page.get_total_order_count()
        assert int(count_after_order) == int(count_before_order) + 1

    @allure.title('Проверка увеличения счетчика заказов за сегодня')
    def test_today_order_counter(self, user_with_order, account_page, main_page, order_feed_page):
        account_page.open_account_page()
        account_page.login_user(user_with_order)
        main_page.find_flurescent_bun()
        main_page.click_on_order_feed_button()
        count_before_order = order_feed_page.get_today_order_count()
        main_page.click_on_constructor_button()
        main_page.add_bun()
        main_page.click_on_place_an_order_button()
        main_page.get_order_number()
        main_page.click_on_close_button_on_order_modal_form()
        main_page.click_on_order_feed_button()
        count_after_order = order_feed_page.get_today_order_count()
        assert int(count_after_order) == int(count_before_order) + 1

    @allure.title('Проверка появления номера заказа в разделе "В работе"')
    def test_order_id_in_work(self, account_page, main_page, order_feed_page, user_with_order):
        account_page.open_account_page()
        account_page.login_user(user_with_order)
        main_page.find_flurescent_bun()
        main_page.add_bun()
        main_page.click_on_place_an_order_button()
        order_number = main_page.get_order_number()
        main_page.click_on_close_button_on_order_modal_form()
        main_page.click_on_order_feed_button()
        order_number_in_work = order_feed_page.get_order_from_section_in_work()
        assert int(order_number_in_work) == int(order_number)
