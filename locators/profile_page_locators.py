from selenium.webdriver.common.by import By


# Локаторы личного кабинета
class ProfilePageLocators:
    # Форма личного кабинета
    PROFILE_FORM = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")
    # Кнопка профиль
    PROFILE_BTN = (By.XPATH, ".//a[text() = 'Профиль']")
    # Кнопка история заказов
    ORDER_HISTORY_BTN = (By.XPATH, ".//a[text() = 'История заказов']")
    # Форма истории заказов
    HISTORY_ORDER_FORM = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")
    # Номер заказа
    NUMBER_ORDER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    # Кнопка отмена
    CANCEL_BTN = (By.XPATH, ".//button[text() = 'Отмена']")
    # Кнопка сохранить
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")
    # Кнопка выход
    EXIT_BTN = (By.XPATH, ".//button[text() = 'Выход']")