import os, re, sys
if sys.version_info[0] < 3:
    try:
        import cPickle
        pickle = cPickle
    except ImportError:
        import pickle

else:
    import pickle
import unittest
from test_all import db, dbtables, test_support, verbose, get_new_environment_path, get_new_database_path

class TableDBTestCase(unittest.TestCase):
    db_name = b'test-table.db'

    def setUp(self):
        import sys
        if sys.version_info[0] >= 3:
            from test_all import do_proxy_db_py3k
            self._flag_proxy_db_py3k = do_proxy_db_py3k(False)
        self.testHomeDir = get_new_environment_path()
        self.tdb = dbtables.bsdTableDB(filename=b'tabletest.db', dbhome=self.testHomeDir, create=1)
        return

    def tearDown(self):
        self.tdb.close()
        import sys
        if sys.version_info[0] >= 3:
            from test_all import do_proxy_db_py3k
            do_proxy_db_py3k(self._flag_proxy_db_py3k)
        test_support.rmtree(self.testHomeDir)
        return

    def test01(self):
        tabname = b'test01'
        colname = b'cool numbers'
        try:
            self.tdb.Drop(tabname)
        except dbtables.TableDBError:
            pass

        self.tdb.CreateTable(tabname, [colname])
        import sys
        if sys.version_info[0] < 3:
            self.tdb.Insert(tabname, {colname: (pickle.dumps(3.14159, 1))})
        else:
            self.tdb.Insert(tabname, {colname: (pickle.dumps(3.14159, 1).decode(b'iso8859-1'))})
        if verbose:
            self.tdb._db_print()
        values = self.tdb.Select(tabname, [colname], conditions={colname: None})
        import sys
        if sys.version_info[0] < 3:
            colval = pickle.loads(values[0][colname])
        else:
            colval = pickle.loads(bytes(values[0][colname], b'iso8859-1'))
        self.assertGreater(colval, 3.141)
        self.assertLess(colval, 3.142)
        return

    def test02(self):
        tabname = b'test02'
        col0 = b'coolness factor'
        col1 = b'but can it fly?'
        col2 = b'Species'
        import sys
        if sys.version_info[0] < 3:
            testinfo = [{col0: (pickle.dumps(8, 1)), col1: b'no', col2: b'Penguin'}, {col0: (pickle.dumps(-1, 1)), col1: b'no', col2: b'Turkey'}, {col0: (pickle.dumps(9, 1)), col1: b'yes', col2: b'SR-71A Blackbird'}]
        else:
            testinfo = [
             {col0: (pickle.dumps(8, 1).decode(b'iso8859-1')), col1: b'no', 
                col2: b'Penguin'},
             {col0: (pickle.dumps(-1, 1).decode(b'iso8859-1')), col1: b'no', 
                col2: b'Turkey'},
             {col0: (pickle.dumps(9, 1).decode(b'iso8859-1')), col1: b'yes', 
                col2: b'SR-71A Blackbird'}]
        try:
            self.tdb.Drop(tabname)
        except dbtables.TableDBError:
            pass

        self.tdb.CreateTable(tabname, [col0, col1, col2])
        for row in testinfo:
            self.tdb.Insert(tabname, row)

        import sys
        if sys.version_info[0] < 3:
            values = self.tdb.Select(tabname, [col2], conditions={col0: (lambda x: pickle.loads(x) >= 8)})
        else:
            values = self.tdb.Select(tabname, [col2], conditions={col0: (lambda x: pickle.loads(bytes(x, b'iso8859-1')) >= 8)})
        self.assertEqual(len(values), 2)
        if values[0][b'Species'] == b'Penguin':
            self.assertEqual(values[1][b'Species'], b'SR-71A Blackbird')
        elif values[0][b'Species'] == b'SR-71A Blackbird':
            self.assertEqual(values[1][b'Species'], b'Penguin')
        elif verbose:
            print b'values= %r' % (values,)
        raise RuntimeError(b'Wrong values returned!')
        return

    def test03(self):
        tabname = b'test03'
        try:
            self.tdb.Drop(tabname)
        except dbtables.TableDBError:
            pass

        if verbose:
            print b'...before CreateTable...'
            self.tdb._db_print()
        self.tdb.CreateTable(tabname, [3, 4, 5, 6, 7])
        if verbose:
            print b'...after CreateTable...'
            self.tdb._db_print()
        self.tdb.Drop(tabname)
        if verbose:
            print b'...after Drop...'
            self.tdb._db_print()
        self.tdb.CreateTable(tabname, [3, 4, 5, 6, 7])
        try:
            self.tdb.Insert(tabname, {b'a': b'', b'e': (pickle.dumps([{4: 5, 6: 7}, b'foo'], 1)), 
               b'f': b'Zero'})
            self.fail(b'Expected an exception')
        except dbtables.TableDBError:
            pass

        try:
            self.tdb.Select(tabname, [], conditions={b'foo': b'123'})
            self.fail(b'Expected an exception')
        except dbtables.TableDBError:
            pass

        self.tdb.Insert(tabname, {b'a': b'42', b'b': b'bad', 
           b'c': b'meep', 
           b'e': b'Fuzzy wuzzy was a bear'})
        self.tdb.Insert(tabname, {b'a': b'581750', b'b': b'good', 
           b'd': b'bla', 
           b'c': b'black', 
           b'e': b'fuzzy was here'})
        self.tdb.Insert(tabname, {b'a': b'800000', b'b': b'good', 
           b'd': b'bla', 
           b'c': b'black', 
           b'e': b'Fuzzy wuzzy is a bear'})
        if verbose:
            self.tdb._db_print()
        values = self.tdb.Select(tabname, [b'b', b'a', b'd'], conditions={b'e': (re.compile(b'wuzzy').search), b'a': (re.compile(b'^[0-9]+$').match)})
        self.assertEqual(len(values), 2)
        self.tdb.Delete(tabname, conditions={b'b': (dbtables.ExactCond(b'good'))})
        values = self.tdb.Select(tabname, [b'a', b'd', b'b'], conditions={b'e': (dbtables.PrefixCond(b'Fuzzy'))})
        self.assertEqual(len(values), 1)
        self.assertEqual(values[0][b'd'], None)
        values = self.tdb.Select(tabname, [b'b'], conditions={b'c': (lambda c: c == b'meep')})
        self.assertEqual(len(values), 1)
        self.assertEqual(values[0][b'b'], b'bad')
        return

    def test04_MultiCondSelect(self):
        tabname = b'test04_MultiCondSelect'
        try:
            self.tdb.Drop(tabname)
        except dbtables.TableDBError:
            pass

        self.tdb.CreateTable(tabname, [2, 3, 4, 5, 6])
        try:
            self.tdb.Insert(tabname, {b'a': b'', b'e': (pickle.dumps([{4: 5, 6: 7}, b'foo'], 1)), 
               b'f': b'Zero'})
            self.fail(b'Expected an exception')
        except dbtables.TableDBError:
            pass

        self.tdb.Insert(tabname, {b'a': b'A', b'b': b'B', b'c': b'C', b'd': b'D', b'e': b'E'})
        self.tdb.Insert(tabname, {b'a': b'-A', b'b': b'-B', b'c': b'-C', b'd': b'-D', b'e': b'-E'})
        self.tdb.Insert(tabname, {b'a': b'A-', b'b': b'B-', b'c': b'C-', b'd': b'D-', b'e': b'E-'})
        if verbose:
            self.tdb._db_print()
        values = self.tdb.Select(tabname, [b'b', b'a', b'd'], conditions={b'e': (dbtables.ExactCond(b'E')), b'a': (dbtables.ExactCond(b'A')), 
           b'd': (dbtables.PrefixCond(b'-'))})
        self.assertEqual(len(values), 0, values)
        return

    def test_CreateOrExtend(self):
        tabname = b'test_CreateOrExtend'
        self.tdb.CreateOrExtendTable(tabname, [2, 3, 4, 5, 6])
        try:
            self.tdb.Insert(tabname, {b'taste': b'crap', b'filling': b'no', 
               b'is it Guinness?': b'no'})
            self.fail(b"Insert should've failed due to bad column name")
        except:
            pass

        self.tdb.CreateOrExtendTable(tabname, [
         b'name', b'taste', b'is it Guinness?'])
        self.tdb.Insert(tabname, {b'taste': b'crap', b'filling': b'no', b'is it Guinness?': b'no'})
        self.tdb.Insert(tabname, {b'taste': b'great', b'filling': b'yes', b'is it Guinness?': b'yes', 
           b'name': b'Guinness'})
        return

    def test_CondObjs(self):
        tabname = b'test_CondObjs'
        self.tdb.CreateTable(tabname, [2, 3, 4, 5, 6, 7])
        self.tdb.Insert(tabname, {b'a': b'the letter A', b'b': b'the letter B', 
           b'c': b'is for cookie'})
        self.tdb.Insert(tabname, {b'a': b'is for aardvark', b'e': b'the letter E', 
           b'c': b'is for cookie', 
           b'd': b'is for dog'})
        self.tdb.Insert(tabname, {b'a': b'the letter A', b'e': b'the letter E', 
           b'c': b'is for cookie', 
           b'p': b'is for Python'})
        values = self.tdb.Select(tabname, [b'p', b'e'], conditions={b'e': (dbtables.PrefixCond(b'the l'))})
        self.assertEqual(len(values), 2, values)
        self.assertEqual(values[0][b'e'], values[1][b'e'], values)
        self.assertNotEqual(values[0][b'p'], values[1][b'p'], values)
        values = self.tdb.Select(tabname, [b'd', b'a'], conditions={b'a': (dbtables.LikeCond(b'%aardvark%'))})
        self.assertEqual(len(values), 1, values)
        self.assertEqual(values[0][b'd'], b'is for dog', values)
        self.assertEqual(values[0][b'a'], b'is for aardvark', values)
        values = self.tdb.Select(tabname, None, {b'b': (dbtables.Cond()), b'e': (dbtables.LikeCond(b'%letter%')), 
           b'a': (dbtables.PrefixCond(b'is')), 
           b'd': (dbtables.ExactCond(b'is for dog')), 
           b'c': (dbtables.PrefixCond(b'is for')), 
           b'p': (lambda s: not s)})
        self.assertEqual(len(values), 1, values)
        self.assertEqual(values[0][b'd'], b'is for dog', values)
        self.assertEqual(values[0][b'a'], b'is for aardvark', values)
        return

    def test_Delete(self):
        tabname = b'test_Delete'
        self.tdb.CreateTable(tabname, [b'x', b'y', b'z'])
        self.tdb.Insert(tabname, {b'x': b'X1', b'y': b'Y1'})
        self.tdb.Insert(tabname, {b'x': b'X2', b'y': b'Y2', b'z': b'Z2'})
        self.tdb.Delete(tabname, conditions={b'x': (dbtables.PrefixCond(b'X'))})
        values = self.tdb.Select(tabname, [b'y'], conditions={b'x': (dbtables.PrefixCond(b'X'))})
        self.assertEqual(len(values), 0)
        return

    def test_Modify(self):
        tabname = b'test_Modify'
        self.tdb.CreateTable(tabname, [b'Name', b'Type', b'Access'])
        self.tdb.Insert(tabname, {b'Name': b'Index to MP3 files.doc', b'Type': b'Word', 
           b'Access': b'8'})
        self.tdb.Insert(tabname, {b'Name': b'Nifty.MP3', b'Access': b'1'})
        self.tdb.Insert(tabname, {b'Type': b'Unknown', b'Access': b'0'})

        def set_type(type):
            if type is None:
                return b'MP3'
            else:
                return type

        def increment_access(count):
            return str(int(count) + 1)

        def remove_value(value):
            return

        self.tdb.Modify(tabname, conditions={b'Access': (dbtables.ExactCond(b'0'))}, mappings={b'Access': remove_value})
        self.tdb.Modify(tabname, conditions={b'Name': (dbtables.LikeCond(b'%MP3%'))}, mappings={b'Type': set_type})
        self.tdb.Modify(tabname, conditions={b'Name': (dbtables.LikeCond(b'%'))}, mappings={b'Access': increment_access})
        try:
            self.tdb.Modify(tabname, conditions={b'Name': (dbtables.LikeCond(b'%'))}, mappings={b'Access': b'What is your quest?'})
        except TypeError:
            pass
        else:
            raise RuntimeError, b'why was TypeError not raised for bad callable?'

        values = self.tdb.Select(tabname, None, conditions={b'Type': (dbtables.ExactCond(b'Unknown'))})
        self.assertEqual(len(values), 1, values)
        self.assertEqual(values[0][b'Name'], None, values)
        self.assertEqual(values[0][b'Access'], None, values)
        values = self.tdb.Select(tabname, None, conditions={b'Name': (dbtables.ExactCond(b'Nifty.MP3'))})
        self.assertEqual(len(values), 1, values)
        self.assertEqual(values[0][b'Type'], b'MP3', values)
        self.assertEqual(values[0][b'Access'], b'2', values)
        values = self.tdb.Select(tabname, None, conditions={b'Name': (dbtables.LikeCond(b'%doc%'))})
        self.assertEqual(len(values), 1, values)
        self.assertEqual(values[0][b'Type'], b'Word', values)
        self.assertEqual(values[0][b'Access'], b'9', values)
        return


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TableDBTestCase))
    return suite


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
