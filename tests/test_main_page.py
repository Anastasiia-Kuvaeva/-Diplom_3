import allure

from config import Urls
from pages.main_page import MainPage

# Тестовый набор для главной страницы
class TestMainPage:

    @allure.title('Тест успешного перехода по клику на "Конструктор"')
    @allure.description('''Алгоритм тестирования: 
                1. Переход на главную страницу
                2. Клик по кнопке "Личный кабинет"
                3. Клик по кнопке "Конструктор"
                4. Проверка ответа отображения формы конструктора и текущего url''')
    def test_follow_to_constructor_page(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        # Клик по кнопке "Личный кабинет"
        main_page.move_to_profile_btn_and_click()
        # Клик по кнопке "Конструктор"
        main_page.click_constructor_btn()
        # Проверка
        assert (main_page.check_constructor_form()
                and main_page.get_current_url() == Urls.BASE_URL)

    @allure.title('Тест успешного перехода по клику на "Лента заказов"')
    @allure.description('''Алгоритм тестирования: 
                    1. Переход на главную страницу
                    2. Клик по кнопке "Лента заказов"                   
                    3. Проверка ответа отображения формы "Лента заказов" и текущего url''')
    def test_follow_to_orders_feed_page(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        # Клик по кнопке "Лента заказов"
        main_page.click_feed_btn()
        # Проверка
        assert (main_page.check_orders_feed_form()
                and main_page.get_current_url() == Urls.FEED_URL)

    @allure.title('Тест успешного появления всплывающего окна с деталями если кликнуть на ингредиент')
    @allure.description('''Алгоритм тестирования: 
                        1. Переход на главную страницу
                        2. Клик по кнопке "Флюорисцентная булка R2-D3"             
                        3. Проверка отображения высплывающего окна с деталями ингредиента''')
    def test_check_ingredient_form(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        # Клик по кнопке "Лента заказов"
        main_page.click_ingredient_btn()
        # Проверка
        assert main_page.check_ingredient_form()

    @allure.title('Тест успешного закрытия всплывающего окна с деталями ингредиента')
    @allure.description('''Алгоритм тестирования: 
                            1. Переход на главную страницу
                            2. Клик по кнопке "Флюорисцентная булка R2-D3"    
                            3. Клик по кнопке закрытия окна         
                            4. Проверка закрытия высплывающего окна с деталями ингредиента''')
    def test_close_fluorescent_bun_form(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        # Клик по кнопке "Лента заказов"
        main_page.click_ingredient_btn()
        # Клик по кнопке закрытия окна
        main_page.close_popup_form()
        # Проверка
        assert main_page.check_close_ingredient_form()

    @allure.title('Тест успешного увеличения счётчика ингридиента при добавлении ингредиента в заказ')
    @allure.description('''Алгоритм тестирования: 
                                1. Переход на главную страницу
                                2. Добавление ингредиента в корзину
                                3. Проверка увеличения счетчика ингредиента''')
    def test_increment_counter_ingredient(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        # Добавление ингредиента в корзину
        main_page.add_bun()
        # Проверка
        assert main_page.check_counter_ingredient() > 0

    @allure.title('Тест успешного оформления заказа авторизованным пользователем')
    @allure.description('''Алгоритм тестирования: 
                                    1. Создание пользователя
                                    2. Переход на главную страницу
                                    3. Авторизация пользователя                                   
                                    4. Оформление заказа (+ добавление ингредиента в корзину)
                                    5. Проверка отображения формы заказа
                                    6. Удаление пользователя''')
    def test_create_order(self, driver, login):
        # Переход на главную страницу
        main_page = MainPage(driver)
        # Создание заказа
        main_page.create_order()
        # Проверка
        assert main_page.check_order_form()
