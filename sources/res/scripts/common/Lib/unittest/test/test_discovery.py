import os, re, sys, unittest, unittest.test

class TestDiscovery(unittest.TestCase):

    def test_get_name_from_path(self):
        loader = unittest.TestLoader()
        loader._top_level_dir = b'/foo'
        name = loader._get_name_from_path(b'/foo/bar/baz.py')
        self.assertEqual(name, b'bar.baz')
        if not __debug__:
            return
        with self.assertRaises(AssertionError):
            loader._get_name_from_path(b'/bar/baz.py')
        return

    def test_find_tests(self):
        loader = unittest.TestLoader()
        original_listdir = os.listdir

        def restore_listdir():
            os.listdir = original_listdir
            return

        original_isfile = os.path.isfile

        def restore_isfile():
            os.path.isfile = original_isfile
            return

        original_isdir = os.path.isdir

        def restore_isdir():
            os.path.isdir = original_isdir
            return

        path_lists = [
         [4, 5, 6, 7, 
          8, 9, 10],
         [
          b'test3.py', b'test4.py']]
        os.listdir = lambda path: path_lists.pop(0)
        self.addCleanup(restore_listdir)

        def isdir(path):
            return path.endswith(b'dir')

        os.path.isdir = isdir
        self.addCleanup(restore_isdir)

        def isfile(path):
            return not path.endswith(b'dir') and b'another_dir' not in path

        os.path.isfile = isfile
        self.addCleanup(restore_isfile)
        loader._get_module_from_name = lambda path: path + b' module'
        loader.loadTestsFromModule = lambda module: module + b' tests'
        top_level = os.path.abspath(b'/foo')
        loader._top_level_dir = top_level
        suite = list(loader._find_tests(top_level, b'test*.py'))
        expected = [name + b' module tests' for name in (b'test1', b'test2')]
        expected.extend([b'test_dir.%s' % name + b' module tests' for name in (b'test3', b'test4')])
        self.assertEqual(suite, expected)
        return

    def test_find_tests_with_package(self):
        loader = unittest.TestLoader()
        original_listdir = os.listdir

        def restore_listdir():
            os.listdir = original_listdir
            return

        original_isfile = os.path.isfile

        def restore_isfile():
            os.path.isfile = original_isfile
            return

        original_isdir = os.path.isdir

        def restore_isdir():
            os.path.isdir = original_isdir
            return

        directories = [b'a_directory', b'test_directory', b'test_directory2']
        path_lists = [directories, [], [], []]
        os.listdir = lambda path: path_lists.pop(0)
        self.addCleanup(restore_listdir)
        os.path.isdir = lambda path: True
        self.addCleanup(restore_isdir)
        os.path.isfile = lambda path: os.path.basename(path) not in directories
        self.addCleanup(restore_isfile)

        class Module(object):
            paths = []
            load_tests_args = []

            def __init__(self, path):
                self.path = path
                self.paths.append(path)
                if os.path.basename(path) == b'test_directory':

                    def load_tests(loader, tests, pattern):
                        self.load_tests_args.append((loader, tests, pattern))
                        return b'load_tests'

                    self.load_tests = load_tests
                return

            def __eq__(self, other):
                return self.path == other.path

            __hash__ = None

        loader._get_module_from_name = lambda name: Module(name)

        def loadTestsFromModule(module, use_load_tests):
            if use_load_tests:
                raise self.failureException(b'use_load_tests should be False for packages')
            return module.path + b' module tests'

        loader.loadTestsFromModule = loadTestsFromModule
        loader._top_level_dir = b'/foo'
        suite = list(loader._find_tests(b'/foo', b'test*'))
        self.assertEqual(suite, [
         b'load_tests', b'test_directory2' + b' module tests'])
        self.assertEqual(Module.paths, [b'test_directory', b'test_directory2'])
        self.assertEqual(Module.load_tests_args, [
         (
          loader, b'test_directory' + b' module tests', b'test*')])
        return

    def test_discover(self):
        loader = unittest.TestLoader()
        original_isfile = os.path.isfile
        original_isdir = os.path.isdir

        def restore_isfile():
            os.path.isfile = original_isfile
            return

        os.path.isfile = lambda path: False
        self.addCleanup(restore_isfile)
        orig_sys_path = sys.path[:]

        def restore_path():
            sys.path[:] = orig_sys_path
            return

        self.addCleanup(restore_path)
        full_path = os.path.abspath(os.path.normpath(b'/foo'))
        with self.assertRaises(ImportError):
            loader.discover(b'/foo/bar', top_level_dir=b'/foo')
        self.assertEqual(loader._top_level_dir, full_path)
        self.assertIn(full_path, sys.path)
        os.path.isfile = lambda path: True
        os.path.isdir = lambda path: True

        def restore_isdir():
            os.path.isdir = original_isdir
            return

        self.addCleanup(restore_isdir)
        _find_tests_args = []

        def _find_tests(start_dir, pattern):
            _find_tests_args.append((start_dir, pattern))
            return [b'tests']

        loader._find_tests = _find_tests
        loader.suiteClass = str
        suite = loader.discover(b'/foo/bar/baz', b'pattern', b'/foo/bar')
        top_level_dir = os.path.abspath(b'/foo/bar')
        start_dir = os.path.abspath(b'/foo/bar/baz')
        self.assertEqual(suite, b"['tests']")
        self.assertEqual(loader._top_level_dir, top_level_dir)
        self.assertEqual(_find_tests_args, [(start_dir, b'pattern')])
        self.assertIn(top_level_dir, sys.path)
        return

    def test_discover_with_modules_that_fail_to_import(self):
        loader = unittest.TestLoader()
        listdir = os.listdir
        os.listdir = lambda _: [b'test_this_does_not_exist.py']
        isfile = os.path.isfile
        os.path.isfile = lambda _: True
        orig_sys_path = sys.path[:]

        def restore():
            os.path.isfile = isfile
            os.listdir = listdir
            sys.path[:] = orig_sys_path
            return

        self.addCleanup(restore)
        suite = loader.discover(b'.')
        self.assertIn(os.getcwd(), sys.path)
        self.assertEqual(suite.countTestCases(), 1)
        test = list(list(suite)[0])[0]
        with self.assertRaises(ImportError):
            test.test_this_does_not_exist()
        return

    def test_command_line_handling_parseArgs(self):
        program = object.__new__(unittest.TestProgram)
        args = []

        def do_discovery(argv):
            args.extend(argv)
            return

        program._do_discovery = do_discovery
        program.parseArgs([b'something', b'discover'])
        self.assertEqual(args, [])
        program.parseArgs([b'something', b'discover', b'foo', b'bar'])
        self.assertEqual(args, [b'foo', b'bar'])
        return

    def test_command_line_handling_do_discovery_too_many_arguments(self):

        class Stop(Exception):
            pass

        def usageExit():
            raise Stop
            return

        program = object.__new__(unittest.TestProgram)
        program.usageExit = usageExit
        program.testLoader = None
        with self.assertRaises(Stop):
            program._do_discovery([b'one', b'two', b'three', b'four'])
        return

    def test_command_line_handling_do_discovery_uses_default_loader(self):
        program = object.__new__(unittest.TestProgram)

        class Loader(object):
            args = []

            def discover(self, start_dir, pattern, top_level_dir):
                self.args.append((start_dir, pattern, top_level_dir))
                return b'tests'

        program.testLoader = Loader()
        program._do_discovery([b'-v'])
        self.assertEqual(Loader.args, [(b'.', b'test*.py', None)])
        return

    def test_command_line_handling_do_discovery_calls_loader(self):
        program = object.__new__(unittest.TestProgram)

        class Loader(object):
            args = []

            def discover(self, start_dir, pattern, top_level_dir):
                self.args.append((start_dir, pattern, top_level_dir))
                return b'tests'

        program._do_discovery([b'-v'], Loader=Loader)
        self.assertEqual(program.verbosity, 2)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'.', b'test*.py', None)])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([b'--verbose'], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'.', b'test*.py', None)])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'.', b'test*.py', None)])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([b'fish'], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'fish', b'test*.py', None)])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([b'fish', b'eggs'], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'fish', b'eggs', None)])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([b'fish', b'eggs', b'ham'], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'fish', b'eggs', b'ham')])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([b'-s', b'fish'], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'fish', b'test*.py', None)])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([b'-t', b'fish'], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'.', b'test*.py', b'fish')])
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([b'-p', b'fish'], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'.', b'fish', None)])
        self.assertFalse(program.failfast)
        self.assertFalse(program.catchbreak)
        Loader.args = []
        program = object.__new__(unittest.TestProgram)
        program._do_discovery([14, 10, 12, 9, 3, 15, 16], Loader=Loader)
        self.assertEqual(program.test, b'tests')
        self.assertEqual(Loader.args, [(b'fish', b'eggs', None)])
        self.assertEqual(program.verbosity, 2)
        self.assertTrue(program.failfast)
        self.assertTrue(program.catchbreak)
        return

    def setup_module_clash(self):

        class Module(object):
            __file__ = b'bar/foo.py'

        sys.modules[b'foo'] = Module
        full_path = os.path.abspath(b'foo')
        original_listdir = os.listdir
        original_isfile = os.path.isfile
        original_isdir = os.path.isdir

        def cleanup():
            os.listdir = original_listdir
            os.path.isfile = original_isfile
            os.path.isdir = original_isdir
            del sys.modules[b'foo']
            if full_path in sys.path:
                sys.path.remove(full_path)
            return

        self.addCleanup(cleanup)

        def listdir(_):
            return [
             b'foo.py']

        def isfile(_):
            return True

        def isdir(_):
            return True

        os.listdir = listdir
        os.path.isfile = isfile
        os.path.isdir = isdir
        return full_path

    def test_detect_module_clash(self):
        full_path = self.setup_module_clash()
        loader = unittest.TestLoader()
        mod_dir = os.path.abspath(b'bar')
        expected_dir = os.path.abspath(b'foo')
        msg = re.escape(b"'foo' module incorrectly imported from %r. Expected %r. Is this module globally installed?" % (
         mod_dir, expected_dir))
        self.assertRaisesRegexp(ImportError, b'^%s$' % msg, loader.discover, start_dir=b'foo', pattern=b'foo.py')
        self.assertEqual(sys.path[0], full_path)
        return

    def test_module_symlink_ok(self):
        full_path = self.setup_module_clash()
        original_realpath = os.path.realpath
        mod_dir = os.path.abspath(b'bar')
        expected_dir = os.path.abspath(b'foo')

        def cleanup():
            os.path.realpath = original_realpath
            return

        self.addCleanup(cleanup)

        def realpath(path):
            if path == os.path.join(mod_dir, b'foo.py'):
                return os.path.join(expected_dir, b'foo.py')
            return path

        os.path.realpath = realpath
        loader = unittest.TestLoader()
        loader.discover(start_dir=b'foo', pattern=b'foo.py')
        return

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


if __name__ == b'__main__':
    unittest.main()
