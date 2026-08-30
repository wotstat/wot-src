import unittest, gc
from Tkinter import Variable, StringVar, IntVar, DoubleVar, BooleanVar, Tcl, TclError

class TestBase(unittest.TestCase):

    def setUp(self):
        self.root = Tcl()
        return

    def tearDown(self):
        del self.root
        return


class TestVariable(TestBase):

    def info_exists(self, *args):
        return self.root.getboolean(self.root.call(b'info', b'exists', *args))

    def test_default(self):
        v = Variable(self.root)
        self.assertEqual(b'', v.get())
        self.assertRegexpMatches(str(v), b'^PY_VAR(\\d+)$')
        return

    def test_name_and_value(self):
        v = Variable(self.root, b'sample string', b'varname')
        self.assertEqual(b'sample string', v.get())
        self.assertEqual(b'varname', str(v))
        return

    def test___del__(self):
        self.assertFalse(self.info_exists(b'varname'))
        v = Variable(self.root, b'sample string', b'varname')
        self.assertTrue(self.info_exists(b'varname'))
        del v
        self.assertFalse(self.info_exists(b'varname'))
        return

    def test_dont_unset_not_existing(self):
        self.assertFalse(self.info_exists(b'varname'))
        v1 = Variable(self.root, name=b'name')
        v2 = Variable(self.root, name=b'name')
        del v1
        self.assertFalse(self.info_exists(b'name'))
        del v2
        self.assertFalse(self.info_exists(b'name'))
        return

    def test___eq__(self):
        v1 = Variable(self.root, name=b'abc')
        v2 = Variable(self.root, name=b'abc')
        self.assertEqual(v1, v2)
        v3 = Variable(self.root, name=b'abc')
        v4 = StringVar(self.root, name=b'abc')
        self.assertNotEqual(v3, v4)
        return

    def test_invalid_name(self):
        with self.assertRaises(TypeError):
            Variable(self.root, name=123)
        return

    def test_null_in_name(self):
        with self.assertRaises(ValueError):
            Variable(self.root, name=b'var\x00name')
        with self.assertRaises(ValueError):
            self.root.globalsetvar(b'var\x00name', b'value')
        with self.assertRaises(ValueError):
            self.root.setvar(b'var\x00name', b'value')
        return

    def test_trace(self):
        v = Variable(self.root)
        vname = str(v)
        trace = []

        def read_tracer(*args):
            trace.append((b'read',) + args)
            return

        def write_tracer(*args):
            trace.append((b'write',) + args)
            return

        cb1 = v.trace_variable(b'r', read_tracer)
        cb2 = v.trace_variable(b'wu', write_tracer)
        self.assertEqual(sorted(v.trace_vinfo()), [(b'r', cb1), (b'wu', cb2)])
        self.assertEqual(trace, [])
        v.set(b'spam')
        self.assertEqual(trace, [(b'write', vname, b'', b'w')])
        trace = []
        v.get()
        self.assertEqual(trace, [(b'read', vname, b'', b'r')])
        trace = []
        info = sorted(v.trace_vinfo())
        v.trace_vdelete(b'w', cb1)
        self.assertEqual(sorted(v.trace_vinfo()), info)
        with self.assertRaises(TclError):
            v.trace_vdelete(b'r', b'spam')
        self.assertEqual(sorted(v.trace_vinfo()), info)
        v.trace_vdelete(b'r', (cb1, 43))
        self.assertEqual(sorted(v.trace_vinfo()), info)
        v.get()
        self.assertEqual(trace, [(b'read', vname, b'', b'r')])
        trace = []
        v.trace_vdelete(b'r', cb1)
        self.assertEqual(v.trace_vinfo(), [(b'wu', cb2)])
        v.get()
        self.assertEqual(trace, [])
        trace = []
        del write_tracer
        gc.collect()
        v.set(b'eggs')
        self.assertEqual(trace, [(b'write', vname, b'', b'w')])
        return


class TestStringVar(TestBase):

    def test_default(self):
        v = StringVar(self.root)
        self.assertEqual(b'', v.get())
        return

    def test_get(self):
        v = StringVar(self.root, b'abc', b'name')
        self.assertEqual(b'abc', v.get())
        self.root.globalsetvar(b'name', b'value')
        self.assertEqual(b'value', v.get())
        return

    def test_get_null(self):
        v = StringVar(self.root, b'abc\x00def', b'name')
        self.assertEqual(b'abc\x00def', v.get())
        self.root.globalsetvar(b'name', b'val\x00ue')
        self.assertEqual(b'val\x00ue', v.get())
        return


