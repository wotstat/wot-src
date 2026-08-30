import sys, time
from . import result
from .signals import registerResult
__unittest = True

class _WritelnDecorator(object):

    def __init__(self, stream):
        self.stream = stream
        return

    def __getattr__(self, attr):
        if attr in (b'stream', b'__getstate__'):
            raise AttributeError(attr)
        return getattr(self.stream, attr)

    def writeln(self, arg=None):
        if arg:
            self.write(arg)
        self.write(b'\n')
        return


class TextTestResult(result.TestResult):
    separator1 = b'=' * 70
    separator2 = b'-' * 70

    def __init__(self, stream, descriptions, verbosity):
        super(TextTestResult, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions
        return

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return (b'\n').join((str(test), doc_first_line))
        else:
            return str(test)

        return

    def startTest(self, test):
        super(TextTestResult, self).startTest(test)
        if self.showAll:
            self.stream.write(self.getDescription(test))
            self.stream.write(b' ... ')
            self.stream.flush()
        return

    def addSuccess(self, test):
        super(TextTestResult, self).addSuccess(test)
        if self.showAll:
            self.stream.writeln(b'ok')
        elif self.dots:
            self.stream.write(b'.')
            self.stream.flush()
        return

    def addError(self, test, err):
        super(TextTestResult, self).addError(test, err)
        if self.showAll:
            self.stream.writeln(b'ERROR')
        elif self.dots:
            self.stream.write(b'E')
            self.stream.flush()
        return

    def addFailure(self, test, err):
        super(TextTestResult, self).addFailure(test, err)
        if self.showAll:
            self.stream.writeln(b'FAIL')
        elif self.dots:
            self.stream.write(b'F')
            self.stream.flush()
        return

    def addSkip(self, test, reason):
        super(TextTestResult, self).addSkip(test, reason)
        if self.showAll:
            self.stream.writeln((b'skipped {0!r}').format(reason))
        elif self.dots:
            self.stream.write(b's')
            self.stream.flush()
        return

    def addExpectedFailure(self, test, err):
        super(TextTestResult, self).addExpectedFailure(test, err)
        if self.showAll:
            self.stream.writeln(b'expected failure')
        elif self.dots:
            self.stream.write(b'x')
            self.stream.flush()
        return

    def addUnexpectedSuccess(self, test):
        super(TextTestResult, self).addUnexpectedSuccess(test)
        if self.showAll:
            self.stream.writeln(b'unexpected success')
        elif self.dots:
            self.stream.write(b'u')
            self.stream.flush()
        return

    def printErrors(self):
        if self.dots or self.showAll:
            self.stream.writeln()
        self.printErrorList(b'ERROR', self.errors)
        self.printErrorList(b'FAIL', self.failures)
        return

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln(self.separator1)
            self.stream.writeln(b'%s: %s' % (flavour, self.getDescription(test)))
            self.stream.writeln(self.separator2)
            self.stream.writeln(b'%s' % err)

        return


class TextTestRunner(object):
    resultclass = TextTestResult

    def __init__(self, stream=sys.stderr, descriptions=True, verbosity=1, failfast=False, buffer=False, resultclass=None):
        self.stream = _WritelnDecorator(stream)
        self.descriptions = descriptions
        self.verbosity = verbosity
        self.failfast = failfast
        self.buffer = buffer
        if resultclass is not None:
            self.resultclass = resultclass
        return

    def _makeResult(self):
        return self.resultclass(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        startTime = time.time()
        startTestRun = getattr(result, b'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        try:
            test(result)
        finally:
            stopTestRun = getattr(result, b'stopTestRun', None)
            if stopTestRun is not None:
                stopTestRun()

        stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()
        if hasattr(result, b'separator2'):
            self.stream.writeln(result.separator2)
        run = result.testsRun
        self.stream.writeln(b'Ran %d test%s in %.3fs' % (
         run, run != 1 and b's' or b'', timeTaken))
        self.stream.writeln()
        expectedFails = unexpectedSuccesses = skipped = 0
        try:
            results = map(len, (result.expectedFailures,
             result.unexpectedSuccesses,
             result.skipped))
        except AttributeError:
            pass
        else:
            expectedFails, unexpectedSuccesses, skipped = results

        infos = []
        if not result.wasSuccessful():
            self.stream.write(b'FAILED')
            failed, errored = map(len, (result.failures, result.errors))
            if failed:
                infos.append(b'failures=%d' % failed)
            if errored:
                infos.append(b'errors=%d' % errored)
        else:
            self.stream.write(b'OK')
        if skipped:
            infos.append(b'skipped=%d' % skipped)
        if expectedFails:
            infos.append(b'expected failures=%d' % expectedFails)
        if unexpectedSuccesses:
            infos.append(b'unexpected successes=%d' % unexpectedSuccesses)
        if infos:
            self.stream.writeln(b' (%s)' % ((b', ').join(infos),))
        else:
            self.stream.write(b'\n')
        return result
