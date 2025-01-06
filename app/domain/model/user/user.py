from app.domain.shared.base_entity import BaseEntity
from app.domain.shared.event import DomainEvent
from app.domain.shared.unit_of_work import UnitOfWorkTracker
from app.domain.model.user.value_objects import Username, Password, Phone, Email, DateOfBorn
from app.domain.model.user.events import UserCreated, UserIsSignedIn, PasswordIsChanged
from uuid import UUID


class User[BaseEntity: UUID]:
    def __init__(self,
                  user_id: UUID,
                  unit_of_work: UnitOfWorkTracker,
                  username: Username,
                  password: Password,
                  phone: Phone,
                  email: Email,
                  date_of_born: DateOfBorn) -> None:
        self.user_id = user_id
        self.unit_of_work = unit_of_work
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.date_of_born = date_of_born
        self._event: list[DomainEvent] = []
        super().__init__(user_id)

        def record_event(self, event: DomainEvent):
            self._event.append(event)

        def register_event(self, event: DomainEvent):
            events = self._event.copy()
            self._event.clear()

            return events

        def sign_in(self) -> None:
            ...

        def change_password(self, password: str) -> None:
            self.unit_of_work.register_dirty(self)
            self.record_event(PasswordIsChanged(user_id=self.user_id, password=password))
        
