import unittest, Tkinter as tkinter
from Tkinter import TclError
import ttk
from test.test_support import requires, run_unittest, have_unicode, u
import sys
from test_functions import MockTclObj
from support import AbstractTkTest, tcl_version, get_tk_patchlevel, simulate_mouse_click
from widget_tests import add_standard_options, noconv, noconv_meth, AbstractWidgetTest, StandardOptionsTests, IntegerSizeTests, PixelSizeTests, setUpModule
requires(b'gui')

class StandardTtkOptionsTests(StandardOptionsTests):

    def test_class(self):
        widget = self.create()
        self.assertEqual(widget[b'class'], b'')
        errmsg = b'attempt to change read-only option'
        if get_tk_patchlevel() < (8, 6, 0, b'beta', 3):
            errmsg = b'Attempt to change read-only option'
        self.checkInvalidParam(widget, b'class', b'Foo', errmsg=errmsg)
        widget2 = self.create(class_=b'Foo')
        self.assertEqual(widget2[b'class'], b'Foo')
        return

    def test_padding(self):
        widget = self.create()
        self.checkParam(widget, b'padding', 0, expected=(b'0',))
        self.checkParam(widget, b'padding', 5, expected=(b'5',))
        self.checkParam(widget, b'padding', (5, 6), expected=(b'5', b'6'))
        self.checkParam(widget, b'padding', (5, 6, 7), expected=(b'5', b'6', b'7'))
        self.checkParam(widget, b'padding', (5, 6, 7, 8), expected=(b'5', b'6', b'7', b'8'))
        self.checkParam(widget, b'padding', (b'5p', b'6p', b'7p', b'8p'))
        self.checkParam(widget, b'padding', (), expected=b'')
        return

    def test_style(self):
        widget = self.create()
        self.assertEqual(widget[b'style'], b'')
        errmsg = b'Layout Foo not found'
        if hasattr(self, b'default_orient'):
            errmsg = b'Layout %s.Foo not found' % getattr(self, b'default_orient').title()
        self.checkInvalidParam(widget, b'style', b'Foo', errmsg=errmsg)
        widget2 = self.create(class_=b'Foo')
        self.assertEqual(widget2[b'class'], b'Foo')
        return


class WidgetTest(AbstractTkTest, unittest.TestCase):

    def setUp(self):
        super(WidgetTest, self).setUp()
        self.widget = ttk.Button(self.root, width=0, text=b'Text')
        self.widget.pack()
        self.widget.wait_visibility()
        return

    def test_identify(self):
        self.widget.update_idletasks()
        self.assertEqual(self.widget.identify(self.widget.winfo_width() // 2, self.widget.winfo_height() // 2), b'label')
        self.assertEqual(self.widget.identify(-1, -1), b'')
        self.assertRaises(tkinter.TclError, self.widget.identify, None, 5)
        self.assertRaises(tkinter.TclError, self.widget.identify, 5, None)
        self.assertRaises(tkinter.TclError, self.widget.identify, 5, b'')
        return

    def test_widget_state(self):
        self.assertEqual(self.widget.state(), ())
        self.assertEqual(self.widget.instate([b'!disabled']), True)
        self.assertEqual(self.widget.state([b'disabled']), (b'!disabled',))
        self.assertEqual(self.widget.state([b'disabled']), ())
        self.assertEqual(self.widget.state([b'!disabled', b'active']), (b'!active', b'disabled'))
        self.assertEqual(self.widget.state([b'!disabled', b'active']), ())
        self.assertEqual(self.widget.state([b'active', b'!disabled']), ())

        def test_cb(arg1, **kw):
            return (
             arg1, kw)

        self.assertEqual(self.widget.instate([b'!disabled'], test_cb, b'hi', **{b'msg': b'there'}), (
         b'hi', {b'msg': b'there'}))
        currstate = self.widget.state()
        self.assertRaises(tkinter.TclError, self.widget.instate, [
         b'badstate'])
        self.assertRaises(tkinter.TclError, self.widget.instate, [
         b'disabled', b'badstate'])
        self.assertEqual(currstate, self.widget.state())
        self.widget.state([b'active', b'!disabled'])
        self.assertEqual(self.widget.state(), (b'active',))
        return


class AbstractToplevelTest(AbstractWidgetTest, PixelSizeTests):
    _conv_pixels = noconv_meth


@add_standard_options(StandardTtkOptionsTests)
class FrameTest(AbstractToplevelTest, unittest.TestCase):
    OPTIONS = (b'borderwidth', b'class', b'cursor', b'height', b'padding', b'relief', b'style', b'takefocus', b'width')

    def create(self, **kwargs):
        return ttk.Frame(self.root, **kwargs)


@add_standard_options(StandardTtkOptionsTests)
class LabelFrameTest(AbstractToplevelTest, unittest.TestCase):
    OPTIONS = (b'borderwidth', b'class', b'cursor', b'height', b'labelanchor', b'labelwidget', b'padding', b'relief', b'style', b'takefocus', b'text', b'underline', b'width')

    def create(self, **kwargs):
        return ttk.LabelFrame(self.root, **kwargs)

    def test_labelanchor(self):
        widget = self.create()
        self.checkEnumParam(widget, b'labelanchor', b'e', b'en', b'es', b'n', b'ne', b'nw', b's', b'se', b'sw', b'w', b'wn', b'ws', errmsg=b'Bad label anchor specification {}')
        self.checkInvalidParam(widget, b'labelanchor', b'center')
        return

    def test_labelwidget(self):
        widget = self.create()
        label = ttk.Label(self.root, text=b'Mupp', name=b'foo')
        self.checkParam(widget, b'labelwidget', label, expected=b'.foo')
        label.destroy()
        return


class AbstractLabelTest(AbstractWidgetTest):

    def checkImageParam(self, widget, name):
        image = tkinter.PhotoImage(master=self.root, name=b'image1')
        image2 = tkinter.PhotoImage(master=self.root, name=b'image2')
        self.checkParam(widget, name, image, expected=(b'image1',))
        self.checkParam(widget, name, b'image1', expected=(b'image1',))
        self.checkParam(widget, name, (image,), expected=(b'image1',))
        self.checkParam(widget, name, (image, b'active', image2), expected=(b'image1', b'active', b'image2'))
        self.checkParam(widget, name, b'image1 active image2', expected=(b'image1', b'active', b'image2'))
        self.checkInvalidParam(widget, name, b'spam', errmsg=b'image "spam" doesn\'t exist')
        return

    def test_compound(self):
        widget = self.create()
        self.checkEnumParam(widget, b'compound', b'none', b'text', b'image', b'center', b'top', b'bottom', b'left', b'right')
        return

    def test_state(self):
        widget = self.create()
        self.checkParams(widget, b'state', b'active', b'disabled', b'normal')
        return

    def test_width(self):
        widget = self.create()
        self.checkParams(widget, b'width', 402, -402, 0)
        return


@add_standard_options(StandardTtkOptionsTests)
class LabelTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'anchor', b'background', b'borderwidth', b'class', b'compound', b'cursor', b'font', b'foreground', b'image', b'justify', b'padding', b'relief', b'state', b'style', b'takefocus', b'text', b'textvariable', b'underline', b'width', b'wraplength')
    _conv_pixels = noconv_meth

    def create(self, **kwargs):
        return ttk.Label(self.root, **kwargs)

    def test_font(self):
        widget = self.create()
        self.checkParam(widget, b'font', b'-Adobe-Helvetica-Medium-R-Normal--*-120-*-*-*-*-*-*')
        return


@add_standard_options(StandardTtkOptionsTests)
class ButtonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'class', b'command', b'compound', b'cursor', b'default', b'image', b'padding', b'state', b'style', b'takefocus', b'text', b'textvariable', b'underline', b'width')

    def create(self, **kwargs):
        return ttk.Button(self.root, **kwargs)

    def test_default(self):
        widget = self.create()
        self.checkEnumParam(widget, b'default', b'normal', b'active', b'disabled')
        return

    def test_invoke(self):
        success = []
        btn = ttk.Button(self.root, command=(lambda : success.append(1)))
        btn.invoke()
        self.assertTrue(success)
        return


