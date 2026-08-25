import unittest, idlelib.CallTips as ct
CTi = ct.CallTips()
import textwrap, types, warnings
default_tip = b''

class TC(object):
    tip = b'(ai=None, *args)'

    def __init__(self, ai=None, *b):
        return

    __init__.tip = b'(self, ai=None, *args)'

    def t1(self):
        return

    t1.tip = b'(self)'

    def t2(self, ai, b=None):
        return

    t2.tip = b'(self, ai, b=None)'

    def t3(self, ai, *args):
        return

    t3.tip = b'(self, ai, *args)'

    def t4(self, *args):
        return

    t4.tip = b'(self, *args)'

    def t5(self, ai, b=None, *args, **kw):
        return

    t5.tip = b'(self, ai, b=None, *args, **kwargs)'

    def t6(no, self):
        return

    t6.tip = b'(no, self)'

    def __call__(self, ci):
        return

    __call__.tip = b'(self, ci)'

    @classmethod
    def cm(cls, a):
        return

    @staticmethod
    def sm(b):
        return


tc = TC()
signature = ct.get_arg_text

class Get_signatureTest(unittest.TestCase):

    def test_builtins(self):

        class List(list):
            pass

        class SB:
            __call__ = None

        def gtest(obj, out):
            self.assertEqual(signature(obj), out)
            return

        if List.__doc__ is not None:
            gtest(List, b'()\n' + List.__doc__)
        gtest(list.__new__, b'T.__new__(S, ...) -> a new object with type S, a subtype of T')
        gtest(list.__init__, b'x.__init__(...) initializes x; see help(type(x)) for signature')
        append_doc = b'L.append(object) -- append object to end'
        gtest(list.append, append_doc)
        gtest([].append, append_doc)
        gtest(List.append, append_doc)
        gtest(types.MethodType, b'()\ninstancemethod(function, instance, class)')
        gtest(SB(), default_tip)
        return

    def test_signature_wrap(self):
        if textwrap.TextWrapper.__doc__ is not None:
            self.assertEqual(signature(textwrap.TextWrapper), b"(width=70, initial_indent='', subsequent_indent='', expand_tabs=True,\n    replace_whitespace=True, fix_sentence_endings=False, break_long_words=True,\n    drop_whitespace=True, break_on_hyphens=True)")
        return

    def test_docline_truncation(self):

        def f():
            return

        f.__doc__ = b'a' * 300
        self.assertEqual(signature(f), b'()\n' + b'a' * (ct._MAX_COLS - 3) + b'...')
        return

    def test_multiline_docstring(self):
        self.assertEqual(signature(list), b"()\nlist() -> new empty list\nlist(iterable) -> new list initialized from iterable's items")

        def f():
            return

        s = b'a\nb\nc\nd\n'
        f.__doc__ = s + 300 * b'e' + b'f'
        self.assertEqual(signature(f), b'()\n' + s + (ct._MAX_COLS - 3) * b'e' + b'...')
        return

    def test_functions(self):

        def t1():
            return

        t1.tip = b'()'

        def t2(a, b=None):
            return

        t2.tip = b'(a, b=None)'

        def t3(a, *args):
            return

        t3.tip = b'(a, *args)'

        def t4(*args):
            return

        t4.tip = b'(*args)'

        def t5(a, b=None, *args, **kwds):
            return

        t5.tip = b'(a, b=None, *args, **kwargs)'
        doc = b'\ndoc' if t1.__doc__ is not None else b''
        for func in (t1, t2, t3, t4, t5, TC):
            self.assertEqual(signature(func), func.tip + doc)

        return

    def test_methods(self):
        doc = b'\ndoc' if TC.__doc__ is not None else b''
        for meth in (TC.t1, TC.t2, TC.t3, TC.t4, TC.t5, TC.t6, TC.__call__):
            self.assertEqual(signature(meth), meth.tip + doc)

        self.assertEqual(signature(TC.cm), b'(a)' + doc)
        self.assertEqual(signature(TC.sm), b'(b)' + doc)
        return

    def test_bound_methods(self):
        doc = b'\ndoc' if TC.__doc__ is not None else b''
        for meth, mtip in ((tc.t1, b'()'), (tc.t4, b'(*args)'), (tc.t6, b'(self)'),
         (
          tc.__call__, b'(ci)'), (tc, b'(ci)'), (TC.cm, b'(a)')):
            self.assertEqual(signature(meth), mtip + doc)

        return

    def test_starred_parameter(self):

        class C:

            def m1(*args):
                return

            def m2(**kwds):
                return

        def f1(args, kwargs, *a, **k):
            return

        def f2(args, kwargs, args1, kwargs1, *a, **k):
            return

        c = C()
        self.assertEqual(signature(C.m1), b'(*args)')
        self.assertEqual(signature(c.m1), b'(*args)')
        self.assertEqual(signature(C.m2), b'(**kwargs)')
        self.assertEqual(signature(c.m2), b'(**kwargs)')
        self.assertEqual(signature(f1), b'(args, kwargs, *args1, **kwargs1)')
        self.assertEqual(signature(f2), b'(args, kwargs, args1, kwargs1, *args2, **kwargs2)')
        return

    def test_no_docstring(self):

        def nd(s):
            return

        TC.nd = nd
        self.assertEqual(signature(nd), b'(s)')
        self.assertEqual(signature(TC.nd), b'(s)')
        self.assertEqual(signature(tc.nd), b'()')
        return

    def test_attribute_exception(self):

        class NoCall(object):

            def __getattr__(self, name):
                raise BaseException
                return

        class Call(NoCall):

            def __call__(self, ci):
                return

        for meth, mtip in ((NoCall, b'()'), (Call, b'()'),
         (
          NoCall(), b''), (Call(), b'(ci)')):
            self.assertEqual(signature(meth), mtip)

        return

    def test_non_callables(self):
        for obj in (0, 0.0, b'0', b'0', [], {}):
            self.assertEqual(signature(obj), b'')

        return


class Get_entityTest(unittest.TestCase):

    def test_bad_entity(self):
        self.assertIsNone(CTi.get_entity(b'1//0'))
        return

    def test_good_entity(self):
        self.assertIs(CTi.get_entity(b'int'), int)
        return


class Py2Test(unittest.TestCase):

    def test_paramtuple_float(self):
        with warnings.catch_warnings():
            warnings.simplefilter(b'ignore')
            exec b'def f((a,b), c=0.0): pass'
        self.assertEqual(signature(f), b'(<tuple>, c=0.0)')
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=False)
