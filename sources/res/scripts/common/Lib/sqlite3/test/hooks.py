import os, unittest, sqlite3 as sqlite

class CollationTests(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

    def CheckCreateCollationNotString(self):
        con = sqlite.connect(b':memory:')
        with self.assertRaises(TypeError):
            con.create_collation(None, (lambda x, y: (x > y) - (x < y)))
        return

    def CheckCreateCollationNotCallable(self):
        con = sqlite.connect(b':memory:')
        try:
            con.create_collation(b'X', 42)
            self.fail(b'should have raised a TypeError')
        except TypeError as e:
            self.assertEqual(e.args[0], b'parameter must be callable')

        return

    def CheckCreateCollationNotAscii(self):
        con = sqlite.connect(b':memory:')
        try:
            con.create_collation(b'coll\xe4', cmp)
            self.fail(b'should have raised a ProgrammingError')
        except sqlite.ProgrammingError as e:
            pass

        return

    def CheckCreateCollationBadUpper(self):

        class BadUpperStr(str):

            def upper(self):
                return

        con = sqlite.connect(b':memory:')
        mycoll = lambda x, y: -((x > y) - (x < y))
        con.create_collation(BadUpperStr(b'mycoll'), mycoll)
        result = con.execute(b"\n            select x from (\n            select 'a' as x\n            union\n            select 'b' as x\n            ) order by x collate mycoll\n            ").fetchall()
        self.assertEqual(result[0][0], b'b')
        self.assertEqual(result[1][0], b'a')
        return

    def CheckCollationIsUsed(self):
        if sqlite.version_info < (3, 2, 1):
            return
        else:

            def mycoll(x, y):
                return -cmp(x, y)

            con = sqlite.connect(b':memory:')
            con.create_collation(b'mycoll', mycoll)
            sql = b"\n            select x from (\n            select 'a' as x\n            union\n            select 'b' as x\n            union\n            select 'c' as x\n            ) order by x collate mycoll\n            "
            result = con.execute(sql).fetchall()
            if result[0][0] != b'c' or result[1][0] != b'b' or result[2][0] != b'a':
                self.fail(b'the expected order was not returned')
            con.create_collation(b'mycoll', None)
            try:
                result = con.execute(sql).fetchall()
                self.fail(b'should have raised an OperationalError')
            except sqlite.OperationalError as e:
                self.assertEqual(e.args[0].lower(), b'no such collation sequence: mycoll')

            return

    def CheckCollationReturnsLargeInteger(self):

        def mycoll(x, y):
            return -((x > y) - (x < y)) * 4294967296L

        con = sqlite.connect(b':memory:')
        con.create_collation(b'mycoll', mycoll)
        sql = b"\n            select x from (\n            select 'a' as x\n            union\n            select 'b' as x\n            union\n            select 'c' as x\n            ) order by x collate mycoll\n            "
        result = con.execute(sql).fetchall()
        self.assertEqual(result, [(b'c',), (b'b',), (b'a',)], msg=b'the expected order was not returned')
        return

    def CheckCollationRegisterTwice(self):
        con = sqlite.connect(b':memory:')
        con.create_collation(b'mycoll', cmp)
        con.create_collation(b'mycoll', (lambda x, y: -cmp(x, y)))
        result = con.execute(b"\n            select x from (select 'a' as x union select 'b' as x) order by x collate mycoll\n            ").fetchall()
        if result[0][0] != b'b' or result[1][0] != b'a':
            self.fail(b'wrong collation function is used')
        return

    def CheckDeregisterCollation(self):
        con = sqlite.connect(b':memory:')
        con.create_collation(b'mycoll', cmp)
        con.create_collation(b'mycoll', None)
        try:
            con.execute(b"select 'a' as x union select 'b' as x order by x collate mycoll")
            self.fail(b'should have raised an OperationalError')
        except sqlite.OperationalError as e:
            if not e.args[0].startswith(b'no such collation sequence'):
                self.fail(b'wrong OperationalError raised')

        return


class ProgressTests(unittest.TestCase):

    def CheckProgressHandlerUsed(self):
        con = sqlite.connect(b':memory:')
        progress_calls = []

        def progress():
            progress_calls.append(None)
            return 0

        con.set_progress_handler(progress, 1)
        con.execute(b'\n            create table foo(a, b)\n            ')
        self.assertTrue(progress_calls)
        return

    def CheckOpcodeCount(self):
        con = sqlite.connect(b':memory:')
        progress_calls = []

        def progress():
            progress_calls.append(None)
            return 0

        con.set_progress_handler(progress, 1)
        curs = con.cursor()
        curs.execute(b'\n            create table foo (a, b)\n            ')
        first_count = len(progress_calls)
        progress_calls = []
        con.set_progress_handler(progress, 2)
        curs.execute(b'\n            create table bar (a, b)\n            ')
        second_count = len(progress_calls)
        self.assertGreaterEqual(first_count, second_count)
        return

    def CheckCancelOperation(self):
        con = sqlite.connect(b':memory:')
        progress_calls = []

        def progress():
            progress_calls.append(None)
            return 1

        con.set_progress_handler(progress, 1)
        curs = con.cursor()
        self.assertRaises(sqlite.OperationalError, curs.execute, b'create table bar (a, b)')
        return

    def CheckClearHandler(self):
        con = sqlite.connect(b':memory:')
        action = []

        def progress():
            action.append(1)
            return 0

        con.set_progress_handler(progress, 1)
        con.set_progress_handler(None, 1)
        con.execute(b'select 1 union select 2 union select 3').fetchall()
        self.assertEqual(len(action), 0, b'progress handler was not cleared')
        return


def suite():
    collation_suite = unittest.makeSuite(CollationTests, b'Check')
    progress_suite = unittest.makeSuite(ProgressTests, b'Check')
    return unittest.TestSuite((collation_suite, progress_suite))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    return


if __name__ == b'__main__':
    test()
