from domain.shared.event import Event
from uuid import UUID


class AccountIsSignedUp(Event):
    def __init__(self,
                user_id: UUID,
                username: str):
        self.user_id = user_id
        self.username = username


class PasswordIsChanged(Event):
    def __init__(self,
                password: str):
        self.password = password
