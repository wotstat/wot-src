import sys, textwrap
from StringIO import StringIO
from test import test_support
import traceback, unittest

class Test_TestResult(unittest.TestCase):

    def test_init(self):
        result = unittest.TestResult()
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 0)
        self.assertEqual(result.shouldStop, False)
        self.assertIsNone(result._stdout_buffer)
        self.assertIsNone(result._stderr_buffer)
        return

    def test_stop(self):
        result = unittest.TestResult()
        result.stop()
        self.assertEqual(result.shouldStop, True)
        return

    def test_startTest(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

        test = Foo(b'test_1')
        result = unittest.TestResult()
        result.startTest(test)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)
        result.stopTest(test)
        return

    def test_stopTest(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

        test = Foo(b'test_1')
        result = unittest.TestResult()
        result.startTest(test)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)
        result.stopTest(test)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)
        return

    def test_startTestRun_stopTestRun(self):
        result = unittest.TestResult()
        result.startTestRun()
        result.stopTestRun()
        return

    def test_addSuccess(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

        test = Foo(b'test_1')
        result = unittest.TestResult()
        result.startTest(test)
        result.addSuccess(test)
        result.stopTest(test)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)
        return

    def test_addFailure(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

        test = Foo(b'test_1')
        try:
            test.fail(b'foo')
        except:
            exc_info_tuple = sys.exc_info()

        result = unittest.TestResult()
        result.startTest(test)
        result.addFailure(test, exc_info_tuple)
        result.stopTest(test)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 1)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)
        test_case, formatted_exc = result.failures[0]
        self.assertIs(test_case, test)
        self.assertIsInstance(formatted_exc, str)
        return

    def test_addError(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

        test = Foo(b'test_1')
        try:
            raise TypeError()
        except:
            exc_info_tuple = sys.exc_info()

        result = unittest.TestResult()
        result.startTest(test)
        result.addError(test, exc_info_tuple)
        result.stopTest(test)
        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)
        test_case, formatted_exc = result.errors[0]
        self.assertIs(test_case, test)
        self.assertIsInstance(formatted_exc, str)
        return

    def testGetDescriptionWithoutDocstring(self):
        result = unittest.TextTestResult(None, True, 1)
        self.assertEqual(result.getDescription(self), b'testGetDescriptionWithoutDocstring (' + __name__ + b'.Test_TestResult)')
        return

    @unittest.skipIf(sys.flags.optimize >= 2, b'Docstrings are omitted with -O2 and above')
    def testGetDescriptionWithOneLineDocstring(self):
        result = unittest.TextTestResult(None, True, 1)
        self.assertEqual(result.getDescription(self), b'testGetDescriptionWithOneLineDocstring (' + __name__ + b'.Test_TestResult)\nTests getDescription() for a method with a docstring.')
        return

    @unittest.skipIf(sys.flags.optimize >= 2, b'Docstrings are omitted with -O2 and above')
    def testGetDescriptionWithMultiLineDocstring(self):
        result = unittest.TextTestResult(None, True, 1)
        self.assertEqual(result.getDescription(self), b'testGetDescriptionWithMultiLineDocstring (' + __name__ + b'.Test_TestResult)\nTests getDescription() for a method with a longer docstring.')
        return

    def testStackFrameTrimming(self):

        class Frame(object):

            class tb_frame(object):
                f_globals = {}

        result = unittest.TestResult()
        self.assertFalse(result._is_relevant_tb_level(Frame))
        Frame.tb_frame.f_globals[b'__unittest'] = True
        self.assertTrue(result._is_relevant_tb_level(Frame))
        return

    def testFailFast(self):
        result = unittest.TestResult()
        result._exc_info_to_string = lambda *_: b''
        result.failfast = True
        result.addError(None, None)
        self.assertTrue(result.shouldStop)
        result = unittest.TestResult()
        result._exc_info_to_string = lambda *_: b''
        result.failfast = True
        result.addFailure(None, None)
        self.assertTrue(result.shouldStop)
        result = unittest.TestResult()
        result._exc_info_to_string = lambda *_: b''
        result.failfast = True
        result.addUnexpectedSuccess(None)
        self.assertTrue(result.shouldStop)
        return

    def testFailFastSetByRunner(self):
        runner = unittest.TextTestRunner(stream=StringIO(), failfast=True)

        def test(result):
            self.assertTrue(result.failfast)
            return

        runner.run(test)
        return


