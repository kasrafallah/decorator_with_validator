import unittest, types
from decorator import decorator

class ScoreListTest(unittest.TestCase):

    def _divs(self, a):
        for it in range(1, a+10):
            if a%it == 0:
                yield it

    def _test(self):
        if isinstance(divs(a), types.GeneratorType) == False:
            self.assertEqual(0, 1)

        it = iter(divs(a))

        for it2 in self._divs(a):
            val = next(it)
            self.assertEqual(val, it2)

    def test_1(self):
        def validator(x):
            return x>0

        @decorator(validator)
        def f(x):
            return x

        self.assertEqual(f(10), 10)
        self.assertEqual(f(-1), 'error')

    def test_2(self):
        def validator(x, y):
            return x>y

        @decorator(validator)
        def f(x, y):
            return x + y

        self.assertEqual(f(20, 10), 30)
        self.assertEqual(f(10, 20), 'error')

    def test_3(self):
        def validator(x):
            return type(x) == list

        @decorator(validator)
        def f(x):
            return x

        self.assertEqual(f([1]), [1])
        self.assertEqual(f(1), 'error')

unittest.main()
