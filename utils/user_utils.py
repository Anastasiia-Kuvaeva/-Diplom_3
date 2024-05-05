# Вспомогательные методы для работы с пользователями
import allure
import requests

from config import Urls


class UserUtils:

    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(data):
        return requests.post(Urls.API_CREATE_USER_URL, data=data)

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        return requests.delete(Urls.API_DELETE_USER_URL, headers={"Authorization": token})
