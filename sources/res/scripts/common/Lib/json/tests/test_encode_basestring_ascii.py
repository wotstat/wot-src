from collections import OrderedDict
from json.tests import PyTest, CTest
CASES = [
 29, 
 30, 
 31, 
 32, 
 33, 
 34, 
 35, 
 36, 
 37, 
 38, 
 39, 
 40, 
 41, 
 42, 
 43, 
 44]

class TestEncodeBasestringAscii(object):

    def test_encode_basestring_ascii(self):
        fname = self.json.encoder.encode_basestring_ascii.__name__
        for input_string, expect in CASES:
            result = self.json.encoder.encode_basestring_ascii(input_string)
            self.assertEqual(result, expect, (b'{0!r} != {1!r} for {2}({3!r})').format(result, expect, fname, input_string))

        return

    def test_ordered_dict(self):
        items = [12, 13, 14, 15, 16]
        s = self.dumps(OrderedDict(items))
        self.assertEqual(s, b'{"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}')
        return


class TestPyEncodeBasestringAscii(TestEncodeBasestringAscii, PyTest):
    pass


class TestCEncodeBasestringAscii(TestEncodeBasestringAscii, CTest):
    pass
