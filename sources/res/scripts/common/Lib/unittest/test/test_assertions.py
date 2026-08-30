import datetime, unittest

class Test_Assertions(unittest.TestCase):

    def test_AlmostEqual(self):
        self.assertAlmostEqual(1.00000001, 1.0)
        self.assertNotAlmostEqual(1.0000001, 1.0)
        self.assertRaises(self.failureException, self.assertAlmostEqual, 1.0000001, 1.0)
        self.assertRaises(self.failureException, self.assertNotAlmostEqual, 1.00000001, 1.0)
        self.assertAlmostEqual(1.1, 1.0, places=0)
        self.assertRaises(self.failureException, self.assertAlmostEqual, 1.1, 1.0, places=1)
        self.assertAlmostEqual(0, complex(0.1, 0.1), places=0)
        self.assertNotAlmostEqual(0, complex(0.1, 0.1), places=1)
        self.assertRaises(self.failureException, self.assertAlmostEqual, 0, complex(0.1, 0.1), places=1)
        self.assertRaises(self.failureException, self.assertNotAlmostEqual, 0, complex(0.1, 0.1), places=0)
        self.assertAlmostEqual(float(b'inf'), float(b'inf'))
        self.assertRaises(self.failureException, self.assertNotAlmostEqual, float(b'inf'), float(b'inf'))
        return

    def test_AmostEqualWithDelta(self):
        self.assertAlmostEqual(1.1, 1.0, delta=0.5)
        self.assertAlmostEqual(1.0, 1.1, delta=0.5)
        self.assertNotAlmostEqual(1.1, 1.0, delta=0.05)
        self.assertNotAlmostEqual(1.0, 1.1, delta=0.05)
        self.assertAlmostEqual(1.0, 1.0, delta=0.5)
        self.assertRaises(self.failureException, self.assertNotAlmostEqual, 1.0, 1.0, delta=0.5)
        self.assertRaises(self.failureException, self.assertAlmostEqual, 1.1, 1.0, delta=0.05)
        self.assertRaises(self.failureException, self.assertNotAlmostEqual, 1.1, 1.0, delta=0.5)
        self.assertRaises(TypeError, self.assertAlmostEqual, 1.1, 1.0, places=2, delta=2)
        self.assertRaises(TypeError, self.assertNotAlmostEqual, 1.1, 1.0, places=2, delta=2)
        first = datetime.datetime.now()
        second = first + datetime.timedelta(seconds=10)
        self.assertAlmostEqual(first, second, delta=datetime.timedelta(seconds=20))
        self.assertNotAlmostEqual(first, second, delta=datetime.timedelta(seconds=5))
        return

    def test_assertRaises(self):

        def _raise(e):
            raise e
            return

        self.assertRaises(KeyError, _raise, KeyError)
        self.assertRaises(KeyError, _raise, KeyError(b'key'))
        try:
            self.assertRaises(KeyError, (lambda : None))
        except self.failureException as e:
            self.assertIn(b'KeyError not raised', e.args)
        else:
            self.fail(b"assertRaises() didn't fail")

        try:
            self.assertRaises(KeyError, _raise, ValueError)
        except ValueError:
            pass
        else:
            self.fail(b"assertRaises() didn't let exception pass through")

        with self.assertRaises(KeyError) as cm:
            try:
                raise KeyError
            except Exception as e:
                raise

        self.assertIs(cm.exception, e)
        with self.assertRaises(KeyError):
            raise KeyError(b'key')
        try:
            with self.assertRaises(KeyError):
                pass
        except self.failureException as e:
            self.assertIn(b'KeyError not raised', e.args)
        else:
            self.fail(b"assertRaises() didn't fail")

        try:
            with self.assertRaises(KeyError):
                raise ValueError
        except ValueError:
            pass
        else:
            self.fail(b"assertRaises() didn't let exception pass through")

        return

    def testAssertNotRegexpMatches(self):
        self.assertNotRegexpMatches(b'Ala ma kota', b'r+')
        try:
            self.assertNotRegexpMatches(b'Ala ma kota', b'k.t', b'Message')
        except self.failureException as e:
            self.assertIn(b"'kot'", e.args[0])
            self.assertIn(b'Message', e.args[0])
        else:
            self.fail(b'assertNotRegexpMatches should have failed.')

        return


