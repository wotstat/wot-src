import datetime, unittest, sqlite3 as sqlite, weakref
from test import support

class RegressionTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        return

    def tearDown(self):
        self.con.close()
        return

    def CheckPragmaUserVersion(self):
        cur = self.con.cursor()
        cur.execute(b'pragma user_version')
        return

    def CheckPragmaSchemaVersion(self):
        con = sqlite.connect(b':memory:', detect_types=sqlite.PARSE_COLNAMES)
        try:
            cur = self.con.cursor()
            cur.execute(b'pragma schema_version')
        finally:
            cur.close()
            con.close()

        return

    def CheckStatementReset(self):
        con = sqlite.connect(b':memory:', cached_statements=5)
        cursors = [con.cursor() for x in xrange(5)]
        cursors[0].execute(b'create table test(x)')
        for i in range(10):
            cursors[0].executemany(b'insert into test(x) values (?)', [(x,) for x in xrange(10)])

        for i in range(5):
            cursors[i].execute(b' ' * i + b'select x from test')

        con.rollback()
        return

    def CheckColumnNameWithSpaces(self):
        cur = self.con.cursor()
        cur.execute(b'select 1 as "foo bar [datetime]"')
        self.assertEqual(cur.description[0][0], b'foo bar')
        cur.execute(b'select 1 as "foo baz"')
        self.assertEqual(cur.description[0][0], b'foo baz')
        return

    def CheckStatementFinalizationOnCloseDb(self):
        con = sqlite.connect(b':memory:')
        cursors = []
        for i in range(105):
            cur = con.cursor()
            cursors.append(cur)
            cur.execute(b'select 1 x union select ' + str(i))

        con.close()
        return

    def CheckOnConflictRollback(self):
        if sqlite.sqlite_version_info < (3, 2, 2):
            return
        con = sqlite.connect(b':memory:')
        con.execute(b'create table foo(x, unique(x) on conflict rollback)')
        con.execute(b'insert into foo(x) values (1)')
        try:
            con.execute(b'insert into foo(x) values (1)')
        except sqlite.DatabaseError:
            pass

        con.execute(b'insert into foo(x) values (2)')
        try:
            con.commit()
        except sqlite.OperationalError:
            self.fail(b'pysqlite knew nothing about the implicit ROLLBACK')

        return

    def CheckWorkaroundForBuggySqliteTransferBindings(self):
        self.con.execute(b'create table foo(bar)')
        self.con.execute(b'drop table foo')
        self.con.execute(b'create table foo(bar)')
        return

    def CheckEmptyStatement(self):
        self.con.execute(b'')
        return

    def CheckUnicodeConnect(self):
        con = sqlite.connect(u':memory:')
        con.close()
        return

    def CheckTypeMapUsage(self):
        SELECT = b'select * from foo'
        con = sqlite.connect(b':memory:', detect_types=sqlite.PARSE_DECLTYPES)
        con.execute(b'create table foo(bar timestamp)')
        con.execute(b'insert into foo(bar) values (?)', (datetime.datetime.now(),))
        con.execute(SELECT)
        con.execute(b'drop table foo')
        con.execute(b'create table foo(bar integer)')
        con.execute(b'insert into foo(bar) values (5)')
        con.execute(SELECT)
        return

    def CheckRegisterAdapter(self):
        self.assertRaises(TypeError, sqlite.register_adapter, {}, None)
        return

    def CheckSetIsolationLevel(self):
        con = sqlite.connect(b':memory:')
        self.assertRaises(UnicodeEncodeError, setattr, con, b'isolation_level', u'\xe9')
        return

    def CheckCursorConstructorCallCheck(self):

        class Cursor(sqlite.Cursor):

            def __init__(self, con):
                return

        con = sqlite.connect(b':memory:')
        cur = Cursor(con)
        try:
            cur.execute(b'select 4+5').fetchall()
            self.fail(b'should have raised ProgrammingError')
        except sqlite.ProgrammingError:
            pass
        except:
            self.fail(b'should have raised ProgrammingError')

        with self.assertRaisesRegexp(sqlite.ProgrammingError, b'^Base Cursor\\.__init__ not called\\.$'):
            cur.close()
        return

    def CheckConnectionConstructorCallCheck(self):

        class Connection(sqlite.Connection):

            def __init__(self, name):
                return

        con = Connection(b':memory:')
        try:
            cur = con.cursor()
            self.fail(b'should have raised ProgrammingError')
        except sqlite.ProgrammingError:
            pass
        except:
            self.fail(b'should have raised ProgrammingError')

        return

    def CheckCursorRegistration(self):

        class Connection(sqlite.Connection):

            def cursor(self):
                return Cursor(self)

        class Cursor(sqlite.Cursor):

            def __init__(self, con):
                sqlite.Cursor.__init__(self, con)
                return

        con = Connection(b':memory:')
        cur = con.cursor()
        cur.execute(b'create table foo(x)')
        cur.executemany(b'insert into foo(x) values (?)', [(3,), (4,), (5,)])
        cur.execute(b'select x from foo')
        con.rollback()
        try:
            cur.fetchall()
            self.fail(b'should have raised InterfaceError')
        except sqlite.InterfaceError:
            pass
        except:
            self.fail(b'should have raised InterfaceError')

        return

    def CheckAutoCommit(self):
        con = sqlite.connect(b':memory:', isolation_level=None)
        return

    def CheckPragmaAutocommit(self):
        cur = self.con.cursor()
        cur.execute(b'create table foo(bar)')
        cur.execute(b'insert into foo(bar) values (5)')
        cur.execute(b'pragma page_size')
        row = cur.fetchone()
        return

    def CheckConnectionCall(self):
        self.assertRaises(sqlite.Warning, self.con, 1)
        return

    def CheckRecursiveCursorUse(self):
        con = sqlite.connect(b':memory:')
        cur = con.cursor()
        cur.execute(b'create table a (bar)')
        cur.execute(b'create table b (baz)')

        def foo():
            cur.execute(b'insert into a (bar) values (?)', (1,))
            yield 1
            return

        with self.assertRaises(sqlite.ProgrammingError):
            cur.executemany(b'insert into b (baz) values (?)', ((i,) for i in foo()))
        return

    def CheckConvertTimestampMicrosecondPadding(self):
        con = sqlite.connect(b':memory:', detect_types=sqlite.PARSE_DECLTYPES)
        cur = con.cursor()
        cur.execute(b'CREATE TABLE t (x TIMESTAMP)')
        cur.execute(b"INSERT INTO t (x) VALUES ('2012-04-04 15:06:00.456')")
        cur.execute(b"INSERT INTO t (x) VALUES ('2012-04-04 15:06:00.123456789')")
        cur.execute(b'SELECT * FROM t')
        values = [x[0] for x in cur.fetchall()]
        self.assertEqual(values, [
         datetime.datetime(2012, 4, 4, 15, 6, 0, 456000),
         datetime.datetime(2012, 4, 4, 15, 6, 0, 123456)])
        return

    def CheckInvalidIsolationLevelType(self):
        self.assertRaises(TypeError, sqlite.connect, b':memory:', isolation_level=123)
        return

    def CheckNullCharacter(self):
        con = sqlite.connect(b':memory:')
        self.assertRaises(ValueError, con, b'\x00select 1')
        self.assertRaises(ValueError, con, b'select 1\x00')
        cur = con.cursor()
        self.assertRaises(ValueError, cur.execute, b' \x00select 2')
        self.assertRaises(ValueError, cur.execute, b'select 2\x00')
        return

    def CheckCommitCursorReset(self):
        con = sqlite.connect(b':memory:')
        con.executescript(b'\n        create table t(c);\n        create table t2(c);\n        insert into t values(0);\n        insert into t values(1);\n        insert into t values(2);\n        ')
        self.assertEqual(con.isolation_level, b'')
        counter = 0
        for i, row in enumerate(con.execute(b'select c from t')):
            con.execute(b'insert into t2(c) values (?)', (i,))
            con.commit()
            if counter == 0:
                self.assertEqual(row[0], 0)
            elif counter == 1:
                self.assertEqual(row[0], 1)
            elif counter == 2:
                self.assertEqual(row[0], 2)
            counter += 1

        self.assertEqual(counter, 3, b'should have returned exactly three rows')
        return

    def CheckBpo31770(self):

        def callback(*args):
            return

        con = sqlite.connect(b':memory:')
        cur = sqlite.Cursor(con)
        ref = weakref.ref(cur, callback)
        cur.__init__(con)
        del cur
        del ref
        support.gc_collect()
        return

    def CheckDelIsolation_levelSegfault(self):
        with self.assertRaises(AttributeError):
            del self.con.isolation_level
        return


