from selenium.webdriver.common.by import By


# Локаторы ленты заказов
class OrderFeedPageLocators:
    # Заголовок h1 страницы
    TITLE_ORDERS_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')
    # Окно детали заказа
    ORDERS_INFO = (By.XPATH, '//p[text()="Cостав"]')
    # Счетчик заказов за все время
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # Счетчик заказов за сегодня
    DAYLY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Заказы "В работе"
    COUNT_ORDER_IN_JOB = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    # Первый заказ в ленте
    ORDER_INFO_WINDOW = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    # Все заказы в ленте
    ORDER_HISTORY = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
