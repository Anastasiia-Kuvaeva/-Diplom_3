import pytest
from selenium import webdriver
from config import Urls
from data import (UserData, OrderData)
from utils.user_utils import UserUtils
from utils.order_utils import OrderUtils
from pages.main_page import MainPage
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", type=str)


# Фикстура получения и закрытия driver
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = None
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


# Фикстура создания м последующего удаления пользователя
@pytest.fixture
def create_and_delete_new_user():
    # Генерация данных нового пользователя
    payload = UserData.generation_valid_data_for_create_user()
    # Создание нового пользователя
    response = UserUtils.create_user(payload)
    yield payload, response
    # Удаление пользователя
    UserUtils.delete_user(response.json()["accessToken"])


# Фикстура авторизации пользователя
@pytest.fixture
def login(driver, create_and_delete_new_user):
    # Создание пользователя
    user_data = create_and_delete_new_user[0]
    main_page = MainPage(driver)
    main_page.click_profile_btn()
    login_page = LoginPage(driver)
    # Авторизация пользователя
    login_page.login(user_data["email"], user_data["password"])
    main_page.wait_load_main_page()


@pytest.fixture
def create_order(create_and_delete_new_user):
    # Создание пользователя
    token = create_and_delete_new_user[1].json()["accessToken"]
    # Создание заказа
    response = OrderUtils.create_order(token, OrderData.INGREDIENTS_VALID)
    return response.json()["order"]["number"]
