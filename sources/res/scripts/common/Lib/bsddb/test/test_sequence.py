import unittest, os
from test_all import db, test_support, get_new_environment_path, get_new_database_path

class DBSequenceTest(unittest.TestCase):

    def setUp(self):
        self.int_32_max = 4294967296L
        self.homeDir = get_new_environment_path()
        self.filename = b'test'
        self.dbenv = db.DBEnv()
        self.dbenv.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL, 438)
        self.d = db.DB(self.dbenv)
        self.d.open(self.filename, db.DB_BTREE, db.DB_CREATE, 438)
        return

    def tearDown(self):
        if hasattr(self, b'seq'):
            self.seq.close()
            del self.seq
        if hasattr(self, b'd'):
            self.d.close()
            del self.d
        if hasattr(self, b'dbenv'):
            self.dbenv.close()
            del self.dbenv
        test_support.rmtree(self.homeDir)
        return

    def test_get(self):
        self.seq = db.DBSequence(self.d, flags=0)
        start_value = 10 * self.int_32_max
        self.assertEqual(42949672960L, start_value)
        self.assertEqual(None, self.seq.initial_value(start_value))
        self.assertEqual(None, self.seq.open(key=b'id', txn=None, flags=db.DB_CREATE))
        self.assertEqual(start_value, self.seq.get(5))
        self.assertEqual(start_value + 5, self.seq.get())
        return

    def test_remove(self):
        self.seq = db.DBSequence(self.d, flags=0)
        self.assertEqual(None, self.seq.open(key=b'foo', txn=None, flags=db.DB_CREATE))
        self.assertEqual(None, self.seq.remove(txn=None, flags=0))
        del self.seq
        return

    def test_get_key(self):
        self.seq = db.DBSequence(self.d, flags=0)
        key = b'foo'
        self.assertEqual(None, self.seq.open(key=key, txn=None, flags=db.DB_CREATE))
        self.assertEqual(key, self.seq.get_key())
        return

    def test_get_dbp(self):
        self.seq = db.DBSequence(self.d, flags=0)
        self.assertEqual(None, self.seq.open(key=b'foo', txn=None, flags=db.DB_CREATE))
        self.assertEqual(self.d, self.seq.get_dbp())
        return

    def test_cachesize(self):
        self.seq = db.DBSequence(self.d, flags=0)
        cashe_size = 10
        self.assertEqual(None, self.seq.set_cachesize(cashe_size))
        self.assertEqual(None, self.seq.open(key=b'foo', txn=None, flags=db.DB_CREATE))
        self.assertEqual(cashe_size, self.seq.get_cachesize())
        return

    def test_flags(self):
        self.seq = db.DBSequence(self.d, flags=0)
        flag = db.DB_SEQ_WRAP
        self.assertEqual(None, self.seq.set_flags(flag))
        self.assertEqual(None, self.seq.open(key=b'foo', txn=None, flags=db.DB_CREATE))
        self.assertEqual(flag, self.seq.get_flags() & flag)
        return

    def test_range(self):
        self.seq = db.DBSequence(self.d, flags=0)
        seq_range = (10 * self.int_32_max, 11 * self.int_32_max - 1)
        self.assertEqual(None, self.seq.set_range(seq_range))
        self.seq.initial_value(seq_range[0])
        self.assertEqual(None, self.seq.open(key=b'foo', txn=None, flags=db.DB_CREATE))
        self.assertEqual(seq_range, self.seq.get_range())
        return

    def test_stat(self):
        self.seq = db.DBSequence(self.d, flags=0)
        self.assertEqual(None, self.seq.open(key=b'foo', txn=None, flags=db.DB_CREATE))
        stat = self.seq.stat()
        for param in (b'nowait', b'min', b'max', b'value', b'current', b'flags', b'cache_size', b'last_value', b'wait'):
            self.assertIn(param, stat, b"parameter %s isn't in stat info" % param)

        return

    if db.version() >= (4, 7):

        def test_stat_crash(self):
            d = db.DB()
            d.open(None, dbtype=db.DB_HASH, flags=db.DB_CREATE)
            seq = db.DBSequence(d, flags=0)
            self.assertRaises(db.DBNotFoundError, seq.open, key=b'id', txn=None, flags=0)
            self.assertRaises(db.DBInvalidArgError, seq.stat)
            d.close()
            return

    def test_64bits(self):
        value_plus = 9223372036854775806L
        self.assertEqual(9223372036854775806L, value_plus)
        value_minus = -9223372036854775807L
        self.assertEqual(-9223372036854775807L, value_minus)
        self.seq = db.DBSequence(self.d, flags=0)
        self.assertEqual(None, self.seq.initial_value(value_plus - 1))
        self.assertEqual(None, self.seq.open(key=b'id', txn=None, flags=db.DB_CREATE))
        self.assertEqual(value_plus - 1, self.seq.get(1))
        self.assertEqual(value_plus, self.seq.get(1))
        self.seq.remove(txn=None, flags=0)
        self.seq = db.DBSequence(self.d, flags=0)
        self.assertEqual(None, self.seq.initial_value(value_minus))
        self.assertEqual(None, self.seq.open(key=b'id', txn=None, flags=db.DB_CREATE))
        self.assertEqual(value_minus, self.seq.get(1))
        self.assertEqual(value_minus + 1, self.seq.get(1))
        return

    def test_multiple_close(self):
        self.seq = db.DBSequence(self.d)
        self.seq.close()
        self.seq.close()
        self.seq.close()
        return


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DBSequenceTest))
    return suite


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
