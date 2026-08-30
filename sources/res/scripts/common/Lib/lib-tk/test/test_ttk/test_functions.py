import sys, unittest, ttk

class MockTkApp():

    def splitlist(self, arg):
        if isinstance(arg, tuple):
            return arg
        return arg.split(b':')

    def wantobjects(self):
        return True


class MockTclObj(object):
    typename = b'test'

    def __init__(self, val):
        self.val = val
        return

    def __str__(self):
        return unicode(self.val)


class MockStateSpec(object):
    typename = b'StateSpec'

    def __init__(self, *args):
        self.val = args
        return

    def __str__(self):
        return (b' ').join(self.val)


class InternalFunctionsTest(unittest.TestCase):

    def test_format_optdict(self):

        def check_against(fmt_opts, result):
            for i in range(0, len(fmt_opts), 2):
                self.assertEqual(result.pop(fmt_opts[i]), fmt_opts[i + 1])

            if result:
                self.fail(b'result still got elements: %s' % result)
            return

        self.assertFalse(ttk._format_optdict({}))
        check_against(ttk._format_optdict({b'fg': b'blue', b'padding': [1, 2, 3, 4]}), {b'-fg': b'blue', b'-padding': b'1 2 3 4'})
        check_against(ttk._format_optdict({b'test': (1, 2, b'', 0)}), {b'-test': b'1 2 {} 0'})
        check_against(ttk._format_optdict({b'test': {b'left': b'as is'}}), {b'-test': {b'left': b'as is'}})
        check_against(ttk._format_optdict({b'test': [4, 19, 12, 20, 13], b'test2': 3, b'test3': b'', 
           b'test4': b'abc def', b'test5': b'"abc"', 
           b'test6': b'{}', b'test7': b'} -spam {'}, script=True), {b'-test': b'{1 -1 {} 2m 0}', b'-test2': b'3', b'-test3': b'{}', 
           b'-test4': b'{abc def}', b'-test5': b'{"abc"}', 
           b'-test6': b'\\{\\}', b'-test7': b'\\}\\ -spam\\ \\{'})
        opts = {u'\u03b1\u03b2\u03b3': True, u'\xe1': False}
        orig_opts = opts.copy()
        check_against(ttk._format_optdict(opts), {u'-\u03b1\u03b2\u03b3': True, u'-\xe1': False})
        self.assertEqual(opts, orig_opts)
        check_against(ttk._format_optdict({b'option': (b'one two', b'three')}), {b'-option': b'{one two} three'})
        check_against(ttk._format_optdict({b'option': (b'one\ttwo', b'three')}), {b'-option': b'{one\ttwo} three'})
        check_against(ttk._format_optdict({b'option': (b'', b'one')}), {b'-option': b'{} one'})
        check_against(ttk._format_optdict({b'option': (b'one} {two', b'three')}), {b'-option': b'one\\}\\ \\{two three'})
        check_against(ttk._format_optdict({b'option': (b'"one"', b'two')}), {b'-option': b'{"one"} two'})
        check_against(ttk._format_optdict({b'option': (b'{one}', b'two')}), {b'-option': b'\\{one\\} two'})
        amount_opts = len(ttk._format_optdict(opts, ignore=u'\xe1')) // 2
        self.assertEqual(amount_opts, len(opts) - 1)
        amount_opts = len(ttk._format_optdict(opts, ignore=(u'\xe1', b'b'))) // 2
        self.assertEqual(amount_opts, len(opts) - 1)
        self.assertFalse(ttk._format_optdict(opts, ignore=opts.keys()))
        return

    def test_format_mapdict(self):
        opts = {b'a': [(b'b', b'c', b'val'), (b'd', b'otherval'), (b'', b'single')]}
        result = ttk._format_mapdict(opts)
        self.assertEqual(len(result), len(opts.keys()) * 2)
        self.assertEqual(result, (b'-a', b'{b c} val d otherval {} single'))
        self.assertEqual(ttk._format_mapdict(opts, script=True), (b'-a', b'{{b c} val d otherval {} single}'))
        self.assertEqual(ttk._format_mapdict({2: []}), (b'-2', b''))
        opts = {u'\xfc\xf1\xed\u0107\xf3d\xe8': [(u'\xe1', u'v\xe3l')]}
        result = ttk._format_mapdict(opts)
        self.assertEqual(result, (u'-\xfc\xf1\xed\u0107\xf3d\xe8', u'\xe1 v\xe3l'))
        valid = {b'opt': [(b'', u'', b'hi')]}
        self.assertEqual(ttk._format_mapdict(valid), (b'-opt', b'{ } hi'))
        invalid = {b'opt': [(1, 2, b'valid val')]}
        self.assertRaises(TypeError, ttk._format_mapdict, invalid)
        invalid = {b'opt': [([1], b'2', b'valid val')]}
        self.assertRaises(TypeError, ttk._format_mapdict, invalid)
        valid = {b'opt': [[1, b'value']]}
        self.assertEqual(ttk._format_mapdict(valid), (b'-opt', b'1 value'))
        for stateval in (None, 0, False, b'', set()):
            valid = {b'opt': [(stateval, b'value')]}
            self.assertEqual(ttk._format_mapdict(valid), (b'-opt', b'{} value'))

        opts = {b'a': None}
        self.assertRaises(TypeError, ttk._format_mapdict, opts)
        self.assertRaises(IndexError, ttk._format_mapdict, {b'a': [(b'invalid',)]})
        return

    def test_format_elemcreate(self):
        self.assertTrue(ttk._format_elemcreate(None), (None, ()))
        self.assertRaises(IndexError, ttk._format_elemcreate, b'image')
        self.assertEqual(ttk._format_elemcreate(b'image', False, b'test'), (
         b'test ', ()))
        self.assertEqual(ttk._format_elemcreate(b'image', False, b'test', (b'', b'a')), (b'test {} a', ()))
        self.assertEqual(ttk._format_elemcreate(b'image', False, b'test', (b'a', b'b', b'c')), (b'test {a b} c', ()))
        res = ttk._format_elemcreate(b'image', False, b'test', (b'a', b'b'), a=b'x', b=b'y')
        self.assertEqual(res[0], b'test a b')
        self.assertEqual(set(res[1]), {b'-a', b'x', b'-b', b'y'})
        self.assertEqual(ttk._format_elemcreate(b'image', True, b'test', (b'a', b'b', b'c', b'd'), x=[2, 3]), (b'{test {a b c} d}', b'-x {2 3}'))
        self.assertRaises(ValueError, ttk._format_elemcreate, b'vsapi')
        self.assertEqual(ttk._format_elemcreate(b'vsapi', False, b'a', b'b'), (
         b'a b ', ()))
        self.assertEqual(ttk._format_elemcreate(b'vsapi', False, b'a', b'b', (b'a', b'b', b'c')), (b'a b {a b} c', ()))
        self.assertEqual(ttk._format_elemcreate(b'vsapi', False, b'a', b'b', (b'a', b'b'), opt=b'x'), (b'a b a b', (b'-opt', b'x')))
        self.assertEqual(ttk._format_elemcreate(b'vsapi', True, b'a', b'b', (
         b'a', b'b', [1, 2]), opt=b'x'), (b'{a b {a b} {1 2}}', b'-opt x'))
        self.assertRaises(IndexError, ttk._format_elemcreate, b'from')
        self.assertEqual(ttk._format_elemcreate(b'from', False, b'a'), (
         b'a', ()))
        self.assertEqual(ttk._format_elemcreate(b'from', False, b'a', b'b'), (
         b'a', (b'b',)))
        self.assertEqual(ttk._format_elemcreate(b'from', True, b'a', b'b'), (b'{a}', b'b'))
        return

    def test_format_layoutlist(self):

        def sample(indent=0, indent_size=2):
            return ttk._format_layoutlist([
             (
              b'a',
              {b'other': [1, 2, 3], b'children': [
                             (
                              b'b',
                              {b'children': [
                                             (
                                              b'c',
                                              {b'children': [
                                                             (
                                                              b'd', {b'nice': b'opt'})], 
                                                 b'something': (1, 2)})]})]})], indent=indent, indent_size=indent_size)[0]

        def sample_expected(indent=0, indent_size=2):
            spaces = lambda amount=0: b' ' * (amount + indent)
            return b'%sa -other {1 2 3} -children {\n%sb -children {\n%sc -something {1 2} -children {\n%sd -nice opt\n%s}\n%s}\n%s}' % (
             spaces(), spaces(indent_size),
             spaces(2 * indent_size), spaces(3 * indent_size),
             spaces(2 * indent_size), spaces(indent_size), spaces())

        self.assertEqual(ttk._format_layoutlist([])[0], b'')
        smallest = ttk._format_layoutlist([(b'a', None)], indent=0)
        self.assertEqual(smallest, ttk._format_layoutlist([(b'a', b'')], indent=0))
        self.assertEqual(smallest[0], b'a')
        self.assertEqual(sample(), sample_expected())
        for i in range(4):
            self.assertEqual(sample(i), sample_expected(i))
            self.assertEqual(sample(i, i), sample_expected(i, i))

        self.assertRaises(ValueError, ttk._format_layoutlist, [
         b'bad', b'format'])
        self.assertRaises(TypeError, ttk._format_layoutlist, None)
        self.assertRaises(AttributeError, ttk._format_layoutlist, [(b'a', b'b')])
        self.assertRaises(ValueError, ttk._format_layoutlist, [
         (
          b'name', {b'children': {b'a': None}})])
        return

    def test_script_from_settings(self):
        self.assertFalse(ttk._script_from_settings({b'name': {b'configure': None, b'map': None, b'element create': None}}))
        self.assertEqual(ttk._script_from_settings({b'name': {b'layout': None}}), b'ttk::style layout name {\nnull\n}')
        configdict = {u'\u03b1\u03b2\u03b3': True, u'\xe1': False}
        self.assertTrue(ttk._script_from_settings({b'name': {b'configure': configdict}}))
        mapdict = {u'\xfc\xf1\xed\u0107\xf3d\xe8': [(u'\xe1', u'v\xe3l')]}
        self.assertTrue(ttk._script_from_settings({b'name': {b'map': mapdict}}))
        self.assertRaises(IndexError, ttk._script_from_settings, {b'name': {b'element create': [b'image']}})
        self.assertTrue(ttk._script_from_settings({b'name': {b'element create': [b'image', b'name']}}))
        image = {b'thing': {b'element create': [
                                        b'image', b'name', (b'state1', b'state2', b'val')]}}
        self.assertEqual(ttk._script_from_settings(image), b'ttk::style element create thing image {name {state1 state2} val} ')
        image[b'thing'][b'element create'].append({b'opt': 30})
        self.assertEqual(ttk._script_from_settings(image), b'ttk::style element create thing image {name {state1 state2} val} -opt 30')
        image[b'thing'][b'element create'][-1][b'opt'] = [
         MockTclObj(3),
         MockTclObj(b'2m')]
        self.assertEqual(ttk._script_from_settings(image), b'ttk::style element create thing image {name {state1 state2} val} -opt {3 2m}')
        return

    def test_tclobj_to_py(self):
        self.assertEqual(ttk._tclobj_to_py((MockStateSpec(b'a', b'b'), b'val')), [
         (b'a', b'b', b'val')])
        self.assertEqual(ttk._tclobj_to_py([MockTclObj(b'1'), 2, MockTclObj(b'3m')]), [
         1, 2, b'3m'])
        return

    def test_list_from_statespec(self):

        def test_it(sspec, value, res_value, states):
            self.assertEqual(ttk._list_from_statespec((
             sspec, value)), [states + (res_value,)])
            return

        states_even = tuple(b'state%d' % i for i in range(6))
        statespec = MockStateSpec(*states_even)
        test_it(statespec, b'val', b'val', states_even)
        test_it(statespec, MockTclObj(b'val'), b'val', states_even)
        states_odd = tuple(b'state%d' % i for i in range(5))
        statespec = MockStateSpec(*states_odd)
        test_it(statespec, b'val', b'val', states_odd)
        test_it((b'a', b'b', b'c'), MockTclObj(b'val'), b'val', (b'a', b'b', b'c'))
        return

    def test_list_from_layouttuple(self):
        tk = MockTkApp()
        self.assertFalse(ttk._list_from_layouttuple(tk, ()))
        self.assertEqual(ttk._list_from_layouttuple(tk, (b'name',)), [
         (
          b'name', {})])
        sample_ltuple = (b'name', b'-option', b'value')
        self.assertEqual(ttk._list_from_layouttuple(tk, sample_ltuple), [
         (
          b'name', {b'option': b'value'})])
        self.assertEqual(ttk._list_from_layouttuple(tk, (
         b'something', b'-children', ())), [
         (
          b'something', {b'children': []})])
        ltuple = (
         b'name', b'-option', b'niceone', b'-children',
         (
          b'otherone', b'-children',
          (b'child',), b'-otheropt', b'othervalue'))
        self.assertEqual(ttk._list_from_layouttuple(tk, ltuple), [
         (
          b'name',
          {b'option': b'niceone', b'children': [
                         (
                          b'otherone',
                          {b'otheropt': b'othervalue', b'children': [
                                         (
                                          b'child', {})]})]})])
        self.assertRaises(ValueError, ttk._list_from_layouttuple, tk, (b'name', b'no_minus'))
        self.assertRaises(ValueError, ttk._list_from_layouttuple, tk, (b'name', b'no_minus', b'value'))
        self.assertRaises(ValueError, ttk._list_from_layouttuple, tk, (b'something', b'-children'))
        return

    def test_val_or_dict(self):

        def func(res, opt=None, val=None):
            if opt is None:
                return res
            else:
                if val is None:
                    return b'test val'
                return (
                 opt, val)

        tk = MockTkApp()
        tk.call = func
        self.assertEqual(ttk._val_or_dict(tk, {}, b'-test:3'), {b'test': b'3'})
        self.assertEqual(ttk._val_or_dict(tk, {}, (b'-test', 3)), {b'test': 3})
        self.assertEqual(ttk._val_or_dict(tk, {b'test': None}, b'x:y'), b'test val')
        self.assertEqual(ttk._val_or_dict(tk, {b'test': 3}, b'x:y'), {b'test': 3})
        return

    def test_convert_stringval(self):
        tests = (
         (0, 0), (b'09', 9), (b'a', b'a'), (u'\xe1\xda', u'\xe1\xda'), ([], b'[]'),
         (None, b'None'))
        for orig, expected in tests:
            self.assertEqual(ttk._convert_stringval(orig), expected)

        if sys.getdefaultencoding() == b'ascii':
            self.assertRaises(UnicodeDecodeError, ttk._convert_stringval, b'\xc3\xa1')
        return


