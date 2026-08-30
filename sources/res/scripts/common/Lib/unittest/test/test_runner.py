import unittest
from cStringIO import StringIO
import pickle
from unittest.test.support import LoggingResult, ResultWithNoStartTestRunStopTestRun

class TestCleanUp(unittest.TestCase):

    def testCleanUp(self):

        class TestableTest(unittest.TestCase):

            def testNothing(self):
                return

        test = TestableTest(b'testNothing')
        self.assertEqual(test._cleanups, [])
        cleanups = []

        def cleanup1(*args, **kwargs):
            cleanups.append((1, args, kwargs))
            return

        def cleanup2(*args, **kwargs):
            cleanups.append((2, args, kwargs))
            return

        test.addCleanup(cleanup1, 1, 2, 3, four=b'hello', five=b'goodbye')
        test.addCleanup(cleanup2)
        self.assertEqual(test._cleanups, [
         (
          cleanup1, (1, 2, 3), dict(four=b'hello', five=b'goodbye')),
         (
          cleanup2, (), {})])
        result = test.doCleanups()
        self.assertTrue(result)
        self.assertEqual(cleanups, [(2, (), {}),
         (1, (1, 2, 3),
          dict(four=b'hello', five=b'goodbye'))])
        return

    def testCleanUpWithErrors(self):

        class TestableTest(unittest.TestCase):

            def testNothing(self):
                return

        class MockResult(object):
            errors = []

            def addError(self, test, exc_info):
                self.errors.append((test, exc_info))
                return

        result = MockResult()
        test = TestableTest(b'testNothing')
        test._resultForDoCleanups = result
        exc1 = Exception(b'foo')
        exc2 = Exception(b'bar')

        def cleanup1():
            raise exc1
            return

        def cleanup2():
            raise exc2
            return

        test.addCleanup(cleanup1)
        test.addCleanup(cleanup2)
        self.assertFalse(test.doCleanups())
        (test1, (Type1, instance1, _)), (test2, (Type2, instance2, _)) = reversed(MockResult.errors)
        self.assertEqual((test1, Type1, instance1), (test, Exception, exc1))
        self.assertEqual((test2, Type2, instance2), (test, Exception, exc2))
        return

    def testCleanupInRun(self):
        blowUp = False
        ordering = []

        class TestableTest(unittest.TestCase):

            def setUp(self):
                ordering.append(b'setUp')
                if blowUp:
                    raise Exception(b'foo')
                return

            def testNothing(self):
                ordering.append(b'test')
                return

            def tearDown(self):
                ordering.append(b'tearDown')
                return

        test = TestableTest(b'testNothing')

        def cleanup1():
            ordering.append(b'cleanup1')
            return

        def cleanup2():
            ordering.append(b'cleanup2')
            return

        test.addCleanup(cleanup1)
        test.addCleanup(cleanup2)

        def success(some_test):
            self.assertEqual(some_test, test)
            ordering.append(b'success')
            return

        result = unittest.TestResult()
        result.addSuccess = success
        test.run(result)
        self.assertEqual(ordering, [7, 8, 9, 
         10, 11, 12])
        blowUp = True
        ordering = []
        test = TestableTest(b'testNothing')
        test.addCleanup(cleanup1)
        test.run(result)
        self.assertEqual(ordering, [b'setUp', b'cleanup1'])
        return

    def testTestCaseDebugExecutesCleanups(self):
        ordering = []

        class TestableTest(unittest.TestCase):

            def setUp(self):
                ordering.append(b'setUp')
                self.addCleanup(cleanup1)
                return

            def testNothing(self):
                ordering.append(b'test')
                return

            def tearDown(self):
                ordering.append(b'tearDown')
                return

        test = TestableTest(b'testNothing')

        def cleanup1():
            ordering.append(b'cleanup1')
            test.addCleanup(cleanup2)
            return

        def cleanup2():
            ordering.append(b'cleanup2')
            return

        test.debug()
        self.assertEqual(ordering, [6, 7, 8, 9, 10])
        return


