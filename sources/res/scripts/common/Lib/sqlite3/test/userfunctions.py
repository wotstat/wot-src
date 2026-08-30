import unittest, sqlite3 as sqlite
from test import test_support

def func_returntext():
    return b'foo'


def func_returnunicode():
    return u'bar'


def func_returnint():
    return 42


def func_returnfloat():
    return 3.14


def func_returnnull():
    return


def func_returnblob():
    with test_support.check_py3k_warnings():
        return buffer(b'blob')
    return


def func_returnlonglong():
    return 2147483648L


def func_raiseexception():
    5 // 0
    return


def func_isstring(v):
    return type(v) is unicode


def func_isint(v):
    return type(v) is int


def func_isfloat(v):
    return type(v) is float


def func_isnone(v):
    return type(v) is type(None)


def func_isblob(v):
    return type(v) is buffer


def func_islonglong(v):
    return isinstance(v, (int, long)) and v >= 2147483648L


class AggrNoStep:

    def __init__(self):
        return

    def finalize(self):
        return 1


class AggrNoFinalize:

    def __init__(self):
        return

    def step(self, x):
        return


class AggrExceptionInInit:

    def __init__(self):
        5 // 0
        return

    def step(self, x):
        return

    def finalize(self):
        return


class AggrExceptionInStep:

    def __init__(self):
        return

    def step(self, x):
        5 // 0
        return

    def finalize(self):
        return 42


class AggrExceptionInFinalize:

    def __init__(self):
        return

    def step(self, x):
        return

    def finalize(self):
        5 // 0
        return


class AggrCheckType:

    def __init__(self):
        self.val = None
        return

    def step(self, whichType, val):
        theType = {b'str': unicode, b'int': int, b'float': float, b'None': (type(None)), b'blob': buffer}
        self.val = int(theType[whichType] is type(val))
        return

    def finalize(self):
        return self.val


class AggrSum:

    def __init__(self):
        self.val = 0.0
        return

    def step(self, val):
        self.val += val
        return

    def finalize(self):
        return self.val


class FunctionTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        self.con.create_function(b'returntext', 0, func_returntext)
        self.con.create_function(b'returnunicode', 0, func_returnunicode)
        self.con.create_function(b'returnint', 0, func_returnint)
        self.con.create_function(b'returnfloat', 0, func_returnfloat)
        self.con.create_function(b'returnnull', 0, func_returnnull)
        self.con.create_function(b'returnblob', 0, func_returnblob)
        self.con.create_function(b'returnlonglong', 0, func_returnlonglong)
        self.con.create_function(b'raiseexception', 0, func_raiseexception)
        self.con.create_function(b'isstring', 1, func_isstring)
        self.con.create_function(b'isint', 1, func_isint)
        self.con.create_function(b'isfloat', 1, func_isfloat)
        self.con.create_function(b'isnone', 1, func_isnone)
        self.con.create_function(b'isblob', 1, func_isblob)
        self.con.create_function(b'islonglong', 1, func_islonglong)
        return

    def tearDown(self):
        self.con.close()
        return

    def CheckFuncErrorOnCreate(self):
        try:
            self.con.create_function(b'bla', -100, (lambda x: 2 * x))
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError:
            pass

        return

    def CheckFuncRefCount(self):

        def getfunc():

            def f():
                return 1

            return f

        f = getfunc()
        globals()[b'foo'] = f
        self.con.create_function(b'reftest', 0, f)
        cur = self.con.cursor()
        cur.execute(b'select reftest()')
        return

    def CheckFuncReturnText(self):
        cur = self.con.cursor()
        cur.execute(b'select returntext()')
        val = cur.fetchone()[0]
        self.assertEqual(type(val), unicode)
        self.assertEqual(val, b'foo')
        return

    def CheckFuncReturnUnicode(self):
        cur = self.con.cursor()
        cur.execute(b'select returnunicode()')
        val = cur.fetchone()[0]
        self.assertEqual(type(val), unicode)
        self.assertEqual(val, u'bar')
        return

    def CheckFuncReturnInt(self):
        cur = self.con.cursor()
        cur.execute(b'select returnint()')
        val = cur.fetchone()[0]
        self.assertEqual(type(val), int)
        self.assertEqual(val, 42)
        return

    def CheckFuncReturnFloat(self):
        cur = self.con.cursor()
        cur.execute(b'select returnfloat()')
        val = cur.fetchone()[0]
        self.assertEqual(type(val), float)
        if val < 3.139 or val > 3.141:
            self.fail(b'wrong value')
        return

    def CheckFuncReturnNull(self):
        cur = self.con.cursor()
        cur.execute(b'select returnnull()')
        val = cur.fetchone()[0]
        self.assertEqual(type(val), type(None))
        self.assertEqual(val, None)
        return

    def CheckFuncReturnBlob(self):
        cur = self.con.cursor()
        cur.execute(b'select returnblob()')
        val = cur.fetchone()[0]
        with test_support.check_py3k_warnings():
            self.assertEqual(type(val), buffer)
            self.assertEqual(val, buffer(b'blob'))
        return

    def CheckFuncReturnLongLong(self):
        cur = self.con.cursor()
        cur.execute(b'select returnlonglong()')
        val = cur.fetchone()[0]
        self.assertEqual(val, 2147483648L)
        return

    def CheckFuncException(self):
        cur = self.con.cursor()
        try:
            cur.execute(b'select raiseexception()')
            cur.fetchone()
            self.fail(b'should have raised OperationalError')
        except sqlite.OperationalError as e:
            self.assertEqual(e.args[0], b'user-defined function raised exception')

        return

    def CheckParamString(self):
        cur = self.con.cursor()
        cur.execute(b'select isstring(?)', (b'foo',))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckParamInt(self):
        cur = self.con.cursor()
        cur.execute(b'select isint(?)', (42,))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckParamFloat(self):
        cur = self.con.cursor()
        cur.execute(b'select isfloat(?)', (3.14,))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckParamNone(self):
        cur = self.con.cursor()
        cur.execute(b'select isnone(?)', (None,))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckParamBlob(self):
        cur = self.con.cursor()
        with test_support.check_py3k_warnings():
            cur.execute(b'select isblob(?)', (buffer(b'blob'),))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckParamLongLong(self):
        cur = self.con.cursor()
        cur.execute(b'select islonglong(?)', (4398046511104L,))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return


class AggregateTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        cur = self.con.cursor()
        cur.execute(b'\n            create table test(\n                t text,\n                i integer,\n                f float,\n                n,\n                b blob\n                )\n            ')
        with test_support.check_py3k_warnings():
            cur.execute(b'insert into test(t, i, f, n, b) values (?, ?, ?, ?, ?)', (
             b'foo', 5, 3.14, None, buffer(b'blob')))
        self.con.create_aggregate(b'nostep', 1, AggrNoStep)
        self.con.create_aggregate(b'nofinalize', 1, AggrNoFinalize)
        self.con.create_aggregate(b'excInit', 1, AggrExceptionInInit)
        self.con.create_aggregate(b'excStep', 1, AggrExceptionInStep)
        self.con.create_aggregate(b'excFinalize', 1, AggrExceptionInFinalize)
        self.con.create_aggregate(b'checkType', 2, AggrCheckType)
        self.con.create_aggregate(b'mysum', 1, AggrSum)
        return

    def tearDown(self):
        return

    def CheckAggrErrorOnCreate(self):
        try:
            self.con.create_function(b'bla', -100, AggrSum)
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError:
            pass

        return

    def CheckAggrNoStep(self):
        cur = self.con.cursor()
        try:
            cur.execute(b'select nostep(t) from test')
            self.fail(b'should have raised an AttributeError')
        except AttributeError as e:
            self.assertEqual(e.args[0], b"AggrNoStep instance has no attribute 'step'")

        return

    def CheckAggrNoFinalize(self):
        cur = self.con.cursor()
        try:
            cur.execute(b'select nofinalize(t) from test')
            val = cur.fetchone()[0]
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError as e:
            self.assertEqual(e.args[0], b"user-defined aggregate's 'finalize' method raised error")

        return

    def CheckAggrExceptionInInit(self):
        cur = self.con.cursor()
        try:
            cur.execute(b'select excInit(t) from test')
            val = cur.fetchone()[0]
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError as e:
            self.assertEqual(e.args[0], b"user-defined aggregate's '__init__' method raised error")

        return

    def CheckAggrExceptionInStep(self):
        cur = self.con.cursor()
        try:
            cur.execute(b'select excStep(t) from test')
            val = cur.fetchone()[0]
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError as e:
            self.assertEqual(e.args[0], b"user-defined aggregate's 'step' method raised error")

        return

    def CheckAggrExceptionInFinalize(self):
        cur = self.con.cursor()
        try:
            cur.execute(b'select excFinalize(t) from test')
            val = cur.fetchone()[0]
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError as e:
            self.assertEqual(e.args[0], b"user-defined aggregate's 'finalize' method raised error")

        return

    def CheckAggrCheckParamStr(self):
        cur = self.con.cursor()
        cur.execute(b"select checkType('str', ?)", (b'foo',))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckAggrCheckParamInt(self):
        cur = self.con.cursor()
        cur.execute(b"select checkType('int', ?)", (42,))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckAggrCheckParamFloat(self):
        cur = self.con.cursor()
        cur.execute(b"select checkType('float', ?)", (3.14,))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckAggrCheckParamNone(self):
        cur = self.con.cursor()
        cur.execute(b"select checkType('None', ?)", (None,))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckAggrCheckParamBlob(self):
        cur = self.con.cursor()
        with test_support.check_py3k_warnings():
            cur.execute(b"select checkType('blob', ?)", (buffer(b'blob'),))
        val = cur.fetchone()[0]
        self.assertEqual(val, 1)
        return

    def CheckAggrCheckAggrSum(self):
        cur = self.con.cursor()
        cur.execute(b'delete from test')
        cur.executemany(b'insert into test(i) values (?)', [(10,), (20,), (30,)])
        cur.execute(b'select mysum(i) from test')
        val = cur.fetchone()[0]
        self.assertEqual(val, 60)
        return


