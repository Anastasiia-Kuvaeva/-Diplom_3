import allure
import pytest

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from utils.order_utils import OrderUtils
from data import OrderData
from locators.order_feed_page_locators import OrderFeedPageLocators


# Тестовый набор для ленты заказов
class TestOrderFeedPage:

    @allure.title('Тест успешного открытия всплывающего окно с деталями при клике на заказ')
    @allure.description('''Алгоритм тестирования: 
                           1. Переход на главную страницу
                           2. Клик на кнопку "Лента заказов"
                           3. Клик по первому заказу
                           4. Проверка отображения формы с деталями заказа''')
    def test_check_order_info_window(self, driver):
        # Переход на главную страницу
        main_page = MainPage(driver)
        feed_order = OrderFeedPage(driver)
        # Переход на страницу ленты заказов
        main_page.click_feed_btn()
        # Переход на страницу ленты заказов
        feed_order.click_order_info()
        # Проверка
        assert feed_order.check_order_info_window()

    @allure.title('Тест успешного наличия созданного заказа в разделе "В работе"')
    @allure.description('''Алгоритм тестирования: 
                           1. Создание пользователя
                           2. Переход на главную страницу
                           3. Клик на кнопку "Лента заказов"
                           4. Создание заказа
                           5. Получение заказов в списке "В работе"
                           6. Получение созданного пользователем заказа
                           7. Проверка, что заказ пользователя в списке заказов "В работе"
                           8. Удаление пользователя''')
    def test_check_user_order_in_job(self, driver, create_and_delete_new_user, login):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Переход на главную страницу
        main_page = MainPage(driver)
        feed_order = OrderFeedPage(driver)
        # Клик на кнопку "Лента заказов"
        main_page.click_feed_btn()
        # Создание заказа
        OrderUtils.create_order(token, OrderData.INGREDIENTS_VALID)
        # Получение заказов в списке "В работе"
        orders_in_jobs = feed_order.get_orders_in_jobs()
        # Получение созданного пользователем заказа
        user_order = str(OrderUtils.get_order_list(token).json()["orders"][0]["number"])
        # Проверка
        assert user_order in orders_in_jobs

    @allure.title('Тест успешного инкремента счетчиков "Выполнено за всё время" и "Выполнено за сегодня" при создании '
                  'нового заказа')
    @allure.description('''Алгоритм тестирования: 
                                1. Создание пользователя                                
                                2. Переход на главную страницу
                                3. Клик на кнопку "Лента заказов" 
                                4. Получение текущего значения счетчика
                                5. Создание заказа                               
                                6. Проверка инкремента значения счетчика
                                7. Удаление пользователя''')
    @pytest.mark.parametrize('counter',
                             [OrderFeedPageLocators.DAYLY_ORDERS_COUNTER, OrderFeedPageLocators.TOTAL_ORDERS_COUNTER])
    def test_update_counter_orders(self, driver, create_and_delete_new_user, login, counter):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Переход на главную страницу
        main_page = MainPage(driver)
        feed_order = OrderFeedPage(driver)
        # Клик на кнопку "Лента заказов"
        main_page.click_feed_btn()
        # Получение текущего значения счетчика
        old_counter = int(feed_order.get_orders_count(counter))
        # Создание заказа
        OrderUtils.create_order(token, OrderData.INGREDIENTS_VALID)
        # Получение текущего значения счетчика
        new_counter = int(feed_order.get_orders_count(counter))
        # Проверка
        assert new_counter > old_counter

    @allure.title('Тест успешного отображения заказов из раздела "История заказов" на странице "Лента заказов"')
    @allure.description('''Алгоритм тестирования: 
                            1. Создание пользователя
                            2. Создание заказа
                            3. Переход на главную страницу
                            4. Клик на кнопку "Лента заказов" 
                            5. Получение созданного пользователем заказа
                            6. Получаем список заказов на странице "Лента заказов"
                            7. Проверка, что заказ пользователя в списке заказов
                            8. Удаление пользователя''')
    def test_check_user_orders_in_orders_history(self, driver, create_and_delete_new_user, create_order, login):
        # Создание пользователя
        token = create_and_delete_new_user[1].json()["accessToken"]
        # Переход на главную страницу
        main_page = MainPage(driver)
        feed_order = OrderFeedPage(driver)
        # Клик на кнопку "Лента заказов"
        main_page.click_feed_btn()
        # Получение созданного пользователем заказа
        user_order = str(OrderUtils.get_order_list(token).json()["orders"][0]["number"])
        # Получаем список заказов на странице "Лента заказов"
        orders_history_in_feed = feed_order.get_orders_history()
        # Проверка
        assert user_order in orders_history_in_feed
