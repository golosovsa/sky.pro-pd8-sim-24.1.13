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
        func_name = "clock_checker"
        func = getattr(main, func_name)

        self.assertTrue(
            func,
            f"%@Проверьте, что функция {func_name} определена в модуле."
        )

        result = func("2021-10-15 18:24:30")
        self.assertIsInstance(
            result, bool,
            "%@Проверьте, что функция возвращает результат типа boolean."
        )

        self.assertTrue(
            result,
            "%@Проверьте, что если на вход ваша функция получает строку, "
            "которая содержит информацию в искомом виде, то она возвращает True."
        )
        for value in ["2021-10-15 18:24:3",
                      "2021-10-15 18:2:31",
                      "2021-10-15 1:24:31",
                      "2021-10-1 18:24:31",
                      "2021-1-15 18:24:31",
                      "202110-15 18:24:31",
                      "2021-1015 18:24:31",
                      "2021-10-15 1824:31",
                      "2021-10-15 18:2431",
                      "2021-10-1518:24:31",
                      ]:
            result = func(value)
            self.assertFalse(
                result,
                "%@Проверьте, что если на вход ваша функция получает строку, не содержащую "
                f"дату в требуемом формате то она возвращает False. (проверочное значение {value})"
            )


if __name__ == "__main__":
    unittest.main()