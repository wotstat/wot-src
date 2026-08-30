import sys, os, re, test_all
from cStringIO import StringIO
import unittest
from test_all import db, dbshelve, test_support, get_new_environment_path, get_new_database_path

def cmp(a, b):
    if a == b:
        return 0
    if a < b:
        return -1
    return 1


lexical_cmp = cmp

def lowercase_cmp(left, right):
    return cmp(left.lower(), right.lower())


def make_reverse_comparator(cmp):

    def reverse(left, right, delegate=cmp):
        return -delegate(left, right)

    return reverse


_expected_lexical_test_data = [
 7, 8, 9, 10, 11, 12, 13, 14]
_expected_lowercase_test_data = [7, 9, 10, 11, 12, 15, 13, 14, 8]

class ComparatorTests(unittest.TestCase):

    def comparator_test_helper(self, comparator, expected_data):
        data = expected_data[:]
        import sys
        if sys.version_info < (2, 6):
            data.sort(cmp=comparator)
        else:
            data2 = []
            for i in data:
                for j, k in enumerate(data2):
                    r = comparator(k, i)
                    if r == 1:
                        data2.insert(j, i)
                        break
                else:
                    data2.append(i)

            data = data2
        self.assertEqual(data, expected_data, b"comparator `%s' is not right: %s vs. %s" % (
         comparator, expected_data, data))
        return

    def test_lexical_comparator(self):
        self.comparator_test_helper(lexical_cmp, _expected_lexical_test_data)
        return

    def test_reverse_lexical_comparator(self):
        rev = _expected_lexical_test_data[:]
        rev.reverse()
        self.comparator_test_helper(make_reverse_comparator(lexical_cmp), rev)
        return

    def test_lowercase_comparator(self):
        self.comparator_test_helper(lowercase_cmp, _expected_lowercase_test_data)
        return


class AbstractBtreeKeyCompareTestCase(unittest.TestCase):
    env = None
    db = None
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0) and sys.version_info < (3, 2):

        def assertLess(self, a, b, msg=None):
            return self.assertTrue(a < b, msg=msg)

    def setUp(self):
        self.filename = self.__class__.__name__ + b'.db'
        self.homeDir = get_new_environment_path()
        env = db.DBEnv()
        env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL | db.DB_INIT_LOCK | db.DB_THREAD)
        self.env = env
        return

    def tearDown(self):
        self.closeDB()
        if self.env is not None:
            self.env.close()
            self.env = None
        test_support.rmtree(self.homeDir)
        return

    def addDataToDB(self, data):
        i = 0
        for item in data:
            self.db.put(item, str(i))
            i = i + 1

        return

    def createDB(self, key_comparator):
        self.db = db.DB(self.env)
        self.setupDB(key_comparator)
        self.db.open(self.filename, b'test', db.DB_BTREE, db.DB_CREATE)
        return

    def setupDB(self, key_comparator):
        self.db.set_bt_compare(key_comparator)
        return

    def closeDB(self):
        if self.db is not None:
            self.db.close()
            self.db = None
        return

    def startTest(self):
        return

    def finishTest(self, expected=None):
        if expected is not None:
            self.check_results(expected)
        self.closeDB()
        return

    def check_results(self, expected):
        curs = self.db.cursor()
        try:
            index = 0
            rec = curs.first()
            while rec:
                key, ignore = rec
                self.assertLess(index, len(expected), b'to many values returned from cursor')
                self.assertEqual(expected[index], key, b"expected value `%s' at %d but got `%s'" % (
                 expected[index], index, key))
                index = index + 1
                rec = curs.next()

            self.assertEqual(index, len(expected), b'not enough values returned from cursor')
        finally:
            curs.close()

        return


