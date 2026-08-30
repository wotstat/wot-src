import unittest, doctest, sys, ctypes.test.test_objects

class TestCase(unittest.TestCase):

    def test(self):
        failures, tests = doctest.testmod(ctypes.test.test_objects)
        self.assertFalse(failures, b'doctests failed, see output above')
        return


if __name__ == b'__main__':
    doctest.testmod(ctypes.test.test_objects)
