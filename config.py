# URL страниц и методов API
class Urls:
    # главная страница
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    # URL страниц и форм
    FEED_URL = BASE_URL + 'feed'
    LOGIN_URL = BASE_URL + 'login'
    PASSWORD_RECOVERY_URL = BASE_URL + 'forgot-password'
    PASSWORD_RESET_URL = BASE_URL + 'reset-password'
    REGISTRATION_URL = BASE_URL + 'register'
    PROFILE_URL = BASE_URL + 'account/profile'
    ORDER_HISTORY_URL = BASE_URL + 'account/order-history'
    # Адреса методов API
    API_CREATE_USER_URL = BASE_URL + 'api/auth/register'
    API_LOGIN_USER_URL = BASE_URL + 'api/auth/login'
    API_DELETE_USER_URL = BASE_URL + 'api/auth/user'
    API_CREATE_ORDER_URL = BASE_URL + 'api/orders'
    API_GET_ORDER_LIST_URL = BASE_URL + 'api/orders'
