from dataclasses import dataclass
from typing import Dict, List


@dataclass
class University:
    chair_name: str
    id: int
    name: str


@dataclass
class Occupation:
    id: int
    type: str


@dataclass
class OnlineInfo:
    visible: bool
    last_seen: int


@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    online_info: OnlineInfo
    occupation: Dict[str, Occupation]
    universities: List[University]


@dataclass
class VkResponse:
    count: int
    items: List[User]


@dataclass
class VkData:
    response: VkResponse
