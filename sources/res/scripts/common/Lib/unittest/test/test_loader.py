import sys, types, unittest

class Test_TestLoader(unittest.TestCase):

    def test_loadTestsFromTestCase(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        tests = unittest.TestSuite([Foo(b'test_1'), Foo(b'test_2')])
        loader = unittest.TestLoader()
        self.assertEqual(loader.loadTestsFromTestCase(Foo), tests)
        return

    def test_loadTestsFromTestCase__no_matches(self):

        class Foo(unittest.TestCase):

            def foo_bar(self):
                return

        empty_suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        self.assertEqual(loader.loadTestsFromTestCase(Foo), empty_suite)
        return

    def test_loadTestsFromTestCase__TestSuite_subclass(self):

        class NotATestCase(unittest.TestSuite):
            pass

        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromTestCase(NotATestCase)
        except TypeError:
            pass
        else:
            self.fail(b'Should raise TypeError')

        return

    def test_loadTestsFromTestCase__default_method_name(self):

        class Foo(unittest.TestCase):

            def runTest(self):
                return

        loader = unittest.TestLoader()
        self.assertFalse((b'runTest').startswith(loader.testMethodPrefix))
        suite = loader.loadTestsFromTestCase(Foo)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [Foo(b'runTest')])
        return

    def test_loadTestsFromModule__TestCase_subclass(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, loader.suiteClass)
        expected = [
         loader.suiteClass([MyTestCase(b'test')])]
        self.assertEqual(list(suite), expected)
        return

    def test_loadTestsFromModule__no_TestCase_instances(self):
        m = types.ModuleType(b'm')
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [])
        return

    def test_loadTestsFromModule__no_TestCase_tests(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):
            pass

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [loader.suiteClass()])
        return

    def test_loadTestsFromModule__not_a_module(self):

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        class NotAModule(object):
            test_2 = MyTestCase

        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(NotAModule)
        reference = [
         unittest.TestSuite([MyTestCase(b'test')])]
        self.assertEqual(list(suite), reference)
        return

    def test_loadTestsFromModule__load_tests(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        load_tests_args = []

        def load_tests(loader, tests, pattern):
            self.assertIsInstance(tests, unittest.TestSuite)
            load_tests_args.extend((loader, tests, pattern))
            return tests

        m.load_tests = load_tests
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, unittest.TestSuite)
        self.assertEqual(load_tests_args, [loader, suite, None])
        load_tests_args = []
        suite = loader.loadTestsFromModule(m, use_load_tests=False)
        self.assertEqual(load_tests_args, [])
        return

    def test_loadTestsFromModule__faulty_load_tests(self):
        m = types.ModuleType(b'm')

        def load_tests(loader, tests, pattern):
            raise TypeError(b'some failure')
            return

        m.load_tests = load_tests
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(m)
        self.assertIsInstance(suite, unittest.TestSuite)
        self.assertEqual(suite.countTestCases(), 1)
        test = list(suite)[0]
        self.assertRaisesRegexp(TypeError, b'some failure', test.m)
        return

    def test_loadTestsFromName__empty_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'')
        except ValueError as e:
            self.assertEqual(str(e), b'Empty module name')
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise ValueError')

        return

    def test_loadTestsFromName__malformed_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'abc () //')
        except ValueError:
            pass
        except ImportError:
            pass
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise ValueError')

        return

    def test_loadTestsFromName__unknown_module_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'sdasfasfasdf')
        except ImportError as e:
            self.assertEqual(str(e), b'No module named sdasfasfasdf')
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise ImportError')

        return

    def test_loadTestsFromName__unknown_attr_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'unittest.sdasfasfasdf')
        except AttributeError as e:
            self.assertEqual(str(e), b"'module' object has no attribute 'sdasfasfasdf'")
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise AttributeError')

        return

    def test_loadTestsFromName__relative_unknown_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'sdasfasfasdf', unittest)
        except AttributeError as e:
            self.assertEqual(str(e), b"'module' object has no attribute 'sdasfasfasdf'")
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise AttributeError')

        return

    def test_loadTestsFromName__relative_empty_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'', unittest)
        except AttributeError:
            pass
        else:
            self.fail(b'Failed to raise AttributeError')

        return

    def test_loadTestsFromName__relative_malformed_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'abc () //', unittest)
        except ValueError:
            pass
        except AttributeError:
            pass
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise ValueError')

        return

    def test_loadTestsFromName__relative_not_a_module(self):

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        class NotAModule(object):
            test_2 = MyTestCase

        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(b'test_2', NotAModule)
        reference = [
         MyTestCase(b'test')]
        self.assertEqual(list(suite), reference)
        return

    def test_loadTestsFromName__relative_bad_object(self):
        m = types.ModuleType(b'm')
        m.testcase_1 = object()
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'testcase_1', m)
        except TypeError:
            pass
        else:
            self.fail(b'Should have raised TypeError')

        return

    def test_loadTestsFromName__relative_TestCase_subclass(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(b'testcase_1', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [MyTestCase(b'test')])
        return

    def test_loadTestsFromName__relative_TestSuite(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testsuite = unittest.TestSuite([MyTestCase(b'test')])
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(b'testsuite', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [MyTestCase(b'test')])
        return

    def test_loadTestsFromName__relative_testmethod(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(b'testcase_1.test', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [MyTestCase(b'test')])
        return

    def test_loadTestsFromName__relative_invalid_testmethod(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'testcase_1.testfoo', m)
        except AttributeError as e:
            self.assertEqual(str(e), b"type object 'MyTestCase' has no attribute 'testfoo'")
        else:
            self.fail(b'Failed to raise AttributeError')

        return

    def test_loadTestsFromName__callable__TestSuite(self):
        m = types.ModuleType(b'm')
        testcase_1 = unittest.FunctionTestCase((lambda : None))
        testcase_2 = unittest.FunctionTestCase((lambda : None))

        def return_TestSuite():
            return unittest.TestSuite([testcase_1, testcase_2])

        m.return_TestSuite = return_TestSuite
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(b'return_TestSuite', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [testcase_1, testcase_2])
        return

    def test_loadTestsFromName__callable__TestCase_instance(self):
        m = types.ModuleType(b'm')
        testcase_1 = unittest.FunctionTestCase((lambda : None))

        def return_TestCase():
            return testcase_1

        m.return_TestCase = return_TestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromName(b'return_TestCase', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [testcase_1])
        return

    def test_loadTestsFromName__callable__TestCase_instance_ProperSuiteClass(self):

        class SubTestSuite(unittest.TestSuite):
            pass

        m = types.ModuleType(b'm')
        testcase_1 = unittest.FunctionTestCase((lambda : None))

        def return_TestCase():
            return testcase_1

        m.return_TestCase = return_TestCase
        loader = unittest.TestLoader()
        loader.suiteClass = SubTestSuite
        suite = loader.loadTestsFromName(b'return_TestCase', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [testcase_1])
        return

    def test_loadTestsFromName__relative_testmethod_ProperSuiteClass(self):

        class SubTestSuite(unittest.TestSuite):
            pass

        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        loader.suiteClass = SubTestSuite
        suite = loader.loadTestsFromName(b'testcase_1.test', m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [MyTestCase(b'test')])
        return

    def test_loadTestsFromName__callable__wrong_type(self):
        m = types.ModuleType(b'm')

        def return_wrong():
            return 6

        m.return_wrong = return_wrong
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromName(b'return_wrong', m)
        except TypeError:
            pass
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise TypeError')

        return

    def test_loadTestsFromName__module_not_loaded(self):
        module_name = b'unittest.test.dummy'
        sys.modules.pop(module_name, None)
        loader = unittest.TestLoader()
        try:
            suite = loader.loadTestsFromName(module_name)
            self.assertIsInstance(suite, loader.suiteClass)
            self.assertEqual(list(suite), [])
            self.assertIn(module_name, sys.modules)
        finally:
            if module_name in sys.modules:
                del sys.modules[module_name]

        return

    def test_loadTestsFromNames__empty_name_list(self):
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([])
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [])
        return

    def test_loadTestsFromNames__relative_empty_name_list(self):
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([], unittest)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [])
        return

    def test_loadTestsFromNames__empty_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b''])
        except ValueError as e:
            self.assertEqual(str(e), b'Empty module name')
        else:
            self.fail(b'TestLoader.loadTestsFromNames failed to raise ValueError')

        return

    def test_loadTestsFromNames__malformed_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'abc () //'])
        except ValueError:
            pass
        except ImportError:
            pass
        else:
            self.fail(b'TestLoader.loadTestsFromNames failed to raise ValueError')

        return

    def test_loadTestsFromNames__unknown_module_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'sdasfasfasdf'])
        except ImportError as e:
            self.assertEqual(str(e), b'No module named sdasfasfasdf')
        else:
            self.fail(b'TestLoader.loadTestsFromNames failed to raise ImportError')

        return

    def test_loadTestsFromNames__unknown_attr_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'unittest.sdasfasfasdf', b'unittest'])
        except AttributeError as e:
            self.assertEqual(str(e), b"'module' object has no attribute 'sdasfasfasdf'")
        else:
            self.fail(b'TestLoader.loadTestsFromNames failed to raise AttributeError')

        return

    def test_loadTestsFromNames__unknown_name_relative_1(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'sdasfasfasdf'], unittest)
        except AttributeError as e:
            self.assertEqual(str(e), b"'module' object has no attribute 'sdasfasfasdf'")
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise AttributeError')

        return

    def test_loadTestsFromNames__unknown_name_relative_2(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'TestCase', b'sdasfasfasdf'], unittest)
        except AttributeError as e:
            self.assertEqual(str(e), b"'module' object has no attribute 'sdasfasfasdf'")
        else:
            self.fail(b'TestLoader.loadTestsFromName failed to raise AttributeError')

        return

    def test_loadTestsFromNames__relative_empty_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b''], unittest)
        except AttributeError:
            pass
        else:
            self.fail(b'Failed to raise ValueError')

        return

    def test_loadTestsFromNames__relative_malformed_name(self):
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'abc () //'], unittest)
        except AttributeError:
            pass
        except ValueError:
            pass
        else:
            self.fail(b'TestLoader.loadTestsFromNames failed to raise ValueError')

        return

    def test_loadTestsFromNames__relative_not_a_module(self):

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        class NotAModule(object):
            test_2 = MyTestCase

        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'test_2'], NotAModule)
        reference = [
         unittest.TestSuite([MyTestCase(b'test')])]
        self.assertEqual(list(suite), reference)
        return

    def test_loadTestsFromNames__relative_bad_object(self):
        m = types.ModuleType(b'm')
        m.testcase_1 = object()
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'testcase_1'], m)
        except TypeError:
            pass
        else:
            self.fail(b'Should have raised TypeError')

        return

    def test_loadTestsFromNames__relative_TestCase_subclass(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'testcase_1'], m)
        self.assertIsInstance(suite, loader.suiteClass)
        expected = loader.suiteClass([MyTestCase(b'test')])
        self.assertEqual(list(suite), [expected])
        return

    def test_loadTestsFromNames__relative_TestSuite(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testsuite = unittest.TestSuite([MyTestCase(b'test')])
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'testsuite'], m)
        self.assertIsInstance(suite, loader.suiteClass)
        self.assertEqual(list(suite), [m.testsuite])
        return

    def test_loadTestsFromNames__relative_testmethod(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'testcase_1.test'], m)
        self.assertIsInstance(suite, loader.suiteClass)
        ref_suite = unittest.TestSuite([MyTestCase(b'test')])
        self.assertEqual(list(suite), [ref_suite])
        return

    def test_loadTestsFromNames__relative_invalid_testmethod(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):

            def test(self):
                return

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'testcase_1.testfoo'], m)
        except AttributeError as e:
            self.assertEqual(str(e), b"type object 'MyTestCase' has no attribute 'testfoo'")
        else:
            self.fail(b'Failed to raise AttributeError')

        return

    def test_loadTestsFromNames__callable__TestSuite(self):
        m = types.ModuleType(b'm')
        testcase_1 = unittest.FunctionTestCase((lambda : None))
        testcase_2 = unittest.FunctionTestCase((lambda : None))

        def return_TestSuite():
            return unittest.TestSuite([testcase_1, testcase_2])

        m.return_TestSuite = return_TestSuite
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'return_TestSuite'], m)
        self.assertIsInstance(suite, loader.suiteClass)
        expected = unittest.TestSuite([testcase_1, testcase_2])
        self.assertEqual(list(suite), [expected])
        return

    def test_loadTestsFromNames__callable__TestCase_instance(self):
        m = types.ModuleType(b'm')
        testcase_1 = unittest.FunctionTestCase((lambda : None))

        def return_TestCase():
            return testcase_1

        m.return_TestCase = return_TestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'return_TestCase'], m)
        self.assertIsInstance(suite, loader.suiteClass)
        ref_suite = unittest.TestSuite([testcase_1])
        self.assertEqual(list(suite), [ref_suite])
        return

    def test_loadTestsFromNames__callable__call_staticmethod(self):
        m = types.ModuleType(b'm')

        class Test1(unittest.TestCase):

            def test(self):
                return

        testcase_1 = Test1(b'test')

        class Foo(unittest.TestCase):

            @staticmethod
            def foo():
                return testcase_1

        m.Foo = Foo
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'Foo.foo'], m)
        self.assertIsInstance(suite, loader.suiteClass)
        ref_suite = unittest.TestSuite([testcase_1])
        self.assertEqual(list(suite), [ref_suite])
        return

    def test_loadTestsFromNames__callable__wrong_type(self):
        m = types.ModuleType(b'm')

        def return_wrong():
            return 6

        m.return_wrong = return_wrong
        loader = unittest.TestLoader()
        try:
            loader.loadTestsFromNames([b'return_wrong'], m)
        except TypeError:
            pass
        else:
            self.fail(b'TestLoader.loadTestsFromNames failed to raise TypeError')

        return

    def test_loadTestsFromNames__module_not_loaded(self):
        module_name = b'unittest.test.dummy'
        sys.modules.pop(module_name, None)
        loader = unittest.TestLoader()
        try:
            suite = loader.loadTestsFromNames([module_name])
            self.assertIsInstance(suite, loader.suiteClass)
            self.assertEqual(list(suite), [unittest.TestSuite()])
            self.assertIn(module_name, sys.modules)
        finally:
            if module_name in sys.modules:
                del sys.modules[module_name]

        return

    def test_getTestCaseNames(self):

        class Test(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foobar(self):
                return

        loader = unittest.TestLoader()
        self.assertEqual(loader.getTestCaseNames(Test), [b'test_1', b'test_2'])
        return

    def test_getTestCaseNames__no_tests(self):

        class Test(unittest.TestCase):

            def foobar(self):
                return

        loader = unittest.TestLoader()
        self.assertEqual(loader.getTestCaseNames(Test), [])
        return

    def test_getTestCaseNames__not_a_TestCase(self):

        class BadCase(int):

            def test_foo(self):
                return

        loader = unittest.TestLoader()
        names = loader.getTestCaseNames(BadCase)
        self.assertEqual(names, [b'test_foo'])
        return

    def test_getTestCaseNames__inheritance(self):

        class TestP(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foobar(self):
                return

        class TestC(TestP):

            def test_1(self):
                return

            def test_3(self):
                return

        loader = unittest.TestLoader()
        names = [
         b'test_1', b'test_2', b'test_3']
        self.assertEqual(loader.getTestCaseNames(TestC), names)
        return

    def test_testMethodPrefix__loadTestsFromTestCase(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        tests_1 = unittest.TestSuite([Foo(b'foo_bar')])
        tests_2 = unittest.TestSuite([Foo(b'test_1'), Foo(b'test_2')])
        loader = unittest.TestLoader()
        loader.testMethodPrefix = b'foo'
        self.assertEqual(loader.loadTestsFromTestCase(Foo), tests_1)
        loader.testMethodPrefix = b'test'
        self.assertEqual(loader.loadTestsFromTestCase(Foo), tests_2)
        return

    def test_testMethodPrefix__loadTestsFromModule(self):
        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        m.Foo = Foo
        tests_1 = [
         unittest.TestSuite([Foo(b'foo_bar')])]
        tests_2 = [unittest.TestSuite([Foo(b'test_1'), Foo(b'test_2')])]
        loader = unittest.TestLoader()
        loader.testMethodPrefix = b'foo'
        self.assertEqual(list(loader.loadTestsFromModule(m)), tests_1)
        loader.testMethodPrefix = b'test'
        self.assertEqual(list(loader.loadTestsFromModule(m)), tests_2)
        return

    def test_testMethodPrefix__loadTestsFromName(self):
        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        m.Foo = Foo
        tests_1 = unittest.TestSuite([Foo(b'foo_bar')])
        tests_2 = unittest.TestSuite([Foo(b'test_1'), Foo(b'test_2')])
        loader = unittest.TestLoader()
        loader.testMethodPrefix = b'foo'
        self.assertEqual(loader.loadTestsFromName(b'Foo', m), tests_1)
        loader.testMethodPrefix = b'test'
        self.assertEqual(loader.loadTestsFromName(b'Foo', m), tests_2)
        return

    def test_testMethodPrefix__loadTestsFromNames(self):
        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        m.Foo = Foo
        tests_1 = unittest.TestSuite([unittest.TestSuite([Foo(b'foo_bar')])])
        tests_2 = unittest.TestSuite([Foo(b'test_1'), Foo(b'test_2')])
        tests_2 = unittest.TestSuite([tests_2])
        loader = unittest.TestLoader()
        loader.testMethodPrefix = b'foo'
        self.assertEqual(loader.loadTestsFromNames([b'Foo'], m), tests_1)
        loader.testMethodPrefix = b'test'
        self.assertEqual(loader.loadTestsFromNames([b'Foo'], m), tests_2)
        return

    def test_testMethodPrefix__default_value(self):
        loader = unittest.TestLoader()
        self.assertTrue(loader.testMethodPrefix == b'test')
        return

    def test_sortTestMethodsUsing__loadTestsFromTestCase(self):

        def reversed_cmp(x, y):
            return -cmp(x, y)

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

        loader = unittest.TestLoader()
        loader.sortTestMethodsUsing = reversed_cmp
        tests = loader.suiteClass([Foo(b'test_2'), Foo(b'test_1')])
        self.assertEqual(loader.loadTestsFromTestCase(Foo), tests)
        return

    def test_sortTestMethodsUsing__loadTestsFromModule(self):

        def reversed_cmp(x, y):
            return -cmp(x, y)

        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

        m.Foo = Foo
        loader = unittest.TestLoader()
        loader.sortTestMethodsUsing = reversed_cmp
        tests = [
         loader.suiteClass([Foo(b'test_2'), Foo(b'test_1')])]
        self.assertEqual(list(loader.loadTestsFromModule(m)), tests)
        return

    def test_sortTestMethodsUsing__loadTestsFromName(self):

        def reversed_cmp(x, y):
            return -cmp(x, y)

        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

        m.Foo = Foo
        loader = unittest.TestLoader()
        loader.sortTestMethodsUsing = reversed_cmp
        tests = loader.suiteClass([Foo(b'test_2'), Foo(b'test_1')])
        self.assertEqual(loader.loadTestsFromName(b'Foo', m), tests)
        return

    def test_sortTestMethodsUsing__loadTestsFromNames(self):

        def reversed_cmp(x, y):
            return -cmp(x, y)

        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

        m.Foo = Foo
        loader = unittest.TestLoader()
        loader.sortTestMethodsUsing = reversed_cmp
        tests = [
         loader.suiteClass([Foo(b'test_2'), Foo(b'test_1')])]
        self.assertEqual(list(loader.loadTestsFromNames([b'Foo'], m)), tests)
        return

    def test_sortTestMethodsUsing__getTestCaseNames(self):

        def reversed_cmp(x, y):
            return -cmp(x, y)

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

        loader = unittest.TestLoader()
        loader.sortTestMethodsUsing = reversed_cmp
        test_names = [
         b'test_2', b'test_1']
        self.assertEqual(loader.getTestCaseNames(Foo), test_names)
        return

    def test_sortTestMethodsUsing__default_value(self):
        loader = unittest.TestLoader()
        self.assertTrue(loader.sortTestMethodsUsing is cmp)
        return

    def test_sortTestMethodsUsing__None(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

        loader = unittest.TestLoader()
        loader.sortTestMethodsUsing = None
        test_names = [
         b'test_2', b'test_1']
        self.assertEqual(set(loader.getTestCaseNames(Foo)), set(test_names))
        return

    def test_suiteClass__loadTestsFromTestCase(self):

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        tests = [
         Foo(b'test_1'), Foo(b'test_2')]
        loader = unittest.TestLoader()
        loader.suiteClass = list
        self.assertEqual(loader.loadTestsFromTestCase(Foo), tests)
        return

    def test_suiteClass__loadTestsFromModule(self):
        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        m.Foo = Foo
        tests = [
         [
          Foo(b'test_1'), Foo(b'test_2')]]
        loader = unittest.TestLoader()
        loader.suiteClass = list
        self.assertEqual(loader.loadTestsFromModule(m), tests)
        return

    def test_suiteClass__loadTestsFromName(self):
        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        m.Foo = Foo
        tests = [
         Foo(b'test_1'), Foo(b'test_2')]
        loader = unittest.TestLoader()
        loader.suiteClass = list
        self.assertEqual(loader.loadTestsFromName(b'Foo', m), tests)
        return

    def test_suiteClass__loadTestsFromNames(self):
        m = types.ModuleType(b'm')

        class Foo(unittest.TestCase):

            def test_1(self):
                return

            def test_2(self):
                return

            def foo_bar(self):
                return

        m.Foo = Foo
        tests = [
         [
          Foo(b'test_1'), Foo(b'test_2')]]
        loader = unittest.TestLoader()
        loader.suiteClass = list
        self.assertEqual(loader.loadTestsFromNames([b'Foo'], m), tests)
        return

    def test_suiteClass__default_value(self):
        loader = unittest.TestLoader()
        self.assertIs(loader.suiteClass, unittest.TestSuite)
        return

    def test_loadTestsFromName__function_with_different_name_than_method(self):
        m = types.ModuleType(b'm')

        class MyTestCase(unittest.TestCase):
            test = lambda : 1

        m.testcase_1 = MyTestCase
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromNames([b'testcase_1.test'], m)
        self.assertIsInstance(suite, loader.suiteClass)
        ref_suite = unittest.TestSuite([MyTestCase(b'test')])
        self.assertEqual(list(suite), [ref_suite])
        return


if __name__ == b'__main__':
    unittest.main()
