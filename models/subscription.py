from abc import ABCMeta

from models.observable import Observable
from patterns.observer import Observer


class Subscription(Observable):
    """Подписка, за обновлениями в услвоиях которой следят тысячи людей."""

    def change_something(self, price: str) -> None:
        """Выпуск очередной новости."""
        self.notify_observers('изменилась цена на подписку '+price)


