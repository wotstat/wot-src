from json.tests import PyTest, CTest

class TestDefault(object):

    def test_default(self):
        self.assertEqual(self.dumps(type, default=repr), self.dumps(repr(type)))
        return


class TestPyDefault(TestDefault, PyTest):
    pass


class TestCDefault(TestDefault, CTest):
    pass
