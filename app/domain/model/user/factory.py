from app.domain.model.user import User
from app.domain.model.user.events import UserCreated
from app.domain.model.user.repository import UserRepository
from app.domain.shared.unit_of_work import UnitOfWorkTracker
from app.domain.model.user.exceptions import UserAlreadyExistsError
from datetime import datetime
from uuid import UUID


class UserFactory:
    def __init__(self, repository: UserRepository, unit_of_work: UnitOfWorkTracker) -> None:
        self.repository = repository
        self.unit_of_work = unit_of_work
    
    async def create_user(self, user_id: UUID, username: str, password: str, phone: int | None, email: str| None, date_of_born: str | None):
        if email and await self.repository.with_email(email):
            raise UserAlreadyExistsError(message="User already exists")

        if phone and await self.repository.with_phone(phone):
            raise UserAlreadyExistsError(message="User already exists")
        
        user = User(user_id, self.unit_of_work, username, password, phone, email, date_of_born)
        user.record_event(UserCreated(user.user_id, username, password, phone, email, date_of_born))

        return user