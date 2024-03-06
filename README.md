#Diplom_3
Для запуска тестов:
pytest -v tests.py

Для формирования отчетов в Allure:
allure serve allure_results

Установка зависимостей:
pip3 install -r requirements.txt

Тестирование веб приложения (https://stellarburgers.nomoreparties.site/)

1. test_main_functionality

Проверка основного функционала:
- переход по клику на «Конструктор»
- переход по клику на «Лента заказов»
- если кликнуть на ингредиент, появится всплывающее окно с деталями
- всплывающее окно закрывается кликом по крестику
- при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается
- залогиненный пользователь может оформить заказ

2. test_order_feed

Раздел «Лента заказов»:
- если кликнуть на заказ, откроется всплывающее окно с деталями
- заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
- при создании нового заказа счётчик Выполнено за всё время увеличивается
- при создании нового заказа счётчик Выполнено за сегодня увеличивается
- после оформления заказа его номер появляется в разделе В работе

3. test_password_recovery

Восстановление пароля:

- переход на страницу восстановления пароля по кнопке «Восстановить пароль»
- ввод почты и клик по кнопке «Восстановить»
- клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его

4. test_personal_account

Личный кабинет: 

- переход по клику на «Личный кабинет»,
- переход в раздел «История заказов»,
- выход из аккаунта.
- 