class Test_TextTestRunner(unittest.TestCase):

    def test_init(self):
        runner = unittest.TextTestRunner()
        self.assertFalse(runner.failfast)
        self.assertFalse(runner.buffer)
        self.assertEqual(runner.verbosity, 1)
        self.assertTrue(runner.descriptions)
        self.assertEqual(runner.resultclass, unittest.TextTestResult)
        return

    def test_multiple_inheritance(self):

        class AResult(unittest.TestResult):

            def __init__(self, stream, descriptions, verbosity):
                super(AResult, self).__init__(stream, descriptions, verbosity)
                return

        class ATextResult(unittest.TextTestResult, AResult):
            pass

        ATextResult(None, None, 1)
        return

    def testBufferAndFailfast(self):

        class Test(unittest.TestCase):

            def testFoo(self):
                return

        result = unittest.TestResult()
        runner = unittest.TextTestRunner(stream=StringIO(), failfast=True, buffer=True)
        runner._makeResult = lambda : result
        runner.run(Test(b'testFoo'))
        self.assertTrue(result.failfast)
        self.assertTrue(result.buffer)
        return

    def testRunnerRegistersResult(self):

        class Test(unittest.TestCase):

            def testFoo(self):
                return

        originalRegisterResult = unittest.runner.registerResult

        def cleanup():
            unittest.runner.registerResult = originalRegisterResult
            return

        self.addCleanup(cleanup)
        result = unittest.TestResult()
        runner = unittest.TextTestRunner(stream=StringIO())
        runner._makeResult = lambda : result
        self.wasRegistered = 0

        def fakeRegisterResult(thisResult):
            self.wasRegistered += 1
            self.assertEqual(thisResult, result)
            return

        unittest.runner.registerResult = fakeRegisterResult
        runner.run(unittest.TestSuite())
        self.assertEqual(self.wasRegistered, 1)
        return

    def test_works_with_result_without_startTestRun_stopTestRun(self):

        class OldTextResult(ResultWithNoStartTestRunStopTestRun):
            separator2 = b''

            def printErrors(self):
                return

        class Runner(unittest.TextTestRunner):

            def __init__(self):
                super(Runner, self).__init__(StringIO())
                return

            def _makeResult(self):
                return OldTextResult()

        runner = Runner()
        runner.run(unittest.TestSuite())
        return

    def test_startTestRun_stopTestRun_called(self):

        class LoggingTextResult(LoggingResult):
            separator2 = b''

            def printErrors(self):
                return

        class LoggingRunner(unittest.TextTestRunner):

            def __init__(self, events):
                super(LoggingRunner, self).__init__(StringIO())
                self._events = events
                return

            def _makeResult(self):
                return LoggingTextResult(self._events)

        events = []
        runner = LoggingRunner(events)
        runner.run(unittest.TestSuite())
        expected = [b'startTestRun', b'stopTestRun']
        self.assertEqual(events, expected)
        return

    def test_pickle_unpickle(self):
        from StringIO import StringIO as PickleableIO
        stream = PickleableIO(b'foo')
        runner = unittest.TextTestRunner(stream)
        for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
            s = pickle.dumps(runner, protocol=protocol)
            obj = pickle.loads(s)
            self.assertEqual(obj.stream.getvalue(), stream.getvalue())

        return

    def test_resultclass(self):

        def MockResultClass(*args):
            return args

        STREAM = object()
        DESCRIPTIONS = object()
        VERBOSITY = object()
        runner = unittest.TextTestRunner(STREAM, DESCRIPTIONS, VERBOSITY, resultclass=MockResultClass)
        self.assertEqual(runner.resultclass, MockResultClass)
        expectedresult = (
         runner.stream, DESCRIPTIONS, VERBOSITY)
        self.assertEqual(runner._makeResult(), expectedresult)
        return


if __name__ == b'__main__':
    unittest.main()
