import allure

from config import Urls
from data import UserData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage


# Тестовый набор для формы восстановления пароля
class TestPasswordRecoveryPage:

    @allure.title('Тест успешного перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('''Алгоритм тестирования: 
                            1. Переход на главную страницу
                            2. Клик на кнопку "Личный кабинет"
                            3. Клик по кнопке "Восстановить пароль"
                            4. Проверка отображения формы восстановления пароля''')
    def test_follow_to_the_password_recovery_page(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = PasswordRecoveryPage(driver)
        # Клик на кнопку "Личный кабинет"
        main_page.move_to_profile_btn_and_click()
        # Клик по кнопке "Восстановить пароль"
        login_page.click_recovery_btn()
        # Проверка
        assert (recovery_page.check_recovery_form()
                and recovery_page.get_current_url() == Urls.PASSWORD_RECOVERY_URL)

    @allure.title('Тест успешного ввода email и клик по кнопке "Восстановить"')
    @allure.description('''Алгоритм тестирования: 
                            1. Переход на главную страницу
                            2. Клик на кнопку "Личный кабинет"
                            3. Клик по кнопке "Восстановить пароль"
                            4. Заполнение поля "Email"
                            5. Клик на кнопку "Восстановить"
                            6. Проверка отображения формы смены пароля''')
    def test_input_password_and_click_recovery_btn(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = PasswordRecoveryPage(driver)
        # Клик на кнопку "Личный кабинет"
        main_page.move_to_profile_btn_and_click()
        # Клик по кнопке "Восстановить пароль"
        login_page.click_recovery_btn()
        # Заполнение поля "Email"
        recovery_page.send_email_to_email_field(UserData.generation_valid_data_for_create_user()["email"])
        # Клик на кнопку "Восстановить"
        recovery_page.click_recovery_btn()
        # Проверка
        assert recovery_page.check_save_btn() and recovery_page.get_current_url() == Urls.PASSWORD_RESET_URL

    @allure.title('Тест успешного клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его"')
    @allure.description('''Алгоритм тестирования: 
                            1. Переход на главную страницу
                            2. Клик на кнопку "Личный кабинет"
                            3. Клик по кнопке "Восстановить пароль"
                            4. Заполнение поля "Email"
                            5. Клик на кнопку "Восстановить"
                            6. Заполнить поле "Пароль"
                            7. Клик на кнопку "Показать"
                            8. Проверка подсветки поля''')
    def test_checking_the_backlight_of_the_password_field(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = PasswordRecoveryPage(driver)
        user_data = UserData.generation_valid_data_for_create_user()
        # Клик на кнопку "Личный кабинет"
        main_page.move_to_profile_btn_and_click()
        # Клик по кнопке "Восстановить пароль"
        login_page.click_recovery_btn()
        # Заполнение поля "Email"
        recovery_page.send_email_to_email_field(user_data["email"])
        # Клик на кнопку "Восстановить"
        recovery_page.click_recovery_btn()
        # Заполнить поле "Пароль" и Клик на кнопку "Показать" и Проверка
        assert recovery_page.check_active_password_field(user_data["password"])
