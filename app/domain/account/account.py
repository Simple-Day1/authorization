from typing import Self


class User:
    def __init__(self: Self,
                 user_id: int,
                 username: str,
                 date_of_born: int,
                 phone_number: int,
                 email: str,
                 password: str) -> None:
        self.user_id = user_id
        self.username = username
        self.date_of_born = date_of_born
        self.phone_number = phone_number
        self.email = email
        self.password = password

    @classmethod
    def create_user(cls):
        ...
