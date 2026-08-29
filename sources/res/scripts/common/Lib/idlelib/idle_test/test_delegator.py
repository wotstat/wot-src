import unittest
from idlelib.Delegator import Delegator

class DelegatorTest(unittest.TestCase):

    def test_mydel(self):
        mydel = Delegator(int)
        self.assertIs(mydel.delegate, int)
        self.assertEqual(mydel._Delegator__cache, set())
        self.assertRaises(AttributeError, mydel.__getattr__, b'xyz')
        bl = mydel.bit_length
        self.assertIs(bl, int.bit_length)
        self.assertIs(mydel.__dict__[b'bit_length'], int.bit_length)
        self.assertEqual(mydel._Delegator__cache, {b'bit_length'})
        mydel.numerator
        self.assertEqual(mydel._Delegator__cache, {b'bit_length', b'numerator'})
        del mydel.numerator
        self.assertNotIn(b'numerator', mydel.__dict__)
        self.assertIn(b'numerator', mydel._Delegator__cache)
        mydel.setdelegate(float)
        self.assertIs(mydel.delegate, float)
        self.assertNotIn(b'bit_length', mydel.__dict__)
        self.assertEqual(mydel._Delegator__cache, set())
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=2)
