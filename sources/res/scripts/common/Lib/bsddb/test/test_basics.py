import os, errno, string
from pprint import pprint
import unittest, time, sys
from test_all import db, test_support, verbose, get_new_environment_path, get_new_database_path
DASH = b'-'

class VersionTestCase(unittest.TestCase):

    def test00_version(self):
        info = db.version()
        if verbose:
            print b'\n', b'-=' * 20
            print b'bsddb.db.version(): %s' % (info,)
            print db.DB_VERSION_STRING
            print b'-=' * 20
        self.assertEqual(info, (db.DB_VERSION_MAJOR, db.DB_VERSION_MINOR,
         db.DB_VERSION_PATCH))
        return


class BasicTestCase(unittest.TestCase):
    dbtype = db.DB_UNKNOWN
    cachesize = (0, 1048576, 1)
    dbopenflags = 0
    dbsetflags = 0
    dbmode = 432
    dbname = None
    useEnv = 0
    envflags = 0
    envsetflags = 0
    _numKeys = 1002

    def setUp(self):
        if self.useEnv:
            self.homeDir = get_new_environment_path()
            try:
                self.env = db.DBEnv()
                self.env.set_lg_max(1048576)
                self.env.set_tx_max(30)
                self._t = int(time.time())
                self.env.set_tx_timestamp(self._t)
                self.env.set_flags(self.envsetflags, 1)
                self.env.open(self.homeDir, self.envflags | db.DB_CREATE)
                self.filename = b'test'
            except:
                test_support.rmtree(self.homeDir)
                raise

        else:
            self.env = None
            self.filename = get_new_database_path()
        self.d = db.DB(self.env)
        if not self.useEnv:
            self.d.set_cachesize(*self.cachesize)
            cachesize = self.d.get_cachesize()
            self.assertEqual(cachesize[0], self.cachesize[0])
            self.assertEqual(cachesize[2], self.cachesize[2])
            self.assertEqual(125, int(100.0 * cachesize[1] / self.cachesize[1]))
        self.d.set_flags(self.dbsetflags)
        if self.dbname:
            self.d.open(self.filename, self.dbname, self.dbtype, self.dbopenflags | db.DB_CREATE, self.dbmode)
        else:
            self.d.open(self.filename, mode=self.dbmode, dbtype=self.dbtype, flags=self.dbopenflags | db.DB_CREATE)
        if not self.useEnv:
            self.assertRaises(db.DBInvalidArgError, self.d.set_cachesize, *self.cachesize)
        self.populateDB()
        return

    def tearDown(self):
        self.d.close()
        if self.env is not None:
            self.env.close()
            test_support.rmtree(self.homeDir)
        else:
            os.remove(self.filename)
        return

    def populateDB(self, _txn=None):
        d = self.d
        for x in range(self._numKeys // 2):
            key = b'%04d' % (self._numKeys - x)
            data = self.makeData(key)
            d.put(key, data, _txn)

        d.put(b'empty value', b'', _txn)
        for x in range(self._numKeys // 2 - 1):
            key = b'%04d' % x
            data = self.makeData(key)
            d.put(key, data, _txn)

        if _txn:
            _txn.commit()
        num = len(d)
        if verbose:
            print b'created %d records' % num
        return

    def makeData(self, key):
        return DASH.join([key] * 5)

    def test01_GetsAndPuts(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test01_GetsAndPuts...' % self.__class__.__name__
        for key in [5, 6, 7, 8, 9]:
            data = d.get(key)
            if verbose:
                print data

        self.assertEqual(d.get(b'0321'), b'0321-0321-0321-0321-0321')
        self.assertEqual(d.get(b'abcd'), None)
        try:
            d.delete(b'abcd')
        except db.DBNotFoundError as val:
            if sys.version_info < (2, 6):
                self.assertEqual(val[0], db.DB_NOTFOUND)
            else:
                self.assertEqual(val.args[0], db.DB_NOTFOUND)
            if verbose:
                print val
        else:
            self.fail(b'expected exception')

        d.put(b'abcd', b'a new record')
        self.assertEqual(d.get(b'abcd'), b'a new record')
        d.put(b'abcd', b'same key')
        if self.dbsetflags & db.DB_DUP:
            self.assertEqual(d.get(b'abcd'), b'a new record')
        else:
            self.assertEqual(d.get(b'abcd'), b'same key')
        try:
            d.put(b'abcd', b'this should fail', flags=db.DB_NOOVERWRITE)
        except db.DBKeyExistError as val:
            if sys.version_info < (2, 6):
                self.assertEqual(val[0], db.DB_KEYEXIST)
            else:
                self.assertEqual(val.args[0], db.DB_KEYEXIST)
            if verbose:
                print val
        else:
            self.fail(b'expected exception')

        if self.dbsetflags & db.DB_DUP:
            self.assertEqual(d.get(b'abcd'), b'a new record')
        else:
            self.assertEqual(d.get(b'abcd'), b'same key')
        d.sync()
        d.close()
        del d
        self.d = db.DB(self.env)
        if self.dbname:
            self.d.open(self.filename, self.dbname)
        else:
            self.d.open(self.filename)
        d = self.d
        self.assertEqual(d.get(b'0321'), b'0321-0321-0321-0321-0321')
        if self.dbsetflags & db.DB_DUP:
            self.assertEqual(d.get(b'abcd'), b'a new record')
        else:
            self.assertEqual(d.get(b'abcd'), b'same key')
        rec = d.get_both(b'0555', b'0555-0555-0555-0555-0555')
        if verbose:
            print rec
        self.assertEqual(d.get_both(b'0555', b'bad data'), None)
        data = d.get(b'bad key', b'bad data')
        self.assertEqual(data, b'bad data')
        data = d.get(b'bad key', self)
        self.assertEqual(data, self)
        s = d.stat()
        self.assertEqual(type(s), type({}))
        if verbose:
            print b'd.stat() returned this dictionary:'
            pprint(s)
        return

    def test02_DictionaryMethods(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test02_DictionaryMethods...' % self.__class__.__name__
        for key in [5, 6, 7, 8, 9]:
            data = d[key]
            self.assertEqual(data, self.makeData(key))
            if verbose:
                print data

        self.assertEqual(len(d), self._numKeys)
        keys = d.keys()
        self.assertEqual(len(keys), self._numKeys)
        self.assertEqual(type(keys), type([]))
        d[b'new record'] = b'a new record'
        self.assertEqual(len(d), self._numKeys + 1)
        keys = d.keys()
        self.assertEqual(len(keys), self._numKeys + 1)
        d[b'new record'] = b'a replacement record'
        self.assertEqual(len(d), self._numKeys + 1)
        keys = d.keys()
        self.assertEqual(len(keys), self._numKeys + 1)
        if verbose:
            print b'the first 10 keys are:'
            pprint(keys[:10])
        self.assertEqual(d[b'new record'], b'a replacement record')
        self.assertEqual(d.has_key(b'0001', None), 1)
        self.assertEqual(d.has_key(b'spam', txn=None), 0)
        items = d.items()
        self.assertEqual(len(items), self._numKeys + 1)
        self.assertEqual(type(items), type([]))
        self.assertEqual(type(items[0]), type(()))
        self.assertEqual(len(items[0]), 2)
        if verbose:
            print b'the first 10 items are:'
            pprint(items[:10])
        values = d.values()
        self.assertEqual(len(values), self._numKeys + 1)
        self.assertEqual(type(values), type([]))
        if verbose:
            print b'the first 10 values are:'
            pprint(values[:10])
        return

    def test02b_SequenceMethods(self):
        d = self.d
        for key in [1, 2, 3, 4, 5]:
            data = d[key]
            self.assertEqual(data, self.makeData(key))
            if verbose:
                print data

        self.assertTrue(hasattr(d, b'__contains__'))
        self.assertTrue(b'0401' in d)
        self.assertFalse(b'1234' in d)
        return

    def test03_SimpleCursorStuff(self, get_raises_error=0, set_raises_error=0):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test03_SimpleCursorStuff (get_error %s, set_error %s)...' % (
             self.__class__.__name__, get_raises_error, set_raises_error)
        if self.env and self.dbopenflags & db.DB_AUTO_COMMIT:
            txn = self.env.txn_begin()
        else:
            txn = None
        c = self.d.cursor(txn=txn)
        rec = c.first()
        count = 0
        while rec is not None:
            count = count + 1
            if verbose and count % 100 == 0:
                print rec
            try:
                rec = c.next()
            except db.DBNotFoundError as val:
                if get_raises_error:
                    if sys.version_info < (2, 6):
                        self.assertEqual(val[0], db.DB_NOTFOUND)
                    else:
                        self.assertEqual(val.args[0], db.DB_NOTFOUND)
                    if verbose:
                        print val
                    rec = None
                else:
                    self.fail(b'unexpected DBNotFoundError')

            self.assertEqual(c.get_current_size(), len(c.current()[1]), b'%s != len(%r)' % (c.get_current_size(), c.current()[1]))

        self.assertEqual(count, self._numKeys)
        rec = c.last()
        count = 0
        while rec is not None:
            count = count + 1
            if verbose and count % 100 == 0:
                print rec
            try:
                rec = c.prev()
            except db.DBNotFoundError as val:
                if get_raises_error:
                    if sys.version_info < (2, 6):
                        self.assertEqual(val[0], db.DB_NOTFOUND)
                    else:
                        self.assertEqual(val.args[0], db.DB_NOTFOUND)
                    if verbose:
                        print val
                    rec = None
                else:
                    self.fail(b'unexpected DBNotFoundError')

        self.assertEqual(count, self._numKeys)
        rec = c.set(b'0505')
        rec2 = c.current()
        self.assertEqual(rec, rec2)
        self.assertEqual(rec[0], b'0505')
        self.assertEqual(rec[1], self.makeData(b'0505'))
        self.assertEqual(c.get_current_size(), len(rec[1]))
        rec = c.set(b'empty value')
        self.assertEqual(rec[1], b'')
        self.assertEqual(c.get_current_size(), 0)
        try:
            n = c.set(b'bad key')
        except db.DBNotFoundError as val:
            if sys.version_info < (2, 6):
                self.assertEqual(val[0], db.DB_NOTFOUND)
            else:
                self.assertEqual(val.args[0], db.DB_NOTFOUND)
            if verbose:
                print val

        if set_raises_error:
            self.fail(b'expected exception')
        if n is not None:
            self.fail(b'expected None: %r' % (n,))
        rec = c.get_both(b'0404', self.makeData(b'0404'))
        self.assertEqual(rec, (b'0404', self.makeData(b'0404')))
        try:
            n = c.get_both(b'0404', b'bad data')
        except db.DBNotFoundError as val:
            if sys.version_info < (2, 6):
                self.assertEqual(val[0], db.DB_NOTFOUND)
            else:
                self.assertEqual(val.args[0], db.DB_NOTFOUND)
            if verbose:
                print val

        if get_raises_error:
            self.fail(b'expected exception')
        if n is not None:
            self.fail(b'expected None: %r' % (n,))
        if self.d.get_type() == db.DB_BTREE:
            rec = c.set_range(b'011')
            if verbose:
                print b"searched for '011', found: ", rec
            rec = c.set_range(b'011', dlen=0, doff=0)
            if verbose:
                print b"searched (partial) for '011', found: ", rec
            if rec[1] != b'':
                self.fail(b'expected empty data portion')
            ev = c.set_range(b'empty value')
            if verbose:
                print b"search for 'empty value' returned", ev
            if ev[1] != b'':
                self.fail(b'empty value lookup failed')
        c.set(b'0499')
        c.delete()
        try:
            rec = c.current()
        except db.DBKeyEmptyError as val:
            if get_raises_error:
                if sys.version_info < (2, 6):
                    self.assertEqual(val[0], db.DB_KEYEMPTY)
                else:
                    self.assertEqual(val.args[0], db.DB_KEYEMPTY)
                if verbose:
                    print val
            else:
                self.fail(b'unexpected DBKeyEmptyError')

        if get_raises_error:
            self.fail(b'DBKeyEmptyError exception expected')
        c.next()
        c2 = c.dup(db.DB_POSITION)
        self.assertEqual(c.current(), c2.current())
        c2.put(b'', b'a new value', db.DB_CURRENT)
        self.assertEqual(c.current(), c2.current())
        self.assertEqual(c.current()[1], b'a new value')
        c2.put(b'', b'er', db.DB_CURRENT, dlen=0, doff=5)
        self.assertEqual(c2.current()[1], b'a newer value')
        c.close()
        c2.close()
        if txn:
            txn.commit()
        methods_to_test = {b'current': (), 
           b'delete': (), 
           b'dup': (
                  db.DB_POSITION,), 
           b'first': (), 
           b'get': (0,), 
           b'next': (), 
           b'prev': (), 
           b'last': (), 
           b'put': (
                  b'', b'spam', db.DB_CURRENT), 
           b'set': (b'0505',)}
        for method, args in methods_to_test.items():
            try:
                if verbose:
                    print b"attempting to use a closed cursor's %s method" % method
                getattr(c, method)(*args)
            except db.DBError as val:
                if sys.version_info < (2, 6):
                    self.assertEqual(val[0], 0)
                else:
                    self.assertEqual(val.args[0], 0)
                if verbose:
                    print val
            else:
                self.fail(b"no exception raised when using a buggy cursor's%s method" % method)

        oldcursor = self.d.cursor(txn=txn)
        self.d.close()
        del oldcursor
        return

    def test03b_SimpleCursorWithoutGetReturnsNone0(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test03b_SimpleCursorStuffWithoutGetReturnsNone...' % self.__class__.__name__
        old = self.d.set_get_returns_none(0)
        self.assertEqual(old, 2)
        self.test03_SimpleCursorStuff(get_raises_error=1, set_raises_error=1)
        return

    def test03b_SimpleCursorWithGetReturnsNone1(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test03b_SimpleCursorStuffWithoutGetReturnsNone...' % self.__class__.__name__
        old = self.d.set_get_returns_none(1)
        self.test03_SimpleCursorStuff(get_raises_error=0, set_raises_error=1)
        return

    def test03c_SimpleCursorGetReturnsNone2(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test03c_SimpleCursorStuffWithoutSetReturnsNone...' % self.__class__.__name__
        old = self.d.set_get_returns_none(1)
        self.assertEqual(old, 2)
        old = self.d.set_get_returns_none(2)
        self.assertEqual(old, 1)
        self.test03_SimpleCursorStuff(get_raises_error=0, set_raises_error=0)
        return

    if db.version() >= (4, 6):

        def test03d_SimpleCursorPriority(self):
            c = self.d.cursor()
            c.set_priority(db.DB_PRIORITY_VERY_LOW)
            self.assertEqual(db.DB_PRIORITY_VERY_LOW, c.get_priority())
            c.set_priority(priority=db.DB_PRIORITY_HIGH)
            self.assertEqual(db.DB_PRIORITY_HIGH, c.get_priority())
            c.close()
            return

    def test04_PartialGetAndPut(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test04_PartialGetAndPut...' % self.__class__.__name__
        key = b'partialTest'
        data = b'1' * 1000 + b'2' * 1000
        d.put(key, data)
        self.assertEqual(d.get(key), data)
        self.assertEqual(d.get(key, dlen=20, doff=990), b'1111111111' + b'2222222222')
        d.put(b'partialtest2', b'1' * 30000 + b'robin')
        self.assertEqual(d.get(b'partialtest2', dlen=5, doff=30000), b'robin')
        if self.dbsetflags != db.DB_DUP:
            d.put(key, b'0000', dlen=2000, doff=0)
            self.assertEqual(d.get(key), b'0000')
            d.put(key, b'1111', dlen=1, doff=2)
            self.assertEqual(d.get(key), b'0011110')
        return

    def test05_GetSize(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test05_GetSize...' % self.__class__.__name__
        for i in range(1, 50000, 500):
            key = b'size%s' % i
            d.put(key, b'1' * i)
            self.assertEqual(d.get_size(key), i)

        return

    def test06_Truncate(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test06_Truncate...' % self.__class__.__name__
        d.put(b'abcde', b'ABCDE')
        num = d.truncate()
        self.assertGreaterEqual(num, 1, b'truncate returned <= 0 on non-empty database')
        num = d.truncate()
        self.assertEqual(num, 0, b'truncate on empty DB returned nonzero (%r)' % (num,))
        return

    def test07_verify(self):
        self.d.close()
        d = db.DB(self.env)
        d.verify(self.filename)
        return

    if db.version() >= (4, 6):

        def test08_exists(self):
            self.d.put(b'abcde', b'ABCDE')
            self.assertEqual(self.d.exists(b'abcde'), True, b'DB->exists() returns wrong value')
            self.assertEqual(self.d.exists(b'x'), False, b'DB->exists() returns wrong value')
            return

    if db.version() >= (4, 7):

        def test_compact(self):
            d = self.d
            self.assertEqual(0, d.compact(flags=db.DB_FREELIST_ONLY))
            self.assertEqual(0, d.compact(flags=db.DB_FREELIST_ONLY))
            d.put(b'abcde', b'ABCDE')
            d.put(b'bcde', b'BCDE')
            d.put(b'abc', b'ABC')
            d.put(b'monty', b'python')
            d.delete(b'abc')
            d.delete(b'bcde')
            d.compact(start=b'abcde', stop=b'monty', txn=None, compact_fillpercent=42, compact_pages=1, compact_timeout=50000000, flags=db.DB_FREELIST_ONLY | db.DB_FREE_SPACE)
            return


class BasicBTreeTestCase(BasicTestCase):
    dbtype = db.DB_BTREE


class BasicHashTestCase(BasicTestCase):
    dbtype = db.DB_HASH


class BasicBTreeWithThreadFlagTestCase(BasicTestCase):
    dbtype = db.DB_BTREE
    dbopenflags = db.DB_THREAD


class BasicHashWithThreadFlagTestCase(BasicTestCase):
    dbtype = db.DB_HASH
    dbopenflags = db.DB_THREAD


class BasicWithEnvTestCase(BasicTestCase):
    dbopenflags = db.DB_THREAD
    useEnv = 1
    envflags = db.DB_THREAD | db.DB_INIT_MPOOL | db.DB_INIT_LOCK

    def test09_EnvRemoveAndRename(self):
        if not self.env:
            return
        else:
            if verbose:
                print b'\n', b'-=' * 30
                print b'Running %s.test09_EnvRemoveAndRename...' % self.__class__.__name__
            self.d.close()
            newname = self.filename + b'.renamed'
            self.env.dbrename(self.filename, None, newname)
            self.env.dbremove(newname)
            return


class BasicBTreeWithEnvTestCase(BasicWithEnvTestCase):
    dbtype = db.DB_BTREE


class BasicHashWithEnvTestCase(BasicWithEnvTestCase):
    dbtype = db.DB_HASH


class BasicTransactionTestCase(BasicTestCase):
    if sys.version_info < (2, 7) or sys.version_info >= (3, 0) and sys.version_info < (3, 2):

        def assertIn(self, a, b, msg=None):
            return self.assertTrue(a in b, msg=msg)

    dbopenflags = db.DB_THREAD | db.DB_AUTO_COMMIT
    useEnv = 1
    envflags = db.DB_THREAD | db.DB_INIT_MPOOL | db.DB_INIT_LOCK | db.DB_INIT_TXN
    envsetflags = db.DB_AUTO_COMMIT

    def tearDown(self):
        self.txn.commit()
        BasicTestCase.tearDown(self)
        return

    def populateDB(self):
        txn = self.env.txn_begin()
        BasicTestCase.populateDB(self, _txn=txn)
        self.txn = self.env.txn_begin()
        return

    def test06_Transactions(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test06_Transactions...' % self.__class__.__name__
        self.assertEqual(d.get(b'new rec', txn=self.txn), None)
        d.put(b'new rec', b'this is a new record', self.txn)
        self.assertEqual(d.get(b'new rec', txn=self.txn), b'this is a new record')
        self.txn.abort()
        self.assertEqual(d.get(b'new rec'), None)
        self.txn = self.env.txn_begin()
        self.assertEqual(d.get(b'new rec', txn=self.txn), None)
        d.put(b'new rec', b'this is a new record', self.txn)
        self.assertEqual(d.get(b'new rec', txn=self.txn), b'this is a new record')
        self.txn.commit()
        self.assertEqual(d.get(b'new rec'), b'this is a new record')
        self.txn = self.env.txn_begin()
        c = d.cursor(self.txn)
        rec = c.first()
        count = 0
        while rec is not None:
            count = count + 1
            if verbose and count % 100 == 0:
                print rec
            rec = c.next()

        self.assertEqual(count, self._numKeys + 1)
        c.close()
        self.txn.commit()
        self.env.txn_checkpoint(0, 0, 0)
        statDict = self.env.log_stat(0)
        self.assertIn(b'magic', statDict)
        self.assertIn(b'version', statDict)
        self.assertIn(b'cur_file', statDict)
        self.assertIn(b'region_nowait', statDict)
        logs = self.env.log_archive(db.DB_ARCH_ABS | db.DB_ARCH_LOG)
        self.assertNotEqual(logs, None)
        for log in logs:
            if verbose:
                print b'log file: ' + log
            logs = self.env.log_archive(db.DB_ARCH_REMOVE)
            self.assertFalse(logs)

        self.txn = self.env.txn_begin()
        return

    if db.version() >= (4, 6):

        def test08_exists(self):
            txn = self.env.txn_begin()
            self.d.put(b'abcde', b'ABCDE', txn=txn)
            txn.commit()
            txn = self.env.txn_begin()
            self.assertEqual(self.d.exists(b'abcde', txn=txn), True, b'DB->exists() returns wrong value')
            self.assertEqual(self.d.exists(b'x', txn=txn), False, b'DB->exists() returns wrong value')
            txn.abort()
            return

    def test09_TxnTruncate(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test09_TxnTruncate...' % self.__class__.__name__
        d.put(b'abcde', b'ABCDE')
        txn = self.env.txn_begin()
        num = d.truncate(txn)
        self.assertGreaterEqual(num, 1, b'truncate returned <= 0 on non-empty database')
        num = d.truncate(txn)
        self.assertEqual(num, 0, b'truncate on empty DB returned nonzero (%r)' % (num,))
        txn.commit()
        return

    def test10_TxnLateUse(self):
        txn = self.env.txn_begin()
        txn.abort()
        try:
            txn.abort()
        except db.DBError as e:
            pass
        else:
            raise RuntimeError, b'DBTxn.abort() called after DB_TXN no longer valid w/o an exception'

        txn = self.env.txn_begin()
        txn.commit()
        try:
            txn.commit()
        except db.DBError as e:
            pass
        else:
            raise RuntimeError, b'DBTxn.commit() called after DB_TXN no longer valid w/o an exception'

        return

    if db.version() >= (4, 4):

        def test_txn_name(self):
            txn = self.env.txn_begin()
            self.assertEqual(txn.get_name(), b'')
            txn.set_name(b'XXYY')
            self.assertEqual(txn.get_name(), b'XXYY')
            txn.set_name(b'')
            self.assertEqual(txn.get_name(), b'')
            txn.abort()
            return

        def test_txn_set_timeout(self):
            txn = self.env.txn_begin()
            txn.set_timeout(1234567, db.DB_SET_LOCK_TIMEOUT)
            txn.set_timeout(2345678, flags=db.DB_SET_TXN_TIMEOUT)
            txn.abort()
            return

        def test_get_tx_max(self):
            self.assertEqual(self.env.get_tx_max(), 30)
            return

        def test_get_tx_timestamp(self):
            self.assertEqual(self.env.get_tx_timestamp(), self._t)
            return


class BTreeTransactionTestCase(BasicTransactionTestCase):
    dbtype = db.DB_BTREE


class HashTransactionTestCase(BasicTransactionTestCase):
    dbtype = db.DB_HASH


class BTreeRecnoTestCase(BasicTestCase):
    dbtype = db.DB_BTREE
    dbsetflags = db.DB_RECNUM

    def test09_RecnoInBTree(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test09_RecnoInBTree...' % self.__class__.__name__
        rec = d.get(200)
        self.assertEqual(type(rec), type(()))
        self.assertEqual(len(rec), 2)
        if verbose:
            print b'Record #200 is ', rec
        c = d.cursor()
        c.set(b'0200')
        num = c.get_recno()
        self.assertEqual(type(num), type(1))
        if verbose:
            print b"recno of d['0200'] is ", num
        rec = c.current()
        self.assertEqual(c.set_recno(num), rec)
        c.close()
        return


class BTreeRecnoWithThreadFlagTestCase(BTreeRecnoTestCase):
    dbopenflags = db.DB_THREAD


class BasicDUPTestCase(BasicTestCase):
    dbsetflags = db.DB_DUP

    def test10_DuplicateKeys(self):
        d = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test10_DuplicateKeys...' % self.__class__.__name__
        d.put(b'dup0', b'before')
        for x in (b'The quick brown fox jumped over the lazy dog.').split():
            d.put(b'dup1', x)

        d.put(b'dup2', b'after')
        data = d.get(b'dup1')
        self.assertEqual(data, b'The')
        if verbose:
            print data
        c = d.cursor()
        rec = c.set(b'dup1')
        self.assertEqual(rec, (b'dup1', b'The'))
        next_reg = c.next()
        self.assertEqual(next_reg, (b'dup1', b'quick'))
        rec = c.set(b'dup1')
        count = c.count()
        self.assertEqual(count, 9)
        next_dup = c.next_dup()
        self.assertEqual(next_dup, (b'dup1', b'quick'))
        rec = c.set(b'dup1')
        while rec is not None:
            if verbose:
                print rec
            rec = c.next_dup()

        c.set(b'dup1')
        rec = c.next_nodup()
        self.assertNotEqual(rec[0], b'dup1')
        if verbose:
            print rec
        c.close()
        return


class BTreeDUPTestCase(BasicDUPTestCase):
    dbtype = db.DB_BTREE


class HashDUPTestCase(BasicDUPTestCase):
    dbtype = db.DB_HASH


class BTreeDUPWithThreadTestCase(BasicDUPTestCase):
    dbtype = db.DB_BTREE
    dbopenflags = db.DB_THREAD


class HashDUPWithThreadTestCase(BasicDUPTestCase):
    dbtype = db.DB_HASH
    dbopenflags = db.DB_THREAD


class BasicMultiDBTestCase(BasicTestCase):
    dbname = b'first'

    def otherType(self):
        if self.dbtype == db.DB_BTREE:
            return db.DB_HASH
        else:
            return db.DB_BTREE

        return

    def test11_MultiDB(self):
        d1 = self.d
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test11_MultiDB...' % self.__class__.__name__
        d2 = db.DB(self.env)
        d2.open(self.filename, b'second', self.dbtype, self.dbopenflags | db.DB_CREATE)
        d3 = db.DB(self.env)
        d3.open(self.filename, b'third', self.otherType(), self.dbopenflags | db.DB_CREATE)
        for x in (b'The quick brown fox jumped over the lazy dog').split():
            d2.put(x, self.makeData(x))

        for x in string.ascii_letters:
            d3.put(x, x * 70)

        d1.sync()
        d2.sync()
        d3.sync()
        d1.close()
        d2.close()
        d3.close()
        self.d = d1 = d2 = d3 = None
        self.d = d1 = db.DB(self.env)
        d1.open(self.filename, self.dbname, flags=self.dbopenflags)
        d2 = db.DB(self.env)
        d2.open(self.filename, b'second', flags=self.dbopenflags)
        d3 = db.DB(self.env)
        d3.open(self.filename, b'third', flags=self.dbopenflags)
        c1 = d1.cursor()
        c2 = d2.cursor()
        c3 = d3.cursor()
        count = 0
        rec = c1.first()
        while rec is not None:
            count = count + 1
            if verbose and count % 50 == 0:
                print rec
            rec = c1.next()

        self.assertEqual(count, self._numKeys)
        count = 0
        rec = c2.first()
        while rec is not None:
            count = count + 1
            if verbose:
                print rec
            rec = c2.next()

        self.assertEqual(count, 9)
        count = 0
        rec = c3.first()
        while rec is not None:
            count = count + 1
            if verbose:
                print rec
            rec = c3.next()

        self.assertEqual(count, len(string.ascii_letters))
        c1.close()
        c2.close()
        c3.close()
        d2.close()
        d3.close()
        return


class BTreeMultiDBTestCase(BasicMultiDBTestCase):
    dbtype = db.DB_BTREE
    dbopenflags = db.DB_THREAD
    useEnv = 1
    envflags = db.DB_THREAD | db.DB_INIT_MPOOL | db.DB_INIT_LOCK


class HashMultiDBTestCase(BasicMultiDBTestCase):
    dbtype = db.DB_HASH
    dbopenflags = db.DB_THREAD
    useEnv = 1
    envflags = db.DB_THREAD | db.DB_INIT_MPOOL | db.DB_INIT_LOCK


class PrivateObject(unittest.TestCase):

    def tearDown(self):
        del self.obj
        return

    def test01_DefaultIsNone(self):
        self.assertEqual(self.obj.get_private(), None)
        return

    def test02_assignment(self):
        a = b'example of private object'
        self.obj.set_private(a)
        b = self.obj.get_private()
        self.assertIs(a, b)
        return

    def test03_leak_assignment(self):
        a = b'example of private object'
        refcount = sys.getrefcount(a)
        self.obj.set_private(a)
        self.assertEqual(refcount + 1, sys.getrefcount(a))
        self.obj.set_private(None)
        self.assertEqual(refcount, sys.getrefcount(a))
        return

    def test04_leak_GC(self):
        a = b'example of private object'
        refcount = sys.getrefcount(a)
        self.obj.set_private(a)
        self.obj = None
        self.assertEqual(refcount, sys.getrefcount(a))
        return


class DBEnvPrivateObject(PrivateObject):

    def setUp(self):
        self.obj = db.DBEnv()
        return


class DBPrivateObject(PrivateObject):

    def setUp(self):
        self.obj = db.DB()
        return


class CrashAndBurn(unittest.TestCase):
    if db.version() < (4, 8):

        def test02_DBEnv_dealloc(self):
            import gc
            self.assertRaises(db.DBInvalidArgError, db.DBEnv, ~db.DB_RPCCLIENT)
            gc.collect()
            return


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(VersionTestCase))
    suite.addTest(unittest.makeSuite(BasicBTreeTestCase))
    suite.addTest(unittest.makeSuite(BasicHashTestCase))
    suite.addTest(unittest.makeSuite(BasicBTreeWithThreadFlagTestCase))
    suite.addTest(unittest.makeSuite(BasicHashWithThreadFlagTestCase))
    suite.addTest(unittest.makeSuite(BasicBTreeWithEnvTestCase))
    suite.addTest(unittest.makeSuite(BasicHashWithEnvTestCase))
    suite.addTest(unittest.makeSuite(BTreeTransactionTestCase))
    suite.addTest(unittest.makeSuite(HashTransactionTestCase))
    suite.addTest(unittest.makeSuite(BTreeRecnoTestCase))
    suite.addTest(unittest.makeSuite(BTreeRecnoWithThreadFlagTestCase))
    suite.addTest(unittest.makeSuite(BTreeDUPTestCase))
    suite.addTest(unittest.makeSuite(HashDUPTestCase))
    suite.addTest(unittest.makeSuite(BTreeDUPWithThreadTestCase))
    suite.addTest(unittest.makeSuite(HashDUPWithThreadTestCase))
    suite.addTest(unittest.makeSuite(BTreeMultiDBTestCase))
    suite.addTest(unittest.makeSuite(HashMultiDBTestCase))
    suite.addTest(unittest.makeSuite(DBEnvPrivateObject))
    suite.addTest(unittest.makeSuite(DBPrivateObject))
    suite.addTest(unittest.makeSuite(CrashAndBurn))
    return suite


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
