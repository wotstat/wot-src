import unittest

class TestHashing(object):

    def test_hash(self):
        for obj_1, obj_2 in self.eq_pairs:
            try:
                if not hash(obj_1) == hash(obj_2):
                    self.fail(b'%r and %r do not hash equal' % (obj_1, obj_2))
            except KeyboardInterrupt:
                raise
            except Exception as e:
                self.fail(b'Problem hashing %r and %r: %s' % (obj_1, obj_2, e))

        for obj_1, obj_2 in self.ne_pairs:
            try:
                if hash(obj_1) == hash(obj_2):
                    self.fail(b"%s and %s hash equal, but shouldn't" % (
                     obj_1, obj_2))
            except KeyboardInterrupt:
                raise
            except Exception as e:
                self.fail(b'Problem hashing %s and %s: %s' % (obj_1, obj_2, e))

        return


class TestEquality(object):

    def test_eq(self):
        for obj_1, obj_2 in self.eq_pairs:
            self.assertEqual(obj_1, obj_2)
            self.assertEqual(obj_2, obj_1)

        return

    def test_ne(self):
        for obj_1, obj_2 in self.ne_pairs:
            self.assertNotEqual(obj_1, obj_2)
            self.assertNotEqual(obj_2, obj_1)

        return


class LoggingResult(unittest.TestResult):

    def __init__(self, log):
        self._events = log
        super(LoggingResult, self).__init__()
        return

    def startTest(self, test):
        self._events.append(b'startTest')
        super(LoggingResult, self).startTest(test)
        return

    def startTestRun(self):
        self._events.append(b'startTestRun')
        super(LoggingResult, self).startTestRun()
        return

    def stopTest(self, test):
        self._events.append(b'stopTest')
        super(LoggingResult, self).stopTest(test)
        return

    def stopTestRun(self):
        self._events.append(b'stopTestRun')
        super(LoggingResult, self).stopTestRun()
        return

    def addFailure(self, *args):
        self._events.append(b'addFailure')
        super(LoggingResult, self).addFailure(*args)
        return

    def addSuccess(self, *args):
        self._events.append(b'addSuccess')
        super(LoggingResult, self).addSuccess(*args)
        return

    def addError(self, *args):
        self._events.append(b'addError')
        super(LoggingResult, self).addError(*args)
        return

    def addSkip(self, *args):
        self._events.append(b'addSkip')
        super(LoggingResult, self).addSkip(*args)
        return

    def addExpectedFailure(self, *args):
        self._events.append(b'addExpectedFailure')
        super(LoggingResult, self).addExpectedFailure(*args)
        return

    def addUnexpectedSuccess(self, *args):
        self._events.append(b'addUnexpectedSuccess')
        super(LoggingResult, self).addUnexpectedSuccess(*args)
        return


class ResultWithNoStartTestRunStopTestRun(object):

    def __init__(self):
        self.failures = []
        self.errors = []
        self.testsRun = 0
        self.skipped = []
        self.expectedFailures = []
        self.unexpectedSuccesses = []
        self.shouldStop = False
        return

    def startTest(self, test):
        return

    def stopTest(self, test):
        return

    def addError(self, test):
        return

    def addFailure(self, test):
        return

    def addSuccess(self, test):
        return

    def wasSuccessful(self):
        return True
