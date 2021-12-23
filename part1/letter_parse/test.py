import sys
import unittest
from pathlib import Path
import os
import main
import inspect

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class ExceptionTestCase(SkyproTestCase):
    def test_init_returns_class_instances(self):
        func_name = "get_plates"
        func = getattr(main, func_name)
        first_type = [
            "заявка от ав333_78",
            "заявка на продажу от вн836_51",
            "заявка на продажу от 'вк817_98'",
        ]
        second_type = [
            "заявка от у444хн58",
            "заявка на продажу от г836св51",
            "заявка на продажу от в544кт51"
        ]

        both_types = first_type + second_type
        both_types.append("заявка от ав333_78 и г855мт61")

        self.assertTrue(
            func,
            f"%@Проверьте, что функция {func_name} определена в модуле."
        )

        self.assertTrue(
            inspect.isgeneratorfunction(func),
            f"%@Проверьте, что функция {func_name} является функцией-генератором",
        )

        result = [x for x in func(first_type)]
        first_answer = ['ав333_78', 'вн836_51', 'вк817_98']

        for value in first_answer:
            self.assertIn(
                value, result,
                "%@Проверьте, что Ваша функция возвращает номера вида аа111_11"
            )

        result = [x for x in func(second_type)]
        second_answer = ['у444хн58', 'г836св51', 'в544кт51']
        for value in second_answer:
            self.assertIn(
                value, result,
                "%@Проверьте, что Ваша функция возвращает номера вида а111аа11"
            )

        result = [x for x in func(both_types)]
        third_answer = first_answer + second_answer + ['ав333_78', 'г855мт61']
        for value in third_answer:
            self.assertIn(
                value, result,
                "%@Проверьте, что Ваша функция возвращает номера как первого (аа111_11) так и второго вида (а111аа11)"
            )


if __name__ == "__main__":
    unittest.main()
