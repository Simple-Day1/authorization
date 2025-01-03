from typing import Self


class Account:
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

    def sign_up_account(self):
        ...

    def sign_in_account(self):
        ...
    
    def change_password(self):
        ...