classDict = dict(unittest.TestResult.__dict__)
for m in (b'addSkip', b'addExpectedFailure', b'addUnexpectedSuccess',
 b'__init__'):
    del classDict[m]

def __init__(self, stream=None, descriptions=None, verbosity=None):
    self.failures = []
    self.errors = []
    self.testsRun = 0
    self.shouldStop = False
    self.buffer = False
    return


classDict[b'__init__'] = __init__
OldResult = type(b'OldResult', (object,), classDict)

class Test_OldTestResult(unittest.TestCase):

    def assertOldResultWarning(self, test, failures):
        with test_support.check_warnings((b'TestResult has no add.+ method,',
         RuntimeWarning)):
            result = OldResult()
            test.run(result)
            self.assertEqual(len(result.failures), failures)
        return

    def testOldTestResult(self):

        class Test(unittest.TestCase):

            def testSkip(self):
                self.skipTest(b'foobar')
                return

            @unittest.expectedFailure
            def testExpectedFail(self):
                raise TypeError
                return

            @unittest.expectedFailure
            def testUnexpectedSuccess(self):
                return

        for test_name, should_pass in ((b'testSkip', True),
         (
          b'testExpectedFail', True),
         (
          b'testUnexpectedSuccess', False)):
            test = Test(test_name)
            self.assertOldResultWarning(test, int(not should_pass))

        return

    def testOldTestTesultSetup(self):

        class Test(unittest.TestCase):

            def setUp(self):
                self.skipTest(b'no reason')
                return

            def testFoo(self):
                return

        self.assertOldResultWarning(Test(b'testFoo'), 0)
        return

    def testOldTestResultClass(self):

        @unittest.skip(b'no reason')
        class Test(unittest.TestCase):

            def testFoo(self):
                return

        self.assertOldResultWarning(Test(b'testFoo'), 0)
        return

    def testOldResultWithRunner(self):

        class Test(unittest.TestCase):

            def testFoo(self):
                return

        runner = unittest.TextTestRunner(resultclass=OldResult, stream=StringIO())
        runner.run(Test(b'testFoo'))
        return


class MockTraceback(object):

    @staticmethod
    def format_exception(*_):
        return [b'A traceback']


def restore_traceback():
    unittest.result.traceback = traceback
    return


