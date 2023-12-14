from abc import ABCMeta

from patterns.observer import Observer


class Observable(metaclass=ABCMeta):
    """Абстрактный наблюдаемый."""

    def __init__(self) -> None:
        """Constructor."""
        self.observers = []

    def register(self, observer: Observer) -> None:
        """Регистрация нового наблюдателя на подписку."""
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        """ Передача сообщения всем наблюдателям, подписанным на события данного объекта наблюдаемого класса."""
        for observer in self.observers:
            observer.update(message)