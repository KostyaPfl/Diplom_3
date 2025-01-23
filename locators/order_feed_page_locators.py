from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_HEADER = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")  # Заголовок страницы
    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')  # Карточка заказа
    ORDER_DETAILS = (By.XPATH, ".//p[text()='Cостав']") # заголовок окна с информацией о заказе
    TOTAL_ORDER_COUNT = By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p" # Счетчик "Всего заказов"
    TODAY_ORDER_COUNT = By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p" # счктчик "Заказов за сегодня"
    ORDERS_LIST = (By.XPATH, '//*[text()="{num_order}"]')  # Список заказов
    ORDER_IN_WORK = (By.XPATH, "//li[contains(text(), '0')]")  # Список заказов в работе
