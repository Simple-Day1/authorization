from dataclasses import dataclass


@dataclass
class Username:
    username: str


@dataclass
class Phone:
    phone: int


@dataclass
class Email:
    email: str


@dataclass
class DateOfBorn:
    date_of_born: int


@dataclass
class Password:
    password: str
