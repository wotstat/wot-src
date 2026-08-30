from json.tests import PyTest, CTest

def default_iterable(obj):
    return list(obj)


class TestCheckCircular(object):

    def test_circular_dict(self):
        dct = {}
        dct[b'a'] = dct
        self.assertRaises(ValueError, self.dumps, dct)
        return

    def test_circular_list(self):
        lst = []
        lst.append(lst)
        self.assertRaises(ValueError, self.dumps, lst)
        return

    def test_circular_composite(self):
        dct2 = {}
        dct2[b'a'] = []
        dct2[b'a'].append(dct2)
        self.assertRaises(ValueError, self.dumps, dct2)
        return

    def test_circular_default(self):
        self.dumps([set()], default=default_iterable)
        self.assertRaises(TypeError, self.dumps, [set()])
        return

    def test_circular_off_default(self):
        self.dumps([set()], default=default_iterable, check_circular=False)
        self.assertRaises(TypeError, self.dumps, [set()], check_circular=False)
        return


class TestPyCheckCircular(TestCheckCircular, PyTest):
    pass


class TestCCheckCircular(TestCheckCircular, CTest):
    pass
