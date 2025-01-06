from domain.shared.event import DomainEvent
from uuid import UUID


class UserCreated(DomainEvent):
    def __init__(self,
                  user_id: UUID,
                  username: str,
                  password: str,
                  phone: int,
                  email: str,
                  date_of_born: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.date_of_born = date_of_born


class UserIsSignedIn(DomainEvent):
    def __init__(self,
                  user_id: UUID,
                  username: str,
                  password: str,
                  phone: int,
                  email: str,
                  date_of_born: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.date_of_born = date_of_born


class PasswordIsChanged(DomainEvent):
    def __init__(self,
                 user_id: UUID,
                 password: str):
        self.user_id = user_id
        self.password = password
