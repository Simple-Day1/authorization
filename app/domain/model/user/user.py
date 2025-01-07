from app.domain.shared.base_entity import BaseEntity
from app.domain.shared.event import DomainEvent
from app.domain.shared.unit_of_work import UnitOfWorkTracker
from app.domain.model.user.events import FullnameIsChanged, ContactsIsChanged, DateOfBornIsChanged
from app.domain.model.user.value_objects import Fullname, Contacts, DateOfBorn
from uuid import UUID
from datetime import datetime, UTC


class User[BaseEntity: UUID]:
    def __init__(
            self, 
            user_id: UUID, 
            unit_of_work: UnitOfWorkTracker, 
            fullname: Fullname,
            contacts: Contacts,
            date_of_born: DateOfBorn) -> None:
        self.user_id = user_id
        self.unit_of_work = unit_of_work
        self.fullname = fullname
        self.contacts = contacts
        self.date_of_born = date_of_born
        self._event: list[DomainEvent] = []
        super().__init__(user_id)

        def record_event(self, event: DomainEvent):
            self._event.append(event)

        def raise_event(self, event: DomainEvent):
            events = self._event.copy()
            self._event.clear()

            return events

        def change_fullname(self, firstname: str, middlename: str | None, lastname: str) -> None:
            self.fullname = Fullname(firstname=firstname, middlename=middlename, lastname=lastname)
            self.unit_of_work.register_dirty(self)
            self.record_event(FullnameIsChanged(self.user_id, firstname, middlename, lastname))

        def change_contacts(self, email: str, phone: int) -> None:
            self.contacts = Contacts(email, phone)
            self.unit_of_work.register_dirty(self)
            self.record_event(ContactsIsChanged(self.user_id, email, phone))

        def change_date_of_born(self, day: int, month: int, year: int) -> None:
            self.date_of_born = DateOfBorn(day, month, year)
            self.unit_of_work.register_dirty(self)
            self.record_event(DateOfBornIsChanged(self.user_id, day, month, year))
        
