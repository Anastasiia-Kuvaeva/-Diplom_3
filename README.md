# Diplom_3
=======
# Тестирование веб-приложения Stellar Burgers

## Описание тестов

- **tests/test_main_page.py** - Тестовый набор для тестирования главной страницы
- **tests/test_order_feed.py** - Тестовый набор для тестирования ленты заказов
- **tests/test_password_recovery_page.py** - Тестовый набор для тестирования восстановления пароля
- **tests/test_profile_page.py** - Тестовый набор для тестирования личного кабинета

- **pages/base_page.py** - Базовая функциональность
- **pages/login_page.py** - Page Object Model для формы авторизации
- **pages/main_page.py** - Page Object Model для главной страницы
- **pages/order_feed_page.py** - Page Object Model для ленты заказов
- **pages/password_recovery_page.py** - Page Object Model для формы восстановления пароля
- **pages/profile_page.py** - Page Object Model для личного кабинета

- **locators/base_page_locators.py** - локаторы общих элементов сайта
- **locators/login_page_locators.py** - локаторы формы авторизации
- **locators/main_page_locators.py** - локаторы главной страницы
- **locators/order_feed_page_locators.py** - локаторы ленты заказов
- **locators/password_recovery_page_locators.py** - локаторы формы восстановления пароля
- **locators/profile_page_locators.py** - локаторы личного кабинета

- **utils/order_utils.py** - Вспомогательные методы для работы с заказами
- **utils/user_utils.py** - Вспомогательные методы для работы с пользователями

- **config.py** - адреса endpoints
- **conftest.py** - содержит фикстуры
- **data.py** - содержит данные для выполнения тестов
- **helpers.py** - содержит вспомогательные методы
- **README.md** - содержит информацию о проекте
- **requirements** - список зависимостей проекта
- **allure_results** - директория с отчетом о тестировании

## Установка зависимостей
```
pip3 install -r requirements.txt
```

## Запуск тестов
```sh
 pytest
```
## Запуск тестов и генерация Allure-отчёта
```sh
 pytest tests.py --alluredir=allure_results
```
## Отображение отчёта в формате веб-страницы
```sh
 allure serve allure_results
```
