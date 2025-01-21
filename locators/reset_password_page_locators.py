from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    RESTORE_PASSWORD_HEADER = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")  #  Заголовок страницы "Восстановление пароля"
    VISIBILITY_ELEM = (By.XPATH, "//div[@class='input__icon input__icon-action']")  # Кнопка показать/скрыть пароль
    CODE_FIELD = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")  #  Введите код из письма
    FIELD_ACTIVE_PASSWORD = (By.XPATH, ".//label[contains(@class,'input__placeholder-focused')]")  # Активное(подсвеченное) поле для ввода пароля (метка)



