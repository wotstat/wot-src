import os, sys, traceback
from StringIO import StringIO
from . import util
from functools import wraps
__unittest = True

def failfast(method):

    @wraps(method)
    def inner(self, *args, **kw):
        if getattr(self, b'failfast', False):
            self.stop()
        return method(self, *args, **kw)

    return inner


STDOUT_LINE = b'\nStdout:\n%s'
STDERR_LINE = b'\nStderr:\n%s'

class TestResult(object):
    _previousTestClass = None
    _testRunEntered = False
    _moduleSetUpFailed = False

    def __init__(self, stream=None, descriptions=None, verbosity=None):
        self.failfast = False
        self.failures = []
        self.errors = []
        self.testsRun = 0
        self.skipped = []
        self.expectedFailures = []
        self.unexpectedSuccesses = []
        self.shouldStop = False
        self.buffer = False
        self._stdout_buffer = None
        self._stderr_buffer = None
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        self._mirrorOutput = False
        return

    def printErrors(self):
        return

    def startTest(self, test):
        self.testsRun += 1
        self._mirrorOutput = False
        self._setupStdout()
        return

    def _setupStdout(self):
        if self.buffer:
            if self._stderr_buffer is None:
                self._stderr_buffer = StringIO()
                self._stdout_buffer = StringIO()
            sys.stdout = self._stdout_buffer
            sys.stderr = self._stderr_buffer
        return

    def startTestRun(self):
        return

    def stopTest(self, test):
        self._restoreStdout()
        self._mirrorOutput = False
        return

    def _restoreStdout(self):
        if self.buffer:
            if self._mirrorOutput:
                output = sys.stdout.getvalue()
                error = sys.stderr.getvalue()
                if output:
                    if not output.endswith(b'\n'):
                        output += b'\n'
                    self._original_stdout.write(STDOUT_LINE % output)
                if error:
                    if not error.endswith(b'\n'):
                        error += b'\n'
                    self._original_stderr.write(STDERR_LINE % error)
            sys.stdout = self._original_stdout
            sys.stderr = self._original_stderr
            self._stdout_buffer.seek(0)
            self._stdout_buffer.truncate()
            self._stderr_buffer.seek(0)
            self._stderr_buffer.truncate()
        return

    def stopTestRun(self):
        return

    @failfast
    def addError(self, test, err):
        self.errors.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        return

    @failfast
    def addFailure(self, test, err):
        self.failures.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        return

    def addSuccess(self, test):
        return

    def addSkip(self, test, reason):
        self.skipped.append((test, reason))
        return

    def addExpectedFailure(self, test, err):
        self.expectedFailures.append((
         test, self._exc_info_to_string(err, test)))
        return

    @failfast
    def addUnexpectedSuccess(self, test):
        self.unexpectedSuccesses.append(test)
        return

    def wasSuccessful(self):
        return len(self.failures) == len(self.errors) == 0

    def stop(self):
        self.shouldStop = True
        return

    def _exc_info_to_string(self, err, test):
        exctype, value, tb = err
        while tb and self._is_relevant_tb_level(tb):
            tb = tb.tb_next

        if exctype is test.failureException:
            length = self._count_relevant_tb_levels(tb)
            msgLines = traceback.format_exception(exctype, value, tb, length)
        else:
            msgLines = traceback.format_exception(exctype, value, tb)
        if self.buffer:
            output = sys.stdout.getvalue()
            error = sys.stderr.getvalue()
            if output:
                if not output.endswith(b'\n'):
                    output += b'\n'
                msgLines.append(STDOUT_LINE % output)
            if error:
                if not error.endswith(b'\n'):
                    error += b'\n'
                msgLines.append(STDERR_LINE % error)
        return (b'').join(msgLines)

    def _is_relevant_tb_level(self, tb):
        return b'__unittest' in tb.tb_frame.f_globals

    def _count_relevant_tb_levels(self, tb):
        length = 0
        while tb and not self._is_relevant_tb_level(tb):
            length += 1
            tb = tb.tb_next

        return length

    def __repr__(self):
        return b'<%s run=%i errors=%i failures=%i>' % (
         util.strclass(self.__class__), self.testsRun, len(self.errors),
         len(self.failures))