@add_standard_options(StandardTtkOptionsTests)
class CheckbuttonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'class', b'command', b'compound', b'cursor', b'image', b'offvalue', b'onvalue', b'padding', b'state', b'style', b'takefocus', b'text', b'textvariable', b'underline', b'variable', b'width')

    def create(self, **kwargs):
        return ttk.Checkbutton(self.root, **kwargs)

    def test_offvalue(self):
        widget = self.create()
        self.checkParams(widget, b'offvalue', 1, 2.3, b'', b'any string')
        return

    def test_onvalue(self):
        widget = self.create()
        self.checkParams(widget, b'onvalue', 1, 2.3, b'', b'any string')
        return

    def test_invoke(self):
        success = []

        def cb_test():
            success.append(1)
            return b'cb test called'

        cbtn = ttk.Checkbutton(self.root, command=cb_test)
        self.assertEqual(cbtn.state(), (b'alternate',))
        self.assertRaises(tkinter.TclError, cbtn.tk.globalgetvar, cbtn[b'variable'])
        res = cbtn.invoke()
        self.assertEqual(res, b'cb test called')
        self.assertEqual(cbtn[b'onvalue'], cbtn.tk.globalgetvar(cbtn[b'variable']))
        self.assertTrue(success)
        cbtn[b'command'] = b''
        res = cbtn.invoke()
        self.assertFalse(str(res))
        self.assertLessEqual(len(success), 1)
        self.assertEqual(cbtn[b'offvalue'], cbtn.tk.globalgetvar(cbtn[b'variable']))
        return


@add_standard_options(IntegerSizeTests, StandardTtkOptionsTests)
class EntryTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'background', b'class', b'cursor', b'exportselection', b'font', b'foreground', b'invalidcommand', b'justify', b'show', b'state', b'style', b'takefocus', b'textvariable', b'validate', b'validatecommand', b'width', b'xscrollcommand')

    def setUp(self):
        super(EntryTest, self).setUp()
        self.entry = self.create()
        return

    def create(self, **kwargs):
        return ttk.Entry(self.root, **kwargs)

    def test_invalidcommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'invalidcommand')
        return

    def test_show(self):
        widget = self.create()
        self.checkParam(widget, b'show', b'*')
        self.checkParam(widget, b'show', b'')
        self.checkParam(widget, b'show', b' ')
        return

    def test_state(self):
        widget = self.create()
        self.checkParams(widget, b'state', b'disabled', b'normal', b'readonly')
        return

    def test_validate(self):
        widget = self.create()
        self.checkEnumParam(widget, b'validate', b'all', b'key', b'focus', b'focusin', b'focusout', b'none')
        return

    def test_validatecommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'validatecommand')
        return

    def test_bbox(self):
        self.assertIsBoundingBox(self.entry.bbox(0))
        self.assertRaises(tkinter.TclError, self.entry.bbox, b'noindex')
        self.assertRaises(tkinter.TclError, self.entry.bbox, None)
        return

    def test_identify(self):
        self.entry.pack()
        self.entry.wait_visibility()
        self.entry.update_idletasks()
        if sys.platform == b'darwin':
            self.assertIn(self.entry.identify(5, 5), (b'textarea', b'Combobox.button'))
        else:
            self.assertEqual(self.entry.identify(5, 5), b'textarea')
        self.assertEqual(self.entry.identify(-1, -1), b'')
        self.assertRaises(tkinter.TclError, self.entry.identify, None, 5)
        self.assertRaises(tkinter.TclError, self.entry.identify, 5, None)
        self.assertRaises(tkinter.TclError, self.entry.identify, 5, b'')
        return

    def test_validation_options(self):
        success = []
        test_invalid = lambda : success.append(True)
        self.entry[b'validate'] = b'none'
        self.entry[b'validatecommand'] = lambda : False
        self.entry[b'invalidcommand'] = test_invalid
        self.entry.validate()
        self.assertTrue(success)
        self.entry[b'invalidcommand'] = b''
        self.entry.validate()
        self.assertEqual(len(success), 1)
        self.entry[b'invalidcommand'] = test_invalid
        self.entry[b'validatecommand'] = lambda : True
        self.entry.validate()
        self.assertEqual(len(success), 1)
        self.entry[b'validatecommand'] = b''
        self.entry.validate()
        self.assertEqual(len(success), 1)
        self.entry[b'validatecommand'] = True
        self.assertRaises(tkinter.TclError, self.entry.validate)
        return

    def test_validation(self):
        validation = []

        def validate(to_insert):
            if not b'a' <= to_insert.lower() <= b'z':
                validation.append(False)
                return False
            validation.append(True)
            return True

        self.entry[b'validate'] = b'key'
        self.entry[b'validatecommand'] = (self.entry.register(validate), b'%S')
        self.entry.insert(b'end', 1)
        self.entry.insert(b'end', b'a')
        self.assertEqual(validation, [False, True])
        self.assertEqual(self.entry.get(), b'a')
        return

    def test_revalidation(self):

        def validate(content):
            for letter in content:
                if not b'a' <= letter.lower() <= b'z':
                    return False

            return True

        self.entry[b'validatecommand'] = (
         self.entry.register(validate), b'%P')
        self.entry.insert(b'end', b'avocado')
        self.assertEqual(self.entry.validate(), True)
        self.assertEqual(self.entry.state(), ())
        self.entry.delete(0, b'end')
        self.assertEqual(self.entry.get(), b'')
        self.entry.insert(b'end', b'a1b')
        self.assertEqual(self.entry.validate(), False)
        self.assertEqual(self.entry.state(), (b'invalid',))
        self.entry.delete(1)
        self.assertEqual(self.entry.validate(), True)
        self.assertEqual(self.entry.state(), ())
        return


