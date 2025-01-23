from selenium.webdriver.common.by import By


class AccountPageLocators:
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # Текстовая ссылка на страницу "Восстановить пароль"
    EMAIL_FIELD = (By.XPATH, "//input[@type = 'text']")  # Поле ввода email на странице авторизации
    PASSWORD_FIELD = (By.XPATH, "//input[@type = 'password']")  # Поле ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # Кнопка "Войти"
    ENTER_HEADER = (By.XPATH, "//h2[contains(text(),'Вход')]")  # Заголовок "Вход"
    ORDER_HISTORY_LIST = (By.XPATH, "//div[contains(@class, 'OrderHistory_orderHistory')]")  # Список в истории заказов
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход"
    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "text text_type_digits")]')
    PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]")  # Ссылка на "Профиль"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(),'История заказов')]")  # Ссылка на "Историю заказов"


