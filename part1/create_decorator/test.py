import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock
import os
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests import StdoutCapturing


class DecoratorTestCase(SkyproTestCase):

    def setUp(self):
        self.mock = MagicMock()
        self.decorated = main.logger(self.mock)

    def test_logger_works_correct_without_exceptions(self):
        self.mock.return_value = 1
        with StdoutCapturing() as output:
            self.mock.return_value = 10
            self.mock.__name__ = 'expected_name'
            self.decorated()
        self.assertIn(
            "expected_name", output,
            "%@Проверьте, если функция отработала штатно, то в терминале выводится только её название."
            "Для этого попробуйте использовать магический метод __name__"
        )

    def test_logger_works_correct_without_exceptions(self):
        self.mock.side_effect = Exception('test_exception')
        with StdoutCapturing() as output:
            self.mock.__name__ = 'expected_name'
            self.decorated()
        self.assertIn(
            "exc_has_appeared", output,
            "%@Проверьте, если функция отработала c ошибкой, "
            "то в терминале выводится фраза "
            "'exc_has_appeared'"
        )
        self.assertIn(
            "exc_has_appeared", output,
            "%@Проверьте, если функция отработала c ошибкой, "
            "то в терминале выводится её название "
            "Для этого попробуйте использовать магический метод __name__"
        )


if __name__ == "__main__":
    unittest.main()
