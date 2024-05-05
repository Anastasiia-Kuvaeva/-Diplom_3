from selenium.webdriver.common.by import By


# Локаторы главной страницы
class MainPageLocators:
    # Форма ленты заказа
    FEED_FORM = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")
    # Форма конструктора
    CONSTRUCTOR_FORM = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")
    # Кнопка оформить заказ
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    # Кнопка флюорисцентной булки
    FLUORESCENT_BUN_BTN = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    # Крестик на модульном окне
    CLOSE_POPUP_FORM = (By.XPATH, '//button[contains(@class,"close")]')
    # Счетчик ингредиента
    COUNTER_INGREDIENT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    # Форма оформленного заказа
    ORDER_CARD_FORM = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")
    # Корзина
    BASKET = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    # Номер заказа
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    # Кнопка личного кабинета
    PROFILE_BTN = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    # Форма флюорисцентной булки
    POPUP_FORM_INGREDIENS = (By.XPATH, "//h2[text()= 'Детали ингредиента']")
