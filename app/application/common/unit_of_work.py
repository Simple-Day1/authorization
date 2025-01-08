from app.domain.shared.unit_of_work import UnitOfWorkTracker
from abc import abstractmethod
from typing import Protocol


class UnitOfWorkCommiter(Protocol):
    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError
    

class UnitOfWork(UnitOfWorkTracker, UnitOfWorkCommiter):
    ...
