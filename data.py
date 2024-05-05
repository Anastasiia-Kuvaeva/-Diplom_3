# Данные для тестов
from faker import Faker


# Данные пользователя
class UserData:

    # Генерация валидных данных для регистрации пользователя
    @staticmethod
    def generation_valid_data_for_create_user():
        faker = Faker('ru_RU')
        data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }
        return data


# Данные заказа
class OrderData:
    # Корректные ингредиенты
    INGREDIENTS_VALID = {
        "ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
    }