class UnhashableFunc():

    def __hash__(self):
        raise TypeError(b'unhashable type')
        return

    def __init__(self, return_value=None):
        self.calls = 0
        self.return_value = return_value
        return

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.return_value


class UnhashableCallbacksTestCase(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        return

    def tearDown(self):
        self.con.close()
        return

    def test_progress_handler(self):
        f = UnhashableFunc(return_value=0)
        with self.assertRaisesRegexp(TypeError, b'unhashable type'):
            self.con.set_progress_handler(f, 1)
        self.con.execute(b'SELECT 1')
        self.assertFalse(f.calls)
        return

    def test_func(self):
        func_name = b'func_name'
        f = UnhashableFunc()
        with self.assertRaisesRegexp(TypeError, b'unhashable type'):
            self.con.create_function(func_name, 0, f)
        msg = b'no such function: %s' % func_name
        with self.assertRaisesRegexp(sqlite.OperationalError, msg):
            self.con.execute(b'SELECT %s()' % func_name)
        self.assertFalse(f.calls)
        return

    def test_authorizer(self):
        f = UnhashableFunc(return_value=sqlite.SQLITE_DENY)
        with self.assertRaisesRegexp(TypeError, b'unhashable type'):
            self.con.set_authorizer(f)
        self.con.execute(b'SELECT 1')
        self.assertFalse(f.calls)
        return

    def test_aggr(self):

        class UnhashableType(type):
            __hash__ = None

        aggr_name = b'aggr_name'
        with self.assertRaisesRegexp(TypeError, b'unhashable type'):
            self.con.create_aggregate(aggr_name, 0, UnhashableType(b'Aggr', (), {}))
        msg = b'no such function: %s' % aggr_name
        with self.assertRaisesRegexp(sqlite.OperationalError, msg):
            self.con.execute(b'SELECT %s()' % aggr_name)
        return


def suite():
    regression_suite = unittest.makeSuite(RegressionTests, b'Check')
    return unittest.TestSuite((
     regression_suite,
     unittest.makeSuite(UnhashableCallbacksTestCase)))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    return


if __name__ == b'__main__':
    test()
