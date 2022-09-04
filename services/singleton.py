from typing import Any


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:  # type: ignore
            instance = super().__call__(*args, **kwargs)  # type: ignore
            cls._instances[cls] = instance  # type: ignore
        return cls._instances[cls]  # type: ignore