@add_standard_options(IntegerSizeTests, StandardTtkOptionsTests)
class ComboboxTest(EntryTest, unittest.TestCase):
    OPTIONS = (b'background', b'class', b'cursor', b'exportselection', b'font', b'foreground', b'height', b'invalidcommand', b'justify', b'postcommand', b'show', b'state', b'style', b'takefocus', b'textvariable', b'validate', b'validatecommand', b'values', b'width', b'xscrollcommand')

    def setUp(self):
        super(ComboboxTest, self).setUp()
        self.combo = self.create()
        return

    def create(self, **kwargs):
        return ttk.Combobox(self.root, **kwargs)

    def test_height(self):
        widget = self.create()
        self.checkParams(widget, b'height', 100, 101.2, 102.6, -100, 0, b'1i')
        return

    def _show_drop_down_listbox(self):
        width = self.combo.winfo_width()
        self.combo.event_generate(b'<ButtonPress-1>', x=width - 5, y=5)
        self.combo.event_generate(b'<ButtonRelease-1>', x=width - 5, y=5)
        self.combo.update_idletasks()
        return

    def test_virtual_event(self):
        success = []
        self.combo[b'values'] = [
         1]
        self.combo.bind(b'<<ComboboxSelected>>', (lambda evt: success.append(True)))
        self.combo.pack()
        self.combo.wait_visibility()
        height = self.combo.winfo_height()
        self._show_drop_down_listbox()
        self.combo.update()
        self.combo.event_generate(b'<Return>')
        self.combo.update()
        self.assertTrue(success)
        return

    def test_postcommand(self):
        success = []
        self.combo[b'postcommand'] = lambda : success.append(True)
        self.combo.pack()
        self.combo.wait_visibility()
        self._show_drop_down_listbox()
        self.assertTrue(success)
        self.combo[b'postcommand'] = b''
        self._show_drop_down_listbox()
        self.assertEqual(len(success), 1)
        return

    def test_values(self):

        def check_get_current(getval, currval):
            self.assertEqual(self.combo.get(), getval)
            self.assertEqual(self.combo.current(), currval)
            return

        self.assertEqual(self.combo[b'values'], () if tcl_version < (8, 5) else b'')
        check_get_current(b'', -1)
        self.checkParam(self.combo, b'values', b'mon tue wed thur', expected=(b'mon', b'tue', b'wed', b'thur'))
        self.checkParam(self.combo, b'values', (b'mon', b'tue', b'wed', b'thur'))
        self.checkParam(self.combo, b'values', (42, 3.14, b'', b'any string'))
        self.checkParam(self.combo, b'values', () if tcl_version < (8, 5) else b'')
        self.combo[b'values'] = [
         b'a', 1, b'c']
        self.combo.set(b'c')
        check_get_current(b'c', 2)
        self.combo.current(0)
        check_get_current(b'a', 0)
        self.combo.set(b'd')
        check_get_current(b'd', -1)
        self.combo.set(b'')
        self.combo[b'values'] = (1, 2, b'', 3)
        check_get_current(b'', 2)
        self.combo.configure(values=[1, b'', 2])
        self.assertEqual(self.combo[b'values'], (b'1', b'', b'2') if self.wantobjects else b'1 {} 2')
        self.combo[b'values'] = [
         b'a b', b'a\tb', b'a\nb']
        self.assertEqual(self.combo[b'values'], (b'a b', b'a\tb', b'a\nb') if self.wantobjects else b'{a b} {a\tb} {a\nb}')
        self.combo[b'values'] = [
         b'a\\tb', b'"a"', b'} {']
        self.assertEqual(self.combo[b'values'], (b'a\\tb', b'"a"', b'} {') if self.wantobjects else b'a\\\\tb {"a"} \\}\\ \\{')
        self.assertRaises(tkinter.TclError, self.combo.current, len(self.combo[b'values']))
        self.assertRaises(tkinter.TclError, self.combo.current, b'')
        combo2 = ttk.Combobox(self.root, values=[1, 2, b''])
        self.assertEqual(combo2[b'values'], (b'1', b'2', b'') if self.wantobjects else b'1 2 {}')
        combo2.destroy()
        return


@add_standard_options(IntegerSizeTests, StandardTtkOptionsTests)
class PanedWindowTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'cursor', b'height', b'orient', b'style', b'takefocus', b'width')

    def setUp(self):
        super(PanedWindowTest, self).setUp()
        self.paned = self.create()
        return

    def create(self, **kwargs):
        return ttk.PanedWindow(self.root, **kwargs)

    def test_orient(self):
        widget = self.create()
        self.assertEqual(str(widget[b'orient']), b'vertical')
        errmsg = b'attempt to change read-only option'
        if get_tk_patchlevel() < (8, 6, 0, b'beta', 3):
            errmsg = b'Attempt to change read-only option'
        self.checkInvalidParam(widget, b'orient', b'horizontal', errmsg=errmsg)
        widget2 = self.create(orient=b'horizontal')
        self.assertEqual(str(widget2[b'orient']), b'horizontal')
        return

    def test_add(self):
        label = ttk.Label(self.paned)
        child = ttk.Label(label)
        self.assertRaises(tkinter.TclError, self.paned.add, child)
        label.destroy()
        child.destroy()
        label = ttk.Label(self.root)
        child = ttk.Label(label)
        self.assertRaises(tkinter.TclError, self.paned.add, child)
        child.destroy()
        label.destroy()
        good_child = ttk.Label(self.root)
        self.paned.add(good_child)
        self.assertRaises(tkinter.TclError, self.paned.add, good_child)
        other_child = ttk.Label(self.paned)
        self.paned.add(other_child)
        self.assertEqual(self.paned.pane(0), self.paned.pane(1))
        self.assertRaises(tkinter.TclError, self.paned.pane, 2)
        good_child.destroy()
        other_child.destroy()
        self.assertRaises(tkinter.TclError, self.paned.pane, 0)
        return

    def test_forget(self):
        self.assertRaises(tkinter.TclError, self.paned.forget, None)
        self.assertRaises(tkinter.TclError, self.paned.forget, 0)
        self.paned.add(ttk.Label(self.root))
        self.paned.forget(0)
        self.assertRaises(tkinter.TclError, self.paned.forget, 0)
        return

    def test_insert(self):
        self.assertRaises(tkinter.TclError, self.paned.insert, None, 0)
        self.assertRaises(tkinter.TclError, self.paned.insert, 0, None)
        self.assertRaises(tkinter.TclError, self.paned.insert, 0, 0)
        child = ttk.Label(self.root)
        child2 = ttk.Label(self.root)
        child3 = ttk.Label(self.root)
        self.assertRaises(tkinter.TclError, self.paned.insert, 0, child)
        self.paned.insert(b'end', child2)
        self.paned.insert(0, child)
        self.assertEqual(self.paned.panes(), (str(child), str(child2)))
        self.paned.insert(0, child2)
        self.assertEqual(self.paned.panes(), (str(child2), str(child)))
        self.paned.insert(b'end', child3)
        self.assertEqual(self.paned.panes(), (
         str(child2), str(child), str(child3)))
        panes = self.paned.panes()
        self.paned.insert(b'end', child3)
        self.assertEqual(panes, self.paned.panes())
        self.paned.insert(child2, child3)
        self.assertEqual(self.paned.panes(), (
         str(child3), str(child2), str(child)))
        return

    def test_pane(self):
        self.assertRaises(tkinter.TclError, self.paned.pane, 0)
        child = ttk.Label(self.root)
        self.paned.add(child)
        self.assertIsInstance(self.paned.pane(0), dict)
        self.assertEqual(self.paned.pane(0, weight=None), 0 if self.wantobjects else b'0')
        self.assertEqual(self.paned.pane(0, b'weight'), 0 if self.wantobjects else b'0')
        self.assertEqual(self.paned.pane(0), self.paned.pane(str(child)))
        self.assertRaises(tkinter.TclError, self.paned.pane, 0, badoption=b'somevalue')
        return

    def test_sashpos(self):
        self.assertRaises(tkinter.TclError, self.paned.sashpos, None)
        self.assertRaises(tkinter.TclError, self.paned.sashpos, b'')
        self.assertRaises(tkinter.TclError, self.paned.sashpos, 0)
        child = ttk.Label(self.paned, text=b'a')
        self.paned.add(child, weight=1)
        self.assertRaises(tkinter.TclError, self.paned.sashpos, 0)
        child2 = ttk.Label(self.paned, text=b'b')
        self.paned.add(child2)
        self.assertRaises(tkinter.TclError, self.paned.sashpos, 1)
        self.paned.pack(expand=True, fill=b'both')
        self.paned.wait_visibility()
        curr_pos = self.paned.sashpos(0)
        self.paned.sashpos(0, 1000)
        self.assertNotEqual(curr_pos, self.paned.sashpos(0))
        self.assertIsInstance(self.paned.sashpos(0), int)
        return


