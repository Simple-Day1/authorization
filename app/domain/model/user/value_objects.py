from dataclasses import dataclass


@dataclass(frozen=True)
class Contacts:
    email: str | None
    phone: int | None


@dataclass(frozen=True)
class Fullname:
    firstname: str
    lastname: str
    middlename: str | None

@dataclass(frozen=True)
class Date:
    day: str
    month: str
    year: str
