# Diplom_3
## В проэкте реализованны тесты веб-приложения Stellar Burgers.
## Список реализованных проверок:
### <u>Восстановление пароля:</u>
1. **test_go_to_restore_page_from_login_page**: Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»
2. **test_restore_password_enter_email_and_click_restore**: Проверка ввода почты и клик по кнопке «Восстановить»
3. **test_click_on_password_button_makes_field_active**: Проверка клика по кнопке показать/скрыть пароль делает поле активным

### <u>Личный кабинет </u>
1. **test_go_to_personal_account_page**:Проверка перехода в личный кабинет нажатием на кнопку «личный кабинет» на главной странице
2. **test_go_to_order_history**: Проверка перехода в историю заказов
3. **test_logout_user**: Проверка выхода из аккаунта

### <u>Проверка основного функционала</u>
1. **test_click_on_constructor_button**: Проверка перехода по кнопке "Конструктор"
2. **test_click_on_order_feed_button**: Проверка перехода по кнопке "Лента заказов"
3. **test_open_ingredient_info_window**: Проверка открытия окна с деталями об ингедиенте
4. **test_close_ingredient_info_window**: Проверка закрытия окна с деталями об ингедиенте
5. **test_increasing_counter_ingredient**: Проверка увеличения счетчика при добавлении ингредиента
6. **test_authorized_user_make_order**: Проверка что авторизованный пользователь может оформить заказ

### <u>Раздел «Лента заказов»</u>
1. **test_open_order_detail_window**: Проверка открытия окна с деталями заказа
2. **test_order_id_in_order_feed**: Проверка появления ID заказа в ленте заказов
3. **test_order_counter_for_all_time**: Проверка увеличения счетчика заказов за все время
4. **test_today_order_counter**: Проверка увеличения счетчика заказов за сегодня
5. **test_order_id_in_work**: Проверка появления номера заказа в разделе "В работе"

Установка внешних зависимостей с помощью команды pip3 install -r requirements.txt

Запуск всех тестов с генерацией отчетов командой: python -m pytest --alluredir allure-results

Просмотреть полученные отчеты командой: allure serve allure-results