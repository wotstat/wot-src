from __future__ import with_statement
import unittest, sqlite3 as sqlite
did_rollback = False

class MyConnection(sqlite.Connection):

    def rollback(self):
        global did_rollback
        did_rollback = True
        sqlite.Connection.rollback(self)
        return


class ContextTests(unittest.TestCase):

    def setUp(self):
        global did_rollback
        self.con = sqlite.connect(b':memory:', factory=MyConnection)
        self.con.execute(b'create table test(c unique)')
        did_rollback = False
        return

    def tearDown(self):
        self.con.close()
        return

    def CheckContextManager(self):
        with self.con:
            pass
        return

    def CheckContextManagerCommit(self):
        with self.con:
            self.con.execute(b"insert into test(c) values ('foo')")
        self.con.rollback()
        count = self.con.execute(b'select count(*) from test').fetchone()[0]
        self.assertEqual(count, 1)
        return

    def CheckContextManagerRollback(self):
        self.assertEqual(did_rollback, False)
        try:
            with self.con:
                self.con.execute(b'insert into test(c) values (4)')
                self.con.execute(b'insert into test(c) values (4)')
        except sqlite.IntegrityError:
            pass

        self.assertEqual(did_rollback, True)
        return


def suite():
    ctx_suite = unittest.makeSuite(ContextTests, b'Check')
    return unittest.TestSuite((ctx_suite,))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    return


if __name__ == b'__main__':
    test()
