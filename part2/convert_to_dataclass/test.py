import sys
import unittest
from pathlib import Path
import os
import main
import solution
import inspect
import datetime

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class DataClassTestCase(SkyproTestCase):
    def setUp(self):
        self.author_person = solution.Person

    def test_dataclass_is_correct(self):
        self.assertTrue(
            hasattr(main, "Person"),
            "%@Проверьте, что класс Person существует в модуле"
        )

        student_person = getattr(main, "Person")
        student_person_code = inspect.getsource(student_person)

        self.assertIn(
            "@dataclass", student_person_code,
            "%@Проверьте, что применили декоратор @dataclass к классу Person"
        )

        expected_fields = [x for x in self.author_person.__dataclass_fields__]
        student_fields = [x for x in student_person.__dataclass_fields__]
        for field in expected_fields:
            self.assertIn(
                field, student_fields,
                f"%@Проверьте, что Ваш новый класс содержит поле {field}"
            )

        expected_annotations = self.author_person.__annotations__
        student_annotations = student_person.__annotations__

        for annotation in expected_annotations:
            self.assertIn(
                annotation, student_annotations,
                f"%@Проверьте что написали аннотацию для аргумента {annotation}"
            )

        for annotation in expected_annotations:
            self.assertEqual(
                student_annotations.get(annotation), expected_annotations.get(annotation),
                f"%@Проверьте что правильно указали аннотацию для аргумента {annotation}"
            )

        test_person = student_person(
            first_name="test",
            last_name="test",
            birthday=datetime.date(year=1988, month=11, day=15),
        )
        self.assertTrue(
            test_person.skills == [],
            "%@Проверьте, что если не указано свойство skills при создании экземпляра класса, "
            "то после его инициализации данному свойству присваивается значение пустого списка"
        )


if __name__ == "__main__":
    unittest.main()
