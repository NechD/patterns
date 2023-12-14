from models.observable import Observable


class Content(Observable):
    """Подписка, за обновлениями в услвоиях которой следят тысячи людей."""

    def change_something(self, price: str) -> None:
        """Выпуск контента"""
        self.notify_observers('вышла новая' + price)

