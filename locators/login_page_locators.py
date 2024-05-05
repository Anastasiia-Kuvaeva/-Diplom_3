from selenium.webdriver.common.by import By


# Локаторы формы авторизации
class LoginPageLocators:
    # Форма авторизации
    LOGIN_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")
    # Поле email
    EMAIL_INPUT = (By.XPATH, ".//input[@name = 'name']")
    # Поле пароля
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    # Кнопка войти
    LOGIN_BTN = (By.XPATH, "//button[text() = 'Войти']")
    # Кнопка зерегистрироваться
    REGISTRATION_BTN = (By.XPATH, "//a[text() = 'Зарегистрироваться']")
    # Кнопка восстановить пароль
    PASSWORD_RECOVERY_BTN = (By.XPATH, "//a[text() = 'Восстановить пароль']")
