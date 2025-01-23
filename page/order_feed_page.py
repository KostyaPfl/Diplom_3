import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from page.base_page import BasePage
from data import URLS


class OrderFeedPage(BasePage):

    @allure.step('Найти заголовок "Лента заказов"')
    def find_order_feed_header(self):
        return self.find_element_with_wait(OrderFeedPageLocators.ORDER_FEED_HEADER)

    @allure.step('Найти заголовок "состав" в окне с деталями о заказе')
    def find_order_detail_window(self):
        return self.find_element_with_wait(OrderFeedPageLocators.ORDER_DETAILS)

    @allure.step('Нажать на карточку заказа')
    def click_on_order_card(self):
        self.find_element_with_wait(OrderFeedPageLocators.ORDER_CARD)
        self.click_to_element(OrderFeedPageLocators.ORDER_CARD)

    @allure.step('Поиск элемента по номеру заказа')
    def search_element_by_order_number(self, order_number):
        search_number_order = OrderFeedPageLocators.ORDERS_LIST
        search_number_order = (search_number_order[0], search_number_order[1].format(num_order=order_number))
        return self.find_element_with_wait(search_number_order)

    @allure.step('Взять значение счетчика выполнено за все время')
    def get_total_order_count(self):
        self.find_element_with_wait(OrderFeedPageLocators.TOTAL_ORDER_COUNT)
        return self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDER_COUNT)

    @allure.step('Взять значение счетчика выполнено за сегодня')
    def get_today_order_count(self):
        self.find_element_with_wait(OrderFeedPageLocators.TODAY_ORDER_COUNT)
        return self.get_text_from_element(OrderFeedPageLocators.TODAY_ORDER_COUNT)

    @allure.step('Получение текущего номера заказа в разделе "В работе"')
    def get_order_from_section_in_work(self):
        return self.find_element_with_wait(OrderFeedPageLocators.ORDER_IN_WORK).text

    @allure.step('Открыть страницу ленты заказов')
    def open_order_feed_page(self):
        self.go_to_url(URLS.ORDER_FEED_PAGE_URL)
