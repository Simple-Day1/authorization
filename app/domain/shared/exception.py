from dataclasses import dataclass, field


@dataclass(eq=True)
class DomainError(Exception):
    massage: str = field(default='Dommain error occured')
