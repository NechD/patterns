from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    """Абстрактный наблюдатель."""

    @abstractmethod
    def update(self, message: str) -> None:
        """Получение нового сообщенияю"""
        pass


class User(Observer):
    """Обычный пользователь, который любит следить за ценой подписки."""

    def __init__(self, name: str) -> None:
        """
        :param name: имя пользователя, чтоб не спутать его с кем-то другим.
        """
        self.name = name

    def update(self, message: str) -> None:
        """Получение информации об изменении в наблюдаемом."""
        print(f'{self.name} узнал {message}')