@add_standard_options(StandardTtkOptionsTests)
class RadiobuttonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'class', b'command', b'compound', b'cursor', b'image', b'padding', b'state', b'style', b'takefocus', b'text', b'textvariable', b'underline', b'value', b'variable', b'width')

    def create(self, **kwargs):
        return ttk.Radiobutton(self.root, **kwargs)

    def test_value(self):
        widget = self.create()
        self.checkParams(widget, b'value', 1, 2.3, b'', b'any string')
        return

    def test_invoke(self):
        success = []

        def cb_test():
            success.append(1)
            return b'cb test called'

        myvar = tkinter.IntVar(self.root)
        cbtn = ttk.Radiobutton(self.root, command=cb_test, variable=myvar, value=0)
        cbtn2 = ttk.Radiobutton(self.root, command=cb_test, variable=myvar, value=1)
        if self.wantobjects:
            conv = lambda x: x
        else:
            conv = int
        res = cbtn.invoke()
        self.assertEqual(res, b'cb test called')
        self.assertEqual(conv(cbtn[b'value']), myvar.get())
        self.assertEqual(myvar.get(), conv(cbtn.tk.globalgetvar(cbtn[b'variable'])))
        self.assertTrue(success)
        cbtn2[b'command'] = b''
        res = cbtn2.invoke()
        self.assertEqual(str(res), b'')
        self.assertLessEqual(len(success), 1)
        self.assertEqual(conv(cbtn2[b'value']), myvar.get())
        self.assertEqual(myvar.get(), conv(cbtn.tk.globalgetvar(cbtn[b'variable'])))
        self.assertEqual(str(cbtn[b'variable']), str(cbtn2[b'variable']))
        return


class MenubuttonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'class', b'compound', b'cursor', b'direction', b'image', b'menu', b'padding', b'state', b'style', b'takefocus', b'text', b'textvariable', b'underline', b'width')

    def create(self, **kwargs):
        return ttk.Menubutton(self.root, **kwargs)

    def test_direction(self):
        widget = self.create()
        self.checkEnumParam(widget, b'direction', b'above', b'below', b'left', b'right', b'flush')
        return

    def test_menu(self):
        widget = self.create()
        menu = tkinter.Menu(widget, name=b'menu')
        self.checkParam(widget, b'menu', menu, conv=str)
        menu.destroy()
        return


@add_standard_options(StandardTtkOptionsTests)
class ScaleTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'command', b'cursor', b'from', b'length', b'orient', b'style', b'takefocus', b'to', b'value', b'variable')
    _conv_pixels = noconv_meth
    default_orient = b'horizontal'

    def setUp(self):
        super(ScaleTest, self).setUp()
        self.scale = self.create()
        self.scale.pack()
        self.scale.update()
        return

    def create(self, **kwargs):
        return ttk.Scale(self.root, **kwargs)

    def test_from(self):
        widget = self.create()
        self.checkFloatParam(widget, b'from', 100, 14.9, 15.1, conv=False)
        return

    def test_length(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'length', 130, 131.2, 135.6, b'5i')
        return

    def test_to(self):
        widget = self.create()
        self.checkFloatParam(widget, b'to', 300, 14.9, 15.1, -10, conv=False)
        return

    def test_value(self):
        widget = self.create()
        self.checkFloatParam(widget, b'value', 300, 14.9, 15.1, -10, conv=False)
        return

    def test_custom_event(self):
        failure = [1, 1, 1]
        funcid = self.scale.bind(b'<<RangeChanged>>', (lambda evt: failure.pop()))
        self.scale[b'from'] = 10
        self.scale[b'from_'] = 10
        self.scale[b'to'] = 3
        self.assertFalse(failure)
        failure = [
         1, 1, 1]
        self.scale.configure(from_=2, to=5)
        self.scale.configure(from_=0, to=-2)
        self.scale.configure(to=10)
        self.assertFalse(failure)
        return

    def test_get(self):
        if self.wantobjects:
            conv = lambda x: x
        else:
            conv = float
        scale_width = self.scale.winfo_width()
        self.assertEqual(self.scale.get(scale_width, 0), self.scale[b'to'])
        self.assertEqual(conv(self.scale.get(0, 0)), conv(self.scale[b'from']))
        self.assertEqual(self.scale.get(), self.scale[b'value'])
        self.scale[b'value'] = 30
        self.assertEqual(self.scale.get(), self.scale[b'value'])
        self.assertRaises(tkinter.TclError, self.scale.get, b'', 0)
        self.assertRaises(tkinter.TclError, self.scale.get, 0, b'')
        return

    def test_set(self):
        if self.wantobjects:
            conv = lambda x: x
        else:
            conv = float
        max = conv(self.scale[b'to'])
        new_max = max + 10
        self.scale.set(new_max)
        self.assertEqual(conv(self.scale.get()), max)
        min = conv(self.scale[b'from'])
        self.scale.set(min - 1)
        self.assertEqual(conv(self.scale.get()), min)
        var = tkinter.DoubleVar(self.root)
        self.scale[b'variable'] = var
        var.set(max + 5)
        self.assertEqual(conv(self.scale.get()), var.get())
        self.assertEqual(conv(self.scale.get()), max + 5)
        del var
        self.scale[b'value'] = max + 10
        self.assertEqual(conv(self.scale.get()), max + 10)
        self.assertEqual(conv(self.scale.get()), conv(self.scale[b'value']))
        self.assertEqual(conv(self.scale.get(0, 0)), min)
        self.assertEqual(conv(self.scale.get(self.scale.winfo_width(), 0)), max)
        self.assertRaises(tkinter.TclError, self.scale.set, None)
        return


@add_standard_options(StandardTtkOptionsTests)
class ProgressbarTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'cursor', b'orient', b'length', b'mode', b'maximum', b'phase', b'style', b'takefocus', b'value', b'variable')
    _conv_pixels = noconv_meth
    default_orient = b'horizontal'

    def create(self, **kwargs):
        return ttk.Progressbar(self.root, **kwargs)

    def test_length(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'length', 100.1, 56.7, b'2i')
        return

    def test_maximum(self):
        widget = self.create()
        self.checkFloatParam(widget, b'maximum', 150.2, 77.7, 0, -10, conv=False)
        return

    def test_mode(self):
        widget = self.create()
        self.checkEnumParam(widget, b'mode', b'determinate', b'indeterminate')
        return

    def test_phase(self):
        return

    def test_value(self):
        widget = self.create()
        self.checkFloatParam(widget, b'value', 150.2, 77.7, 0, -10, conv=False)
        return


