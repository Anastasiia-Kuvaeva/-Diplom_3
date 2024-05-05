from selenium.webdriver.common.by import By


# Локаторы общих элементов страниц
class BaseLocators:
    # Кнопка конструктор
    CONSTRUCTOR_BTN = (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    # Кнопка лента заказов
    FEED_BTN = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    # Кнопка личного кабинета
    PROFILE_BTN = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")