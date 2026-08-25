import sys, os, types
from . import loader, runner
from .signals import installHandler
__unittest = True
FAILFAST = b'  -f, --failfast   Stop on first failure\n'
CATCHBREAK = b'  -c, --catch      Catch control-C and display results\n'
BUFFEROUTPUT = b'  -b, --buffer     Buffer stdout and stderr during test runs\n'
USAGE_AS_MAIN = b"Usage: %(progName)s [options] [tests]\n\nOptions:\n  -h, --help       Show this message\n  -v, --verbose    Verbose output\n  -q, --quiet      Minimal output\n%(failfast)s%(catchbreak)s%(buffer)s\nExamples:\n  %(progName)s test_module               - run tests from test_module\n  %(progName)s module.TestClass          - run tests from module.TestClass\n  %(progName)s module.Class.test_method  - run specified test method\n\n[tests] can be a list of any number of test modules, classes and test\nmethods.\n\nAlternative Usage: %(progName)s discover [options]\n\nOptions:\n  -v, --verbose    Verbose output\n%(failfast)s%(catchbreak)s%(buffer)s  -s directory     Directory to start discovery ('.' default)\n  -p pattern       Pattern to match test files ('test*.py' default)\n  -t directory     Top level directory of project (default to\n                   start directory)\n\nFor test discovery all test modules must be importable from the top\nlevel directory of the project.\n"
USAGE_FROM_MODULE = b"Usage: %(progName)s [options] [test] [...]\n\nOptions:\n  -h, --help       Show this message\n  -v, --verbose    Verbose output\n  -q, --quiet      Minimal output\n%(failfast)s%(catchbreak)s%(buffer)s\nExamples:\n  %(progName)s                               - run default set of tests\n  %(progName)s MyTestSuite                   - run suite 'MyTestSuite'\n  %(progName)s MyTestCase.testSomething      - run MyTestCase.testSomething\n  %(progName)s MyTestCase                    - run all 'test*' test methods\n                                               in MyTestCase\n"

class TestProgram(object):
    USAGE = USAGE_FROM_MODULE
    failfast = catchbreak = buffer = progName = None

    def __init__(self, module=b'__main__', defaultTest=None, argv=None, testRunner=None, testLoader=loader.defaultTestLoader, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None):
        if isinstance(module, basestring):
            self.module = __import__(module)
            for part in module.split(b'.')[1:]:
                self.module = getattr(self.module, part)

        else:
            self.module = module
        if argv is None:
            argv = sys.argv
        self.exit = exit
        self.failfast = failfast
        self.catchbreak = catchbreak
        self.verbosity = verbosity
        self.buffer = buffer
        self.defaultTest = defaultTest
        self.testRunner = testRunner
        self.testLoader = testLoader
        self.progName = os.path.basename(argv[0])
        self.parseArgs(argv)
        self.runTests()
        return

    def usageExit(self, msg=None):
        if msg:
            print msg
        usage = {b'progName': (self.progName), b'catchbreak': b'', b'failfast': b'', b'buffer': b''}
        if self.failfast != False:
            usage[b'failfast'] = FAILFAST
        if self.catchbreak != False:
            usage[b'catchbreak'] = CATCHBREAK
        if self.buffer != False:
            usage[b'buffer'] = BUFFEROUTPUT
        print self.USAGE % usage
        sys.exit(2)
        return

    def parseArgs(self, argv):
        if len(argv) > 1 and argv[1].lower() == b'discover':
            self._do_discovery(argv[2:])
            return
        else:
            import getopt
            long_opts = [
             5, 6, 7, 8, 9, 10]
            try:
                options, args = getopt.getopt(argv[1:], b'hHvqfcb', long_opts)
                for opt, value in options:
                    if opt in (b'-h', b'-H', b'--help'):
                        self.usageExit()
                    if opt in (b'-q', b'--quiet'):
                        self.verbosity = 0
                    if opt in (b'-v', b'--verbose'):
                        self.verbosity = 2
                    if opt in (b'-f', b'--failfast'):
                        if self.failfast is None:
                            self.failfast = True
                    if opt in (b'-c', b'--catch'):
                        if self.catchbreak is None:
                            self.catchbreak = True
                    if opt in (b'-b', b'--buffer'):
                        if self.buffer is None:
                            self.buffer = True

                if len(args) == 0 and self.defaultTest is None:
                    self.testNames = None
                elif len(args) > 0:
                    self.testNames = args
                    if __name__ == b'__main__':
                        self.module = None
                else:
                    self.testNames = (
                     self.defaultTest,)
                self.createTests()
            except getopt.error as msg:
                self.usageExit(msg)

            return

    def createTests(self):
        if self.testNames is None:
            self.test = self.testLoader.loadTestsFromModule(self.module)
        else:
            self.test = self.testLoader.loadTestsFromNames(self.testNames, self.module)
        return

    def _do_discovery(self, argv, Loader=None):
        if Loader is None:
            Loader = lambda : self.testLoader
        self.progName = b'%s discover' % self.progName
        import optparse
        parser = optparse.OptionParser()
        parser.prog = self.progName
        parser.add_option(b'-v', b'--verbose', dest=b'verbose', default=False, help=b'Verbose output', action=b'store_true')
        if self.failfast != False:
            parser.add_option(b'-f', b'--failfast', dest=b'failfast', default=False, help=b'Stop on first fail or error', action=b'store_true')
        if self.catchbreak != False:
            parser.add_option(b'-c', b'--catch', dest=b'catchbreak', default=False, help=b'Catch Ctrl-C and display results so far', action=b'store_true')
        if self.buffer != False:
            parser.add_option(b'-b', b'--buffer', dest=b'buffer', default=False, help=b'Buffer stdout and stderr during tests', action=b'store_true')
        parser.add_option(b'-s', b'--start-directory', dest=b'start', default=b'.', help=b"Directory to start discovery ('.' default)")
        parser.add_option(b'-p', b'--pattern', dest=b'pattern', default=b'test*.py', help=b"Pattern to match tests ('test*.py' default)")
        parser.add_option(b'-t', b'--top-level-directory', dest=b'top', default=None, help=b'Top level directory of project (defaults to start directory)')
        options, args = parser.parse_args(argv)
        if len(args) > 3:
            self.usageExit()
        for name, value in zip((b'start', b'pattern', b'top'), args):
            setattr(options, name, value)

        if self.failfast is None:
            self.failfast = options.failfast
        if self.catchbreak is None:
            self.catchbreak = options.catchbreak
        if self.buffer is None:
            self.buffer = options.buffer
        if options.verbose:
            self.verbosity = 2
        start_dir = options.start
        pattern = options.pattern
        top_level_dir = options.top
        loader = Loader()
        self.test = loader.discover(start_dir, pattern, top_level_dir)
        return

    def runTests(self):
        if self.catchbreak:
            installHandler()
        if self.testRunner is None:
            self.testRunner = runner.TextTestRunner
        if isinstance(self.testRunner, (type, types.ClassType)):
            try:
                testRunner = self.testRunner(verbosity=self.verbosity, failfast=self.failfast, buffer=self.buffer)
            except TypeError:
                testRunner = self.testRunner()

        else:
            testRunner = self.testRunner
        self.result = testRunner.run(self.test)
        if self.exit:
            sys.exit(not self.result.wasSuccessful())
        return


main = TestProgram