class AuthorizerTests(unittest.TestCase):

    @staticmethod
    def authorizer_cb(action, arg1, arg2, dbname, source):
        if action != sqlite.SQLITE_SELECT:
            return sqlite.SQLITE_DENY
        if arg2 == b'c2' or arg1 == b't2':
            return sqlite.SQLITE_DENY
        return sqlite.SQLITE_OK

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        self.con.executescript(b'\n            create table t1 (c1, c2);\n            create table t2 (c1, c2);\n            insert into t1 (c1, c2) values (1, 2);\n            insert into t2 (c1, c2) values (4, 5);\n            ')
        self.con.execute(b'select c2 from t2')
        self.con.set_authorizer(self.authorizer_cb)
        return

    def tearDown(self):
        return

    def test_table_access(self):
        try:
            self.con.execute(b'select * from t2')
        except sqlite.DatabaseError as e:
            if not e.args[0].endswith(b'prohibited'):
                self.fail(b'wrong exception text: %s' % e.args[0])
            return

        self.fail(b'should have raised an exception due to missing privileges')
        return

    def test_column_access(self):
        try:
            self.con.execute(b'select c2 from t1')
        except sqlite.DatabaseError as e:
            if not e.args[0].endswith(b'prohibited'):
                self.fail(b'wrong exception text: %s' % e.args[0])
            return

        self.fail(b'should have raised an exception due to missing privileges')
        return


class AuthorizerRaiseExceptionTests(AuthorizerTests):

    @staticmethod
    def authorizer_cb(action, arg1, arg2, dbname, source):
        if action != sqlite.SQLITE_SELECT:
            raise ValueError
        if arg2 == b'c2' or arg1 == b't2':
            raise ValueError
        return sqlite.SQLITE_OK


class AuthorizerIllegalTypeTests(AuthorizerTests):

    @staticmethod
    def authorizer_cb(action, arg1, arg2, dbname, source):
        if action != sqlite.SQLITE_SELECT:
            return 0.0
        if arg2 == b'c2' or arg1 == b't2':
            return 0.0
        return sqlite.SQLITE_OK


class AuthorizerLargeIntegerTests(AuthorizerTests):

    @staticmethod
    def authorizer_cb(action, arg1, arg2, dbname, source):
        if action != sqlite.SQLITE_SELECT:
            return 4294967296L
        if arg2 == b'c2' or arg1 == b't2':
            return 4294967296L
        return sqlite.SQLITE_OK


def suite():
    function_suite = unittest.makeSuite(FunctionTests, b'Check')
    aggregate_suite = unittest.makeSuite(AggregateTests, b'Check')
    authorizer_suite = unittest.makeSuite(AuthorizerTests)
    return unittest.TestSuite((
     function_suite,
     aggregate_suite,
     authorizer_suite,
     unittest.makeSuite(AuthorizerRaiseExceptionTests),
     unittest.makeSuite(AuthorizerIllegalTypeTests),
     unittest.makeSuite(AuthorizerLargeIntegerTests)))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    return


if __name__ == b'__main__':
    test()
