from typing import Callable
from interface.Message import IMessage
from services.singleton import SingletonMeta  # type: ignore
from reactivex import Subject, operators as ops  # type: ignore


class Broker(metaclass=SingletonMeta):
    _subject = Subject[IMessage]()

    def emit(self, event: IMessage):
        self._subject.on_next(event)

    def on(self, event: str,  action: Callable[[str], None]):
        # return self._subject.subscribe(action)
        result = self._subject.pipe(ops.filter(
            lambda e: e.name == event), ops.map(lambda e: e.value))
        return result.subscribe(action)


# filter(lambda e: e.name == = event), ops.map(lambda e: e.value)
