import unittest, sys
from ctypes import *
import _ctypes_test

class ValuesTestCase(unittest.TestCase):

    def test_an_integer(self):
        ctdll = CDLL(_ctypes_test.__file__)
        an_integer = c_int.in_dll(ctdll, b'an_integer')
        x = an_integer.value
        self.assertEqual(x, ctdll.get_an_integer())
        an_integer.value *= 2
        self.assertEqual(x * 2, ctdll.get_an_integer())
        return

    def test_undefined(self):
        ctdll = CDLL(_ctypes_test.__file__)
        self.assertRaises(ValueError, c_int.in_dll, ctdll, b'Undefined_Symbol')
        return


class PythonValuesTestCase(unittest.TestCase):

    def test_optimizeflag(self):
        opt = c_int.in_dll(pythonapi, b'Py_OptimizeFlag').value
        if ValuesTestCase.__doc__ is not None:
            self.assertEqual(opt, 1)
        else:
            self.assertEqual(opt, 2)
        return

    def test_frozentable(self):

        class struct_frozen(Structure):
            _fields_ = [
             (
              b'name', c_char_p),
             (
              b'code', POINTER(c_ubyte)),
             (
              b'size', c_int)]

        FrozenTable = POINTER(struct_frozen)
        ft = FrozenTable.in_dll(pythonapi, b'PyImport_FrozenModules')
        items = []
        for entry in ft:
            if entry.name is None:
                break
            items.append((entry.name, entry.size))

        expected = [(b'__hello__', 104),
         (b'__phello__', -104),
         (b'__phello__.spam', 104)]
        self.assertEqual(items, expected)
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[struct_frozen]
        return

    def test_undefined(self):
        self.assertRaises(ValueError, c_int.in_dll, pythonapi, b'Undefined_Symbol')
        return


if __name__ == b'__main__':
    unittest.main()
