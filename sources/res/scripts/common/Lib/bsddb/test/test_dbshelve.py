import os, string, sys, random, unittest
from test_all import db, dbshelve, test_support, verbose, get_new_environment_path, get_new_database_path

class DataClass:

    def __init__(self):
        self.value = random.random()
        return

    def __repr__(self):
        return b'DataClass %f' % self.value

    def __cmp__(self, other):
        return cmp(self.value, other)


class DBShelveTestCase(unittest.TestCase):
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0) and sys.version_info < (3, 2):

        def assertIn(self, a, b, msg=None):
            return self.assertTrue(a in b, msg=msg)

    def setUp(self):
        if sys.version_info[0] >= 3:
            from test_all import do_proxy_db_py3k
            self._flag_proxy_db_py3k = do_proxy_db_py3k(False)
        self.filename = get_new_database_path()
        self.do_open()
        return

    def tearDown(self):
        if sys.version_info[0] >= 3:
            from test_all import do_proxy_db_py3k
            do_proxy_db_py3k(self._flag_proxy_db_py3k)
        self.do_close()
        test_support.unlink(self.filename)
        return

    def mk(self, key):
        if sys.version_info[0] < 3:
            return key
        else:
            return bytes(key, b'iso8859-1')

        return

    def populateDB(self, d):
        for x in string.ascii_letters:
            d[self.mk(b'S' + x)] = 10 * x
            d[self.mk(b'I' + x)] = ord(x)
            d[self.mk(b'L' + x)] = [x] * 10
            inst = DataClass()
            inst.S = 10 * x
            inst.I = ord(x)
            inst.L = [x] * 10
            d[self.mk(b'O' + x)] = inst

        return

    def do_open(self):
        self.d = dbshelve.open(self.filename)
        return

    def do_close(self):
        self.d.close()
        return

    def test01_basics(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test01_basics...' % self.__class__.__name__
        self.populateDB(self.d)
        self.d.sync()
        self.do_close()
        self.do_open()
        d = self.d
        l = len(d)
        k = d.keys()
        s = d.stat()
        f = d.fd()
        if verbose:
            print b'length:', l
            print b'keys:', k
            print b'stats:', s
        self.assertEqual(0, d.has_key(self.mk(b'bad key')))
        self.assertEqual(1, d.has_key(self.mk(b'IA')))
        self.assertEqual(1, d.has_key(self.mk(b'OA')))
        d.delete(self.mk(b'IA'))
        del d[self.mk(b'OA')]
        self.assertEqual(0, d.has_key(self.mk(b'IA')))
        self.assertEqual(0, d.has_key(self.mk(b'OA')))
        self.assertEqual(len(d), l - 2)
        values = []
        for key in d.keys():
            value = d[key]
            values.append(value)
            if verbose:
                print b'%s: %s' % (key, value)
            self.checkrec(key, value)

        dbvalues = d.values()
        self.assertEqual(len(dbvalues), len(d.keys()))
        if sys.version_info < (2, 6):
            values.sort()
            dbvalues.sort()
            self.assertEqual(values, dbvalues)
        else:
            values.sort(key=(lambda x: str(x)))
            dbvalues.sort(key=(lambda x: str(x)))
            self.assertEqual(repr(values), repr(dbvalues))
        items = d.items()
        self.assertEqual(len(items), len(values))
        for key, value in items:
            self.checkrec(key, value)

        self.assertEqual(d.get(self.mk(b'bad key')), None)
        self.assertEqual(d.get(self.mk(b'bad key'), None), None)
        self.assertEqual(d.get(self.mk(b'bad key'), b'a string'), b'a string')
        self.assertEqual(d.get(self.mk(b'bad key'), [1, 2, 3]), [1, 2, 3])
        d.set_get_returns_none(0)
        self.assertRaises(db.DBNotFoundError, d.get, self.mk(b'bad key'))
        d.set_get_returns_none(1)
        d.put(self.mk(b'new key'), b'new data')
        self.assertEqual(d.get(self.mk(b'new key')), b'new data')
        self.assertEqual(d[self.mk(b'new key')], b'new data')
        return

    def test02_cursors(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test02_cursors...' % self.__class__.__name__
        self.populateDB(self.d)
        d = self.d
        count = 0
        c = d.cursor()
        rec = c.first()
        while rec is not None:
            count = count + 1
            if verbose:
                print rec
            key, value = rec
            self.checkrec(key, value)
            rec = getattr(c, b'next')()

        del c
        self.assertEqual(count, len(d))
        count = 0
        c = d.cursor()
        rec = c.last()
        while rec is not None:
            count = count + 1
            if verbose:
                print rec
            key, value = rec
            self.checkrec(key, value)
            rec = c.prev()

        self.assertEqual(count, len(d))
        c.set(self.mk(b'SS'))
        key, value = c.current()
        self.checkrec(key, value)
        del c
        return

    def test03_append(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test03_append...' % self.__class__.__name__
        self.assertRaises(dbshelve.DBShelveError, self.d.append, b'unit test was here')
        return

    def test04_iterable(self):
        self.populateDB(self.d)
        d = self.d
        keys = d.keys()
        keyset = set(keys)
        self.assertEqual(len(keyset), len(keys))
        for key in d:
            self.assertIn(key, keyset)
            keyset.remove(key)

        self.assertEqual(len(keyset), 0)
        return

    def checkrec(self, key, value):
        if sys.version_info[0] >= 3:
            if isinstance(key, bytes):
                key = key.decode(b'iso8859-1')
        x = key[1]
        if key[0] == b'S':
            self.assertEqual(type(value), str)
            self.assertEqual(value, 10 * x)
        elif key[0] == b'I':
            self.assertEqual(type(value), int)
            self.assertEqual(value, ord(x))
        elif key[0] == b'L':
            self.assertEqual(type(value), list)
            self.assertEqual(value, [x] * 10)
        elif key[0] == b'O':
            if sys.version_info[0] < 3:
                from types import InstanceType
                self.assertEqual(type(value), InstanceType)
            else:
                self.assertEqual(type(value), DataClass)
            self.assertEqual(value.S, 10 * x)
            self.assertEqual(value.I, ord(x))
            self.assertEqual(value.L, [x] * 10)
        else:
            self.fail(b'Unknown key type, fix the test')
        return


class BasicShelveTestCase(DBShelveTestCase):

    def do_open(self):
        self.d = dbshelve.DBShelf()
        self.d.open(self.filename, self.dbtype, self.dbflags)
        return

    def do_close(self):
        self.d.close()
        return


class BTreeShelveTestCase(BasicShelveTestCase):
    dbtype = db.DB_BTREE
    dbflags = db.DB_CREATE


class HashShelveTestCase(BasicShelveTestCase):
    dbtype = db.DB_HASH
    dbflags = db.DB_CREATE


class ThreadBTreeShelveTestCase(BasicShelveTestCase):
    dbtype = db.DB_BTREE
    dbflags = db.DB_CREATE | db.DB_THREAD


class ThreadHashShelveTestCase(BasicShelveTestCase):
    dbtype = db.DB_HASH
    dbflags = db.DB_CREATE | db.DB_THREAD


class BasicEnvShelveTestCase(DBShelveTestCase):

    def do_open(self):
        self.env = db.DBEnv()
        self.env.open(self.homeDir, self.envflags | db.DB_INIT_MPOOL | db.DB_CREATE)
        self.filename = os.path.split(self.filename)[1]
        self.d = dbshelve.DBShelf(self.env)
        self.d.open(self.filename, self.dbtype, self.dbflags)
        return

    def do_close(self):
        self.d.close()
        self.env.close()
        return

    def setUp(self):
        self.homeDir = get_new_environment_path()
        DBShelveTestCase.setUp(self)
        return

    def tearDown(self):
        if sys.version_info[0] >= 3:
            from test_all import do_proxy_db_py3k
            do_proxy_db_py3k(self._flag_proxy_db_py3k)
        self.do_close()
        test_support.rmtree(self.homeDir)
        return


class EnvBTreeShelveTestCase(BasicEnvShelveTestCase):
    envflags = 0
    dbtype = db.DB_BTREE
    dbflags = db.DB_CREATE


class EnvHashShelveTestCase(BasicEnvShelveTestCase):
    envflags = 0
    dbtype = db.DB_HASH
    dbflags = db.DB_CREATE


class EnvThreadBTreeShelveTestCase(BasicEnvShelveTestCase):
    envflags = db.DB_THREAD
    dbtype = db.DB_BTREE
    dbflags = db.DB_CREATE | db.DB_THREAD


class EnvThreadHashShelveTestCase(BasicEnvShelveTestCase):
    envflags = db.DB_THREAD
    dbtype = db.DB_HASH
    dbflags = db.DB_CREATE | db.DB_THREAD


class RecNoShelveTestCase(BasicShelveTestCase):
    dbtype = db.DB_RECNO
    dbflags = db.DB_CREATE

    def setUp(self):
        BasicShelveTestCase.setUp(self)
        self.key_pool = list(range(1, 5000))
        self.key_map = {}
        self.intkey_map = {}
        return

    def mk(self, key):
        if key not in self.key_map:
            self.key_map[key] = self.key_pool.pop(0)
            self.intkey_map[self.key_map[key]] = key
        return self.key_map[key]

    def checkrec(self, intkey, value):
        key = self.intkey_map[intkey]
        BasicShelveTestCase.checkrec(self, key, value)
        return

    def test03_append(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test03_append...' % self.__class__.__name__
        self.d[1] = b'spam'
        self.d[5] = b'eggs'
        self.assertEqual(6, self.d.append(b'spam'))
        self.assertEqual(7, self.d.append(b'baked beans'))
        self.assertEqual(b'spam', self.d.get(6))
        self.assertEqual(b'spam', self.d.get(1))
        self.assertEqual(b'baked beans', self.d.get(7))
        self.assertEqual(b'eggs', self.d.get(5))
        return


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DBShelveTestCase))
    suite.addTest(unittest.makeSuite(BTreeShelveTestCase))
    suite.addTest(unittest.makeSuite(HashShelveTestCase))
    suite.addTest(unittest.makeSuite(ThreadBTreeShelveTestCase))
    suite.addTest(unittest.makeSuite(ThreadHashShelveTestCase))
    suite.addTest(unittest.makeSuite(EnvBTreeShelveTestCase))
    suite.addTest(unittest.makeSuite(EnvHashShelveTestCase))
    suite.addTest(unittest.makeSuite(EnvThreadBTreeShelveTestCase))
    suite.addTest(unittest.makeSuite(EnvThreadHashShelveTestCase))
    suite.addTest(unittest.makeSuite(RecNoShelveTestCase))
    return suite


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
