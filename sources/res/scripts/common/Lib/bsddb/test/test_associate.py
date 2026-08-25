import sys, os, string, time
from pprint import pprint
import unittest
from test_all import db, dbshelve, test_support, verbose, have_threads, get_new_environment_path
musicdata = {1: (b'Bad English', b'The Price Of Love', b'Rock'), 
   2: (b'DNA featuring Suzanne Vega', b"Tom's Diner", b'Rock'), 
   3: (b'George Michael', b'Praying For Time', b'Rock'), 
   4: (b'Gloria Estefan', b'Here We Are', b'Rock'), 
   5: (b'Linda Ronstadt', b"Don't Know Much", b'Rock'), 
   6: (b'Michael Bolton', b'How Am I Supposed To Live Without You', b'Blues'), 
   7: (b'Paul Young', b'Oh Girl', b'Rock'), 
   8: (b'Paula Abdul', b'Opposites Attract', b'Rock'), 
   9: (b'Richard Marx', b"Should've Known Better", b'Rock'), 
   10: (b'Rod Stewart', b'Forever Young', b'Rock'), 
   11: (b'Roxette', b'Dangerous', b'Rock'), 
   12: (b'Sheena Easton', b'The Lover In Me', b'Rock'), 
   13: (b"Sinead O'Connor", b'Nothing Compares 2 U', b'Rock'), 
   14: (b'Stevie B.', b'Because I Love You', b'Rock'), 
   15: (b'Taylor Dayne', b'Love Will Lead You Back', b'Rock'), 
   16: (b'The Bangles', b'Eternal Flame', b'Rock'), 
   17: (b'Wilson Phillips', b'Release Me', b'Rock'), 
   18: (b'Billy Joel', b'Blonde Over Blue', b'Rock'), 
   19: (b'Billy Joel', b'Famous Last Words', b'Rock'), 
   20: (b'Billy Joel', b'Lullabye (Goodnight, My Angel)', b'Rock'), 
   21: (b'Billy Joel', b'The River Of Dreams', b'Rock'), 
   22: (b'Billy Joel', b'Two Thousand Years', b'Rock'), 
   23: (b'Janet Jackson', b'Alright', b'Rock'), 
   24: (b'Janet Jackson', b'Black Cat', b'Rock'), 
   25: (b'Janet Jackson', b'Come Back To Me', b'Rock'), 
   26: (b'Janet Jackson', b'Escapade', b'Rock'), 
   27: (b'Janet Jackson', b'Love Will Never Do (Without You)', b'Rock'), 
   28: (b'Janet Jackson', b'Miss You Much', b'Rock'), 
   29: (b'Janet Jackson', b'Rhythm Nation', b'Rock'), 
   30: (b'Janet Jackson', b'State Of The World', b'Rock'), 
   31: (b'Janet Jackson', b'The Knowledge', b'Rock'), 
   32: (b'Spyro Gyra', b'End of Romanticism', b'Jazz'), 
   33: (b'Spyro Gyra', b'Heliopolis', b'Jazz'), 
   34: (b'Spyro Gyra', b'Jubilee', b'Jazz'), 
   35: (b'Spyro Gyra', b'Little Linda', b'Jazz'), 
   36: (b'Spyro Gyra', b'Morning Dance', b'Jazz'), 
   37: (b'Spyro Gyra', b'Song for Lorraine', b'Jazz'), 
   38: (b'Yes', b'Owner Of A Lonely Heart', b'Rock'), 
   39: (b'Yes', b'Rhythm Of Love', b'Rock'), 
   40: (b'Cusco', b'Dream Catcher', b'New Age'), 
   41: (b'Cusco', b'Geronimos Laughter', b'New Age'), 
   42: (b'Cusco', b'Ghost Dance', b'New Age'), 
   43: (b'Blue Man Group', b'Drumbone', b'New Age'), 
   44: (b'Blue Man Group', b'Endless Column', b'New Age'), 
   45: (b'Blue Man Group', b'Klein Mandelbrot', b'New Age'), 
   46: (b'Kenny G', b'Silhouette', b'Jazz'), 
   47: (b'Sade', b'Smooth Operator', b'Jazz'), 
   48: (b'David Arkenstone', b'Papillon (On The Wings Of The Butterfly)', b'New Age'), 
   49: (b'David Arkenstone', b'Stepping Stars', b'New Age'), 
   50: (b'David Arkenstone', b'Carnation Lily Lily Rose', b'New Age'), 
   51: (b'David Lanz', b'Behind The Waterfall', b'New Age'), 
   52: (b'David Lanz', b"Cristofori's Dream", b'New Age'), 
   53: (b'David Lanz', b'Heartsounds', b'New Age'), 
   54: (b'David Lanz', b'Leaves on the Seine', b'New Age'), 
   99: (b'unknown artist', b'Unnamed song', b'Unknown')}

class AssociateErrorTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = self.__class__.__name__ + b'.db'
        self.homeDir = get_new_environment_path()
        self.env = db.DBEnv()
        self.env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL)
        return

    def tearDown(self):
        self.env.close()
        self.env = None
        test_support.rmtree(self.homeDir)
        return

    def test00_associateDBError(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test00_associateDBError...' % self.__class__.__name__
        dupDB = db.DB(self.env)
        dupDB.set_flags(db.DB_DUP)
        dupDB.open(self.filename, b'primary', db.DB_BTREE, db.DB_CREATE)
        secDB = db.DB(self.env)
        secDB.open(self.filename, b'secondary', db.DB_BTREE, db.DB_CREATE)
        try:

            def f(a, b):
                return a + b

            dupDB.associate(secDB, f)
        except db.DBError:
            secDB.close()
            dupDB.close()
        else:
            secDB.close()
            dupDB.close()
            self.fail(b'DBError exception was expected')

        return

    @unittest.skipUnless(db.version() >= (4, 6), b'Needs 4.6+')
    def test_associateListError(self):
        db1 = db.DB(self.env)
        db1.open(b'bad.db', b'a.db', db.DB_BTREE, db.DB_CREATE)
        db2 = db.DB(self.env)
        db2.open(b'bad.db', b'b.db', db.DB_BTREE, db.DB_CREATE)
        db1.associate(db2, (lambda a, b: [0]))
        msg = b'TypeError: The list returned by DB->associate callback should be a list of strings.'
        with test_support.captured_output(b'stderr') as s:
            db1.put(b'0', b'1')
        db1.close()
        db2.close()
        self.assertEquals(s.getvalue().strip(), msg)
        return


class AssociateTestCase(unittest.TestCase):
    keytype = b''
    envFlags = 0
    dbFlags = 0

    def setUp(self):
        self.filename = self.__class__.__name__ + b'.db'
        self.homeDir = get_new_environment_path()
        self.env = db.DBEnv()
        self.env.open(self.homeDir, db.DB_CREATE | db.DB_INIT_MPOOL | db.DB_INIT_LOCK | db.DB_THREAD | self.envFlags)
        return

    def tearDown(self):
        self.closeDB()
        self.env.close()
        self.env = None
        test_support.rmtree(self.homeDir)
        return

    def addDataToDB(self, d, txn=None):
        for key, value in musicdata.items():
            if type(self.keytype) == type(b''):
                key = b'%02d' % key
            d.put(key, (b'|').join(value), txn=txn)

        return

    def createDB(self, txn=None):
        self.cur = None
        self.secDB = None
        self.primary = db.DB(self.env)
        self.primary.set_get_returns_none(2)
        self.primary.open(self.filename, b'primary', self.dbtype, db.DB_CREATE | db.DB_THREAD | self.dbFlags, txn=txn)
        return

    def closeDB(self):
        if self.cur:
            self.cur.close()
            self.cur = None
        if self.secDB:
            self.secDB.close()
            self.secDB = None
        self.primary.close()
        self.primary = None
        return

    def getDB(self):
        return self.primary

    def _associateWithDB(self, getGenre):
        self.createDB()
        self.secDB = db.DB(self.env)
        self.secDB.set_flags(db.DB_DUP)
        self.secDB.set_get_returns_none(2)
        self.secDB.open(self.filename, b'secondary', db.DB_BTREE, db.DB_CREATE | db.DB_THREAD | self.dbFlags)
        self.getDB().associate(self.secDB, getGenre)
        self.addDataToDB(self.getDB())
        self.finish_test(self.secDB)
        return

    def test01_associateWithDB(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test01_associateWithDB...' % self.__class__.__name__
        return self._associateWithDB(self.getGenre)

    def _associateAfterDB(self, getGenre):
        self.createDB()
        self.addDataToDB(self.getDB())
        self.secDB = db.DB(self.env)
        self.secDB.set_flags(db.DB_DUP)
        self.secDB.open(self.filename, b'secondary', db.DB_BTREE, db.DB_CREATE | db.DB_THREAD | self.dbFlags)
        self.getDB().associate(self.secDB, getGenre, db.DB_CREATE)
        self.finish_test(self.secDB)
        return

    def test02_associateAfterDB(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test02_associateAfterDB...' % self.__class__.__name__
        return self._associateAfterDB(self.getGenre)

    if db.version() >= (4, 6):

        def test03_associateWithDB(self):
            if verbose:
                print b'\n', b'-=' * 30
                print b'Running %s.test03_associateWithDB...' % self.__class__.__name__
            return self._associateWithDB(self.getGenreList)

        def test04_associateAfterDB(self):
            if verbose:
                print b'\n', b'-=' * 30
                print b'Running %s.test04_associateAfterDB...' % self.__class__.__name__
            return self._associateAfterDB(self.getGenreList)

    def finish_test(self, secDB, txn=None):
        vals = secDB.pget(b'Blues', txn=txn)
        self.assertEqual(vals, None, vals)
        vals = secDB.pget(b'Unknown', txn=txn)
        self.assertIn(vals[0], (99, b'99'), vals)
        vals[1].index(b'Unknown')
        vals[1].index(b'Unnamed')
        vals[1].index(b'unknown')
        if verbose:
            print b'Primary key traversal:'
        self.cur = self.getDB().cursor(txn)
        count = 0
        rec = self.cur.first()
        while rec is not None:
            if type(self.keytype) == type(b''):
                self.assertTrue(int(rec[0]))
            else:
                self.assertTrue(rec[0])
                self.assertIs(type(rec[0]), int)
            count = count + 1
            if verbose:
                print rec
            rec = getattr(self.cur, b'next')()

        self.assertEqual(count, len(musicdata))
        if verbose:
            print b'Secondary key traversal:'
        self.cur = secDB.cursor(txn)
        count = 0
        vals = self.cur.pget(b'Unknown', flags=db.DB_LAST)
        self.assertIn(vals[1], (99, b'99'), vals)
        self.assertEqual(vals[0], b'Unknown')
        vals[2].index(b'Unknown')
        vals[2].index(b'Unnamed')
        vals[2].index(b'unknown')
        vals = self.cur.pget(b'Unknown', data=b'wrong value', flags=db.DB_GET_BOTH)
        self.assertEqual(vals, None, vals)
        rec = self.cur.first()
        self.assertEqual(rec[0], b'Jazz')
        while rec is not None:
            count = count + 1
            if verbose:
                print rec
            rec = getattr(self.cur, b'next')()

        self.assertEqual(count, len(musicdata) - 1)
        self.cur = None
        return

    def getGenre(self, priKey, priData):
        self.assertEqual(type(priData), type(b''))
        genre = priData.split(b'|')[2]
        if verbose:
            print b'getGenre key: %r data: %r' % (priKey, priData)
        if genre == b'Blues':
            return db.DB_DONOTINDEX
        else:
            return genre

        return

    def getGenreList(self, priKey, PriData):
        v = self.getGenre(priKey, PriData)
        if type(v) == type(b''):
            v = [
             v]
        return v


class AssociateHashTestCase(AssociateTestCase):
    dbtype = db.DB_HASH


class AssociateBTreeTestCase(AssociateTestCase):
    dbtype = db.DB_BTREE


class AssociateRecnoTestCase(AssociateTestCase):
    dbtype = db.DB_RECNO
    keytype = 0


class AssociateBTreeTxnTestCase(AssociateBTreeTestCase):
    envFlags = db.DB_INIT_TXN
    dbFlags = 0

    def txn_finish_test(self, sDB, txn):
        try:
            self.finish_test(sDB, txn=txn)
        finally:
            if self.cur:
                self.cur.close()
                self.cur = None
            if txn:
                txn.commit()

        return

    def test13_associate_in_transaction(self):
        if verbose:
            print b'\n', b'-=' * 30
            print b'Running %s.test13_associateAutoCommit...' % self.__class__.__name__
        txn = self.env.txn_begin()
        try:
            self.createDB(txn=txn)
            self.secDB = db.DB(self.env)
            self.secDB.set_flags(db.DB_DUP)
            self.secDB.set_get_returns_none(2)
            self.secDB.open(self.filename, b'secondary', db.DB_BTREE, db.DB_CREATE | db.DB_THREAD, txn=txn)
            self.getDB().associate(self.secDB, self.getGenre, txn=txn)
            self.addDataToDB(self.getDB(), txn=txn)
        except:
            txn.abort()
            raise

        self.txn_finish_test(self.secDB, txn=txn)
        return


class ShelveAssociateTestCase(AssociateTestCase):

    def createDB(self):
        self.primary = dbshelve.open(self.filename, dbname=b'primary', dbenv=self.env, filetype=self.dbtype)
        return

    def addDataToDB(self, d):
        for key, value in musicdata.items():
            if type(self.keytype) == type(b''):
                key = b'%02d' % key
            d.put(key, value)

        return

    def getGenre(self, priKey, priData):
        self.assertEqual(type(priData), type(()))
        if verbose:
            print b'getGenre key: %r data: %r' % (priKey, priData)
        genre = priData[2]
        if genre == b'Blues':
            return db.DB_DONOTINDEX
        else:
            return genre

        return


class ShelveAssociateHashTestCase(ShelveAssociateTestCase):
    dbtype = db.DB_HASH


class ShelveAssociateBTreeTestCase(ShelveAssociateTestCase):
    dbtype = db.DB_BTREE


class ShelveAssociateRecnoTestCase(ShelveAssociateTestCase):
    dbtype = db.DB_RECNO
    keytype = 0


class ThreadedAssociateTestCase(AssociateTestCase):

    def addDataToDB(self, d):
        t1 = Thread(target=self.writer1, args=(
         d,))
        t2 = Thread(target=self.writer2, args=(
         d,))
        t1.setDaemon(True)
        t2.setDaemon(True)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return

    def writer1(self, d):
        for key, value in musicdata.items():
            if type(self.keytype) == type(b''):
                key = b'%02d' % key
            d.put(key, (b'|').join(value))

        return

    def writer2(self, d):
        for x in range(100, 600):
            key = b'z%2d' % x
            value = [key] * 4
            d.put(key, (b'|').join(value))

        return


class ThreadedAssociateHashTestCase(ShelveAssociateTestCase):
    dbtype = db.DB_HASH


class ThreadedAssociateBTreeTestCase(ShelveAssociateTestCase):
    dbtype = db.DB_BTREE


class ThreadedAssociateRecnoTestCase(ShelveAssociateTestCase):
    dbtype = db.DB_RECNO
    keytype = 0


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AssociateErrorTestCase))
    suite.addTest(unittest.makeSuite(AssociateHashTestCase))
    suite.addTest(unittest.makeSuite(AssociateBTreeTestCase))
    suite.addTest(unittest.makeSuite(AssociateRecnoTestCase))
    suite.addTest(unittest.makeSuite(AssociateBTreeTxnTestCase))
    suite.addTest(unittest.makeSuite(ShelveAssociateHashTestCase))
    suite.addTest(unittest.makeSuite(ShelveAssociateBTreeTestCase))
    suite.addTest(unittest.makeSuite(ShelveAssociateRecnoTestCase))
    if have_threads:
        suite.addTest(unittest.makeSuite(ThreadedAssociateHashTestCase))
        suite.addTest(unittest.makeSuite(ThreadedAssociateBTreeTestCase))
        suite.addTest(unittest.makeSuite(ThreadedAssociateRecnoTestCase))
    return suite


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