class TestLongMessage(unittest.TestCase):

    def setUp(self):

        class TestableTestFalse(unittest.TestCase):
            longMessage = False
            failureException = self.failureException

            def testTest(self):
                return

        class TestableTestTrue(unittest.TestCase):
            longMessage = True
            failureException = self.failureException

            def testTest(self):
                return

        self.testableTrue = TestableTestTrue(b'testTest')
        self.testableFalse = TestableTestFalse(b'testTest')
        return

    def testDefault(self):
        self.assertFalse(unittest.TestCase.longMessage)
        return

    def test_formatMsg(self):
        self.assertEqual(self.testableFalse._formatMessage(None, b'foo'), b'foo')
        self.assertEqual(self.testableFalse._formatMessage(b'foo', b'bar'), b'foo')
        self.assertEqual(self.testableTrue._formatMessage(None, b'foo'), b'foo')
        self.assertEqual(self.testableTrue._formatMessage(b'foo', b'bar'), b'bar : foo')
        self.testableTrue._formatMessage(object(), b'foo')
        return

    def test_formatMessage_unicode_error(self):
        one = (b'').join(chr(i) for i in range(255))
        self.testableTrue._formatMessage(one, u'\ufffd')
        return

    def assertMessages(self, methodName, args, errors):

        def getMethod(i):
            useTestableFalse = i < 2
            if useTestableFalse:
                test = self.testableFalse
            else:
                test = self.testableTrue
            return getattr(test, methodName)

        for i, expected_regexp in enumerate(errors):
            testMethod = getMethod(i)
            kwargs = {}
            withMsg = i % 2
            if withMsg:
                kwargs = {b'msg': b'oops'}
            with self.assertRaisesRegexp(self.failureException, expected_regexp=expected_regexp):
                testMethod(*args, **kwargs)

        return

    def testAssertTrue(self):
        self.assertMessages(b'assertTrue', (False,), [
         b'^False is not true$', b'^oops$', b'^False is not true$',
         b'^False is not true : oops$'])
        return

    def testAssertFalse(self):
        self.assertMessages(b'assertFalse', (True,), [
         b'^True is not false$', b'^oops$', b'^True is not false$',
         b'^True is not false : oops$'])
        return

    def testNotEqual(self):
        self.assertMessages(b'assertNotEqual', (1, 1), [
         b'^1 == 1$', b'^oops$', b'^1 == 1$',
         b'^1 == 1 : oops$'])
        return

    def testAlmostEqual(self):
        self.assertMessages(b'assertAlmostEqual', (1, 2), [
         b'^1 != 2 within 7 places$', b'^oops$',
         b'^1 != 2 within 7 places$', b'^1 != 2 within 7 places : oops$'])
        return

    def testNotAlmostEqual(self):
        self.assertMessages(b'assertNotAlmostEqual', (1, 1), [
         b'^1 == 1 within 7 places$', b'^oops$',
         b'^1 == 1 within 7 places$', b'^1 == 1 within 7 places : oops$'])
        return

    def test_baseAssertEqual(self):
        self.assertMessages(b'_baseAssertEqual', (1, 2), [
         b'^1 != 2$', b'^oops$', b'^1 != 2$', b'^1 != 2 : oops$'])
        return

    def testAssertSequenceEqual(self):
        self.assertMessages(b'assertSequenceEqual', ([], [None]), [
         b'\\+ \\[None\\]$', b'^oops$', b'\\+ \\[None\\]$',
         b'\\+ \\[None\\] : oops$'])
        return

    def testAssertSetEqual(self):
        self.assertMessages(b'assertSetEqual', (set(), set([None])), [
         b'None$', b'^oops$', b'None$',
         b'None : oops$'])
        return

    def testAssertIn(self):
        self.assertMessages(b'assertIn', (None, []), [
         b'^None not found in \\[\\]$', b'^oops$',
         b'^None not found in \\[\\]$',
         b'^None not found in \\[\\] : oops$'])
        return

    def testAssertNotIn(self):
        self.assertMessages(b'assertNotIn', (None, [None]), [
         b'^None unexpectedly found in \\[None\\]$', b'^oops$',
         b'^None unexpectedly found in \\[None\\]$',
         b'^None unexpectedly found in \\[None\\] : oops$'])
        return

    def testAssertDictEqual(self):
        self.assertMessages(b'assertDictEqual', ({}, {b'key': b'value'}), [
         b"\\+ \\{'key': 'value'\\}$", b'^oops$',
         b"\\+ \\{'key': 'value'\\}$",
         b"\\+ \\{'key': 'value'\\} : oops$"])
        return

    def testAssertDictContainsSubset(self):
        self.assertMessages(b'assertDictContainsSubset', ({b'key': b'value'}, {}), [
         b"^Missing: 'key'$", b'^oops$',
         b"^Missing: 'key'$",
         b"^Missing: 'key' : oops$"])
        return

    def testAssertMultiLineEqual(self):
        self.assertMessages(b'assertMultiLineEqual', (b'', b'foo'), [
         b'\\+ foo$', b'^oops$',
         b'\\+ foo$',
         b'\\+ foo : oops$'])
        return

    def testAssertLess(self):
        self.assertMessages(b'assertLess', (2, 1), [
         b'^2 not less than 1$', b'^oops$',
         b'^2 not less than 1$', b'^2 not less than 1 : oops$'])
        return

    def testAssertLessEqual(self):
        self.assertMessages(b'assertLessEqual', (2, 1), [
         b'^2 not less than or equal to 1$', b'^oops$',
         b'^2 not less than or equal to 1$',
         b'^2 not less than or equal to 1 : oops$'])
        return

    def testAssertGreater(self):
        self.assertMessages(b'assertGreater', (1, 2), [
         b'^1 not greater than 2$', b'^oops$',
         b'^1 not greater than 2$',
         b'^1 not greater than 2 : oops$'])
        return

    def testAssertGreaterEqual(self):
        self.assertMessages(b'assertGreaterEqual', (1, 2), [
         b'^1 not greater than or equal to 2$', b'^oops$',
         b'^1 not greater than or equal to 2$',
         b'^1 not greater than or equal to 2 : oops$'])
        return

    def testAssertIsNone(self):
        self.assertMessages(b'assertIsNone', (b'not None',), [
         b"^'not None' is not None$", b'^oops$',
         b"^'not None' is not None$",
         b"^'not None' is not None : oops$"])
        return

    def testAssertIsNotNone(self):
        self.assertMessages(b'assertIsNotNone', (None,), [
         b'^unexpectedly None$', b'^oops$',
         b'^unexpectedly None$',
         b'^unexpectedly None : oops$'])
        return

    def testAssertIs(self):
        self.assertMessages(b'assertIs', (None, b'foo'), [
         b"^None is not 'foo'$", b'^oops$',
         b"^None is not 'foo'$",
         b"^None is not 'foo' : oops$"])
        return

    def testAssertIsNot(self):
        self.assertMessages(b'assertIsNot', (None, None), [
         b'^unexpectedly identical: None$', b'^oops$',
         b'^unexpectedly identical: None$',
         b'^unexpectedly identical: None : oops$'])
        return


if __name__ == b'__main__':
    unittest.main()
