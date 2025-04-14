from selenium.webdriver.common.by import By

class Locators:
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input") # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input") # Поле ввода пароля

    ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']") # Кнопка "Личный Кабинет"
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text() = 'История заказов']") # Кнопка "История заказов"
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[@class='text text_type_digits-default'])[1]") # Номер заказа в истории заказов
    ORDER_NUMBER_IN_CONSTRUCTOR = (By.XPATH, "(//h2[contains(@class, 'text_type_digits-large')])") # Номер заказа в конструкторе
    SIGN_OUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") # Кнопка "Выход"

    ORDER_FEED_BUTTON = (By.XPATH, "//p[text() = 'Лента Заказов']") # Кнопка "Лента Заказов"
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text() = 'Лента заказов']") # Заголовок "Лента заказов"
    ORDER_NUMBER_IN_WORK = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']") # Номер заказа в разделе "В работе"
    ORDER_IN_FEED_BUTTON = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']") # Кнопка созданного заказа в ленте
    ORDER_NUMBER_IN_DETAILS = (By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']") # Номер заказа в окне деталей заказа
    COMPLETED_ORDERS_ALL_TIME = (By.XPATH, "//div[p[contains(text(), 'Выполнено за все время')]]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Количество выполненных заказов за все время
    COMPLETED_ORDERS_TODAY = (By.XPATH, "//div[p[contains(text(), 'Выполнено за сегодня')]]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Количество выполненных заказов за сегодня

    PASSWORD_RECOVERY_HYPERLINK = (By.XPATH, "//a[text() = 'Восстановить пароль']") # Гиперссылка "Восстановить пароль"
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']") # Кнопка "Восстановить"
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]") # Кнопка показать/скрыть пароль
    ACTIVE_PASSWORD_FIELD = (By.XPATH, "//div[contains(@class, 'input_status_active')]") # Активное поле ввода пароля

    OVERLAY = (By.CLASS_NAME, "Modal_modal__loading__3534A") # Модальное окно
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка "Конструктор"
    CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]") # Корзина
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']") # Кнопка "Оформить заказ"
    R2_D3_BUN_BUTTON = (By.XPATH, "//p[text() = 'Флюоресцентная булка R2-D3']") # Кнопка "Флюоресцентная булка R2-D3"
    R2_D3_BUN_TOP = (By.XPATH, "//span[text() = 'Флюоресцентная булка R2-D3 (верх)']") # Ингредиент "Флюоресцентная булка R2-D3 верх"
    R2_D3_BUN_BOTTOM = (By.XPATH, "//span[text() = 'Флюоресцентная булка R2-D3 (низ)']") # Ингредиент "Флюоресцентная булка R2-D3 низ"
    R2_D3_BUN_COUNTER = (By.XPATH, '//a[.//p[text()="Флюоресцентная булка R2-D3"]]//p[@class="counter_counter__num__3nue1"]') # Счетчик ингредиента "Флюоресцентная булка R2-D3"
    INGREDIENT_DETAILS_TITLE = (By.XPATH, "//h2[text() = 'Детали ингредиента']") # Заголовок "Детали ингредиента"
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # Кнопка закрытия окна с деталями ингредиента