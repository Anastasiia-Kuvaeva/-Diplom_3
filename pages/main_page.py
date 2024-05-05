import allure

from pages.base_page import BasePage
from locators.base_page_locators import BaseLocators
from locators.main_page_locators import MainPageLocators

# Page Object Model главной страницы
class MainPage(BasePage):

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_btn(self):
        self.move_to_element_and_click(BaseLocators.CONSTRUCTOR_BTN)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_feed_btn(self):
        self.move_to_element_and_click(BaseLocators.FEED_BTN)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_profile_btn(self):
        self.move_to_element_and_click(BaseLocators.PROFILE_BTN)

    @allure.step('Переход и клик по кнопке "Личный Кабинет"')
    def move_to_profile_btn_and_click(self):
        self.move_to_element_and_click(MainPageLocators.PROFILE_BTN)

    @allure.step('Проверка отображения формы конструктор')
    def check_constructor_form(self):
        return self.check_element(MainPageLocators.CONSTRUCTOR_FORM)

    @allure.step('Проверка отображения формы ленты заказов')
    def check_orders_feed_form(self):
        return self.check_element(MainPageLocators.FEED_FORM)

    @allure.step('Клик по ингредиенту')
    def click_ingredient_btn(self):
        self.click_button(MainPageLocators.FLUORESCENT_BUN_BTN)

    @allure.step('Проверка отображения формы ингредиента')
    def check_ingredient_form(self):
        return self.check_element(MainPageLocators.POPUP_FORM_INGREDIENS)

    @allure.step('Проверка закрытия формы ингредиента')
    def check_close_ingredient_form(self):
        return self.check_element_is_not_visible(MainPageLocators.POPUP_FORM_INGREDIENS)

    @allure.step('Закрытие формы информации об ингридиенте')
    def close_popup_form(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_POPUP_FORM)

    @allure.step('Добавить булку в корзину')
    def add_bun(self):
        self.drag_and_drop(MainPageLocators.FLUORESCENT_BUN_BTN, MainPageLocators.BASKET)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_place_order_button(self):
        self.click_button(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        return int(self.get_text_locator(MainPageLocators.COUNTER_INGREDIENT))

    @allure.step('Проверка отображения формы Оформление заказа')
    def check_order_form(self):
        return self.check_element(MainPageLocators.ORDER_CARD_FORM)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        return self.get_text_locator(MainPageLocators.ORDER_NUMBER)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_load_main_page(self):
        self.wait_for_load_element(MainPageLocators.CREATE_ORDER_BUTTON)