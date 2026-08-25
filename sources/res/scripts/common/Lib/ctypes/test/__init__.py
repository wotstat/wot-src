import os, sys, unittest, getopt, time
use_resources = []
import ctypes
ctypes_symbols = dir(ctypes)

def need_symbol(name):
    return unittest.skipUnless(name in ctypes_symbols, (b'{!r} is required').format(name))


class ResourceDenied(unittest.SkipTest):
    pass


def is_resource_enabled(resource):
    if sys._getframe().f_back.f_globals.get(b'__name__') == b'__main__':
        return True
    else:
        result = use_resources is not None and (resource in use_resources or b'*' in use_resources)
        if not result:
            _unavail[resource] = None
        return result


_unavail = {}

def requires(resource, msg=None):
    if sys._getframe().f_back.f_globals.get(b'__name__') == b'__main__':
        return
    else:
        if not is_resource_enabled(resource):
            if msg is None:
                msg = b"Use of the `%s' resource not enabled" % resource
            raise ResourceDenied(msg)
        return


def find_package_modules(package, mask):
    import fnmatch
    if hasattr(package, b'__loader__') and hasattr(package.__loader__, b'_files'):
        path = package.__name__.replace(b'.', os.path.sep)
        mask = os.path.join(path, mask)
        for fnm in package.__loader__._files.iterkeys():
            if fnmatch.fnmatchcase(fnm, mask):
                yield os.path.splitext(fnm)[0].replace(os.path.sep, b'.')

    else:
        path = package.__path__[0]
        for fnm in os.listdir(path):
            if fnmatch.fnmatchcase(fnm, mask):
                yield b'%s.%s' % (package.__name__, os.path.splitext(fnm)[0])

    return


def get_tests(package, mask, verbosity, exclude=()):
    tests = []
    skipped = []
    for modname in find_package_modules(package, mask):
        if modname.split(b'.')[-1] in exclude:
            skipped.append(modname)
            if verbosity > 1:
                print >> sys.stderr, b'Skipped %s: excluded' % modname
            continue
        try:
            mod = __import__(modname, globals(), locals(), [b'*'])
        except (ResourceDenied, unittest.SkipTest) as detail:
            skipped.append(modname)
            if verbosity > 1:
                print >> sys.stderr, b'Skipped %s: %s' % (modname, detail)
            continue

        for name in dir(mod):
            if name.startswith(b'_'):
                continue
            o = getattr(mod, name)
            if type(o) is type(unittest.TestCase) and issubclass(o, unittest.TestCase):
                tests.append(o)

    return (
     skipped, tests)


def usage():
    print __doc__
    return 1


def test_with_refcounts(runner, verbosity, testcase):
    import gc, ctypes
    ptc = ctypes._pointer_type_cache.copy()
    cfc = ctypes._c_functype_cache.copy()
    wfc = ctypes._win_functype_cache.copy()

    def cleanup():
        ctypes._pointer_type_cache = ptc.copy()
        ctypes._c_functype_cache = cfc.copy()
        ctypes._win_functype_cache = wfc.copy()
        gc.collect()
        return

    test = unittest.makeSuite(testcase)
    for i in range(5):
        rc = sys.gettotalrefcount()
        runner.run(test)
        cleanup()

    COUNT = 5
    refcounts = [None] * COUNT
    for i in range(COUNT):
        rc = sys.gettotalrefcount()
        runner.run(test)
        cleanup()
        refcounts[i] = sys.gettotalrefcount() - rc

    if filter(None, refcounts):
        print b'%s leaks:\n\t' % testcase, refcounts
    elif verbosity:
        print b'%s: ok.' % testcase
    return


class TestRunner(unittest.TextTestRunner):

    def run(self, test, skipped):
        result = self._makeResult()
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()
        self.stream.writeln(result.separator2)
        run = result.testsRun
        if _unavail:
            requested = _unavail.keys()
            requested.sort()
            self.stream.writeln(b'Ran %d test%s in %.3fs (%s module%s skipped)' % (
             run, run != 1 and b's' or b'', timeTaken,
             len(skipped),
             len(skipped) != 1 and b's' or b''))
            self.stream.writeln(b'Unavailable resources: %s' % (b', ').join(requested))
        else:
            self.stream.writeln(b'Ran %d test%s in %.3fs' % (
             run, run != 1 and b's' or b'', timeTaken))
        self.stream.writeln()
        if not result.wasSuccessful():
            self.stream.write(b'FAILED (')
            failed, errored = map(len, (result.failures, result.errors))
            if failed:
                self.stream.write(b'failures=%d' % failed)
            if errored:
                if failed:
                    self.stream.write(b', ')
                self.stream.write(b'errors=%d' % errored)
            self.stream.writeln(b')')
        else:
            self.stream.writeln(b'OK')
        return result


def main(*packages):
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'rqvu:x:')
    except getopt.error:
        return usage()

    verbosity = 1
    search_leaks = False
    exclude = []
    for flag, value in opts:
        if flag == b'-q':
            verbosity -= 1
        elif flag == b'-v':
            verbosity += 1
        elif flag == b'-r':
            try:
                sys.gettotalrefcount
            except AttributeError:
                print >> sys.stderr, b'-r flag requires Python debug build'
                return -1

            search_leaks = True
        elif flag == b'-u':
            use_resources.extend(value.split(b','))
        elif flag == b'-x':
            exclude.extend(value.split(b','))

    mask = b'test_*.py'
    if args:
        mask = args[0]
    for package in packages:
        run_tests(package, mask, verbosity, search_leaks, exclude)

    return


def run_tests(package, mask, verbosity, search_leaks, exclude):
    skipped, testcases = get_tests(package, mask, verbosity, exclude)
    runner = TestRunner(verbosity=verbosity)
    suites = [unittest.makeSuite(o) for o in testcases]
    suite = unittest.TestSuite(suites)
    result = runner.run(suite, skipped)
    if search_leaks:
        runner = BasicTestRunner()
        for t in testcases:
            test_with_refcounts(runner, verbosity, t)

    return bool(result.errors)


class BasicTestRunner:

    def run(self, test):
        result = unittest.TestResult()
        test(result)
        return result
