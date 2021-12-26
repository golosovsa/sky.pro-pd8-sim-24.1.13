import sys
import unittest
from pathlib import Path
import os
import main
import solution
from typing import Dict, List, Union

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.utils.annotations import get_union_annotations  # noqa: E402


class ExceptionTestCase(SkyproTestCase):

    def setUp(self):
        expected_any = solution.get_postcode_with_any.__annotations__
        expected_union = solution.get_postcode_with_union.__annotations__
        self.expected = get_union_annotations(expected_any, expected_union)

    def test_func_has_annotations(self):
        self.assertTrue(
            hasattr(main, "get_postcode"),
            "%@Проверьте, что не изменяли название функции get_postcode"
        )

        annotations = main.get_postcode.__annotations__

        for annotation in self.expected:
            if annotation != "return":
                self.assertIn(
                    annotation, annotations,
                    f"%@Проверьте что написали аннотацию для аргумента {annotation}"
                )
            else:
                self.assertIn(
                    annotation, annotations,
                    f"%@Проверьте что Вы написали аннотацию на значение, которое возвращается функцией"
                )

        for annotation in self.expected:
            if annotation != "return":
                self.assertIn(
                    annotations.get(annotation), self.expected.get(annotation),
                    f"%@Проверьте правильно ли Ва написали аннотацию для аргумента {annotation}"
                )
            else:
                self.assertIn(
                    annotations.get(annotation), self.expected.get(annotation),
                    f"%@ПроПроверьте правильно ли Ва написали аннотацию для данных, которые возвращаются функцией"
                )


if __name__ == "__main__":
    unittest.main()