@unittest.skipIf(sys.platform == b'darwin', b'ttk.Scrollbar is special on MacOSX')
@add_standard_options(StandardTtkOptionsTests)
class ScrollbarTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'command', b'cursor', b'orient', b'style', b'takefocus')
    default_orient = b'vertical'

    def create(self, **kwargs):
        return ttk.Scrollbar(self.root, **kwargs)


@add_standard_options(IntegerSizeTests, StandardTtkOptionsTests)
class NotebookTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'cursor', b'height', b'padding', b'style', b'takefocus', b'width')

    def setUp(self):
        super(NotebookTest, self).setUp()
        self.nb = self.create(padding=0)
        self.child1 = ttk.Label(self.root)
        self.child2 = ttk.Label(self.root)
        self.nb.add(self.child1, text=b'a')
        self.nb.add(self.child2, text=b'b')
        return

    def create(self, **kwargs):
        return ttk.Notebook(self.root, **kwargs)

    def test_tab_identifiers(self):
        self.nb.forget(0)
        self.nb.hide(self.child2)
        self.assertRaises(tkinter.TclError, self.nb.tab, self.child1)
        self.assertEqual(self.nb.index(b'end'), 1)
        self.nb.add(self.child2)
        self.assertEqual(self.nb.index(b'end'), 1)
        self.nb.select(self.child2)
        self.assertTrue(self.nb.tab(b'current'))
        self.nb.add(self.child1, text=b'a')
        self.nb.pack()
        self.nb.wait_visibility()
        if sys.platform == b'darwin':
            tb_idx = b'@20,5'
        else:
            tb_idx = b'@5,5'
        self.assertEqual(self.nb.tab(tb_idx), self.nb.tab(b'current'))
        for i in range(5, 100, 5):
            try:
                if self.nb.tab(b'@%d, 5' % i, text=None) == b'a':
                    break
            except tkinter.TclError:
                pass

        else:
            self.fail(b"Tab with text 'a' not found")

        return

    def test_add_and_hidden(self):
        self.assertRaises(tkinter.TclError, self.nb.hide, -1)
        self.assertRaises(tkinter.TclError, self.nb.hide, b'hi')
        self.assertRaises(tkinter.TclError, self.nb.hide, None)
        self.assertRaises(tkinter.TclError, self.nb.add, None)
        self.assertRaises(tkinter.TclError, self.nb.add, ttk.Label(self.root), unknown=b'option')
        tabs = self.nb.tabs()
        self.nb.hide(self.child1)
        self.nb.add(self.child1)
        self.assertEqual(self.nb.tabs(), tabs)
        child = ttk.Label(self.root)
        self.nb.add(child, text=b'c')
        tabs = self.nb.tabs()
        curr = self.nb.index(b'current')
        child2_index = self.nb.index(self.child2)
        self.nb.hide(self.child2)
        self.nb.add(self.child2)
        self.assertEqual(self.nb.tabs(), tabs)
        self.assertEqual(self.nb.index(self.child2), child2_index)
        self.assertEqual(str(self.child2), self.nb.tabs()[child2_index])
        self.assertEqual(self.nb.index(b'current'), curr + 1)
        return

    def test_forget(self):
        self.assertRaises(tkinter.TclError, self.nb.forget, -1)
        self.assertRaises(tkinter.TclError, self.nb.forget, b'hi')
        self.assertRaises(tkinter.TclError, self.nb.forget, None)
        tabs = self.nb.tabs()
        child1_index = self.nb.index(self.child1)
        self.nb.forget(self.child1)
        self.assertNotIn(str(self.child1), self.nb.tabs())
        self.assertEqual(len(tabs) - 1, len(self.nb.tabs()))
        self.nb.add(self.child1)
        self.assertEqual(self.nb.index(self.child1), 1)
        self.assertNotEqual(child1_index, self.nb.index(self.child1))
        return

    def test_index(self):
        self.assertRaises(tkinter.TclError, self.nb.index, -1)
        self.assertRaises(tkinter.TclError, self.nb.index, None)
        self.assertIsInstance(self.nb.index(b'end'), int)
        self.assertEqual(self.nb.index(self.child1), 0)
        self.assertEqual(self.nb.index(self.child2), 1)
        self.assertEqual(self.nb.index(b'end'), 2)
        return

    def test_insert(self):
        tabs = self.nb.tabs()
        self.nb.insert(1, tabs[0])
        self.assertEqual(self.nb.tabs(), (tabs[1], tabs[0]))
        self.nb.insert(self.child1, self.child2)
        self.assertEqual(self.nb.tabs(), tabs)
        self.nb.insert(b'end', self.child1)
        self.assertEqual(self.nb.tabs(), (tabs[1], tabs[0]))
        self.nb.insert(b'end', 0)
        self.assertEqual(self.nb.tabs(), tabs)
        self.assertRaises(tkinter.TclError, self.nb.insert, 2, tabs[0])
        self.assertRaises(tkinter.TclError, self.nb.insert, -1, tabs[0])
        child3 = ttk.Label(self.root)
        self.nb.insert(1, child3)
        self.assertEqual(self.nb.tabs(), (tabs[0], str(child3), tabs[1]))
        self.nb.forget(child3)
        self.assertEqual(self.nb.tabs(), tabs)
        self.nb.insert(self.child1, child3)
        self.assertEqual(self.nb.tabs(), (str(child3),) + tabs)
        self.nb.forget(child3)
        self.assertRaises(tkinter.TclError, self.nb.insert, 2, child3)
        self.assertRaises(tkinter.TclError, self.nb.insert, -1, child3)
        self.assertRaises(tkinter.TclError, self.nb.insert, b'end', None)
        self.assertRaises(tkinter.TclError, self.nb.insert, None, 0)
        self.assertRaises(tkinter.TclError, self.nb.insert, None, None)
        return

    def test_select(self):
        self.nb.pack()
        self.nb.wait_visibility()
        success = []
        tab_changed = []
        self.child1.bind(b'<Unmap>', (lambda evt: success.append(True)))
        self.nb.bind(b'<<NotebookTabChanged>>', (lambda evt: tab_changed.append(True)))
        self.assertEqual(self.nb.select(), str(self.child1))
        self.nb.select(self.child2)
        self.assertTrue(success)
        self.assertEqual(self.nb.select(), str(self.child2))
        self.nb.update()
        self.assertTrue(tab_changed)
        return

    def test_tab(self):
        self.assertRaises(tkinter.TclError, self.nb.tab, -1)
        self.assertRaises(tkinter.TclError, self.nb.tab, b'notab')
        self.assertRaises(tkinter.TclError, self.nb.tab, None)
        self.assertIsInstance(self.nb.tab(self.child1), dict)
        self.assertEqual(self.nb.tab(self.child1, text=None), b'a')
        self.assertEqual(self.nb.tab(self.child1, b'text'), b'a')
        self.nb.tab(self.child1, text=b'abc')
        self.assertEqual(self.nb.tab(self.child1, text=None), b'abc')
        self.assertEqual(self.nb.tab(self.child1, b'text'), b'abc')
        return

    def test_tabs(self):
        self.assertEqual(len(self.nb.tabs()), 2)
        self.nb.forget(self.child1)
        self.nb.forget(self.child2)
        self.assertEqual(self.nb.tabs(), ())
        return

    def test_traversal(self):
        self.nb.pack()
        self.nb.wait_visibility()
        self.nb.select(0)
        simulate_mouse_click(self.nb, 5, 5)
        self.nb.focus_force()
        self.nb.event_generate(b'<Control-Tab>')
        self.assertEqual(self.nb.select(), str(self.child2))
        self.nb.focus_force()
        self.nb.event_generate(b'<Shift-Control-Tab>')
        self.assertEqual(self.nb.select(), str(self.child1))
        self.nb.focus_force()
        self.nb.event_generate(b'<Shift-Control-Tab>')
        self.assertEqual(self.nb.select(), str(self.child2))
        self.nb.tab(self.child1, text=b'a', underline=0)
        self.nb.enable_traversal()
        self.nb.focus_force()
        simulate_mouse_click(self.nb, 5, 5)
        if sys.platform == b'darwin':
            self.nb.event_generate(b'<Option-a>')
        else:
            self.nb.event_generate(b'<Alt-a>')
        self.assertEqual(self.nb.select(), str(self.child1))
        return


