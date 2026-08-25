import os, string, unittest
from test_all import db, hashopen, btopen, rnopen, verbose, get_new_database_path

class CompatibilityTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = get_new_database_path()
        return

    def tearDown(self):
        try:
            os.remove(self.filename)
        except os.error:
            pass

        return

    def test01_btopen(self):
        self.do_bthash_test(btopen, b'btopen')
        return

    def test02_hashopen(self):
        self.do_bthash_test(hashopen, b'hashopen')
        return

    def test03_rnopen(self):
        data = (b'The quick brown fox jumped over the lazy dog.').split()
        if verbose:
            print b'\nTesting: rnopen'
        f = rnopen(self.filename, b'c')
        for x in range(len(data)):
            f[x + 1] = data[x]

        getTest = (f[1], f[2], f[3])
        if verbose:
            print b'%s %s %s' % getTest
        self.assertEqual(getTest[1], b'quick', b'data mismatch!')
        rv = f.set_location(3)
        if rv != (3, b'brown'):
            self.fail(b'recno database set_location failed: ' + repr(rv))
        f[25] = b'twenty-five'
        f.close()
        del f
        f = rnopen(self.filename, b'w')
        f[20] = b'twenty'

        def noRec(f):
            rec = f[15]
            return

        self.assertRaises(KeyError, noRec, f)

        def badKey(f):
            rec = f[b'a string']
            return

        self.assertRaises(TypeError, badKey, f)
        del f[3]
        rec = f.first()
        while rec:
            if verbose:
                print rec
            try:
                rec = f.next()
            except KeyError:
                break

        f.close()
        return

    def test04_n_flag(self):
        f = hashopen(self.filename, b'n')
        f.close()
        return

    def do_bthash_test(self, factory, what):
        if verbose:
            print b'\nTesting: ', what
        f = factory(self.filename, b'c')
        if verbose:
            print b'creation...'
        if f:
            if verbose:
                print b'truth test: true'
        elif verbose:
            print b'truth test: false'
        f[b'0'] = b''
        f[b'a'] = b'Guido'
        f[b'b'] = b'van'
        f[b'c'] = b'Rossum'
        f[b'd'] = b'invented'
        f[b'f'] = b'Python'
        if verbose:
            print b'%s %s %s' % (f[b'a'], f[b'b'], f[b'c'])
        if verbose:
            print b'key ordering...'
        start = f.set_location(f.first()[0])
        if start != (b'0', b''):
            self.fail(b'incorrect first() result: ' + repr(start))
        while 1:
            try:
                rec = f.next()
            except KeyError:
                self.assertEqual(rec, f.last(), b'Error, last <> last!')
                f.previous()
                break

            if verbose:
                print rec

        self.assertTrue(f.has_key(b'f'), b'Error, missing key!')
        if factory == btopen:
            e = f.set_location(b'e')
            if e != (b'f', b'Python'):
                self.fail(b'wrong key,value returned: ' + repr(e))
        else:
            try:
                e = f.set_location(b'e')
            except KeyError:
                pass
            else:
                self.fail(b'set_location on non-existent key did not raise KeyError')

        f.sync()
        f.close()
        try:
            if f:
                if verbose:
                    print b'truth test: true'
            elif verbose:
                print b'truth test: false'
        except db.DBError:
            pass
        else:
            self.fail(b'Exception expected')

        del f
        if verbose:
            print b'modification...'
        f = factory(self.filename, b'w')
        f[b'd'] = b'discovered'
        if verbose:
            print b'access...'
        for key in f.keys():
            word = f[key]
            if verbose:
                print word

        def noRec(f):
            rec = f[b'no such key']
            return

        self.assertRaises(KeyError, noRec, f)

        def badKey(f):
            rec = f[15]
            return

        self.assertRaises(TypeError, badKey, f)
        f.close()
        return


def test_suite():
    return unittest.makeSuite(CompatibilityTestCase)


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