class TclObjsToPyTest(unittest.TestCase):

    def test_unicode(self):
        adict = {b'opt': u'v\xe4l\xfa\xe8'}
        self.assertEqual(ttk.tclobjs_to_py(adict), {b'opt': u'v\xe4l\xfa\xe8'})
        adict[b'opt'] = MockTclObj(adict[b'opt'])
        self.assertEqual(ttk.tclobjs_to_py(adict), {b'opt': u'v\xe4l\xfa\xe8'})
        return

    def test_multivalues(self):
        adict = {b'opt': [1, 2, 3, 4]}
        self.assertEqual(ttk.tclobjs_to_py(adict), {b'opt': [1, 2, 3, 4]})
        adict[b'opt'] = [
         1, b'xm', 3]
        self.assertEqual(ttk.tclobjs_to_py(adict), {b'opt': [1, b'xm', 3]})
        adict[b'opt'] = (
         MockStateSpec(b'a', b'b'), u'v\xe1l\u0169\xe8')
        self.assertEqual(ttk.tclobjs_to_py(adict), {b'opt': [(b'a', b'b', u'v\xe1l\u0169\xe8')]})
        self.assertEqual(ttk.tclobjs_to_py({b'x': [b'y z']}), {b'x': [b'y z']})
        return

    def test_nosplit(self):
        self.assertEqual(ttk.tclobjs_to_py({b'text': b'some text'}), {b'text': b'some text'})
        return


tests_nogui = (
 InternalFunctionsTest, TclObjsToPyTest)
if __name__ == b'__main__':
    from test.test_support import run_unittest
    run_unittest(*tests_nogui)
