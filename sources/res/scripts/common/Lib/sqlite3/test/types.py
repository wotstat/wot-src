import datetime, unittest, sqlite3 as sqlite
from test import test_support
try:
    import zlib
except ImportError:
    zlib = None

class SqliteTypeTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        self.cur = self.con.cursor()
        self.cur.execute(b'create table test(i integer, s varchar, f number, b blob)')
        return

    def tearDown(self):
        self.cur.close()
        self.con.close()
        return

    def CheckString(self):
        self.cur.execute(b'insert into test(s) values (?)', (u'\xd6sterreich',))
        self.cur.execute(b'select s from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], u'\xd6sterreich')
        return

    def CheckSmallInt(self):
        self.cur.execute(b'insert into test(i) values (?)', (42,))
        self.cur.execute(b'select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], 42)
        return

    def CheckLargeInt(self):
        num = 1099511627776L
        self.cur.execute(b'insert into test(i) values (?)', (num,))
        self.cur.execute(b'select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], num)
        return

    def CheckFloat(self):
        val = 3.14
        self.cur.execute(b'insert into test(f) values (?)', (val,))
        self.cur.execute(b'select f from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)
        return

    def CheckBlob(self):
        with test_support.check_py3k_warnings():
            val = buffer(b'Guglhupf')
        self.cur.execute(b'insert into test(b) values (?)', (val,))
        self.cur.execute(b'select b from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)
        return

    def CheckUnicodeExecute(self):
        self.cur.execute(u"select '\xd6sterreich'")
        row = self.cur.fetchone()
        self.assertEqual(row[0], u'\xd6sterreich')
        return

    def CheckNonUtf8_Default(self):
        try:
            self.cur.execute(b'select ?', (chr(150),))
            self.fail(b'should have raised a ProgrammingError')
        except sqlite.ProgrammingError:
            pass

        return

    def CheckNonUtf8_TextFactoryString(self):
        orig_text_factory = self.con.text_factory
        try:
            self.con.text_factory = str
            self.cur.execute(b'select ?', (chr(150),))
        finally:
            self.con.text_factory = orig_text_factory

        return

    def CheckNonUtf8_TextFactoryOptimizedUnicode(self):
        orig_text_factory = self.con.text_factory
        try:
            try:
                self.con.text_factory = sqlite.OptimizedUnicode
                self.cur.execute(b'select ?', (chr(150),))
                self.fail(b'should have raised a ProgrammingError')
            except sqlite.ProgrammingError:
                pass

        finally:
            self.con.text_factory = orig_text_factory

        return


class DeclTypesTests(unittest.TestCase):

    class Foo:

        def __init__(self, _val):
            self.val = _val
            return

        def __cmp__(self, other):
            if not isinstance(other, DeclTypesTests.Foo):
                raise ValueError
            if self.val == other.val:
                return 0
            else:
                return 1

            return

        def __conform__(self, protocol):
            if protocol is sqlite.PrepareProtocol:
                return self.val
            else:
                return
                return

        def __str__(self):
            return b'<%s>' % self.val

    def setUp(self):
        self.con = sqlite.connect(b':memory:', detect_types=sqlite.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.cur.execute(b'create table test(i int, s str, f float, b bool, u unicode, foo foo, bin blob, n1 number, n2 number(5))')
        sqlite.converters[b'FLOAT'] = lambda x: 47.2
        sqlite.converters[b'BOOL'] = lambda x: bool(int(x))
        sqlite.converters[b'FOO'] = DeclTypesTests.Foo
        sqlite.converters[b'WRONG'] = lambda x: b'WRONG'
        sqlite.converters[b'NUMBER'] = float
        return

    def tearDown(self):
        del sqlite.converters[b'FLOAT']
        del sqlite.converters[b'BOOL']
        del sqlite.converters[b'FOO']
        del sqlite.converters[b'NUMBER']
        self.cur.close()
        self.con.close()
        return

    def CheckString(self):
        self.cur.execute(b'insert into test(s) values (?)', (b'foo',))
        self.cur.execute(b'select s as "s [WRONG]" from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], b'foo')
        return

    def CheckSmallInt(self):
        self.cur.execute(b'insert into test(i) values (?)', (42,))
        self.cur.execute(b'select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], 42)
        return

    def CheckLargeInt(self):
        num = 1099511627776L
        self.cur.execute(b'insert into test(i) values (?)', (num,))
        self.cur.execute(b'select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], num)
        return

    def CheckFloat(self):
        val = 3.14
        self.cur.execute(b'insert into test(f) values (?)', (val,))
        self.cur.execute(b'select f from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], 47.2)
        return

    def CheckBool(self):
        self.cur.execute(b'insert into test(b) values (?)', (False,))
        self.cur.execute(b'select b from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], False)
        self.cur.execute(b'delete from test')
        self.cur.execute(b'insert into test(b) values (?)', (True,))
        self.cur.execute(b'select b from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], True)
        return

    def CheckUnicode(self):
        val = u'\xd6sterreich'
        self.cur.execute(b'insert into test(u) values (?)', (val,))
        self.cur.execute(b'select u from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)
        return

    def CheckFoo(self):
        val = DeclTypesTests.Foo(b'bla')
        self.cur.execute(b'insert into test(foo) values (?)', (val,))
        self.cur.execute(b'select foo from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)
        return

    def CheckUnsupportedSeq(self):

        class Bar:
            pass

        val = Bar()
        try:
            self.cur.execute(b'insert into test(f) values (?)', (val,))
            self.fail(b'should have raised an InterfaceError')
        except sqlite.InterfaceError:
            pass
        except:
            self.fail(b'should have raised an InterfaceError')

        return

    def CheckUnsupportedDict(self):

        class Bar:
            pass

        val = Bar()
        try:
            self.cur.execute(b'insert into test(f) values (:val)', {b'val': val})
            self.fail(b'should have raised an InterfaceError')
        except sqlite.InterfaceError:
            pass
        except:
            self.fail(b'should have raised an InterfaceError')

        return

    def CheckBlob(self):
        with test_support.check_py3k_warnings():
            val = buffer(b'Guglhupf')
        self.cur.execute(b'insert into test(bin) values (?)', (val,))
        self.cur.execute(b'select bin from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)
        return

    def CheckNumber1(self):
        self.cur.execute(b'insert into test(n1) values (5)')
        value = self.cur.execute(b'select n1 from test').fetchone()[0]
        self.assertEqual(type(value), float)
        return

    def CheckNumber2(self):
        self.cur.execute(b'insert into test(n2) values (5)')
        value = self.cur.execute(b'select n2 from test').fetchone()[0]
        self.assertEqual(type(value), float)
        return


class ColNamesTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:', detect_types=sqlite.PARSE_COLNAMES)
        self.cur = self.con.cursor()
        self.cur.execute(b'create table test(x foo)')
        sqlite.converters[b'FOO'] = lambda x: b'[%s]' % x
        sqlite.converters[b'BAR'] = lambda x: b'<%s>' % x
        sqlite.converters[b'EXC'] = lambda x: 5 // 0
        sqlite.converters[b'B1B1'] = lambda x: b'MARKER'
        return

    def tearDown(self):
        del sqlite.converters[b'FOO']
        del sqlite.converters[b'BAR']
        del sqlite.converters[b'EXC']
        del sqlite.converters[b'B1B1']
        self.cur.close()
        self.con.close()
        return

    def CheckDeclTypeNotUsed(self):
        self.cur.execute(b'insert into test(x) values (?)', (b'xxx',))
        self.cur.execute(b'select x from test')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, b'xxx')
        return

    def CheckNone(self):
        self.cur.execute(b'insert into test(x) values (?)', (None,))
        self.cur.execute(b'select x from test')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, None)
        return

    def CheckColName(self):
        self.cur.execute(b'insert into test(x) values (?)', (b'xxx',))
        self.cur.execute(b'select x as "x [bar]" from test')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, b'<xxx>')
        self.assertEqual(self.cur.description[0][0], b'x')
        return

    def CheckCaseInConverterName(self):
        self.cur.execute(b'select \'other\' as "x [b1b1]"')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, b'MARKER')
        return

    def CheckCursorDescriptionNoRow(self):
        self.cur.execute(b'select * from test where 0 = 1')
        self.assertEqual(self.cur.description[0][0], b'x')
        return


class ObjectAdaptationTests(unittest.TestCase):

    def cast(obj):
        return float(obj)

    cast = staticmethod(cast)

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        try:
            del sqlite.adapters[int]
        except:
            pass

        sqlite.register_adapter(int, ObjectAdaptationTests.cast)
        self.cur = self.con.cursor()
        return

    def tearDown(self):
        del sqlite.adapters[(int, sqlite.PrepareProtocol)]
        self.cur.close()
        self.con.close()
        return

    def CheckCasterIsUsed(self):
        self.cur.execute(b'select ?', (4,))
        val = self.cur.fetchone()[0]
        self.assertEqual(type(val), float)
        return


@unittest.skipUnless(zlib, b'requires zlib')
class BinaryConverterTests(unittest.TestCase):

    def convert(s):
        return zlib.decompress(s)

    convert = staticmethod(convert)

    def setUp(self):
        self.con = sqlite.connect(b':memory:', detect_types=sqlite.PARSE_COLNAMES)
        sqlite.register_converter(b'bin', BinaryConverterTests.convert)
        return

    def tearDown(self):
        self.con.close()
        return

    def CheckBinaryInputForConverter(self):
        testdata = b'abcdefg' * 10
        with test_support.check_py3k_warnings():
            result = self.con.execute(b'select ? as "x [bin]"', (buffer(zlib.compress(testdata)),)).fetchone()[0]
        self.assertEqual(testdata, result)
        return


class DateTimeTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:', detect_types=sqlite.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.cur.execute(b'create table test(d date, ts timestamp)')
        return

    def tearDown(self):
        self.cur.close()
        self.con.close()
        return

    def CheckSqliteDate(self):
        d = sqlite.Date(2004, 2, 14)
        self.cur.execute(b'insert into test(d) values (?)', (d,))
        self.cur.execute(b'select d from test')
        d2 = self.cur.fetchone()[0]
        self.assertEqual(d, d2)
        return

    def CheckSqliteTimestamp(self):
        ts = sqlite.Timestamp(2004, 2, 14, 7, 15, 0)
        self.cur.execute(b'insert into test(ts) values (?)', (ts,))
        self.cur.execute(b'select ts from test')
        ts2 = self.cur.fetchone()[0]
        self.assertEqual(ts, ts2)
        return

    def CheckSqlTimestamp(self):
        if sqlite.sqlite_version_info < (3, 1):
            return
        now = datetime.datetime.utcnow()
        self.cur.execute(b'insert into test(ts) values (current_timestamp)')
        self.cur.execute(b'select ts from test')
        ts = self.cur.fetchone()[0]
        self.assertEqual(type(ts), datetime.datetime)
        self.assertEqual(ts.year, now.year)
        return

    def CheckDateTimeSubSeconds(self):
        ts = sqlite.Timestamp(2004, 2, 14, 7, 15, 0, 500000)
        self.cur.execute(b'insert into test(ts) values (?)', (ts,))
        self.cur.execute(b'select ts from test')
        ts2 = self.cur.fetchone()[0]
        self.assertEqual(ts, ts2)
        return

    def CheckDateTimeSubSecondsFloatingPoint(self):
        ts = sqlite.Timestamp(2004, 2, 14, 7, 15, 0, 510241)
        self.cur.execute(b'insert into test(ts) values (?)', (ts,))
        self.cur.execute(b'select ts from test')
        ts2 = self.cur.fetchone()[0]
        self.assertEqual(ts, ts2)
        return


def suite():
    sqlite_type_suite = unittest.makeSuite(SqliteTypeTests, b'Check')
    decltypes_type_suite = unittest.makeSuite(DeclTypesTests, b'Check')
    colnames_type_suite = unittest.makeSuite(ColNamesTests, b'Check')
    adaptation_suite = unittest.makeSuite(ObjectAdaptationTests, b'Check')
    bin_suite = unittest.makeSuite(BinaryConverterTests, b'Check')
    date_suite = unittest.makeSuite(DateTimeTests, b'Check')
    return unittest.TestSuite((sqlite_type_suite, decltypes_type_suite, colnames_type_suite, adaptation_suite, bin_suite, date_suite))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    return


if __name__ == b'__main__':
    test()
