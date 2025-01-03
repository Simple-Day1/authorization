from abc import abstractmethod
from typing import Protocol
from app.domain.account.account import Account


class UserRepository(Protocol):
    @abstractmethod
    async def add(self, account: Account):
        ...
    
    @abstractmethod
    async def delete(self, account: Account):
        ...

    @abstractmethod
    async def update(self, account: Account):
        ...
