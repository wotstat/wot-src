from json.tests import PyTest, CTest
JSON = b'\n[[[[[[[[[[[[[[[[[[["Not too deep"]]]]]]]]]]]]]]]]]]]\n'

class TestPass2(object):

    def test_parse(self):
        res = self.loads(JSON)
        out = self.dumps(res)
        self.assertEqual(res, self.loads(out))
        return


class TestPyPass2(TestPass2, PyTest):
    pass


class TestCPass2(TestPass2, CTest):
    pass
