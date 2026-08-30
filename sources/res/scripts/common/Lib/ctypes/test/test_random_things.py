from ctypes import *
import unittest, sys

def callback_func(arg):
    42 // arg
    raise ValueError(arg)
    return


@unittest.skipUnless(sys.platform == b'win32', b'Windows-specific test')
class call_function_TestCase(unittest.TestCase):

    def test(self):
        from _ctypes import call_function
        windll.kernel32.LoadLibraryA.restype = c_void_p
        windll.kernel32.GetProcAddress.argtypes = (c_void_p, c_char_p)
        windll.kernel32.GetProcAddress.restype = c_void_p
        hdll = windll.kernel32.LoadLibraryA(b'kernel32')
        funcaddr = windll.kernel32.GetProcAddress(hdll, b'GetModuleHandleA')
        self.assertEqual(call_function(funcaddr, (None,)), windll.kernel32.GetModuleHandleA(None))
        return


class CallbackTracbackTestCase(unittest.TestCase):

    def capture_stderr(self, func, *args, **kw):
        import StringIO
        old_stderr = sys.stderr
        logger = sys.stderr = StringIO.StringIO()
        try:
            func(*args, **kw)
        finally:
            sys.stderr = old_stderr

        return logger.getvalue()

    def test_ValueError(self):
        cb = CFUNCTYPE(c_int, c_int)(callback_func)
        out = self.capture_stderr(cb, 42)
        self.assertEqual(out.splitlines()[-1], b'ValueError: 42')
        return

    def test_IntegerDivisionError(self):
        cb = CFUNCTYPE(c_int, c_int)(callback_func)
        out = self.capture_stderr(cb, 0)
        self.assertEqual(out.splitlines()[-1][:19], b'ZeroDivisionError: ')
        return

    def test_FloatDivisionError(self):
        cb = CFUNCTYPE(c_int, c_double)(callback_func)
        out = self.capture_stderr(cb, 0.0)
        self.assertEqual(out.splitlines()[-1][:19], b'ZeroDivisionError: ')
        return

    def test_TypeErrorDivisionError(self):
        cb = CFUNCTYPE(c_int, c_char_p)(callback_func)
        out = self.capture_stderr(cb, b'spam')
        self.assertEqual(out.splitlines()[-1], b"TypeError: unsupported operand type(s) for //: 'int' and 'str'")
        return


if __name__ == b'__main__':
    unittest.main()
