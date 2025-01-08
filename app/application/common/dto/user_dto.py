from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class UserDTO:
    user_id: UUID
    firstname: str 
    middlename: str | None
    lastname: str
    phone: int | None 
    email: str| None 
    day: str
    month: str
    year: str
