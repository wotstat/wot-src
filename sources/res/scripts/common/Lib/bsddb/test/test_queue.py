import os, string
from pprint import pprint
import unittest
from test_all import db, verbose, get_new_database_path

class SimpleQueueTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = get_new_database_path()
        return

    def tearDown(self):
        try:
            os.remove(self.filename)
        except os.error:
            pass

        return

    def test01_basic(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test01_basic...' % self.__class__.__name__
        d = db.DB()
        d.set_re_len(40)
        d.open(self.filename, db.DB_QUEUE, db.DB_CREATE)
        if verbose:
            print b'before appends' + b'-' * 30
            pprint(d.stat())
        for x in string.ascii_letters:
            d.append(x * 40)

        self.assertEqual(len(d), len(string.ascii_letters))
        d.put(100, b'some more data')
        d.put(101, b'and some more ')
        d.put(75, b'out of order')
        d.put(1, b'replacement data')
        self.assertEqual(len(d), len(string.ascii_letters) + 3)
        if verbose:
            print b'before close' + b'-' * 30
            pprint(d.stat())
        d.close()
        del d
        d = db.DB()
        d.open(self.filename)
        if verbose:
            print b'after open' + b'-' * 30
            pprint(d.stat())
        d.append(b'one more', None)
        d.append(b'another one', txn=None)
        c = d.cursor()
        if verbose:
            print b'after append' + b'-' * 30
            pprint(d.stat())
        rec = c.consume()
        while rec:
            if verbose:
                print rec
            rec = c.consume()

        c.close()
        if verbose:
            print b'after consume loop' + b'-' * 30
            pprint(d.stat())
        self.assertEqual(len(d), 0, b'if you see this message then you need to rebuild Berkeley DB 3.1.17 with the patch in patches/qam_stat.diff')
        d.close()
        return

    def test02_basicPost32(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test02_basicPost32...' % self.__class__.__name__
        d = db.DB()
        d.set_re_len(40)
        d.open(self.filename, db.DB_QUEUE, db.DB_CREATE)
        if verbose:
            print b'before appends' + b'-' * 30
            pprint(d.stat())
        for x in string.ascii_letters:
            d.append(x * 40)

        self.assertEqual(len(d), len(string.ascii_letters))
        d.put(100, b'some more data')
        d.put(101, b'and some more ')
        d.put(75, b'out of order')
        d.put(1, b'replacement data')
        self.assertEqual(len(d), len(string.ascii_letters) + 3)
        if verbose:
            print b'before close' + b'-' * 30
            pprint(d.stat())
        d.close()
        del d
        d = db.DB()
        d.open(self.filename)
        if verbose:
            print b'after open' + b'-' * 30
            pprint(d.stat())
        d.append(b'one more')
        if verbose:
            print b'after append' + b'-' * 30
            pprint(d.stat())
        rec = d.consume()
        while rec:
            if verbose:
                print rec
            rec = d.consume()

        if verbose:
            print b'after consume loop' + b'-' * 30
            pprint(d.stat())
        d.close()
        return


def test_suite():
    return unittest.makeSuite(SimpleQueueTestCase)


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
