from typing import Self
from app.domain.account.value_objects import Username, DateOfBorn, Phone, Email, Password
from app.domain.account.exceptions import AccountIsAlreadyExistError, AccountNotFoundError
from app.domain.account.events import AccountIsSignedUp, PasswordIsChanged
from app.domain.shared.event import Event
from app.domain.shared.base_entity import BaseEntity
from uuid import UUID


class Account(BaseEntity[UUID]):
    def __init__(self: Self,
                 user_id: UUID,
                 username: Username,
                 date_of_born: DateOfBorn,
                 phone: Phone,
                 email: Email,
                 password: Password) -> None:
        self.user_id = user_id
        self.username = username
        self.date_of_born = date_of_born
        self.phone_number = phone
        self.email = email
        self.password = password

    def record_event(self, event: Event) -> None:
        self._events.append(event)

    def sign_up_account(self):
        ...

    def sign_in_account(self):
        ...
    
    def change_password(self):
        ...
