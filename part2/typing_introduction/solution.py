from dataclasses import dataclass
from typing import Dict, List, Tuple, Set

import marshmallow_dataclass
import marshmallow
from vk_data import vk_data


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


VkDataSchema = marshmallow_dataclass.class_schema(VkData)


def get_vk_data(data) -> VkData:
    try:
        return VkDataSchema().load(data)
    except marshmallow.exceptions.ValidationError:
        raise ValueError


@dataclass
class UniversityInfo:
    name: str
    count: int = 0


def get_university_pairs(data: dict) -> List[Tuple[str, int]]:
    data_obj: VkData = get_vk_data(data)
    universities: Dict[int, UniversityInfo] = {}
    for user in data_obj.response.items:
        university_set: Set[int] = set()
        for university in user.universities:
            if university.id not in universities:
                universities[university.id] = UniversityInfo(university.name)
            if university.id not in university_set:
                # условие нужно для того, чтобы в результате не учитывать 2 раза один и тот же университет,
                # если человек учился, например, в бакалавриате и магистратуре
                universities[university.id].count += 1
                university_set.add(university.id)
    res = sorted(
        map(lambda u: (u.name, u.count), universities.values()),
        reverse=False
    )
    return res[:3]


if __name__ == "__main__":
    print(get_university_pairs(vk_data))
