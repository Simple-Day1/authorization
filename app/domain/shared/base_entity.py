from uuid import UUID


class BaseEntity[TEntityId: UUID]:
    def __init__(self, entity_id: TEntityId) -> None:
        self.entity_id = entity_id