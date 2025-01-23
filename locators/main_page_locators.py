from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")  # Кнопка "Личный кабинет" на главной странице
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")  # Кнопка "Лента заказов"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')] ")  # Заголовок "Соберите бургер"
    INGREDIENT_DETAILS_HEADER = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Заголовок окна с деталями об ингредиенте
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]") # Кнопка закрытия окна информации об ингридиенте
    INGREDIENT_DETAILS_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal')]") # Окно с информацией об ингридиенте
    COUNTER_INGREDIENT = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]') # Счетчик добавленного ингридиента
    ORDER_ID_WINDOW_HEADER = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]")
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка "Оформить заказ"
    ORDER_MODAL_FORM_CLOSE_BUTTON = By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified')]" # Кнопка закрытия окна оформленного заказа
    CREATED_ORDER_NUMBER = By.XPATH, ".//h2[contains(@class,'Modal_modal__title_shadow')]" # Номер созданного заказа
    FLUORESCENT_BUN = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"  # Флюоресцентная булка в списке ингредиентов
    TARGET_CREATE_ORDER = By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']"  # цель для перетягивания булки
