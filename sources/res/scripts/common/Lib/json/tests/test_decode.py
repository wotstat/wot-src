import decimal
from StringIO import StringIO
from collections import OrderedDict
from json.tests import PyTest, CTest

class TestDecode(object):

    def test_decimal(self):
        rval = self.loads(b'1.1', parse_float=decimal.Decimal)
        self.assertTrue(isinstance(rval, decimal.Decimal))
        self.assertEqual(rval, decimal.Decimal(b'1.1'))
        return

    def test_float(self):
        rval = self.loads(b'1', parse_int=float)
        self.assertTrue(isinstance(rval, float))
        self.assertEqual(rval, 1.0)
        return

    def test_decoder_optimizations(self):
        rval = self.loads(b'{   "key"    :    "value"    ,  "k":"v"    }')
        self.assertEqual(rval, {b'key': b'value', b'k': b'v'})
        return

    def test_empty_objects(self):
        self.assertEqual(self.loads(b'{}'), {})
        self.assertEqual(self.loads(b'[]'), [])
        self.assertEqual(self.loads(b'""'), u'')
        self.assertIsInstance(self.loads(b'""'), unicode)
        return

    def test_object_pairs_hook(self):
        s = b'{"xkd":1, "kcw":2, "art":3, "hxm":4, "qrt":5, "pad":6, "hoy":7}'
        p = [24, 25, 26, 27, 
         28, 29, 30]
        self.assertEqual(self.loads(s), eval(s))
        self.assertEqual(self.loads(s, object_pairs_hook=(lambda x: x)), p)
        self.assertEqual(self.json.load(StringIO(s), object_pairs_hook=(lambda x: x)), p)
        od = self.loads(s, object_pairs_hook=OrderedDict)
        self.assertEqual(od, OrderedDict(p))
        self.assertEqual(type(od), OrderedDict)
        self.assertEqual(self.loads(s, object_pairs_hook=OrderedDict, object_hook=(lambda x: None)), OrderedDict(p))
        self.assertEqual(self.loads(b'{}', object_pairs_hook=OrderedDict), OrderedDict())
        self.assertEqual(self.loads(b'{"empty": {}}', object_pairs_hook=OrderedDict), OrderedDict([(b'empty', OrderedDict())]))
        return

    def test_extra_data(self):
        s = b'[1, 2, 3]5'
        msg = b'Extra data'
        self.assertRaisesRegexp(ValueError, msg, self.loads, s)
        return

    def test_invalid_escape(self):
        s = b'["abc\\y"]'
        msg = b'escape'
        self.assertRaisesRegexp(ValueError, msg, self.loads, s)
        return

    def test_negative_index(self):
        d = self.json.JSONDecoder()
        self.assertRaises(ValueError, d.raw_decode, b'a' * 42, -50000)
        self.assertRaises(ValueError, d.raw_decode, u'a' * 42, -50000)
        return


class TestPyDecode(TestDecode, PyTest):
    pass


class TestCDecode(TestDecode, CTest):
    pass
