from uuid import UUID, uuid4
from datetime import datetime, UTC


class Event:
    def __init__(self,
                  event_uuid: UUID = uuid4,
                  event_time: datetime = datetime.now(UTC)):
        self.event_uuid = event_uuid
        self.event_time = event_time