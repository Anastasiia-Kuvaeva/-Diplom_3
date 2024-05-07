import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


# Page Object Model формы авторизации
class LoginPage(BasePage):

    @allure.step('Проверка отображения формы логина')
    def check_authorization_form_verification(self):
        return self.check_element(LoginPageLocators.LOGIN_FORM)

    @allure.step('Заполнение поля "Email"')
    def send_email_to_email_field(self, email):
        self.send_keys_to_field(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполнение поля "Password"')
    def send_password_to_password_field(self, password):
        self.send_keys_to_field(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик по кнопке "Войти"')
    def click_login_btn(self):
        self.move_to_element_and_click(LoginPageLocators.LOGIN_BTN)

    @allure.step('Авторизация пользователя')
    def login(self, email, password):
        self.send_email_to_email_field(email)
        self.send_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_recovery_btn(self):
        self.move_to_element_and_click(LoginPageLocators.PASSWORD_RECOVERY_BTN)

    @allure.step('Клик по кнопке "Зарегистрироваться"')
    def click_register_btn(self):
        self.move_to_element_and_click(LoginPageLocators.REGISTRATION_BTN)
