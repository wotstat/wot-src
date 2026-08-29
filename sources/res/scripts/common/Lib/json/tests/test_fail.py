from json.tests import PyTest, CTest
JSONDOCS = [
 2, 
 3, 
 4, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22, 
 23, 
 24, 
 25, 
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32, 
 33, 
 34, 
 35]
SKIPS = {1: b'why not have a string payload?', 
   18: b"spec doesn't specify any nesting limitations"}

class TestFail(object):

    def test_failures(self):
        for idx, doc in enumerate(JSONDOCS):
            idx = idx + 1
            if idx in SKIPS:
                self.loads(doc)
                continue
            try:
                self.loads(doc)
            except ValueError:
                pass
            else:
                self.fail((b'Expected failure for fail{0}.json: {1!r}').format(idx, doc))

        return

    def test_non_string_keys_dict(self):
        data = {b'a': 1, (1, 2): 2}
        self.assertRaises(TypeError, self.dumps, data)
        self.assertRaises(TypeError, self.dumps, data, indent=True)
        return


class TestPyFail(TestFail, PyTest):
    pass


class TestCFail(TestFail, CTest):
    pass
