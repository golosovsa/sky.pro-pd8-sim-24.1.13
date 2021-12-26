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
        self.author_point = solution.Point

    def test_dataclass_is_correct(self):
        self.assertTrue(
            hasattr(main, "Point"),
            "%@Проверьте, что класс Point существует в модуле"
        )

        student_point = getattr(main, "Point")
        student_point_code = inspect.getsource(student_point)

        self.assertNotIn(
            "@dataclass", student_point_code,
            "%@Проверьте, что Ваш класс больше не является датаклассом"
        )
        try:
            point = student_point(x="test1", y="test2")
        except:
            self.fail(msg="%@Проверьте, что правильно указали аттрибуты класса ")

        expected_annotations = self.author_point.__annotations__
        student_annotations = student_point.__annotations__

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


if __name__ == "__main__":
    unittest.main()
