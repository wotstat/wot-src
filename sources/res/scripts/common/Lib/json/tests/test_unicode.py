from collections import OrderedDict
from json.tests import PyTest, CTest

class TestUnicode(object):

    def test_encoding1(self):
        encoder = self.json.JSONEncoder(encoding=b'utf-8')
        u = u'\u03b1\u03a9'
        s = u.encode(b'utf-8')
        ju = encoder.encode(u)
        js = encoder.encode(s)
        self.assertEqual(ju, js)
        return

    def test_encoding2(self):
        u = u'\u03b1\u03a9'
        s = u.encode(b'utf-8')
        ju = self.dumps(u, encoding=b'utf-8')
        js = self.dumps(s, encoding=b'utf-8')
        self.assertEqual(ju, js)
        return

    def test_encoding3(self):
        u = u'\u03b1\u03a9'
        j = self.dumps(u)
        self.assertEqual(j, b'"\\u03b1\\u03a9"')
        return

    def test_encoding4(self):
        u = u'\u03b1\u03a9'
        j = self.dumps([u])
        self.assertEqual(j, b'["\\u03b1\\u03a9"]')
        return

    def test_encoding5(self):
        u = u'\u03b1\u03a9'
        j = self.dumps(u, ensure_ascii=False)
        self.assertEqual(j, (u'"{0}"').format(u))
        return

    def test_encoding6(self):
        u = u'\u03b1\u03a9'
        j = self.dumps([u], ensure_ascii=False)
        self.assertEqual(j, (u'["{0}"]').format(u))
        return

    def test_big_unicode_encode(self):
        u = u'\U0001d120'
        self.assertEqual(self.dumps(u), b'"\\ud834\\udd20"')
        self.assertEqual(self.dumps(u, ensure_ascii=False), u'"\U0001d120"')
        return

    def test_big_unicode_decode(self):
        u = u'z\U0001d120x'
        self.assertEqual(self.loads(b'"' + u + b'"'), u)
        self.assertEqual(self.loads(b'"z\\ud834\\udd20x"'), u)
        return

    def test_unicode_decode(self):
        for i in range(0, 55295):
            u = unichr(i)
            s = (b'"\\u{0:04x}"').format(i)
            self.assertEqual(self.loads(s), u)

        return

    def test_object_pairs_hook_with_unicode(self):
        s = u'{"xkd":1, "kcw":2, "art":3, "hxm":4, "qrt":5, "pad":6, "hoy":7}'
        p = [20, 21, 22, 23, 
         24, 25, 26]
        self.assertEqual(self.loads(s), eval(s))
        self.assertEqual(self.loads(s, object_pairs_hook=(lambda x: x)), p)
        od = self.loads(s, object_pairs_hook=OrderedDict)
        self.assertEqual(od, OrderedDict(p))
        self.assertEqual(type(od), OrderedDict)
        self.assertEqual(self.loads(s, object_pairs_hook=OrderedDict, object_hook=(lambda x: None)), OrderedDict(p))
        return

    def test_default_encoding(self):
        self.assertEqual(self.loads((u'{"a": "\xe9"}').encode(b'utf-8')), {b'a': u'\xe9'})
        return

    def test_unicode_preservation(self):
        self.assertEqual(type(self.loads(u'""')), unicode)
        self.assertEqual(type(self.loads(u'"a"')), unicode)
        self.assertEqual(type(self.loads(u'["a"]')[0]), unicode)
        self.assertEqual(type(self.loads(b'"foo"')), unicode)
        return

    def test_bad_encoding(self):
        self.assertRaises(UnicodeEncodeError, self.loads, b'"a"', u'rat\xe9')
        self.assertRaises(TypeError, self.loads, b'"a"', 1)
        return


class TestPyUnicode(TestUnicode, PyTest):
    pass


class TestCUnicode(TestUnicode, CTest):
    pass
