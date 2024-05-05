import allure

from config import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


# Тестовый набор для личного кабинета
class TestProfilelPage:

    @allure.title('Тест успешного перехода в "Личный кабинет"')
    @allure.description('''Алгоритм тестирования: 
                    1. Создание пользователя                    
                    2. Переход на главную страницу
                    3. Авторизация пользователя
                    4. Клик по кнопке "Личный кабинет"
                    5. Проверка отображение формы "Личный кабинет"
                    6. Удаление пользователя''')
    def test_go_to_profile__page(self, driver, create_and_delete_new_user, login):
        # Переход на главную страницу
        main_page = MainPage(driver)
        profile_area = ProfilePage(driver)
        # Клик по кнопке "Личный кабинет"
        main_page.click_profile_btn()
        # Проверка
        assert profile_area.check_profile_area_form() and profile_area.get_current_url() == Urls.PROFILE_URL

    @allure.title('Тест успешного перехода в "История Заказов"')
    @allure.description('''Алгоритм тестирования: 
                        1. Создание пользователя                    
                        2. Переход на главную страницу
                        3. Авторизация пользователя
                        4. Клик по кнопке "Личный кабинет"
                        5. Клик по кноке "История заказов"
                        6. Проверка отображение формы "История заказов"
                        7. Удаление пользователя''')
    def test_go_to_feed_orders(self, driver, create_and_delete_new_user, login):
        # Переход на главную страницу
        main_page = MainPage(driver)
        profile_area = ProfilePage(driver)
        # Клик по кнопке "Личный кабинет"
        main_page.click_profile_btn()
        # Клик по кноке "История заказов"
        profile_area.click_history_orders_btn()
        # Проверка
        assert profile_area.check_profile_area_form() and profile_area.get_current_url() == Urls.ORDER_HISTORY_URL

    @allure.title('Тест успешного выхода из аккаунта"')
    @allure.description('''Алгоритм тестирования: 
                            1. Создание пользователя                    
                            2. Переход на главную страницу
                            3. Авторизация пользователя
                            4. Клик по кнопке "Личный кабинет"
                            5. Клик по кноке "Выход"
                            6. Проверка выхода из аккаунта
                            7. Удаление пользователя''')
    def test_exit_profile_area(self, driver, create_and_delete_new_user, login):
        # Переход на главную страницу
        main_page = MainPage(driver)
        profile_area = ProfilePage(driver)
        login_page = LoginPage(driver)
        # Клик по кнопке "Личный кабинет"
        main_page.click_profile_btn()
        # Клик по кноке "Выход"
        profile_area.click_exit_btn()
        # Проверка
        assert login_page.check_authorization_form_verification() and login_page.get_current_url() == Urls.LOGIN_URL
