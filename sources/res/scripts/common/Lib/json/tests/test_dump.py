from cStringIO import StringIO
from json.tests import PyTest, CTest

class TestDump(object):

    def test_dump(self):
        sio = StringIO()
        self.json.dump({}, sio)
        self.assertEqual(sio.getvalue(), b'{}')
        return

    def test_dumps(self):
        self.assertEqual(self.dumps({}), b'{}')
        return

    def test_encode_truefalse(self):
        self.assertEqual(self.dumps({True: False, False: True}, sort_keys=True), b'{"false": true, "true": false}')
        self.assertEqual(self.dumps({2: 3.0, 4.0: 5L, False: 1, 6L: True}, sort_keys=True), b'{"false": 1, "2": 3.0, "4.0": 5, "6": true}')
        return

    def test_encode_mutated(self):
        a = [
         object()] * 10

        def crasher(obj):
            del a[-1]
            return

        self.assertEqual(self.dumps(a, default=crasher), b'[null, null, null, null, null]')
        return


class TestPyDump(TestDump, PyTest):
    pass


class TestCDump(TestDump, CTest):
    pass
