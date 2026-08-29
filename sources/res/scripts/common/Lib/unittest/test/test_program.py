from cStringIO import StringIO
import os, sys, unittest, unittest.test

class Test_TestProgram(unittest.TestCase):

    def test_discovery_from_dotted_path(self):
        loader = unittest.TestLoader()
        tests = [
         self]
        expectedPath = os.path.abspath(os.path.dirname(unittest.test.__file__))
        self.wasRun = False

        def _find_tests(start_dir, pattern):
            self.wasRun = True
            self.assertEqual(start_dir, expectedPath)
            return tests

        loader._find_tests = _find_tests
        suite = loader.discover(b'unittest.test')
        self.assertTrue(self.wasRun)
        self.assertEqual(suite._tests, tests)
        return

    def testNoExit(self):
        result = object()
        test = object()

        class FakeRunner(object):

            def run(self, test):
                self.test = test
                return result

        runner = FakeRunner()
        oldParseArgs = unittest.TestProgram.parseArgs

        def restoreParseArgs():
            unittest.TestProgram.parseArgs = oldParseArgs
            return

        unittest.TestProgram.parseArgs = lambda *args: None
        self.addCleanup(restoreParseArgs)

        def removeTest():
            del unittest.TestProgram.test
            return

        unittest.TestProgram.test = test
        self.addCleanup(removeTest)
        program = unittest.TestProgram(testRunner=runner, exit=False, verbosity=2)
        self.assertEqual(program.result, result)
        self.assertEqual(runner.test, test)
        self.assertEqual(program.verbosity, 2)
        return

    class FooBar(unittest.TestCase):

        def testPass(self):
            return

        def testFail(self):
            return

    class FooBarLoader(unittest.TestLoader):

        def loadTestsFromModule(self, module):
            return self.suiteClass([
             self.loadTestsFromTestCase(Test_TestProgram.FooBar)])

    def test_NonExit(self):
        program = unittest.main(exit=False, argv=[
         b'foobar'], testRunner=unittest.TextTestRunner(stream=StringIO()), testLoader=self.FooBarLoader())
        self.assertTrue(hasattr(program, b'result'))
        return

    def test_Exit(self):
        self.assertRaises(SystemExit, unittest.main, argv=[
         b'foobar'], testRunner=unittest.TextTestRunner(stream=StringIO()), exit=True, testLoader=self.FooBarLoader())
        return

    def test_ExitAsDefault(self):
        self.assertRaises(SystemExit, unittest.main, argv=[
         b'foobar'], testRunner=unittest.TextTestRunner(stream=StringIO()), testLoader=self.FooBarLoader())
        return


class InitialisableProgram(unittest.TestProgram):
    exit = False
    result = None
    verbosity = 1
    defaultTest = None
    testRunner = None
    testLoader = unittest.defaultTestLoader
    progName = b'test'
    test = b'test'

    def __init__(self, *args):
        return


RESULT = object()

class FakeRunner(object):
    initArgs = None
    test = None
    raiseError = False

    def __init__(self, **kwargs):
        FakeRunner.initArgs = kwargs
        if FakeRunner.raiseError:
            FakeRunner.raiseError = False
            raise TypeError
        return

    def run(self, test):
        FakeRunner.test = test
        return RESULT


class TestCommandLineArgs(unittest.TestCase):

    def setUp(self):
        self.program = InitialisableProgram()
        self.program.createTests = lambda : None
        FakeRunner.initArgs = None
        FakeRunner.test = None
        FakeRunner.raiseError = False
        return

    def testHelpAndUnknown(self):
        program = self.program

        def usageExit(msg=None):
            program.msg = msg
            program.exit = True
            return

        program.usageExit = usageExit
        for opt in (b'-h', b'-H', b'--help'):
            program.exit = False
            program.parseArgs([None, opt])
            self.assertTrue(program.exit)
            self.assertIsNone(program.msg)

        program.parseArgs([None, b'-$'])
        self.assertTrue(program.exit)
        self.assertIsNotNone(program.msg)
        return

    def testVerbosity(self):
        program = self.program
        for opt in (b'-q', b'--quiet'):
            program.verbosity = 1
            program.parseArgs([None, opt])
            self.assertEqual(program.verbosity, 0)

        for opt in (b'-v', b'--verbose'):
            program.verbosity = 1
            program.parseArgs([None, opt])
            self.assertEqual(program.verbosity, 2)

        return

    def testBufferCatchFailfast(self):
        program = self.program
        for arg, attr in ((b'buffer', b'buffer'), (b'failfast', b'failfast'),
         (b'catch', b'catchbreak')):
            if attr == b'catch' and not hasInstallHandler:
                continue
            short_opt = b'-%s' % arg[0]
            long_opt = b'--%s' % arg
            for opt in (short_opt, long_opt):
                setattr(program, attr, None)
                program.parseArgs([None, opt])
                self.assertTrue(getattr(program, attr))

            for opt in (short_opt, long_opt):
                not_none = object()
                setattr(program, attr, not_none)
                program.parseArgs([None, opt])
                self.assertEqual(getattr(program, attr), not_none)

        return

    def testRunTestsRunnerClass(self):
        program = self.program
        program.testRunner = FakeRunner
        program.verbosity = b'verbosity'
        program.failfast = b'failfast'
        program.buffer = b'buffer'
        program.runTests()
        self.assertEqual(FakeRunner.initArgs, {b'verbosity': b'verbosity', b'failfast': b'failfast', 
           b'buffer': b'buffer'})
        self.assertEqual(FakeRunner.test, b'test')
        self.assertIs(program.result, RESULT)
        return

    def testRunTestsRunnerInstance(self):
        program = self.program
        program.testRunner = FakeRunner()
        FakeRunner.initArgs = None
        program.runTests()
        self.assertIsNone(FakeRunner.initArgs)
        self.assertEqual(FakeRunner.test, b'test')
        self.assertIs(program.result, RESULT)
        return

    def testRunTestsOldRunnerClass(self):
        program = self.program
        FakeRunner.raiseError = True
        program.testRunner = FakeRunner
        program.verbosity = b'verbosity'
        program.failfast = b'failfast'
        program.buffer = b'buffer'
        program.test = b'test'
        program.runTests()
        self.assertEqual(FakeRunner.initArgs, {})
        self.assertEqual(FakeRunner.test, b'test')
        self.assertIs(program.result, RESULT)
        return

    def testCatchBreakInstallsHandler(self):
        module = sys.modules[b'unittest.main']
        original = module.installHandler

        def restore():
            module.installHandler = original
            return

        self.addCleanup(restore)
        self.installed = False

        def fakeInstallHandler():
            self.installed = True
            return

        module.installHandler = fakeInstallHandler
        program = self.program
        program.catchbreak = True
        program.testRunner = FakeRunner
        program.runTests()
        self.assertTrue(self.installed)
        return


if __name__ == b'__main__':
    unittest.main()
