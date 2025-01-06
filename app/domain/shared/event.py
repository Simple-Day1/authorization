from uuid import UUID, uuid4
from datetime import datetime, UTC


class DomainEvent:
    def __init__(self,
                  event_uuid: UUID = uuid4,
                  event_timestamp: datetime = datetime.now(UTC)):
        self.event_uuid = event_uuid
        self.event_timestamp = event_timestamp