class BtreeKeyCompareTestCase(AbstractBtreeKeyCompareTestCase):

    def runCompareTest(self, comparator, data):
        self.startTest()
        self.createDB(comparator)
        self.addDataToDB(data)
        self.finishTest(data)
        return

    def test_lexical_ordering(self):
        self.runCompareTest(lexical_cmp, _expected_lexical_test_data)
        return

    def test_reverse_lexical_ordering(self):
        expected_rev_data = _expected_lexical_test_data[:]
        expected_rev_data.reverse()
        self.runCompareTest(make_reverse_comparator(lexical_cmp), expected_rev_data)
        return

    def test_compare_function_useless(self):
        self.startTest()

        def socialist_comparator(l, r):
            return 0

        self.createDB(socialist_comparator)
        self.addDataToDB([b'b', b'a', b'd'])
        self.finishTest([b'b'])
        return


class BtreeExceptionsTestCase(AbstractBtreeKeyCompareTestCase):

    def test_raises_non_callable(self):
        self.startTest()
        self.assertRaises(TypeError, self.createDB, b'abc')
        self.assertRaises(TypeError, self.createDB, None)
        self.finishTest()
        return

    def test_set_bt_compare_with_function(self):
        self.startTest()
        self.createDB(lexical_cmp)
        self.finishTest()
        return

    def check_results(self, results):
        return

    def test_compare_function_incorrect(self):
        self.startTest()

        def bad_comparator(l, r):
            return 1

        self.assertRaises(TypeError, self.createDB, bad_comparator)
        self.finishTest()
        return

    def verifyStderr(self, method, successRe):
        stdErr = sys.stderr
        sys.stderr = StringIO()
        try:
            method()
        finally:
            temp = sys.stderr
            sys.stderr = stdErr
            errorOut = temp.getvalue()
            if not successRe.search(errorOut):
                self.fail(b'unexpected stderr output:\n' + errorOut)

        if sys.version_info < (3, 0):
            sys.exc_traceback = sys.last_traceback = None
        return

    def _test_compare_function_exception(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            raise RuntimeError, b"i'm a naughty comparison function"
            return

        self.createDB(bad_comparator)
        self.addDataToDB([b'a', b'b', b'c'])
        self.finishTest()
        return

    def test_compare_function_exception(self):
        self.verifyStderr(self._test_compare_function_exception, re.compile(b'(^RuntimeError:.* naughty.*){2}', re.M | re.S))
        return

    def _test_compare_function_bad_return(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            return l

        self.createDB(bad_comparator)
        self.addDataToDB([b'a', b'b', b'c'])
        self.finishTest()
        return

    def test_compare_function_bad_return(self):
        self.verifyStderr(self._test_compare_function_bad_return, re.compile(b'(^TypeError:.* return an int.*){2}', re.M | re.S))
        return

    def test_cannot_assign_twice(self):

        def my_compare(a, b):
            return 0

        self.startTest()
        self.createDB(my_compare)
        self.assertRaises(RuntimeError, self.db.set_bt_compare, my_compare)
        return


class AbstractDuplicateCompareTestCase(unittest.TestCase):
    env = None
    db = None
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0) and sys.version_info < (3, 2):

        def assertLess(self, a, b, msg=None):
            return self.assertTrue(a < b, msg=msg)

    def setUp(self):
        self.filename = self.__class__.__name__ + b'.db'
        self.homeDir = get_new_environment_path()
        env = db.DBEnv()
        env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL | db.DB_INIT_LOCK | db.DB_THREAD)
        self.env = env
        return

    def tearDown(self):
        self.closeDB()
        if self.env is not None:
            self.env.close()
            self.env = None
        test_support.rmtree(self.homeDir)
        return

    def addDataToDB(self, data):
        for item in data:
            self.db.put(b'key', item)

        return

    def createDB(self, dup_comparator):
        self.db = db.DB(self.env)
        self.setupDB(dup_comparator)
        self.db.open(self.filename, b'test', db.DB_BTREE, db.DB_CREATE)
        return

    def setupDB(self, dup_comparator):
        self.db.set_flags(db.DB_DUPSORT)
        self.db.set_dup_compare(dup_comparator)
        return

    def closeDB(self):
        if self.db is not None:
            self.db.close()
            self.db = None
        return

    def startTest(self):
        return

    def finishTest(self, expected=None):
        if expected is not None:
            self.check_results(expected)
        self.closeDB()
        return

    def check_results(self, expected):
        curs = self.db.cursor()
        try:
            index = 0
            rec = curs.first()
            while rec:
                ignore, data = rec
                self.assertLess(index, len(expected), b'to many values returned from cursor')
                self.assertEqual(expected[index], data, b"expected value `%s' at %d but got `%s'" % (
                 expected[index], index, data))
                index = index + 1
                rec = curs.next()

            self.assertEqual(index, len(expected), b'not enough values returned from cursor')
        finally:
            curs.close()

        return


