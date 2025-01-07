from domain.shared.event import DomainEvent
from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class UserCreated(DomainEvent):
    user_id: UUID
    firstname: str
    middlename: str
    lastname: str
    password: str
    date_of_born: str


@dataclass(frozen=True)
class FullnameIsChanged(DomainEvent):
    user_id: UUID
    firstname: str
    middlename: str | None
    lastname: str


@dataclass(frozen=True)
class ContactsIsChanged(DomainEvent):
    user_id: UUID
    email: str | None
    phone: int | None


@dataclass(frozen=True)
class DateOfBornIsChanged(DomainEvent):
    user_id: UUID
    day: int
    month: int
    year: int
