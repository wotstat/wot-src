import os, sys, json, doctest, unittest
from test import test_support
cjson = test_support.import_fresh_module(b'json', fresh=[b'_json'])
pyjson = test_support.import_fresh_module(b'json', blocked=[b'_json'])

class PyTest(unittest.TestCase):
    json = pyjson
    loads = staticmethod(pyjson.loads)
    dumps = staticmethod(pyjson.dumps)


@unittest.skipUnless(cjson, b'requires _json')
class CTest(unittest.TestCase):
    if cjson is not None:
        json = cjson
        loads = staticmethod(cjson.loads)
        dumps = staticmethod(cjson.dumps)


class TestPyTest(PyTest):

    def test_pyjson(self):
        self.assertEqual(self.json.scanner.make_scanner.__module__, b'json.scanner')
        self.assertEqual(self.json.decoder.scanstring.__module__, b'json.decoder')
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, b'json.encoder')
        return


class TestCTest(CTest):

    def test_cjson(self):
        self.assertEqual(self.json.scanner.make_scanner.__module__, b'_json')
        self.assertEqual(self.json.decoder.scanstring.__module__, b'_json')
        self.assertEqual(self.json.encoder.c_make_encoder.__module__, b'_json')
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, b'_json')
        return


here = os.path.dirname(__file__)

def test_suite():
    suite = additional_tests()
    loader = unittest.TestLoader()
    for fn in os.listdir(here):
        if fn.startswith(b'test') and fn.endswith(b'.py'):
            modname = b'json.tests.' + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTests(loader.loadTestsFromModule(module))

    return suite


def additional_tests():
    suite = unittest.TestSuite()
    for mod in (json, json.encoder, json.decoder):
        suite.addTest(doctest.DocTestSuite(mod))

    suite.addTest(TestPyTest(b'test_pyjson'))
    suite.addTest(TestCTest(b'test_cjson'))
    return suite


def main():
    suite = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
    return


if __name__ == b'__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()
