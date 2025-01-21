import allure
from locators.main_page_locators import MainPageLocators
from page.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_on_personal_account_button(self):
        self.find_element_with_wait(MainPageLocators.FLUORESCENT_BUN)
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)


    @allure.step('Нажатие на кнопку "Лента заказов"')
    def click_on_order_feed_button(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('найти ингридиент')
    def find_flurescent_bun(self):
        self.find_element_with_wait(MainPageLocators.FLUORESCENT_BUN)



    @allure.step('Нажатие на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Найти заголовок "Соберите бургер"')
    def find_constructor_header(self):
        return self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step('Нажатие на ингридиент')
    def click_on_ingredient(self):
        self.click_to_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step('Найти заголовок окна с информацией об ингредиенте')
    def find_ingredient_info_header(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.step('Нажатие на кнопку закрытия окна информации об ингредиенте')
    def click_on_ingredient_info_close_button(self):
        self.click_to_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step('Дождаться исчезновения окна с информацией об ингредиенте')
    def find_ingredient_info_window(self):
        self.wait_element_invisibility(MainPageLocators.INGREDIENT_DETAILS_WINDOW)
        return True


    @allure.step('Добавить булку в корзину')
    def add_bun(self):
        self.find_element_with_wait(MainPageLocators.FLUORESCENT_BUN)
        self.drag_and_drop_element(MainPageLocators.FLUORESCENT_BUN, MainPageLocators.TARGET_CREATE_ORDER)


    @allure.step('найти счетчик ингредиента в корзине')
    def find_ingredient_counter(self):
        return self.find_element_with_wait(MainPageLocators.COUNTER_INGREDIENT)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_on_place_an_order_button(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('найти заголовок "Идентификатор заказа"')
    def find_order_id_header(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_ID_WINDOW_HEADER)

    @allure.step('Нажать кнопку закрыть на окне с информацией о заказе')
    def click_on_close_button_on_order_modal_form(self):
        self.find_element_with_wait(MainPageLocators.ORDER_MODAL_FORM_CLOSE_BUTTON)
        self.click_to_element(MainPageLocators.ORDER_MODAL_FORM_CLOSE_BUTTON)

    @allure.step('Получить номер созданного заказа')
    def get_order_number(self):
        order_number = self.get_text_from_element(MainPageLocators.CREATED_ORDER_NUMBER)
        while order_number == '9999':
            order_number = self.get_text_from_element(MainPageLocators.CREATED_ORDER_NUMBER)
        return order_number

