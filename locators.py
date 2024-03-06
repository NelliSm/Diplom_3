from selenium.webdriver.common.by import By


class Locators:
    #авторизация, регистрация, восстановление пароля
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # кнопка "Войти в аккаунт" на главной странице
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")  #кнопка "Личный кабинет" на главной странице
    NAME_FIELD_REGISTRATION = (By.XPATH, "(//input[@name= 'name'])[1]")    #поле для ввода имени с названием "Имя" в форме авторизации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, "(//input[@name= 'name'])[2]")   #поле для ввода mail с названием "Email" в форме авторизации
    PASSWORD_FIELD_REGISTRATION = (By.XPATH, "//input[@name= 'Пароль']")   #поле для ввода пароля с названием "Пароль" в форме авторизации
    REG_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")       #кнопка "Зарегистрироваться" после ввода данных

    BUTTON_LINK_LOGIN = (By.XPATH, ".//a[@href='/login']")            #ссылка на форму авторизации по кнопке "Войти" на /registr
    BUTTON_LINK_REGISTRATION = (By.XPATH, ".//a[@href='/registr']")   #ссылка на форму регистрации по кнопке "Зарегистрироваться" на /login
    EMAIL_AUTHORISATION = (By.XPATH, ".//input[@name='name']")        #поле для ввода email с названием "Email" в форме авторизации
    PASSWORD_AUTHORISATION = (By.XPATH, ".//input[@name='Пароль']")   #поле для ввода пароля с названием "Пароль" в форме авторизации
    BUTTON_ENTER = (By.XPATH, "//button[contains(text(), 'Войти')]")  #кнопка "Войти" в форме авторизации
    BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")             #кнопка в личном кабинете с названием "Выход"

    BUTTON_LINK_RECOVER_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")         #кнопка со ссылкой на форму восстановления пароля
    BUT_RECOVER = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")             #кнопка Восстановить пароль на странице авторизации /login
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//button[contains(text(),'Восстановить')]")   #кнопка "Восстановить" на /forgot-password
    EYE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]") #кнопка "Показать пароль" на странице восстановления пароля /reset-password
    BEFORE_CLICK = (By.XPATH, ".//label[contains(@class, 'input__placeholder text noselect text_type_main-default')]")  #поле с паролем до нажатия кнопки "Показать пароль"

    #локаторы на основной странице site/
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")     #кнопка с названием "Конструктор"
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")            #кнопка Лента заказов на главной

    #оформление заказа
    PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка "Оформить заказ" на главной странице
    ORDER = (By.XPATH, "//p[text()='идентификатор заказа']")        #номер заказа в окне создания заказа
    ORDER_FIRST_ACCOUNT = (By.XPATH, ".//a[@href = '/account/order-history/65db910a9ed280001b3bdcc0']") #первый заказ в истории заказов /order-history
    ORDER_STRUCTURE = (By.XPATH, "//p[contains(text(),'Cостав')]")  #состав заказа
    ORDER_LIST_USER = (By.XPATH, ".//ul[@class = 'OrderHistory_profileList__374GU OrderHistory_list__KcLDB']") #поле с карточками заказов в Истории заказов
    COUNT_ORDERS = (By.XPATH, ".//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")  # счетчик заказов Всего в Ленте заказов
    CLOSE = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified__')]")     #кнопка закрыть созданный заказ
    COUNT_ORDERS_TODAY = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__')]")         #счетчик Выполнено заказов за сегодня
    ORDER_AT_WORK = (By.XPATH, ".//li[@class = 'text text_type_digits-default mb-2']")     #номер заказа "в работе"
    ORDER_FEED_ALL = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list__')]")             #лента заказов
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__')]")    #номер созданного заказа
    ORDER_HISTORY = (By.XPATH, ".//a[@href='/account/order-history']")  #кнопка "История заказов" в личном кабинете /profile

    #ингредиенты
    INGRED_BREAD = (By.XPATH, "//p[text() ='Флюоресцентная булка R2-D3']")  #название ингредиента Флюоресцентная булка
    INGRED_SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']")                 #название ингредиента соуса Spicy-X
    DETAILS_INGRED = (By.XPATH, "//h2[text()='Детали ингредиента']")        #локатор с деталями заказа, который отображается по клику на ингредиент, если окно открыто
    BUTTON_CLOSE_INGRED = (By.XPATH,  "//button[contains(@class, 'Modal_modal__close_modified__')]") #кнопка закрывающая окно с деталями ингредиента
    Wind_Close = (By.CLASS_NAME, 'Modal_modal__P3_V5')                          #окно ингредиента закрыто
    Wind_Open = (By.CLASS_NAME, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5') #окно ингредиента открыто
    BASKET = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")  #поле с добавленными ингредиентами для заказа (корзина)
    COUNT_INGRED_BREAD = (By.XPATH, ".//p[@class = 'counter_counter__num__3nue1']") #отображает кол-во добавленных ингредиентов
