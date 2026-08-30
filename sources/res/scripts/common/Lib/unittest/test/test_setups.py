import sys
from cStringIO import StringIO
import unittest

def resultFactory(*_):
    return unittest.TestResult()


class TestSetups(unittest.TestCase):

    def getRunner(self):
        return unittest.TextTestRunner(resultclass=resultFactory, stream=StringIO())

    def runTests(self, *cases):
        suite = unittest.TestSuite()
        for case in cases:
            tests = unittest.defaultTestLoader.loadTestsFromTestCase(case)
            suite.addTests(tests)

        runner = self.getRunner()
        realSuite = unittest.TestSuite()
        realSuite.addTest(suite)
        suite.addTest(unittest.TestSuite())
        realSuite.addTest(unittest.TestSuite())
        return runner.run(realSuite)

    def test_setup_class(self):

        class Test(unittest.TestCase):
            setUpCalled = 0

            @classmethod
            def setUpClass(cls):
                Test.setUpCalled += 1
                unittest.TestCase.setUpClass()
                return

            def test_one(self):
                return

            def test_two(self):
                return

        result = self.runTests(Test)
        self.assertEqual(Test.setUpCalled, 1)
        self.assertEqual(result.testsRun, 2)
        self.assertEqual(len(result.errors), 0)
        return

    def test_teardown_class(self):

        class Test(unittest.TestCase):
            tearDownCalled = 0

            @classmethod
            def tearDownClass(cls):
                Test.tearDownCalled += 1
                unittest.TestCase.tearDownClass()
                return

            def test_one(self):
                return

            def test_two(self):
                return

        result = self.runTests(Test)
        self.assertEqual(Test.tearDownCalled, 1)
        self.assertEqual(result.testsRun, 2)
        self.assertEqual(len(result.errors), 0)
        return

    def test_teardown_class_two_classes(self):

        class Test(unittest.TestCase):
            tearDownCalled = 0

            @classmethod
            def tearDownClass(cls):
                Test.tearDownCalled += 1
                unittest.TestCase.tearDownClass()
                return

            def test_one(self):
                return

            def test_two(self):
                return

        class Test2(unittest.TestCase):
            tearDownCalled = 0

            @classmethod
            def tearDownClass(cls):
                Test2.tearDownCalled += 1
                unittest.TestCase.tearDownClass()
                return

            def test_one(self):
                return

            def test_two(self):
                return

        result = self.runTests(Test, Test2)
        self.assertEqual(Test.tearDownCalled, 1)
        self.assertEqual(Test2.tearDownCalled, 1)
        self.assertEqual(result.testsRun, 4)
        self.assertEqual(len(result.errors), 0)
        return

    def test_error_in_setupclass(self):

        class BrokenTest(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                raise TypeError(b'foo')
                return

            def test_one(self):
                return

            def test_two(self):
                return

        result = self.runTests(BrokenTest)
        self.assertEqual(result.testsRun, 0)
        self.assertEqual(len(result.errors), 1)
        error, _ = result.errors[0]
        self.assertEqual(str(error), b'setUpClass (%s.BrokenTest)' % __name__)
        return

    def test_error_in_teardown_class(self):

        class Test(unittest.TestCase):
            tornDown = 0

            @classmethod
            def tearDownClass(cls):
                Test.tornDown += 1
                raise TypeError(b'foo')
                return

            def test_one(self):
                return

            def test_two(self):
                return

        class Test2(unittest.TestCase):
            tornDown = 0

            @classmethod
            def tearDownClass(cls):
                Test2.tornDown += 1
                raise TypeError(b'foo')
                return

            def test_one(self):
                return

            def test_two(self):
                return

        result = self.runTests(Test, Test2)
        self.assertEqual(result.testsRun, 4)
        self.assertEqual(len(result.errors), 2)
        self.assertEqual(Test.tornDown, 1)
        self.assertEqual(Test2.tornDown, 1)
        error, _ = result.errors[0]
        self.assertEqual(str(error), b'tearDownClass (%s.Test)' % __name__)
        return

    def test_class_not_torndown_when_setup_fails(self):

        class Test(unittest.TestCase):
            tornDown = False

            @classmethod
            def setUpClass(cls):
                raise TypeError
                return

            @classmethod
            def tearDownClass(cls):
                Test.tornDown = True
                raise TypeError(b'foo')
                return

            def test_one(self):
                return

        self.runTests(Test)
        self.assertFalse(Test.tornDown)
        return

    def test_class_not_setup_or_torndown_when_skipped(self):

        class Test(unittest.TestCase):
            classSetUp = False
            tornDown = False

            @classmethod
            def setUpClass(cls):
                Test.classSetUp = True
                return

            @classmethod
            def tearDownClass(cls):
                Test.tornDown = True
                return

            def test_one(self):
                return

        Test = unittest.skip(b'hop')(Test)
        self.runTests(Test)
        self.assertFalse(Test.classSetUp)
        self.assertFalse(Test.tornDown)
        return

    def test_setup_teardown_order_with_pathological_suite(self):
        results = []

        class Module1(object):

            @staticmethod
            def setUpModule():
                results.append(b'Module1.setUpModule')
                return

            @staticmethod
            def tearDownModule():
                results.append(b'Module1.tearDownModule')
                return

        class Module2(object):

            @staticmethod
            def setUpModule():
                results.append(b'Module2.setUpModule')
                return

            @staticmethod
            def tearDownModule():
                results.append(b'Module2.tearDownModule')
                return

        class Test1(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                results.append(b'setup 1')
                return

            @classmethod
            def tearDownClass(cls):
                results.append(b'teardown 1')
                return

            def testOne(self):
                results.append(b'Test1.testOne')
                return

            def testTwo(self):
                results.append(b'Test1.testTwo')
                return

        class Test2(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                results.append(b'setup 2')
                return

            @classmethod
            def tearDownClass(cls):
                results.append(b'teardown 2')
                return

            def testOne(self):
                results.append(b'Test2.testOne')
                return

            def testTwo(self):
                results.append(b'Test2.testTwo')
                return

        class Test3(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                results.append(b'setup 3')
                return

            @classmethod
            def tearDownClass(cls):
                results.append(b'teardown 3')
                return

            def testOne(self):
                results.append(b'Test3.testOne')
                return

            def testTwo(self):
                results.append(b'Test3.testTwo')
                return

        Test1.__module__ = Test2.__module__ = b'Module'
        Test3.__module__ = b'Module2'
        sys.modules[b'Module'] = Module1
        sys.modules[b'Module2'] = Module2
        first = unittest.TestSuite((Test1(b'testOne'),))
        second = unittest.TestSuite((Test1(b'testTwo'),))
        third = unittest.TestSuite((Test2(b'testOne'),))
        fourth = unittest.TestSuite((Test2(b'testTwo'),))
        fifth = unittest.TestSuite((Test3(b'testOne'),))
        sixth = unittest.TestSuite((Test3(b'testTwo'),))
        suite = unittest.TestSuite((first, second, third, fourth, fifth, sixth))
        runner = self.getRunner()
        result = runner.run(suite)
        self.assertEqual(result.testsRun, 6)
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(results, [
         16, 17, 
         18, 19, 20, 
         21, 
         22, 23, 
         24, 25, 
         26, 
         27, 
         28, 29, 
         30, 31])
        return

    def test_setup_module(self):

        class Module(object):
            moduleSetup = 0

            @staticmethod
            def setUpModule():
                Module.moduleSetup += 1
                return

        class Test(unittest.TestCase):

            def test_one(self):
                return

            def test_two(self):
                return

        Test.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        result = self.runTests(Test)
        self.assertEqual(Module.moduleSetup, 1)
        self.assertEqual(result.testsRun, 2)
        self.assertEqual(len(result.errors), 0)
        return

    def test_error_in_setup_module(self):

        class Module(object):
            moduleSetup = 0
            moduleTornDown = 0

            @staticmethod
            def setUpModule():
                Module.moduleSetup += 1
                raise TypeError(b'foo')
                return

            @staticmethod
            def tearDownModule():
                Module.moduleTornDown += 1
                return

        class Test(unittest.TestCase):
            classSetUp = False
            classTornDown = False

            @classmethod
            def setUpClass(cls):
                Test.classSetUp = True
                return

            @classmethod
            def tearDownClass(cls):
                Test.classTornDown = True
                return

            def test_one(self):
                return

            def test_two(self):
                return

        class Test2(unittest.TestCase):

            def test_one(self):
                return

            def test_two(self):
                return

        Test.__module__ = b'Module'
        Test2.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        result = self.runTests(Test, Test2)
        self.assertEqual(Module.moduleSetup, 1)
        self.assertEqual(Module.moduleTornDown, 0)
        self.assertEqual(result.testsRun, 0)
        self.assertFalse(Test.classSetUp)
        self.assertFalse(Test.classTornDown)
        self.assertEqual(len(result.errors), 1)
        error, _ = result.errors[0]
        self.assertEqual(str(error), b'setUpModule (Module)')
        return

    def test_testcase_with_missing_module(self):

        class Test(unittest.TestCase):

            def test_one(self):
                return

            def test_two(self):
                return

        Test.__module__ = b'Module'
        sys.modules.pop(b'Module', None)
        result = self.runTests(Test)
        self.assertEqual(result.testsRun, 2)
        return

    def test_teardown_module(self):

        class Module(object):
            moduleTornDown = 0

            @staticmethod
            def tearDownModule():
                Module.moduleTornDown += 1
                return

        class Test(unittest.TestCase):

            def test_one(self):
                return

            def test_two(self):
                return

        Test.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        result = self.runTests(Test)
        self.assertEqual(Module.moduleTornDown, 1)
        self.assertEqual(result.testsRun, 2)
        self.assertEqual(len(result.errors), 0)
        return

    def test_error_in_teardown_module(self):

        class Module(object):
            moduleTornDown = 0

            @staticmethod
            def tearDownModule():
                Module.moduleTornDown += 1
                raise TypeError(b'foo')
                return

        class Test(unittest.TestCase):
            classSetUp = False
            classTornDown = False

            @classmethod
            def setUpClass(cls):
                Test.classSetUp = True
                return

            @classmethod
            def tearDownClass(cls):
                Test.classTornDown = True
                return

            def test_one(self):
                return

            def test_two(self):
                return

        class Test2(unittest.TestCase):

            def test_one(self):
                return

            def test_two(self):
                return

        Test.__module__ = b'Module'
        Test2.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        result = self.runTests(Test, Test2)
        self.assertEqual(Module.moduleTornDown, 1)
        self.assertEqual(result.testsRun, 4)
        self.assertTrue(Test.classSetUp)
        self.assertTrue(Test.classTornDown)
        self.assertEqual(len(result.errors), 1)
        error, _ = result.errors[0]
        self.assertEqual(str(error), b'tearDownModule (Module)')
        return

    def test_skiptest_in_setupclass(self):

        class Test(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                raise unittest.SkipTest(b'foo')
                return

            def test_one(self):
                return

            def test_two(self):
                return

        result = self.runTests(Test)
        self.assertEqual(result.testsRun, 0)
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.skipped), 1)
        skipped = result.skipped[0][0]
        self.assertEqual(str(skipped), b'setUpClass (%s.Test)' % __name__)
        return

    def test_skiptest_in_setupmodule(self):

        class Test(unittest.TestCase):

            def test_one(self):
                return

            def test_two(self):
                return

        class Module(object):

            @staticmethod
            def setUpModule():
                raise unittest.SkipTest(b'foo')
                return

        Test.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        result = self.runTests(Test)
        self.assertEqual(result.testsRun, 0)
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.skipped), 1)
        skipped = result.skipped[0][0]
        self.assertEqual(str(skipped), b'setUpModule (Module)')
        return

    def test_suite_debug_executes_setups_and_teardowns(self):
        ordering = []

        class Module(object):

            @staticmethod
            def setUpModule():
                ordering.append(b'setUpModule')
                return

            @staticmethod
            def tearDownModule():
                ordering.append(b'tearDownModule')
                return

        class Test(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                ordering.append(b'setUpClass')
                return

            @classmethod
            def tearDownClass(cls):
                ordering.append(b'tearDownClass')
                return

            def test_something(self):
                ordering.append(b'test_something')
                return

        Test.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
        suite.debug()
        expectedOrder = [5, 6, 7, 8, 9]
        self.assertEqual(ordering, expectedOrder)
        return

    def test_suite_debug_propagates_exceptions(self):

        class Module(object):

            @staticmethod
            def setUpModule():
                if phase == 0:
                    raise Exception(b'setUpModule')
                return

            @staticmethod
            def tearDownModule():
                if phase == 1:
                    raise Exception(b'tearDownModule')
                return

        class Test(unittest.TestCase):

            @classmethod
            def setUpClass(cls):
                if phase == 2:
                    raise Exception(b'setUpClass')
                return

            @classmethod
            def tearDownClass(cls):
                if phase == 3:
                    raise Exception(b'tearDownClass')
                return

            def test_something(self):
                if phase == 4:
                    raise Exception(b'test_something')
                return

        Test.__module__ = b'Module'
        sys.modules[b'Module'] = Module
        _suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
        suite = unittest.TestSuite()
        suite.addTest(_suite)
        messages = (b'setUpModule', b'tearDownModule', b'setUpClass', b'tearDownClass', b'test_something')
        for phase, msg in enumerate(messages):
            with self.assertRaisesRegexp(Exception, msg):
                suite.debug()

        return


if __name__ == b'__main__':
    unittest.main()
