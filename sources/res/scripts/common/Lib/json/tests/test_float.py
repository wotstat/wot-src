import math
from json.tests import PyTest, CTest

class TestFloat(object):

    def test_floats(self):
        for num in [1617161771.765, math.pi, math.pi ** 100,
         math.pi ** (-100), 3.1]:
            self.assertEqual(float(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)

        return

    def test_ints(self):
        for num in [1, 1L, 4294967296L, 18446744073709551616L]:
            self.assertEqual(self.dumps(num), str(num))
            self.assertEqual(int(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)

        return

    def test_out_of_range(self):
        self.assertEqual(self.loads(b'[23456789012E666]'), [float(b'inf')])
        self.assertEqual(self.loads(b'[-23456789012E666]'), [float(b'-inf')])
        return

    def test_allow_nan(self):
        for val in (float(b'inf'), float(b'-inf'), float(b'nan')):
            out = self.dumps([val])
            if val == val:
                self.assertEqual(self.loads(out), [val])
            else:
                res = self.loads(out)
                self.assertEqual(len(res), 1)
                self.assertNotEqual(res[0], res[0])
            self.assertRaises(ValueError, self.dumps, [val], allow_nan=False)

        return

    def test_float_subclasses_use_float_repr(self):

        class PeculiarFloat(float):

            def __repr__(self):
                return b"I'm not valid JSON"

            def __str__(self):
                return b'Neither am I'

        val = PeculiarFloat(3.2)
        self.assertEqual(self.loads(self.dumps(val)), val)
        return


class TestPyFloat(TestFloat, PyTest):
    pass


class TestCFloat(TestFloat, CTest):
    pass
