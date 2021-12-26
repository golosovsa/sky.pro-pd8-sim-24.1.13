import marshmallow_dataclass
import marshmallow

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


VkDataSchema = marshmallow_dataclass.class_schema(VkData)
vk_data = {
   "response": {
       "count": 1,
       "items": [{
           "id": 100,
           "first_name": "Иван",
           "last_name": "Иванов",
           "online_info": {
               "visible": True,
               "last_seen": 1639414645
           },
           "occupation": {
               "KTS": {
                   "id": 1,
                   "type": "work"
               }
           },
           "universities": [{
               "chair_name": "Автоматизированные системы обработки информации и управления",
               "id": 250,
               "name": "МГТУ им. Н.Э. Баумана"
           }],
       }]
   }
}


def get_vk_data(data) -> VkData:
    try:
        return VkDataSchema().load(data)
    except marshmallow.exceptions.ValidationError:
        raise ValueError


if __name__ == "__main__":
    print(get_vk_data(vk_data))
