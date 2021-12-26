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


class PointFactoryTestCase(SkyproTestCase):
    def setUp(self):
        self.author_point = solution.Point

    def test_dataclass_is_correct(self):
        function_name = "point_factory"
        self.assertTrue(
            hasattr(main, "Point"),
            "%@Проверьте, что Вы не удалили класс Point из модуля"
        )

        student_point_factory = getattr(main, function_name)
        self.assertTrue(
            student_point_factory, f"%@Проверьте, что функция {function_name} существует в модуле"
        )

        try:
            student_point_factory(4)
        except:
            self.fail(msg=f"%@Проверьте что при вызове функции {function_name} нет ошибок")

        point = student_point_factory(4)

        self.assertIsInstance(
            point, list,
            f"%@Проверьте, что функция {function_name} возвращает список"
        )

        student_point_class = main.Point

        for index in range(4):
            self.assertIsInstance(
                point[index], student_point_class,
                "%@Проверьте, что элементы списка, возвращаемого функцией являются экземплярами класса point"
            )
            self.assertTrue(
                point[index].x == index + 1,
                "%@Проверьте, экземпляры класса Point в ответе, который возвращает функция содержат верные значения свойств"
            )

            self.assertTrue(
                point[index].y == index + 1,
                "%@Проверьте, экземпляры класса Point в ответе, который возвращает функция содержат верные значения свойств"
            )

if __name__ == "__main__":
    unittest.main()
