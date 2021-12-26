import datetime
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class Person:
    first_name: str
    last_name: str
    birthday: datetime.date
    middle_name: Optional[str] = None
    skills: List[str] = field(default_factory=list)
