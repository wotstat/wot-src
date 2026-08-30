from json.tests import PyTest, CTest

class JSONTestObject:
    pass


class TestRecursion(object):

    def test_listrecursion(self):
        x = []
        x.append(x)
        try:
            self.dumps(x)
        except ValueError:
            pass
        else:
            self.fail(b"didn't raise ValueError on list recursion")

        x = []
        y = [
         x]
        x.append(y)
        try:
            self.dumps(x)
        except ValueError:
            pass
        else:
            self.fail(b"didn't raise ValueError on alternating list recursion")

        y = []
        x = [
         y, y]
        self.dumps(x)
        return

    def test_dictrecursion(self):
        x = {}
        x[b'test'] = x
        try:
            self.dumps(x)
        except ValueError:
            pass
        else:
            self.fail(b"didn't raise ValueError on dict recursion")

        x = {}
        y = {b'a': x, b'b': x}
        self.dumps(x)
        return

    def test_defaultrecursion(self):

        class RecursiveJSONEncoder(self.json.JSONEncoder):
            recurse = False

            def default(self, o):
                if o is JSONTestObject:
                    if self.recurse:
                        return [JSONTestObject]
                    else:
                        return b'JSONTestObject'

                return pyjson.JSONEncoder.default(o)

        enc = RecursiveJSONEncoder()
        self.assertEqual(enc.encode(JSONTestObject), b'"JSONTestObject"')
        enc.recurse = True
        try:
            enc.encode(JSONTestObject)
        except ValueError:
            pass
        else:
            self.fail(b"didn't raise ValueError on default recursion")

        return

    def test_highly_nested_objects_decoding(self):
        with self.assertRaises(RuntimeError):
            self.loads(b'{"a":' * 100000 + b'1' + b'}' * 100000)
        with self.assertRaises(RuntimeError):
            self.loads(b'{"a":' * 100000 + b'[1]' + b'}' * 100000)
        with self.assertRaises(RuntimeError):
            self.loads(b'[' * 100000 + b'1' + b']' * 100000)
        with self.assertRaises(RuntimeError):
            self.loads(u'{"a":' * 100000 + u'1' + u'}' * 100000)
        with self.assertRaises(RuntimeError):
            self.loads(u'{"a":' * 100000 + u'[1]' + u'}' * 100000)
        with self.assertRaises(RuntimeError):
            self.loads(u'[' * 100000 + u'1' + u']' * 100000)
        return

    def test_highly_nested_objects_encoding(self):
        l, d = [], {}
        for x in xrange(100000):
            l, d = [
             l], {b'k': d}

        with self.assertRaises(RuntimeError):
            self.dumps(l)
        with self.assertRaises(RuntimeError):
            self.dumps(d)
        return

    def test_endless_recursion(self):

        class EndlessJSONEncoder(self.json.JSONEncoder):

            def default(self, o):
                return [
                 o]

        with self.assertRaises(RuntimeError):
            EndlessJSONEncoder(check_circular=False).encode(complex(0.0, 5.0))
        return


class TestPyRecursion(TestRecursion, PyTest):
    pass


class TestCRecursion(TestRecursion, CTest):
    pass
