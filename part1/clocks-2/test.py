import sys
import unittest
from pathlib import Path
import os
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402


class ExceptionTestCase(SkyproTestCase):
    def test_init_returns_class_instances(self):
        func_name = "find_date"
        input_text = """
        63.140.98.80 - - [20/May/2015:21:05:28 +0000]
        63.140.98.80 - - [20/May/2015:21:05:50 +0000]
        66.249.73.135 - - [20/May/2015:21:05:00 +0000]
        180.76.6.56 - - [20May2015:21:05:56 +0000] 
        180.76.6.56 - - [20/May2015:21:05:56 +0000]
        180.76.6.56 - - [20/May/201521:05:56 +0000]
        180.76.6.56 - - [20/May/2015:210556 +0000]       
        """
        func = getattr(main, func_name)

        self.assertTrue(
            func,
            f"%@Проверьте, что функция {func_name} определена в модуле."
        )

        result = func(input_text)
        self.assertIsInstance(
            result, list,
            "%@Проверьте, что функция возвращает результат типа list."
        )
        self.assertTrue(
            len(result) != 0,
            "%@Проверьте, что список возвращаемый функцией не пустой."
        )

        self.assertTrue(
            len(result) == 3,
            "%@Проверьте, что Ваша функция выбирает даты только правильного формата."
            "Возможно Вы не указали какой-нибудь разделительный знак"
        )


if __name__ == "__main__":
    unittest.main()
