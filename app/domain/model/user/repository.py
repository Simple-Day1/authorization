from app.domain.model.user import User
from abc import abstractmethod
from uuid import UUID
from typing import Protocol


class UserRepository(Protocol):
    @abstractmethod
    def add(self, user: User) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, user: User) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def with_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError