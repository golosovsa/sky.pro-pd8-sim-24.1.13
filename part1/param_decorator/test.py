import sys
import unittest
from pathlib import Path
from collections import Counter
import os
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase   # noqa: E402
from ttools.skyprotests.tests import StdoutCapturing  # noqa: E402


class DecoratorTestCase(SkyproTestCase):

    def setUp(self):
        self.count = 0

        def counter_works_on_3():
            self.count += 1
            if self.count < 3:
                raise ValueError
            print("test_func has finished")

        def counter_works_on_10():
            self.count += 1
            if self.count < 10:
                raise ValueError
            print("test_func has finished")

        self.counter_works_3 = counter_works_on_3
        self.counter_works_10 = counter_works_on_10
        self.decorator = main.retry

    def test_retry_decorator_works_correct(self):
        with StdoutCapturing() as output:
            self.decorator(3)(self.counter_works_3)()
        counter = Counter(output)
        self.assertTrue(
            counter.get('exc_has_appeared'),
            "%@Проверьте, что если в декорируемой функции срабатывает исключение, а лимит повторов не превышен "
            "то в терминал выводится фраза 'exc_has_appeared'"
        )

        with self.assertRaises(
                Exception,
                msg=("%@Проверьте, что выбрасывается исключение если лимит повторов превышен, "
                     "а функция так и не сработала")):
            with StdoutCapturing() as output:
                self.decorator(5)(self.counter_works_10)()


if __name__ == "__main__":
    unittest.main()
