# Представьте, что ваш руководитель поручил
# вам внедрить датаклассы в проект. Перепишите
# класс Person на использование датаклассов.
# Обратите внимание на переменную skills,
# после создания объекта Person значение skills будет []

# Подсказка: для решения задачи нужно использовать:
# from dataclasses import field


import datetime
from typing import Optional, List
from dataclasses import dataclass, field


@dataclass
class Person:
    first_name: str
    last_name: str
    birthday: datetime.date
    middle_name: Optional[str] = ""
    skills: List[str] = field(default_factory=list)