class DuplicateCompareTestCase(AbstractDuplicateCompareTestCase):

    def runCompareTest(self, comparator, data):
        self.startTest()
        self.createDB(comparator)
        self.addDataToDB(data)
        self.finishTest(data)
        return

    def test_lexical_ordering(self):
        self.runCompareTest(lexical_cmp, _expected_lexical_test_data)
        return

    def test_reverse_lexical_ordering(self):
        expected_rev_data = _expected_lexical_test_data[:]
        expected_rev_data.reverse()
        self.runCompareTest(make_reverse_comparator(lexical_cmp), expected_rev_data)
        return


class DuplicateExceptionsTestCase(AbstractDuplicateCompareTestCase):

    def test_raises_non_callable(self):
        self.startTest()
        self.assertRaises(TypeError, self.createDB, b'abc')
        self.assertRaises(TypeError, self.createDB, None)
        self.finishTest()
        return

    def test_set_dup_compare_with_function(self):
        self.startTest()
        self.createDB(lexical_cmp)
        self.finishTest()
        return

    def check_results(self, results):
        return

    def test_compare_function_incorrect(self):
        self.startTest()

        def bad_comparator(l, r):
            return 1

        self.assertRaises(TypeError, self.createDB, bad_comparator)
        self.finishTest()
        return

    def test_compare_function_useless(self):
        self.startTest()

        def socialist_comparator(l, r):
            return 0

        self.createDB(socialist_comparator)
        self.assertRaises(db.DBKeyExistError, self.addDataToDB, [b'b', b'a', b'd'])
        self.finishTest()
        return

    def verifyStderr(self, method, successRe):
        stdErr = sys.stderr
        sys.stderr = StringIO()
        try:
            method()
        finally:
            temp = sys.stderr
            sys.stderr = stdErr
            errorOut = temp.getvalue()
            if not successRe.search(errorOut):
                self.fail(b'unexpected stderr output:\n' + errorOut)

        if sys.version_info < (3, 0):
            sys.exc_traceback = sys.last_traceback = None
        return

    def _test_compare_function_exception(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            raise RuntimeError, b"i'm a naughty comparison function"
            return

        self.createDB(bad_comparator)
        self.addDataToDB([b'a', b'b', b'c'])
        self.finishTest()
        return

    def test_compare_function_exception(self):
        self.verifyStderr(self._test_compare_function_exception, re.compile(b'(^RuntimeError:.* naughty.*){2}', re.M | re.S))
        return

    def _test_compare_function_bad_return(self):
        self.startTest()

        def bad_comparator(l, r):
            if l == r:
                return 0
            return l

        self.createDB(bad_comparator)
        self.addDataToDB([b'a', b'b', b'c'])
        self.finishTest()
        return

    def test_compare_function_bad_return(self):
        self.verifyStderr(self._test_compare_function_bad_return, re.compile(b'(^TypeError:.* return an int.*){2}', re.M | re.S))
        return

    def test_cannot_assign_twice(self):

        def my_compare(a, b):
            return 0

        self.startTest()
        self.createDB(my_compare)
        self.assertRaises(RuntimeError, self.db.set_dup_compare, my_compare)
        return


def test_suite():
    res = unittest.TestSuite()
    res.addTest(unittest.makeSuite(ComparatorTests))
    res.addTest(unittest.makeSuite(BtreeExceptionsTestCase))
    res.addTest(unittest.makeSuite(BtreeKeyCompareTestCase))
    res.addTest(unittest.makeSuite(DuplicateExceptionsTestCase))
    res.addTest(unittest.makeSuite(DuplicateCompareTestCase))
    return res


if __name__ == b'__main__':
    unittest.main(defaultTest=b'suite')
