import sys, os, unittest, sqlite3 as sqlite

def get_db_path():
    return b'sqlite_testdb'


class TransactionTests(unittest.TestCase):

    def setUp(self):
        try:
            os.remove(get_db_path())
        except OSError:
            pass

        self.con1 = sqlite.connect(get_db_path(), timeout=0.1)
        self.cur1 = self.con1.cursor()
        self.con2 = sqlite.connect(get_db_path(), timeout=0.1)
        self.cur2 = self.con2.cursor()
        return

    def tearDown(self):
        self.cur1.close()
        self.con1.close()
        self.cur2.close()
        self.con2.close()
        try:
            os.unlink(get_db_path())
        except OSError:
            pass

        return

    def CheckDMLdoesAutoCommitBefore(self):
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        self.cur1.execute(b'create table test2(j)')
        self.cur2.execute(b'select i from test')
        res = self.cur2.fetchall()
        self.assertEqual(len(res), 1)
        return

    def CheckInsertStartsTransaction(self):
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        self.cur2.execute(b'select i from test')
        res = self.cur2.fetchall()
        self.assertEqual(len(res), 0)
        return

    def CheckUpdateStartsTransaction(self):
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        self.con1.commit()
        self.cur1.execute(b'update test set i=6')
        self.cur2.execute(b'select i from test')
        res = self.cur2.fetchone()[0]
        self.assertEqual(res, 5)
        return

    def CheckDeleteStartsTransaction(self):
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        self.con1.commit()
        self.cur1.execute(b'delete from test')
        self.cur2.execute(b'select i from test')
        res = self.cur2.fetchall()
        self.assertEqual(len(res), 1)
        return

    def CheckReplaceStartsTransaction(self):
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        self.con1.commit()
        self.cur1.execute(b'replace into test(i) values (6)')
        self.cur2.execute(b'select i from test')
        res = self.cur2.fetchall()
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0][0], 5)
        return

    def CheckToggleAutoCommit(self):
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        self.con1.isolation_level = None
        self.assertEqual(self.con1.isolation_level, None)
        self.cur2.execute(b'select i from test')
        res = self.cur2.fetchall()
        self.assertEqual(len(res), 1)
        self.con1.isolation_level = b'DEFERRED'
        self.assertEqual(self.con1.isolation_level, b'DEFERRED')
        self.cur1.execute(b'insert into test(i) values (5)')
        self.cur2.execute(b'select i from test')
        res = self.cur2.fetchall()
        self.assertEqual(len(res), 1)
        return

    def CheckRaiseTimeout(self):
        if sqlite.sqlite_version_info < (3, 2, 2):
            return
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        try:
            self.cur2.execute(b'insert into test(i) values (5)')
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError:
            pass
        except:
            self.fail(b'should have raised an OperationalError')

        return

    def CheckLocking(self):
        if sqlite.sqlite_version_info < (3, 2, 2):
            return
        self.cur1.execute(b'create table test(i)')
        self.cur1.execute(b'insert into test(i) values (5)')
        try:
            self.cur2.execute(b'insert into test(i) values (5)')
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError:
            pass
        except:
            self.fail(b'should have raised an OperationalError')

        self.con1.commit()
        return

    def CheckRollbackCursorConsistency(self):
        con = sqlite.connect(b':memory:')
        cur = con.cursor()
        cur.execute(b'create table test(x)')
        cur.execute(b'insert into test(x) values (5)')
        cur.execute(b'select 1 union select 2 union select 3')
        con.rollback()
        try:
            cur.fetchall()
            self.fail(b'InterfaceError should have been raised')
        except sqlite.InterfaceError as e:
            pass
        except:
            self.fail(b'InterfaceError should have been raised')

        return


class SpecialCommandTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(b':memory:')
        self.cur = self.con.cursor()
        return

    def CheckVacuum(self):
        self.cur.execute(b'create table test(i)')
        self.cur.execute(b'insert into test(i) values (5)')
        self.cur.execute(b'vacuum')
        return

    def CheckDropTable(self):
        self.cur.execute(b'create table test(i)')
        self.cur.execute(b'insert into test(i) values (5)')
        self.cur.execute(b'drop table test')
        return

    def CheckPragma(self):
        self.cur.execute(b'create table test(i)')
        self.cur.execute(b'insert into test(i) values (5)')
        self.cur.execute(b'pragma count_changes=1')
        return

    def tearDown(self):
        self.cur.close()
        self.con.close()
        return


def suite():
    default_suite = unittest.makeSuite(TransactionTests, b'Check')
    special_command_suite = unittest.makeSuite(SpecialCommandTests, b'Check')
    return unittest.TestSuite((default_suite, special_command_suite))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    return


if __name__ == b'__main__':
    test()
