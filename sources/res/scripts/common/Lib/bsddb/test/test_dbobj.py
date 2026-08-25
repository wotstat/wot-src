import os, string, unittest
from test_all import db, dbobj, test_support, get_new_environment_path, get_new_database_path

class dbobjTestCase(unittest.TestCase):
    db_name = b'test-dbobj.db'

    def setUp(self):
        self.homeDir = get_new_environment_path()
        return

    def tearDown(self):
        if hasattr(self, b'db'):
            del self.db
        if hasattr(self, b'env'):
            del self.env
        test_support.rmtree(self.homeDir)
        return

    def test01_both(self):

        class TestDBEnv(dbobj.DBEnv):
            pass

        class TestDB(dbobj.DB):

            def put(self, key, *args, **kwargs):
                key = key.upper()
                return dbobj.DB.put(self, key, *args, **kwargs)

        self.env = TestDBEnv()
        self.env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL)
        self.db = TestDB(self.env)
        self.db.open(self.db_name, db.DB_HASH, db.DB_CREATE)
        self.db.put(b'spam', b'eggs')
        self.assertEqual(self.db.get(b'spam'), None, b'overridden dbobj.DB.put() method failed [1]')
        self.assertEqual(self.db.get(b'SPAM'), b'eggs', b'overridden dbobj.DB.put() method failed [2]')
        self.db.close()
        self.env.close()
        return

    def test02_dbobj_dict_interface(self):
        self.env = dbobj.DBEnv()
        self.env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL)
        self.db = dbobj.DB(self.env)
        self.db.open(self.db_name + b'02', db.DB_HASH, db.DB_CREATE)
        self.db[b'spam'] = b'eggs'
        self.assertEqual(len(self.db), 1)
        self.assertEqual(self.db[b'spam'], b'eggs')
        del self.db[b'spam']
        self.assertEqual(self.db.get(b'spam'), None, b'dbobj __del__ failed')
        self.db.close()
        self.env.close()
        return

    def test03_dbobj_type_before_open(self):
        self.assertRaises(db.DBInvalidArgError, db.DB().type)
        return


def test_suite():
    return unittest.makeSuite(dbobjTestCase)


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