@add_standard_options(StandardTtkOptionsTests)
class TreeviewTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'columns', b'cursor', b'displaycolumns', b'height', b'padding', b'selectmode', b'show', b'style', b'takefocus', b'xscrollcommand', b'yscrollcommand')

    def setUp(self):
        super(TreeviewTest, self).setUp()
        self.tv = self.create(padding=0)
        return

    def create(self, **kwargs):
        return ttk.Treeview(self.root, **kwargs)

    def test_columns(self):
        widget = self.create()
        self.checkParam(widget, b'columns', b'a b c', expected=(b'a', b'b', b'c'))
        self.checkParam(widget, b'columns', (b'a', b'b', b'c'))
        self.checkParam(widget, b'columns', () if tcl_version < (8, 5) else b'')
        return

    def test_displaycolumns(self):
        widget = self.create()
        widget[b'columns'] = (b'a', b'b', b'c')
        self.checkParam(widget, b'displaycolumns', b'b a c', expected=(b'b', b'a', b'c'))
        self.checkParam(widget, b'displaycolumns', (b'b', b'a', b'c'))
        self.checkParam(widget, b'displaycolumns', b'#all', expected=(b'#all',))
        self.checkParam(widget, b'displaycolumns', (2, 1, 0))
        self.checkInvalidParam(widget, b'displaycolumns', (b'a', b'b', b'd'), errmsg=b'Invalid column index d')
        self.checkInvalidParam(widget, b'displaycolumns', (1, 2, 3), errmsg=b'Column index 3 out of bounds')
        self.checkInvalidParam(widget, b'displaycolumns', (1, -2), errmsg=b'Column index -2 out of bounds')
        return

    def test_height(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'height', 100, -100, 0, b'3c', conv=False)
        self.checkPixelsParam(widget, b'height', 101.2, 102.6, conv=noconv)
        return

    def test_selectmode(self):
        widget = self.create()
        self.checkEnumParam(widget, b'selectmode', b'none', b'browse', b'extended')
        return

    def test_show(self):
        widget = self.create()
        self.checkParam(widget, b'show', b'tree headings', expected=(b'tree', b'headings'))
        self.checkParam(widget, b'show', (b'tree', b'headings'))
        self.checkParam(widget, b'show', (b'headings', b'tree'))
        self.checkParam(widget, b'show', b'tree', expected=(b'tree',))
        self.checkParam(widget, b'show', b'headings', expected=(b'headings',))
        return

    def test_bbox(self):
        self.tv.pack()
        self.assertEqual(self.tv.bbox(b''), b'')
        self.tv.wait_visibility()
        self.tv.update()
        item_id = self.tv.insert(b'', b'end')
        children = self.tv.get_children()
        self.assertTrue(children)
        bbox = self.tv.bbox(children[0])
        self.assertIsBoundingBox(bbox)
        self.tv[b'columns'] = [
         b'test']
        self.tv.column(b'test', width=50)
        bbox_column0 = self.tv.bbox(children[0], 0)
        root_width = self.tv.column(b'#0', width=None)
        if not self.wantobjects:
            root_width = int(root_width)
        self.assertEqual(bbox_column0[0], bbox[0] + root_width)
        child1 = self.tv.insert(item_id, b'end')
        self.assertEqual(self.tv.bbox(child1), b'')
        return

    def test_children(self):
        self.assertEqual(self.tv.get_children(), ())
        item_id = self.tv.insert(b'', b'end')
        self.assertIsInstance(self.tv.get_children(), tuple)
        self.assertEqual(self.tv.get_children()[0], item_id)
        child2 = self.tv.insert(b'', b'end')
        child3 = self.tv.insert(b'', b'end')
        self.tv.set_children(child2, item_id, child3)
        self.assertEqual(self.tv.get_children(child2), (item_id, child3))
        self.assertRaises(tkinter.TclError, self.tv.set_children, child3, child2)
        self.tv.set_children(child2)
        self.assertEqual(self.tv.get_children(child2), ())
        self.tv.set_children(b'')
        self.assertEqual(self.tv.get_children(), ())
        return

    def test_column(self):
        self.assertIsInstance(self.tv.column(b'#0'), dict)
        if self.wantobjects:
            self.assertIsInstance(self.tv.column(b'#0', width=None), int)
        self.tv.column(b'#0', width=10)
        self.assertEqual(self.tv.column(b'#0', b'width'), 10 if self.wantobjects else b'10')
        self.assertEqual(self.tv.column(b'#0', width=None), 10 if self.wantobjects else b'10')
        self.assertRaises(tkinter.TclError, self.tv.column, b'#0', id=b'X')
        self.assertRaises(tkinter.TclError, self.tv.column, b'invalid')
        invalid_kws = [{b'unknown_option': b'some value'}, {b'stretch': b'wrong'}, {b'anchor': b'wrong'}, {b'width': b'wrong'}, {b'minwidth': b'wrong'}]
        for kw in invalid_kws:
            self.assertRaises(tkinter.TclError, self.tv.column, b'#0', **kw)

        return

    def test_delete(self):
        self.assertRaises(tkinter.TclError, self.tv.delete, b'#0')
        item_id = self.tv.insert(b'', b'end')
        item2 = self.tv.insert(item_id, b'end')
        self.assertEqual(self.tv.get_children(), (item_id,))
        self.assertEqual(self.tv.get_children(item_id), (item2,))
        self.tv.delete(item_id)
        self.assertFalse(self.tv.get_children())
        self.assertRaises(tkinter.TclError, self.tv.reattach, item_id, b'', b'end')
        item1 = self.tv.insert(b'', b'end')
        item2 = self.tv.insert(b'', b'end')
        self.assertEqual(self.tv.get_children(), (item1, item2))
        self.tv.delete(item1, item2)
        self.assertFalse(self.tv.get_children())
        return

    def test_detach_reattach(self):
        item_id = self.tv.insert(b'', b'end')
        item2 = self.tv.insert(item_id, b'end')
        prev = self.tv.get_children()
        self.tv.detach()
        self.assertEqual(prev, self.tv.get_children())
        self.assertEqual(self.tv.get_children(), (item_id,))
        self.assertEqual(self.tv.get_children(item_id), (item2,))
        self.tv.detach(item_id)
        self.assertFalse(self.tv.get_children())
        self.tv.reattach(item_id, b'', b'end')
        self.assertEqual(self.tv.get_children(), (item_id,))
        self.assertEqual(self.tv.get_children(item_id), (item2,))
        self.tv.move(item2, b'', b'end')
        self.assertEqual(self.tv.get_children(), (item_id, item2))
        self.assertEqual(self.tv.get_children(item_id), ())
        self.assertRaises(tkinter.TclError, self.tv.reattach, b'nonexistent', b'', b'end')
        self.assertRaises(tkinter.TclError, self.tv.detach, b'nonexistent')
        self.assertRaises(tkinter.TclError, self.tv.reattach, item2, b'otherparent', b'end')
        self.assertRaises(tkinter.TclError, self.tv.reattach, item2, b'', b'invalid')
        self.tv.detach(item_id, item2)
        self.assertEqual(self.tv.get_children(), ())
        self.assertEqual(self.tv.get_children(item_id), ())
        return

    def test_exists(self):
        self.assertEqual(self.tv.exists(b'something'), False)
        self.assertEqual(self.tv.exists(b''), True)
        self.assertEqual(self.tv.exists({}), False)
        self.assertRaises(tkinter.TclError, self.tv.exists, None)
        return

    def test_focus(self):
        self.assertEqual(self.tv.focus(), b'')
        item1 = self.tv.insert(b'', b'end')
        self.tv.focus(item1)
        self.assertEqual(self.tv.focus(), item1)
        self.tv.delete(item1)
        self.assertEqual(self.tv.focus(), b'')
        self.assertRaises(tkinter.TclError, self.tv.focus, b'hi')
        return

    def test_heading(self):
        self.assertIsInstance(self.tv.heading(b'#0'), dict)
        self.tv.heading(b'#0', text=b'hi')
        self.assertEqual(self.tv.heading(b'#0', b'text'), b'hi')
        self.assertEqual(self.tv.heading(b'#0', text=None), b'hi')
        self.assertRaises(tkinter.TclError, self.tv.heading, b'#0', background=None)
        self.assertRaises(tkinter.TclError, self.tv.heading, b'#0', anchor=1)
        return

    def test_heading_callback(self):

        def simulate_heading_click(x, y):
            simulate_mouse_click(self.tv, x, y)
            self.tv.update()
            return

        success = []
        self.tv.pack()
        self.tv.wait_visibility()
        self.tv.heading(b'#0', command=(lambda : success.append(True)))
        self.tv.column(b'#0', width=100)
        self.tv.update()
        simulate_heading_click(5, 5)
        if not success:
            self.fail(b"The command associated to the treeview heading wasn't invoked.")
        success = []
        commands = self.tv.master._tclCommands
        self.tv.heading(b'#0', command=str(self.tv.heading(b'#0', command=None)))
        self.assertEqual(commands, self.tv.master._tclCommands)
        simulate_heading_click(5, 5)
        if not success:
            self.fail(b"The command associated to the treeview heading wasn't invoked.")
        return

    def test_index(self):
        self.assertRaises(tkinter.TclError, self.tv.index, b'what')
        self.assertEqual(self.tv.index(b''), 0)
        item1 = self.tv.insert(b'', b'end')
        item2 = self.tv.insert(b'', b'end')
        c1 = self.tv.insert(item1, b'end')
        c2 = self.tv.insert(item1, b'end')
        self.assertEqual(self.tv.index(item1), 0)
        self.assertEqual(self.tv.index(c1), 0)
        self.assertEqual(self.tv.index(c2), 1)
        self.assertEqual(self.tv.index(item2), 1)
        self.tv.move(item2, b'', 0)
        self.assertEqual(self.tv.index(item2), 0)
        self.assertEqual(self.tv.index(item1), 1)
        self.tv.detach(item1)
        self.assertEqual(self.tv.index(c2), 1)
        self.tv.detach(c1)
        self.assertEqual(self.tv.index(c2), 0)
        self.tv.delete(item1)
        self.assertRaises(tkinter.TclError, self.tv.index, c2)
        return

    def test_insert_item(self):
        self.assertRaises(tkinter.TclError, self.tv.insert, b'none', b'end')
        self.assertRaises(tkinter.TclError, self.tv.insert, b'', b'end', open=b'')
        self.assertRaises(tkinter.TclError, self.tv.insert, b'', b'end', open=b'please')
        self.assertFalse(self.tv.delete(self.tv.insert(b'', b'end', open=True)))
        self.assertFalse(self.tv.delete(self.tv.insert(b'', b'end', open=False)))
        self.assertRaises(tkinter.TclError, self.tv.insert, b'', b'middle')
        itemid = self.tv.insert(b'', b'end', b'first-item')
        self.assertEqual(itemid, b'first-item')
        self.assertRaises(tkinter.TclError, self.tv.insert, b'', b'end', b'first-item')
        self.assertRaises(tkinter.TclError, self.tv.insert, b'', b'end', MockTclObj(b'first-item'))
        value = u'\xe1ba'
        item = self.tv.insert(b'', b'end', values=(value,))
        self.assertEqual(self.tv.item(item, b'values'), (value,) if self.wantobjects else value)
        self.assertEqual(self.tv.item(item, values=None), (value,) if self.wantobjects else value)
        self.tv.item(item, values=self.root.splitlist(self.tv.item(item, values=None)))
        self.assertEqual(self.tv.item(item, values=None), (value,) if self.wantobjects else value)
        self.assertIsInstance(self.tv.item(item), dict)
        self.tv.item(item, values=b'')
        self.assertFalse(self.tv.item(item, values=None))
        item = self.tv.insert(b'', b'end', tags=[1, 2, value])
        self.assertEqual(self.tv.item(item, tags=None), (b'1', b'2', value) if self.wantobjects else b'1 2 %s' % value)
        self.tv.item(item, tags=[])
        self.assertFalse(self.tv.item(item, tags=None))
        self.tv.item(item, tags=(1, 2))
        self.assertEqual(self.tv.item(item, tags=None), (b'1', b'2') if self.wantobjects else b'1 2')
        item = self.tv.insert(b'', b'end', values=(b'a b c',
         b'%s %s' % (value, value)))
        self.assertEqual(self.tv.item(item, values=None), (b'a b c', b'%s %s' % (value, value)) if self.wantobjects else b'{a b c} {%s %s}' % (value, value))
        self.assertEqual(self.tv.item(self.tv.insert(b'', b'end', text=b'Label here'), text=None), b'Label here')
        self.assertEqual(self.tv.item(self.tv.insert(b'', b'end', text=value), text=None), value)
        itemid = self.tv.insert(b'', b'end', 0)
        self.assertEqual(itemid, b'0')
        itemid = self.tv.insert(b'', b'end', 0.0)
        self.assertEqual(itemid, b'0.0')
        self.assertRaises(tkinter.TclError, self.tv.insert, b'', b'end', False)
        self.assertRaises(tkinter.TclError, self.tv.insert, b'', b'end', b'')
        return

    def test_selection(self):
        self.assertRaises(tkinter.TclError, self.tv.selection_set, b'none')
        self.assertRaises(tkinter.TclError, self.tv.selection_add, b'none')
        self.assertRaises(tkinter.TclError, self.tv.selection_remove, b'none')
        self.assertRaises(tkinter.TclError, self.tv.selection_toggle, b'none')
        item1 = self.tv.insert(b'', b'end')
        item2 = self.tv.insert(b'', b'end')
        c1 = self.tv.insert(item1, b'end')
        c2 = self.tv.insert(item1, b'end')
        c3 = self.tv.insert(item1, b'end')
        self.assertEqual(self.tv.selection(), ())
        self.tv.selection_set((c1, item2))
        self.assertEqual(self.tv.selection(), (c1, item2))
        self.tv.selection_set(c2)
        self.assertEqual(self.tv.selection(), (c2,))
        self.tv.selection_add((c1, item2))
        self.assertEqual(self.tv.selection(), (c1, c2, item2))
        self.tv.selection_add(item1)
        self.assertEqual(self.tv.selection(), (item1, c1, c2, item2))
        self.tv.selection_remove((item1, c3))
        self.assertEqual(self.tv.selection(), (c1, c2, item2))
        self.tv.selection_remove(c2)
        self.assertEqual(self.tv.selection(), (c1, item2))
        self.tv.selection_toggle((c1, c3))
        self.assertEqual(self.tv.selection(), (c3, item2))
        self.tv.selection_toggle(item2)
        self.assertEqual(self.tv.selection(), (c3,))
        self.tv.insert(b'', b'end', id=b'with spaces')
        self.tv.selection_set(b'with spaces')
        self.assertEqual(self.tv.selection(), (b'with spaces',))
        self.tv.insert(b'', b'end', id=b'{brace')
        self.tv.selection_set(b'{brace')
        self.assertEqual(self.tv.selection(), (b'{brace',))
        if have_unicode:
            self.tv.insert(b'', b'end', id=u(b'unicode\\u20ac'))
            self.tv.selection_set(u(b'unicode\\u20ac'))
            self.assertEqual(self.tv.selection(), (u(b'unicode\\u20ac'),))
        self.tv.insert(b'', b'end', id=b'bytes\xe2\x82\xac')
        self.tv.selection_set(b'bytes\xe2\x82\xac')
        self.assertEqual(self.tv.selection(), (
         u(b'bytes\\u20ac') if have_unicode else b'bytes\xe2\x82\xac',))
        return

    def test_set(self):
        self.tv[b'columns'] = [
         b'A', b'B']
        item = self.tv.insert(b'', b'end', values=[b'a', b'b'])
        self.assertEqual(self.tv.set(item), {b'A': b'a', b'B': b'b'})
        self.tv.set(item, b'B', b'a')
        self.assertEqual(self.tv.item(item, values=None), (b'a', b'a') if self.wantobjects else b'a a')
        self.tv[b'columns'] = [
         b'B']
        self.assertEqual(self.tv.set(item), {b'B': b'a'})
        self.tv.set(item, b'B', b'b')
        self.assertEqual(self.tv.set(item, column=b'B'), b'b')
        self.assertEqual(self.tv.item(item, values=None), (b'b', b'a') if self.wantobjects else b'b a')
        self.tv.set(item, b'B', 123)
        self.assertEqual(self.tv.set(item, b'B'), 123 if self.wantobjects else b'123')
        self.assertEqual(self.tv.item(item, values=None), (123, b'a') if self.wantobjects else b'123 a')
        self.assertEqual(self.tv.set(item), {b'B': 123} if self.wantobjects else {b'B': b'123'})
        self.assertRaises(tkinter.TclError, self.tv.set, item, b'A')
        self.assertRaises(tkinter.TclError, self.tv.set, item, b'A', b'b')
        self.assertRaises(tkinter.TclError, self.tv.set, b'notme')
        return

    def test_tag_bind(self):
        events = []
        item1 = self.tv.insert(b'', b'end', tags=[b'call'])
        item2 = self.tv.insert(b'', b'end', tags=[b'call'])
        self.tv.tag_bind(b'call', b'<ButtonPress-1>', (lambda evt: events.append(1)))
        self.tv.tag_bind(b'call', b'<ButtonRelease-1>', (lambda evt: events.append(2)))
        self.tv.pack()
        self.tv.wait_visibility()
        self.tv.update()
        pos_y = set()
        found = set()
        for i in range(0, 100, 10):
            if len(found) == 2:
                break
            item_id = self.tv.identify_row(i)
            if item_id and item_id not in found:
                pos_y.add(i)
                found.add(item_id)

        self.assertEqual(len(pos_y), 2)
        for y in pos_y:
            simulate_mouse_click(self.tv, 0, y)

        self.assertEqual(len(events), 4)
        for evt in zip(events[::2], events[1::2]):
            self.assertEqual(evt, (1, 2))

        return

    def test_tag_configure(self):
        self.assertRaises(TypeError, self.tv.tag_configure)
        self.assertRaises(tkinter.TclError, self.tv.tag_configure, b'test', sky=b'blue')
        self.tv.tag_configure(b'test', foreground=b'blue')
        self.assertEqual(str(self.tv.tag_configure(b'test', b'foreground')), b'blue')
        self.assertEqual(str(self.tv.tag_configure(b'test', foreground=None)), b'blue')
        self.assertIsInstance(self.tv.tag_configure(b'test'), dict)
        return

    def test_tag_has(self):
        item1 = self.tv.insert(b'', b'end', text=b'Item 1', tags=[b'tag1'])
        item2 = self.tv.insert(b'', b'end', text=b'Item 2', tags=[b'tag2'])
        self.assertRaises(TypeError, self.tv.tag_has)
        self.assertRaises(TclError, self.tv.tag_has, b'tag1', b'non-existing')
        self.assertTrue(self.tv.tag_has(b'tag1', item1))
        self.assertFalse(self.tv.tag_has(b'tag1', item2))
        self.assertFalse(self.tv.tag_has(b'tag2', item1))
        self.assertTrue(self.tv.tag_has(b'tag2', item2))
        self.assertFalse(self.tv.tag_has(b'tag3', item1))
        self.assertFalse(self.tv.tag_has(b'tag3', item2))
        self.assertEqual(self.tv.tag_has(b'tag1'), (item1,))
        self.assertEqual(self.tv.tag_has(b'tag2'), (item2,))
        self.assertEqual(self.tv.tag_has(b'tag3'), ())
        return


@add_standard_options(StandardTtkOptionsTests)
class SeparatorTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'cursor', b'orient', b'style', b'takefocus')
    default_orient = b'horizontal'

    def create(self, **kwargs):
        return ttk.Separator(self.root, **kwargs)


@add_standard_options(StandardTtkOptionsTests)
class SizegripTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'class', b'cursor', b'style', b'takefocus')

    def create(self, **kwargs):
        return ttk.Sizegrip(self.root, **kwargs)


tests_gui = (
 ButtonTest, CheckbuttonTest, ComboboxTest, EntryTest,
 FrameTest, LabelFrameTest, LabelTest, MenubuttonTest,
 NotebookTest, PanedWindowTest, ProgressbarTest,
 RadiobuttonTest, ScaleTest, ScrollbarTest, SeparatorTest,
 SizegripTest, TreeviewTest, WidgetTest)
if __name__ == b'__main__':
    run_unittest(*tests_gui)
