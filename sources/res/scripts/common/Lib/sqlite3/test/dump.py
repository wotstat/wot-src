import unittest, sqlite3 as sqlite

class DumpTests(unittest.TestCase):

    def setUp(self):
        self.cx = sqlite.connect(b':memory:')
        self.cu = self.cx.cursor()
        return

    def tearDown(self):
        self.cx.close()
        return

    def CheckTableDump(self):
        expected_sqls = [
         1, 
         2, 
         3, 
         4, 
         5, 
         6, 
         7, 
         8, 
         9, 
         10, 
         11]
        [self.cu.execute(s) for s in expected_sqls]
        i = self.cx.iterdump()
        actual_sqls = [s for s in i]
        expected_sqls = [b'BEGIN TRANSACTION;'] + expected_sqls + [
         b'COMMIT;']
        [self.assertEqual(expected_sqls[i], actual_sqls[i]) for i in xrange(len(expected_sqls))]
        return

    def CheckUnorderableRow(self):

        class UnorderableRow:

            def __init__(self, cursor, row):
                self.row = row
                return

            def __getitem__(self, index):
                return self.row[index]

        self.cx.row_factory = UnorderableRow
        CREATE_ALPHA = b'CREATE TABLE "alpha" ("one");'
        CREATE_BETA = b'CREATE TABLE "beta" ("two");'
        expected = [
         b'BEGIN TRANSACTION;',
         CREATE_ALPHA,
         CREATE_BETA,
         b'COMMIT;']
        self.cu.execute(CREATE_BETA)
        self.cu.execute(CREATE_ALPHA)
        got = list(self.cx.iterdump())
        self.assertEqual(expected, got)
        return


def suite():
    return unittest.TestSuite(unittest.makeSuite(DumpTests, b'Check'))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    return


if __name__ == b'__main__':
    test()
