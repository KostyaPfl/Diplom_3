from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")  #  Кнопка "Восстановить"
    EMAIL_FIELD = (By.XPATH, "//input[@class = 'text input__textfield text_type_main-default']")  #  Поле ввода email
