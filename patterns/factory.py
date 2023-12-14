from typing import Hashable, Callable

from models.content import Content
from models.subscription import Observable, Subscription


class Factory(object):
    """Фабрика, позволяет создавать объекты подписка и контент."""
    @staticmethod
    def get(class_name: Hashable) -> Observable:
        if not isinstance(class_name, Hashable):
            raise ValueError()

        classes: dict[Hashable, Callable[..., Observable]] = {
            "Subscription": Subscription,
            "Content": Content
        }

        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_()

        raise ValueError
