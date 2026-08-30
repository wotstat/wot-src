import unittest
from unittest.test.support import LoggingResult

class Test_FunctionTestCase(unittest.TestCase):

    def test_countTestCases(self):
        test = unittest.FunctionTestCase((lambda : None))
        self.assertEqual(test.countTestCases(), 1)
        return

    def test_run_call_order__error_in_setUp(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append(b'setUp')
            raise RuntimeError(b'raised by setUp')
            return

        def test():
            events.append(b'test')
            return

        def tearDown():
            events.append(b'tearDown')
            return

        expected = [b'startTest', b'setUp', b'addError', b'stopTest']
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)
        return

    def test_run_call_order__error_in_test(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append(b'setUp')
            return

        def test():
            events.append(b'test')
            raise RuntimeError(b'raised by test')
            return

        def tearDown():
            events.append(b'tearDown')
            return

        expected = [4, 5, 6, 7, 8, 
         9]
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)
        return

    def test_run_call_order__failure_in_test(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append(b'setUp')
            return

        def test():
            events.append(b'test')
            self.fail(b'raised by test')
            return

        def tearDown():
            events.append(b'tearDown')
            return

        expected = [4, 5, 6, 7, 8, 
         9]
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)
        return

    def test_run_call_order__error_in_tearDown(self):
        events = []
        result = LoggingResult(events)

        def setUp():
            events.append(b'setUp')
            return

        def test():
            events.append(b'test')
            return

        def tearDown():
            events.append(b'tearDown')
            raise RuntimeError(b'raised by tearDown')
            return

        expected = [4, 5, 6, 7, 8, 
         9]
        unittest.FunctionTestCase(test, setUp, tearDown).run(result)
        self.assertEqual(events, expected)
        return

    def test_id(self):
        test = unittest.FunctionTestCase((lambda : None))
        self.assertIsInstance(test.id(), basestring)
        return

    def test_shortDescription__no_docstring(self):
        test = unittest.FunctionTestCase((lambda : None))
        self.assertEqual(test.shortDescription(), None)
        return

    def test_shortDescription__singleline_docstring(self):
        desc = b'this tests foo'
        test = unittest.FunctionTestCase((lambda : None), description=desc)
        self.assertEqual(test.shortDescription(), b'this tests foo')
        return


if __name__ == b'__main__':
    unittest.main()
