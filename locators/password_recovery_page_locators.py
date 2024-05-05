from selenium.webdriver.common.by import By


# Локаторы формы восстановления пароля
class PasswordRecoveryPageLocators:
    # Поле email
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    # Кнопка восстановить
    RECOVER_BTN = (By.XPATH, ".//button[text() = 'Восстановить']")
    # Кнопка войти
    LOGIN_ACCOUNT_BTN = (By.XPATH, ".//a[text() = 'Войти']")
    # Поле ввода нового пароля
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    # Поле ввода кода из письма
    CODE_FROM_MAIL = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    # Кнопка Сохранить
    SAVE_BTN = (By.XPATH, ".//button[text() = 'Сохранить']")
    # ФОрма восстановления пароля
    RECOVERY_TEXT_FORM = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    # Показать пароль
    SHOW_BTN = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    # Подсветка поля пароль
    INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")
