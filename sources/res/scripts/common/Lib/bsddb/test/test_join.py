import os, unittest
from test_all import db, dbshelve, test_support, verbose, get_new_environment_path, get_new_database_path
ProductIndex = [
 20, 
 21, 
 22, 
 23, 
 24, 
 25]
ColorIndex = [
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32]

class JoinTestCase(unittest.TestCase):
    keytype = b''

    def setUp(self):
        self.filename = self.__class__.__name__ + b'.db'
        self.homeDir = get_new_environment_path()
        self.env = db.DBEnv()
        self.env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL | db.DB_INIT_LOCK)
        return

    def tearDown(self):
        self.env.close()
        test_support.rmtree(self.homeDir)
        return

    def test01_join(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test01_join...' % self.__class__.__name__
        priDB = db.DB(self.env)
        priDB.open(self.filename, b'primary', db.DB_BTREE, db.DB_CREATE)
        map((lambda t, priDB=priDB: priDB.put(*t)), ProductIndex)
        secDB = db.DB(self.env)
        secDB.set_flags(db.DB_DUP | db.DB_DUPSORT)
        secDB.open(self.filename, b'secondary', db.DB_BTREE, db.DB_CREATE)
        map((lambda t, secDB=secDB: secDB.put(*t)), ColorIndex)
        sCursor = None
        jCursor = None
        try:
            sCursor = secDB.cursor()
            tmp = sCursor.set(b'red')
            self.assertTrue(tmp)
            jCursor = priDB.join([sCursor])
            if jCursor.get(0) != (b'apple', b'Convenience Store'):
                self.fail(b'join cursor positioned wrong')
            if jCursor.join_item() != b'chainsaw':
                self.fail(b'DBCursor.join_item returned wrong item')
            if jCursor.get(0)[0] != b'strawberry':
                self.fail(b'join cursor returned wrong thing')
            if jCursor.get(0):
                self.fail(b'join cursor returned too many items')
        finally:
            if jCursor:
                jCursor.close()
            if sCursor:
                sCursor.close()
            priDB.close()
            secDB.close()

        return


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(JoinTestCase))
    return suite
