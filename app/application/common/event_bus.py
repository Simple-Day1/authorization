from app.domain.shared.event import DomainEvent
from abc import abstractmethod
from typing import Protocol


class EventBus(Protocol):
    @abstractmethod
    def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError