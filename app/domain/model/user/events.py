from domain.shared.event import DomainEvent
from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class UserCreated(DomainEvent):
    user_id: UUID
    username: str
    password: str
    phone: int
    email: str
    date_of_born: str


@dataclass(frozen=True)
class UsernameIsChanged(DomainEvent):
    user_id: UUID
    username: str


@dataclass(frozen=True)
class PasswordIsChanged(DomainEvent):
    user_id: UUID
    password: str


@dataclass(frozen=True)
class PhoneIsChanged(DomainEvent):
    user_id: UUID
    phone: int


@dataclass(frozen=True)
class EmailIsChanged(DomainEvent):
    user_id: UUID
    email: str


@dataclass(frozen=True)
class DateOfBornIsChanged(DomainEvent):
    user_id: UUID
    date_of_born: str