class TestIntVar(TestBase):

    def test_default(self):
        v = IntVar(self.root)
        self.assertEqual(0, v.get())
        return

    def test_get(self):
        v = IntVar(self.root, 123, b'name')
        self.assertEqual(123, v.get())
        self.root.globalsetvar(b'name', b'345')
        self.assertEqual(345, v.get())
        return

    def test_invalid_value(self):
        v = IntVar(self.root, name=b'name')
        self.root.globalsetvar(b'name', b'value')
        with self.assertRaises(ValueError):
            v.get()
        self.root.globalsetvar(b'name', b'345.0')
        with self.assertRaises(ValueError):
            v.get()
        return


class TestDoubleVar(TestBase):

    def test_default(self):
        v = DoubleVar(self.root)
        self.assertEqual(0.0, v.get())
        return

    def test_get(self):
        v = DoubleVar(self.root, 1.23, b'name')
        self.assertAlmostEqual(1.23, v.get())
        self.root.globalsetvar(b'name', b'3.45')
        self.assertAlmostEqual(3.45, v.get())
        return

    def test_get_from_int(self):
        v = DoubleVar(self.root, 1.23, b'name')
        self.assertAlmostEqual(1.23, v.get())
        self.root.globalsetvar(b'name', b'3.45')
        self.assertAlmostEqual(3.45, v.get())
        self.root.globalsetvar(b'name', b'456')
        self.assertAlmostEqual(456, v.get())
        return

    def test_invalid_value(self):
        v = DoubleVar(self.root, name=b'name')
        self.root.globalsetvar(b'name', b'value')
        with self.assertRaises(ValueError):
            v.get()
        return


class TestBooleanVar(TestBase):

    def test_default(self):
        v = BooleanVar(self.root)
        self.assertIs(v.get(), False)
        return

    def test_get(self):
        v = BooleanVar(self.root, True, b'name')
        self.assertIs(v.get(), True)
        self.root.globalsetvar(b'name', b'0')
        self.assertIs(v.get(), False)
        self.root.globalsetvar(b'name', 42 if self.root.wantobjects() else 1)
        self.assertIs(v.get(), True)
        self.root.globalsetvar(b'name', 0)
        self.assertIs(v.get(), False)
        self.root.globalsetvar(b'name', 42L if self.root.wantobjects() else 1L)
        self.assertIs(v.get(), True)
        self.root.globalsetvar(b'name', 0L)
        self.assertIs(v.get(), False)
        self.root.globalsetvar(b'name', b'on')
        self.assertIs(v.get(), True)
        self.root.globalsetvar(b'name', u'0')
        self.assertIs(v.get(), False)
        self.root.globalsetvar(b'name', u'on')
        self.assertIs(v.get(), True)
        return

    def test_set(self):
        true = 1 if self.root.wantobjects() else b'1'
        false = 0 if self.root.wantobjects() else b'0'
        v = BooleanVar(self.root, name=b'name')
        v.set(True)
        self.assertEqual(self.root.globalgetvar(b'name'), true)
        v.set(b'0')
        self.assertEqual(self.root.globalgetvar(b'name'), false)
        v.set(42)
        self.assertEqual(self.root.globalgetvar(b'name'), true)
        v.set(0)
        self.assertEqual(self.root.globalgetvar(b'name'), false)
        v.set(42L)
        self.assertEqual(self.root.globalgetvar(b'name'), true)
        v.set(0L)
        self.assertEqual(self.root.globalgetvar(b'name'), false)
        v.set(b'on')
        self.assertEqual(self.root.globalgetvar(b'name'), true)
        v.set(u'0')
        self.assertEqual(self.root.globalgetvar(b'name'), false)
        v.set(u'on')
        self.assertEqual(self.root.globalgetvar(b'name'), true)
        return

    def test_invalid_value_domain(self):
        false = 0 if self.root.wantobjects() else b'0'
        v = BooleanVar(self.root, name=b'name')
        with self.assertRaises(TclError):
            v.set(b'value')
        self.assertEqual(self.root.globalgetvar(b'name'), false)
        self.root.globalsetvar(b'name', b'value')
        with self.assertRaises(TclError):
            v.get()
        self.root.globalsetvar(b'name', b'1.0')
        with self.assertRaises(TclError):
            v.get()
        return


tests_gui = (TestVariable, TestStringVar, TestIntVar,
 TestDoubleVar, TestBooleanVar)
if __name__ == b'__main__':
    from test.support import run_unittest
    run_unittest(*tests_gui)
