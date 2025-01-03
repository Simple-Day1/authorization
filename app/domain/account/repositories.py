from abc import abstractmethod
from typing import Protocol
from app.domain.user.user import User


class UserRepository(Protocol):
    @abstractmethod
    async def add(self, user: User):
        ...
    
    @abstractmethod
    async def delete(self, user: User):
        ...

    @abstractmethod
    async def update(self, user: User):
        ...
