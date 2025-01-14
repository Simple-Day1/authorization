from app.domain.shared.base_entity import BaseEntity
from app.domain.shared.event import DomainEvent
from app.domain.shared.unit_of_work import UnitOfWorkTracker
from app.domain.model.user.events import FullnameIsChanged, ContactsIsChanged, DateOfBornIsChanged
from app.domain.model.user.value_objects import Fullname, Contacts, Date
from uuid import UUID


class User[BaseEntity: UUID]:
    def __init__(
        self, 
        user_id: UUID, 
        unit_of_work: UnitOfWorkTracker, 
        fullname: Fullname,
        contacts: Contacts,
        date: Date) -> None:
        super().__init__(user_id)
        self.user_id = user_id
        self.unit_of_work = unit_of_work
        self.fullname = fullname
        self.contacts = contacts
        self.date = date
        self._events: list[DomainEvent] = []

    def record_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def raise_event(self) -> list[DomainEvent]:
        events = self._events.copy()
        self._events.clear()

        return events

    def change_fullname(self, firstname: str, middlename: str | None, lastname: str) -> None:
        self.fullname = Fullname(firstname=firstname, middlename=middlename, lastname=lastname)
        self.unit_of_work.register_dirty(self)
        self.record_event(FullnameIsChanged(self.user_id, firstname, middlename, lastname))

    def change_contacts(self, email: str, phone: int) -> None:
        self.contacts = Contacts(email, phone)
        self.unit_of_work.register_dirty(self)
        self.record_event(ContactsIsChanged(self.user_id, email, phone))

    def change_date(self, day: int, month: int, year: int) -> None:
        self.date = Date(day, month, year)
        self.unit_of_work.register_dirty(self)
        self.record_event(DateOfBornIsChanged(self.user_id, day, month, year))
        