class TestOutputBuffering(unittest.TestCase):

    def setUp(self):
        self._real_out = sys.stdout
        self._real_err = sys.stderr
        return

    def tearDown(self):
        sys.stdout = self._real_out
        sys.stderr = self._real_err
        return

    def testBufferOutputOff(self):
        real_out = self._real_out
        real_err = self._real_err
        result = unittest.TestResult()
        self.assertFalse(result.buffer)
        self.assertIs(real_out, sys.stdout)
        self.assertIs(real_err, sys.stderr)
        result.startTest(self)
        self.assertIs(real_out, sys.stdout)
        self.assertIs(real_err, sys.stderr)
        return

    def testBufferOutputStartTestAddSuccess(self):
        real_out = self._real_out
        real_err = self._real_err
        result = unittest.TestResult()
        self.assertFalse(result.buffer)
        result.buffer = True
        self.assertIs(real_out, sys.stdout)
        self.assertIs(real_err, sys.stderr)
        result.startTest(self)
        self.assertIsNot(real_out, sys.stdout)
        self.assertIsNot(real_err, sys.stderr)
        self.assertIsInstance(sys.stdout, StringIO)
        self.assertIsInstance(sys.stderr, StringIO)
        self.assertIsNot(sys.stdout, sys.stderr)
        out_stream = sys.stdout
        err_stream = sys.stderr
        result._original_stdout = StringIO()
        result._original_stderr = StringIO()
        print b'foo'
        print >> sys.stderr, b'bar'
        self.assertEqual(out_stream.getvalue(), b'foo\n')
        self.assertEqual(err_stream.getvalue(), b'bar\n')
        self.assertEqual(result._original_stdout.getvalue(), b'')
        self.assertEqual(result._original_stderr.getvalue(), b'')
        result.addSuccess(self)
        result.stopTest(self)
        self.assertIs(sys.stdout, result._original_stdout)
        self.assertIs(sys.stderr, result._original_stderr)
        self.assertEqual(result._original_stdout.getvalue(), b'')
        self.assertEqual(result._original_stderr.getvalue(), b'')
        self.assertEqual(out_stream.getvalue(), b'')
        self.assertEqual(err_stream.getvalue(), b'')
        return

    def getStartedResult(self):
        result = unittest.TestResult()
        result.buffer = True
        result.startTest(self)
        return result

    def testBufferOutputAddErrorOrFailure(self):
        unittest.result.traceback = MockTraceback
        self.addCleanup(restore_traceback)
        for message_attr, add_attr, include_error in [
         (
          b'errors', b'addError', True),
         (
          b'failures', b'addFailure', False),
         (
          b'errors', b'addError', True),
         (
          b'failures', b'addFailure', False)]:
            result = self.getStartedResult()
            buffered_out = sys.stdout
            buffered_err = sys.stderr
            result._original_stdout = StringIO()
            result._original_stderr = StringIO()
            print >> sys.stdout, b'foo'
            if include_error:
                print >> sys.stderr, b'bar'
            addFunction = getattr(result, add_attr)
            addFunction(self, (None, None, None))
            result.stopTest(self)
            result_list = getattr(result, message_attr)
            self.assertEqual(len(result_list), 1)
            test, message = result_list[0]
            expectedOutMessage = textwrap.dedent(b'\n                Stdout:\n                foo\n            ')
            expectedErrMessage = b''
            if include_error:
                expectedErrMessage = textwrap.dedent(b'\n                Stderr:\n                bar\n            ')
            expectedFullMessage = b'A traceback%s%s' % (expectedOutMessage, expectedErrMessage)
            self.assertIs(test, self)
            self.assertEqual(result._original_stdout.getvalue(), expectedOutMessage)
            self.assertEqual(result._original_stderr.getvalue(), expectedErrMessage)
            self.assertMultiLineEqual(message, expectedFullMessage)

        return

    def testBufferSetupClass(self):
        result = unittest.TestResult()
        result.buffer = True

        class Foo(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                1 // 0
                return

            def test_foo(self):
                return

        suite = unittest.TestSuite([Foo(b'test_foo')])
        suite(result)
        self.assertEqual(len(result.errors), 1)
        return

    def testBufferTearDownClass(self):
        result = unittest.TestResult()
        result.buffer = True

        class Foo(unittest.TestCase):

            @classmethod
            def tearDownClass(cls):
                1 // 0
                return

            def test_foo(self):
                return

        suite = unittest.TestSuite([Foo(b'test_foo')])
        suite(result)
        self.assertEqual(len(result.errors), 1)
        return

    def testBufferSetUpModule(self):
        result = unittest.TestResult()
        result.buffer = True

        class Foo(unittest.TestCase):

            def test_foo(self):
                return

        class Module(object):

            @staticmethod
            def setUpModule():
                1 // 0
                return

        Foo.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        self.addCleanup(sys.modules.pop, b'Module')
        suite = unittest.TestSuite([Foo(b'test_foo')])
        suite(result)
        self.assertEqual(len(result.errors), 1)
        return

    def testBufferTearDownModule(self):
        result = unittest.TestResult()
        result.buffer = True

        class Foo(unittest.TestCase):

            def test_foo(self):
                return

        class Module(object):

            @staticmethod
            def tearDownModule():
                1 // 0
                return

        Foo.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        self.addCleanup(sys.modules.pop, b'Module')
        suite = unittest.TestSuite([Foo(b'test_foo')])
        suite(result)
        self.assertEqual(len(result.errors), 1)
        return


if __name__ == b'__main__':
    unittest.main()
