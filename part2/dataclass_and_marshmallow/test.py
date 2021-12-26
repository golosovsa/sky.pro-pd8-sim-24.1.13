import sys
import unittest
from pathlib import Path
import os
import solution
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import AnnotationsCheckMixin  # noqa: E402


class DataClassesTestCase(SkyproTestCase, AnnotationsCheckMixin):

    def test_function_vk_data_works_correct(self):
        function_name = "get_vk_data"
        valid_json = solution.vk_data
        invalid_json = {}
        vkdata_class = main.VkData
        self.assertTrue(
            hasattr(main, function_name),
            "%@Проверьте что в модуле есть функция get_vk_data"
        )
        try:
            result = main.get_vk_data(valid_json)
        except:
            self.fail(f"%@Проверьте, что при вызове функции {function_name} с корректными данными не происходит ошибки")

        self.assertIsInstance(
            result, vkdata_class,
            f"%@Проверьте, что функция {function_name} возвращает экземпляр класса {vkdata_class.__name__}"
        )

        with self.assertRaises(
                ValueError,
                msg=f"%@Проверьте, что при вызове функции {function_name} с некорректными данными выбрасывается исключение ValueError"
        ):
            main.get_vk_data(invalid_json)


if __name__ == "__main__":
    unittest.main()
