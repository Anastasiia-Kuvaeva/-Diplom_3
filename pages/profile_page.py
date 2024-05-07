import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


# Page Object Model личного кабинета
class ProfilePage(BasePage):

    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_profile_area_form(self):
        return self.check_element(ProfilePageLocators.PROFILE_FORM)

    @allure.step('Клик по кнопке "Профиль"')
    def click_profile_btn(self):
        self.click_button(ProfilePageLocators.PROFILE_BTN)

    @allure.step('Клик по кнопке "История заказов"')
    def click_history_orders_btn(self):
        self.click_button(ProfilePageLocators.ORDER_HISTORY_BTN)

    @allure.step('Проверка отображения формы "История заказов"')
    def check_history_form(self):
        return self.check_element(ProfilePageLocators.HISTORY_ORDER_FORM)

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_btn(self):
        self.click_button(ProfilePageLocators.EXIT_BTN)

    @allure.step('Клик по кнопке "Отмена"')
    def click_cansel_btn(self):
        self.click_button(ProfilePageLocators.CANCEL_BTN)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_btn(self):
        self.click_button(ProfilePageLocators.SAVE_BTN)

    @allure.step('Получение номера заказа в истории')
    def get_orders_number(self):
        return self.get_text_locator(ProfilePageLocators.NUMBER_ORDER)
