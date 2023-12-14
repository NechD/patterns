from patterns.factory import Factory
from patterns.observer import User

if __name__ == '__main__':
    # Пример использования фабрики и наблюдателя
    factory = Factory()

    # Создание контента
    teen_wolf_content = factory.get('Content')

    # Создание подписки
    monthly_subsciption = factory.get('Subscription')

    # Создание пользователей
    user1 = User('Робин')
    user2 = User('Бобин')

    teen_wolf_content.register(user1)
    monthly_subsciption.register(user2)
    monthly_subsciption.register(user1)

    teen_wolf_content.change_something(' Серия 3')
    monthly_subsciption.change_something(' 4000 рублей')


