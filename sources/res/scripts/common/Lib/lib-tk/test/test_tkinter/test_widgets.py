import unittest, Tkinter as tkinter
from Tkinter import TclError
import os, sys
from test.test_support import requires, run_unittest
from test_ttk.support import tcl_version, requires_tcl, get_tk_patchlevel, widget_eq
from widget_tests import add_standard_options, noconv, noconv_meth, int_round, pixels_round, AbstractWidgetTest, StandardOptionsTests, IntegerSizeTests, PixelSizeTests, setUpModule
requires(b'gui')

class AbstractToplevelTest(AbstractWidgetTest, PixelSizeTests):
    _conv_pad_pixels = noconv_meth

    def test_class(self):
        widget = self.create()
        self.assertEqual(widget[b'class'], widget.__class__.__name__.title())
        self.checkInvalidParam(widget, b'class', b'Foo', errmsg=b"can't modify -class option after widget is created")
        widget2 = self.create(class_=b'Foo')
        self.assertEqual(widget2[b'class'], b'Foo')
        return

    def test_colormap(self):
        widget = self.create()
        self.assertEqual(widget[b'colormap'], b'')
        self.checkInvalidParam(widget, b'colormap', b'new', errmsg=b"can't modify -colormap option after widget is created")
        widget2 = self.create(colormap=b'new')
        self.assertEqual(widget2[b'colormap'], b'new')
        return

    def test_container(self):
        widget = self.create()
        self.assertEqual(widget[b'container'], 0 if self.wantobjects else b'0')
        self.checkInvalidParam(widget, b'container', 1, errmsg=b"can't modify -container option after widget is created")
        widget2 = self.create(container=True)
        self.assertEqual(widget2[b'container'], 1 if self.wantobjects else b'1')
        return

    def test_visual(self):
        widget = self.create()
        self.assertEqual(widget[b'visual'], b'')
        self.checkInvalidParam(widget, b'visual', b'default', errmsg=b"can't modify -visual option after widget is created")
        widget2 = self.create(visual=b'default')
        self.assertEqual(widget2[b'visual'], b'default')
        return


@add_standard_options(StandardOptionsTests)
class ToplevelTest(AbstractToplevelTest, unittest.TestCase):
    OPTIONS = (b'background', b'borderwidth', b'class', b'colormap', b'container', b'cursor', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'menu', b'padx', b'pady', b'relief', b'screen', b'takefocus', b'use', b'visual', b'width')

    def create(self, **kwargs):
        return tkinter.Toplevel(self.root, **kwargs)

    def test_menu(self):
        widget = self.create()
        menu = tkinter.Menu(self.root)
        self.checkParam(widget, b'menu', menu, eq=widget_eq)
        self.checkParam(widget, b'menu', b'')
        return

    def test_screen(self):
        widget = self.create()
        self.assertEqual(widget[b'screen'], b'')
        try:
            display = os.environ[b'DISPLAY']
        except KeyError:
            self.skipTest(b'No $DISPLAY set.')

        self.checkInvalidParam(widget, b'screen', display, errmsg=b"can't modify -screen option after widget is created")
        widget2 = self.create(screen=display)
        self.assertEqual(widget2[b'screen'], display)
        return

    def test_use(self):
        widget = self.create()
        self.assertEqual(widget[b'use'], b'')
        parent = self.create(container=True)
        wid = b'%#x' % parent.winfo_id()
        widget2 = self.create(use=wid)
        self.assertEqual(widget2[b'use'], wid)
        return


@add_standard_options(StandardOptionsTests)
class FrameTest(AbstractToplevelTest, unittest.TestCase):
    OPTIONS = (b'background', b'borderwidth', b'class', b'colormap', b'container', b'cursor', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'padx', b'pady', b'relief', b'takefocus', b'visual', b'width')

    def create(self, **kwargs):
        return tkinter.Frame(self.root, **kwargs)


@add_standard_options(StandardOptionsTests)
class LabelFrameTest(AbstractToplevelTest, unittest.TestCase):
    OPTIONS = (b'background', b'borderwidth', b'class', b'colormap', b'container', b'cursor', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'labelanchor', b'labelwidget', b'padx', b'pady', b'relief', b'takefocus', b'text', b'visual', b'width')

    def create(self, **kwargs):
        return tkinter.LabelFrame(self.root, **kwargs)

    def test_labelanchor(self):
        widget = self.create()
        self.checkEnumParam(widget, b'labelanchor', b'e', b'en', b'es', b'n', b'ne', b'nw', b's', b'se', b'sw', b'w', b'wn', b'ws')
        self.checkInvalidParam(widget, b'labelanchor', b'center')
        return

    def test_labelwidget(self):
        widget = self.create()
        label = tkinter.Label(self.root, text=b'Mupp', name=b'foo')
        self.checkParam(widget, b'labelwidget', label, expected=b'.foo')
        label.destroy()
        return


class AbstractLabelTest(AbstractWidgetTest, IntegerSizeTests):
    _conv_pixels = noconv_meth

    def test_highlightthickness(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'highlightthickness', 0, 1.3, 2.6, 6, -2, b'10p')
        return


@add_standard_options(StandardOptionsTests)
class LabelTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'activeforeground', b'anchor', b'background', b'bitmap', b'borderwidth', b'compound', b'cursor', b'disabledforeground', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'image', b'justify', b'padx', b'pady', b'relief', b'state', b'takefocus', b'text', b'textvariable', b'underline', b'width', b'wraplength')

    def create(self, **kwargs):
        return tkinter.Label(self.root, **kwargs)


@add_standard_options(StandardOptionsTests)
class ButtonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'activeforeground', b'anchor', b'background', b'bitmap', b'borderwidth', b'command', b'compound', b'cursor', b'default', b'disabledforeground', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'image', b'justify', b'overrelief', b'padx', b'pady', b'relief', b'repeatdelay', b'repeatinterval', b'state', b'takefocus', b'text', b'textvariable', b'underline', b'width', b'wraplength')

    def create(self, **kwargs):
        return tkinter.Button(self.root, **kwargs)

    def test_default(self):
        widget = self.create()
        self.checkEnumParam(widget, b'default', b'active', b'disabled', b'normal')
        return


@add_standard_options(StandardOptionsTests)
class CheckbuttonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'activeforeground', b'anchor', b'background', b'bitmap', b'borderwidth', b'command', b'compound', b'cursor', b'disabledforeground', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'image', b'indicatoron', b'justify', b'offrelief', b'offvalue', b'onvalue', b'overrelief', b'padx', b'pady', b'relief', b'selectcolor', b'selectimage', b'state', b'takefocus', b'text', b'textvariable', b'tristateimage', b'tristatevalue', b'underline', b'variable', b'width', b'wraplength')

    def create(self, **kwargs):
        return tkinter.Checkbutton(self.root, **kwargs)

    def test_offvalue(self):
        widget = self.create()
        self.checkParams(widget, b'offvalue', 1, 2.3, b'', b'any string')
        return

    def test_onvalue(self):
        widget = self.create()
        self.checkParams(widget, b'onvalue', 1, 2.3, b'', b'any string')
        return


@add_standard_options(StandardOptionsTests)
class RadiobuttonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'activeforeground', b'anchor', b'background', b'bitmap', b'borderwidth', b'command', b'compound', b'cursor', b'disabledforeground', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'image', b'indicatoron', b'justify', b'offrelief', b'overrelief', b'padx', b'pady', b'relief', b'selectcolor', b'selectimage', b'state', b'takefocus', b'text', b'textvariable', b'tristateimage', b'tristatevalue', b'underline', b'value', b'variable', b'width', b'wraplength')

    def create(self, **kwargs):
        return tkinter.Radiobutton(self.root, **kwargs)

    def test_value(self):
        widget = self.create()
        self.checkParams(widget, b'value', 1, 2.3, b'', b'any string')
        return


@add_standard_options(StandardOptionsTests)
class MenubuttonTest(AbstractLabelTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'activeforeground', b'anchor', b'background', b'bitmap', b'borderwidth', b'compound', b'cursor', b'direction', b'disabledforeground', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'image', b'indicatoron', b'justify', b'menu', b'padx', b'pady', b'relief', b'state', b'takefocus', b'text', b'textvariable', b'underline', b'width', b'wraplength')
    _conv_pixels = staticmethod(pixels_round)

    def create(self, **kwargs):
        return tkinter.Menubutton(self.root, **kwargs)

    def test_direction(self):
        widget = self.create()
        self.checkEnumParam(widget, b'direction', b'above', b'below', b'flush', b'left', b'right')
        return

    def test_height(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'height', 100, -100, 0, conv=str)
        return

    test_highlightthickness = StandardOptionsTests.test_highlightthickness.im_func

    @unittest.skipIf(sys.platform == b'darwin', b'crashes with Cocoa Tk (issue19733)')
    def test_image(self):
        widget = self.create()
        image = tkinter.PhotoImage(master=self.root, name=b'image1')
        self.checkParam(widget, b'image', image, conv=str)
        errmsg = b'image "spam" doesn\'t exist'
        with self.assertRaises(tkinter.TclError) as cm:
            widget[b'image'] = b'spam'
        if errmsg is not None:
            self.assertEqual(str(cm.exception), errmsg)
        with self.assertRaises(tkinter.TclError) as cm:
            widget.configure({b'image': b'spam'})
        if errmsg is not None:
            self.assertEqual(str(cm.exception), errmsg)
        return

    def test_menu(self):
        widget = self.create()
        menu = tkinter.Menu(widget, name=b'menu')
        self.checkParam(widget, b'menu', menu, eq=widget_eq)
        menu.destroy()
        return

    def test_padx(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'padx', 3, 4.4, 5.6, b'12m')
        self.checkParam(widget, b'padx', -2, expected=0)
        return

    def test_pady(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'pady', 3, 4.4, 5.6, b'12m')
        self.checkParam(widget, b'pady', -2, expected=0)
        return

    def test_width(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'width', 402, -402, 0, conv=str)
        return


class OptionMenuTest(MenubuttonTest, unittest.TestCase):

    def create(self, default=b'b', values=(b'a', b'b', b'c'), **kwargs):
        return tkinter.OptionMenu(self.root, None, default, *values, **kwargs)


@add_standard_options(IntegerSizeTests, StandardOptionsTests)
class EntryTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'background', b'borderwidth', b'cursor', b'disabledbackground', b'disabledforeground', b'exportselection', b'font', b'foreground', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'insertbackground', b'insertborderwidth', b'insertofftime', b'insertontime', b'insertwidth', b'invalidcommand', b'justify', b'readonlybackground', b'relief', b'selectbackground', b'selectborderwidth', b'selectforeground', b'show', b'state', b'takefocus', b'textvariable', b'validate', b'validatecommand', b'width', b'xscrollcommand')

    def create(self, **kwargs):
        return tkinter.Entry(self.root, **kwargs)

    def test_disabledbackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'disabledbackground')
        return

    def test_insertborderwidth(self):
        widget = self.create(insertwidth=100)
        self.checkPixelsParam(widget, b'insertborderwidth', 0, 1.3, 2.6, 6, -2, b'10p')
        self.checkParam(widget, b'insertborderwidth', 60, expected=50)
        return

    def test_insertwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'insertwidth', 1.3, 3.6, b'10p')
        self.checkParam(widget, b'insertwidth', 0.1, expected=2)
        self.checkParam(widget, b'insertwidth', -2, expected=2)
        if pixels_round(0.9) <= 0:
            self.checkParam(widget, b'insertwidth', 0.9, expected=2)
        else:
            self.checkParam(widget, b'insertwidth', 0.9, expected=1)
        return

    def test_invalidcommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'invalidcommand')
        self.checkCommandParam(widget, b'invcmd')
        return

    def test_readonlybackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'readonlybackground')
        return

    def test_show(self):
        widget = self.create()
        self.checkParam(widget, b'show', b'*')
        self.checkParam(widget, b'show', b'')
        self.checkParam(widget, b'show', b' ')
        return

    def test_state(self):
        widget = self.create()
        self.checkEnumParam(widget, b'state', b'disabled', b'normal', b'readonly')
        return

    def test_validate(self):
        widget = self.create()
        self.checkEnumParam(widget, b'validate', b'all', b'key', b'focus', b'focusin', b'focusout', b'none')
        return

    def test_validatecommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'validatecommand')
        self.checkCommandParam(widget, b'vcmd')
        return


@add_standard_options(StandardOptionsTests)
class SpinboxTest(EntryTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'background', b'borderwidth', b'buttonbackground', b'buttoncursor', b'buttondownrelief', b'buttonuprelief', b'command', b'cursor', b'disabledbackground', b'disabledforeground', b'exportselection', b'font', b'foreground', b'format', b'from', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'increment', b'insertbackground', b'insertborderwidth', b'insertofftime', b'insertontime', b'insertwidth', b'invalidcommand', b'justify', b'relief', b'readonlybackground', b'repeatdelay', b'repeatinterval', b'selectbackground', b'selectborderwidth', b'selectforeground', b'state', b'takefocus', b'textvariable', b'to', b'validate', b'validatecommand', b'values', b'width', b'wrap', b'xscrollcommand')

    def create(self, **kwargs):
        return tkinter.Spinbox(self.root, **kwargs)

    test_show = None

    def test_buttonbackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'buttonbackground')
        return

    def test_buttoncursor(self):
        widget = self.create()
        self.checkCursorParam(widget, b'buttoncursor')
        return

    def test_buttondownrelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'buttondownrelief')
        return

    def test_buttonuprelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'buttonuprelief')
        return

    def test_format(self):
        widget = self.create()
        self.checkParam(widget, b'format', b'%2f')
        self.checkParam(widget, b'format', b'%2.2f')
        self.checkParam(widget, b'format', b'%.2f')
        self.checkParam(widget, b'format', b'%2.f')
        self.checkInvalidParam(widget, b'format', b'%2e-1f')
        self.checkInvalidParam(widget, b'format', b'2.2')
        self.checkInvalidParam(widget, b'format', b'%2.-2f')
        self.checkParam(widget, b'format', b'%-2.02f')
        self.checkParam(widget, b'format', b'% 2.02f')
        self.checkParam(widget, b'format', b'% -2.200f')
        self.checkParam(widget, b'format', b'%09.200f')
        self.checkInvalidParam(widget, b'format', b'%d')
        return

    def test_from(self):
        widget = self.create()
        self.checkParam(widget, b'to', 100.0)
        self.checkFloatParam(widget, b'from', -10, 10.2, 11.7)
        self.checkInvalidParam(widget, b'from', 200, errmsg=b'-to value must be greater than -from value')
        return

    def test_increment(self):
        widget = self.create()
        self.checkFloatParam(widget, b'increment', -1, 1, 10.2, 12.8, 0)
        return

    def test_to(self):
        widget = self.create()
        self.checkParam(widget, b'from', -100.0)
        self.checkFloatParam(widget, b'to', -10, 10.2, 11.7)
        self.checkInvalidParam(widget, b'to', -200, errmsg=b'-to value must be greater than -from value')
        return

    def test_values(self):
        widget = self.create()
        self.assertEqual(widget[b'values'], b'')
        self.checkParam(widget, b'values', b'mon tue wed thur')
        self.checkParam(widget, b'values', (b'mon', b'tue', b'wed', b'thur'), expected=b'mon tue wed thur')
        self.checkParam(widget, b'values', (42, 3.14, b'', b'any string'), expected=b'42 3.14 {} {any string}')
        self.checkParam(widget, b'values', b'')
        return

    def test_wrap(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'wrap')
        return

    def test_bbox(self):
        widget = self.create()
        self.assertIsBoundingBox(widget.bbox(0))
        self.assertRaises(tkinter.TclError, widget.bbox, b'noindex')
        self.assertRaises(tkinter.TclError, widget.bbox, None)
        self.assertRaises(TypeError, widget.bbox)
        self.assertRaises(TypeError, widget.bbox, 0, 1)
        return

    def test_selection_element(self):
        widget = self.create()
        self.assertEqual(widget.selection_element(), b'none')
        widget.selection_element(b'buttonup')
        self.assertEqual(widget.selection_element(), b'buttonup')
        widget.selection_element(b'buttondown')
        self.assertEqual(widget.selection_element(), b'buttondown')
        return


@add_standard_options(StandardOptionsTests)
class TextTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'autoseparators', b'background', b'blockcursor', b'borderwidth', b'cursor', b'endline', b'exportselection', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'inactiveselectbackground', b'insertbackground', b'insertborderwidth', b'insertofftime', b'insertontime', b'insertunfocussed', b'insertwidth', b'maxundo', b'padx', b'pady', b'relief', b'selectbackground', b'selectborderwidth', b'selectforeground', b'setgrid', b'spacing1', b'spacing2', b'spacing3', b'startline', b'state', b'tabs', b'tabstyle', b'takefocus', b'undo', b'width', b'wrap', b'xscrollcommand', b'yscrollcommand')
    if tcl_version < (8, 5):
        _stringify = True

    def create(self, **kwargs):
        return tkinter.Text(self.root, **kwargs)

    def test_autoseparators(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'autoseparators')
        return

    @requires_tcl(8, 5)
    def test_blockcursor(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'blockcursor')
        return

    @requires_tcl(8, 5)
    def test_endline(self):
        widget = self.create()
        text = (b'\n').join(b'Line %d' for i in range(100))
        widget.insert(b'end', text)
        self.checkParam(widget, b'endline', 200, expected=b'')
        self.checkParam(widget, b'endline', -10, expected=b'')
        self.checkInvalidParam(widget, b'endline', b'spam', errmsg=b'expected integer but got "spam"')
        self.checkParam(widget, b'endline', 50)
        self.checkParam(widget, b'startline', 15)
        self.checkInvalidParam(widget, b'endline', 10, errmsg=b'-startline must be less than or equal to -endline')
        return

    def test_height(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'height', 100, 101.2, 102.6, b'3c')
        self.checkParam(widget, b'height', -100, expected=1)
        self.checkParam(widget, b'height', 0, expected=1)
        return

    def test_maxundo(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'maxundo', 0, 5, -1)
        return

    @requires_tcl(8, 5)
    def test_inactiveselectbackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'inactiveselectbackground')
        return

    @requires_tcl(8, 6)
    def test_insertunfocussed(self):
        widget = self.create()
        self.checkEnumParam(widget, b'insertunfocussed', b'hollow', b'none', b'solid')
        return

    def test_selectborderwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'selectborderwidth', 1.3, 2.6, -2, b'10p', conv=noconv, keep_orig=tcl_version >= (8, 5))
        return

    def test_spacing1(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'spacing1', 20, 21.4, 22.6, b'0.5c')
        self.checkParam(widget, b'spacing1', -5, expected=0)
        return

    def test_spacing2(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'spacing2', 5, 6.4, 7.6, b'0.1c')
        self.checkParam(widget, b'spacing2', -1, expected=0)
        return

    def test_spacing3(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'spacing3', 20, 21.4, 22.6, b'0.5c')
        self.checkParam(widget, b'spacing3', -10, expected=0)
        return

    @requires_tcl(8, 5)
    def test_startline(self):
        widget = self.create()
        text = (b'\n').join(b'Line %d' for i in range(100))
        widget.insert(b'end', text)
        self.checkParam(widget, b'startline', 200, expected=b'')
        self.checkParam(widget, b'startline', -10, expected=b'')
        self.checkInvalidParam(widget, b'startline', b'spam', errmsg=b'expected integer but got "spam"')
        self.checkParam(widget, b'startline', 10)
        self.checkParam(widget, b'endline', 50)
        self.checkInvalidParam(widget, b'startline', 70, errmsg=b'-startline must be less than or equal to -endline')
        return

    def test_state(self):
        widget = self.create()
        if tcl_version < (8, 5):
            self.checkParams(widget, b'state', b'disabled', b'normal')
        else:
            self.checkEnumParam(widget, b'state', b'disabled', b'normal')
        return

    def test_tabs(self):
        widget = self.create()
        if get_tk_patchlevel() < (8, 5, 11):
            self.checkParam(widget, b'tabs', (10.2, 20.7, b'1i', b'2i'), expected=(b'10.2', b'20.7', b'1i', b'2i'))
        else:
            self.checkParam(widget, b'tabs', (10.2, 20.7, b'1i', b'2i'))
        self.checkParam(widget, b'tabs', b'10.2 20.7 1i 2i', expected=(b'10.2', b'20.7', b'1i', b'2i'))
        self.checkParam(widget, b'tabs', b'2c left 4c 6c center', expected=(b'2c', b'left', b'4c', b'6c', b'center'))
        self.checkInvalidParam(widget, b'tabs', b'spam', errmsg=b'bad screen distance "spam"', keep_orig=tcl_version >= (8, 5))
        return

    @requires_tcl(8, 5)
    def test_tabstyle(self):
        widget = self.create()
        self.checkEnumParam(widget, b'tabstyle', b'tabular', b'wordprocessor')
        return

    def test_undo(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'undo')
        return

    def test_width(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'width', 402)
        self.checkParam(widget, b'width', -402, expected=1)
        self.checkParam(widget, b'width', 0, expected=1)
        return

    def test_wrap(self):
        widget = self.create()
        if tcl_version < (8, 5):
            self.checkParams(widget, b'wrap', b'char', b'none', b'word')
        else:
            self.checkEnumParam(widget, b'wrap', b'char', b'none', b'word')
        return

    def test_bbox(self):
        widget = self.create()
        self.assertIsBoundingBox(widget.bbox(b'1.1'))
        self.assertIsNone(widget.bbox(b'end'))
        self.assertRaises(tkinter.TclError, widget.bbox, b'noindex')
        self.assertRaises(tkinter.TclError, widget.bbox, None)
        self.assertRaises(tkinter.TclError, widget.bbox)
        self.assertRaises(tkinter.TclError, widget.bbox, b'1.1', b'end')
        return


@add_standard_options(PixelSizeTests, StandardOptionsTests)
class CanvasTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'background', b'borderwidth', b'closeenough', b'confine', b'cursor', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'insertbackground', b'insertborderwidth', b'insertofftime', b'insertontime', b'insertwidth', b'offset', b'relief', b'scrollregion', b'selectbackground', b'selectborderwidth', b'selectforeground', b'state', b'takefocus', b'xscrollcommand', b'xscrollincrement', b'yscrollcommand', b'yscrollincrement', b'width')
    _conv_pixels = staticmethod(int_round)
    _stringify = True

    def create(self, **kwargs):
        return tkinter.Canvas(self.root, **kwargs)

    def test_closeenough(self):
        widget = self.create()
        self.checkFloatParam(widget, b'closeenough', 24, 2.4, 3.6, -3, conv=float)
        return

    def test_confine(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'confine')
        return

    def test_offset(self):
        widget = self.create()
        self.assertEqual(widget[b'offset'], b'0,0')
        self.checkParams(widget, b'offset', b'n', b'ne', b'e', b'se', b's', b'sw', b'w', b'nw', b'center')
        self.checkParam(widget, b'offset', b'10,20')
        self.checkParam(widget, b'offset', b'#5,6')
        self.checkInvalidParam(widget, b'offset', b'spam')
        return

    def test_scrollregion(self):
        widget = self.create()
        self.checkParam(widget, b'scrollregion', b'0 0 200 150')
        self.checkParam(widget, b'scrollregion', (0, 0, 200, 150), expected=b'0 0 200 150')
        self.checkParam(widget, b'scrollregion', b'')
        self.checkInvalidParam(widget, b'scrollregion', b'spam', errmsg=b'bad scrollRegion "spam"')
        self.checkInvalidParam(widget, b'scrollregion', (0, 0, 200, b'spam'))
        self.checkInvalidParam(widget, b'scrollregion', (0, 0, 200))
        self.checkInvalidParam(widget, b'scrollregion', (0, 0, 200, 150, 0))
        return

    def test_state(self):
        widget = self.create()
        self.checkEnumParam(widget, b'state', b'disabled', b'normal', errmsg=b'bad state value "{}": must be normal or disabled')
        return

    def test_xscrollincrement(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'xscrollincrement', 40, 0, 41.2, 43.6, -40, b'0.5i')
        return

    def test_yscrollincrement(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'yscrollincrement', 10, 0, 11.2, 13.6, -10, b'0.1i')
        return


@add_standard_options(IntegerSizeTests, StandardOptionsTests)
class ListboxTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'activestyle', b'background', b'borderwidth', b'cursor', b'disabledforeground', b'exportselection', b'font', b'foreground', b'height', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'justify', b'listvariable', b'relief', b'selectbackground', b'selectborderwidth', b'selectforeground', b'selectmode', b'setgrid', b'state', b'takefocus', b'width', b'xscrollcommand', b'yscrollcommand')

    def create(self, **kwargs):
        return tkinter.Listbox(self.root, **kwargs)

    def test_activestyle(self):
        widget = self.create()
        self.checkEnumParam(widget, b'activestyle', b'dotbox', b'none', b'underline')
        return

    test_justify = requires_tcl(8, 6, 5)(StandardOptionsTests.test_justify.im_func)

    def test_listvariable(self):
        widget = self.create()
        var = tkinter.DoubleVar(self.root)
        self.checkVariableParam(widget, b'listvariable', var)
        return

    def test_selectmode(self):
        widget = self.create()
        self.checkParam(widget, b'selectmode', b'single')
        self.checkParam(widget, b'selectmode', b'browse')
        self.checkParam(widget, b'selectmode', b'multiple')
        self.checkParam(widget, b'selectmode', b'extended')
        return

    def test_state(self):
        widget = self.create()
        self.checkEnumParam(widget, b'state', b'disabled', b'normal')
        return

    def test_itemconfigure(self):
        widget = self.create()
        with self.assertRaisesRegexp(TclError, b'item number "0" out of range'):
            widget.itemconfigure(0)
        colors = (b'red orange yellow green blue white violet').split()
        widget.insert(b'end', *colors)
        for i, color in enumerate(colors):
            widget.itemconfigure(i, background=color)

        with self.assertRaises(TypeError):
            widget.itemconfigure()
        with self.assertRaisesRegexp(TclError, b'bad listbox index "red"'):
            widget.itemconfigure(b'red')
        self.assertEqual(widget.itemconfigure(0, b'background'), (b'background', b'background', b'Background', b'', b'red'))
        self.assertEqual(widget.itemconfigure(b'end', b'background'), (b'background', b'background', b'Background', b'', b'violet'))
        self.assertEqual(widget.itemconfigure(b'@0,0', b'background'), (b'background', b'background', b'Background', b'', b'red'))
        d = widget.itemconfigure(0)
        self.assertIsInstance(d, dict)
        for k, v in d.items():
            self.assertIn(len(v), (2, 5))
            if len(v) == 5:
                self.assertEqual(v, widget.itemconfigure(0, k))
                self.assertEqual(v[4], widget.itemcget(0, k))

        return

    def check_itemconfigure(self, name, value):
        widget = self.create()
        widget.insert(b'end', b'a', b'b', b'c', b'd')
        widget.itemconfigure(0, **{name: value})
        self.assertEqual(widget.itemconfigure(0, name)[4], value)
        self.assertEqual(widget.itemcget(0, name), value)
        with self.assertRaisesRegexp(TclError, b'unknown color name "spam"'):
            widget.itemconfigure(0, **{name: b'spam'})
        return

    def test_itemconfigure_background(self):
        self.check_itemconfigure(b'background', b'#ff0000')
        return

    def test_itemconfigure_bg(self):
        self.check_itemconfigure(b'bg', b'#ff0000')
        return

    def test_itemconfigure_fg(self):
        self.check_itemconfigure(b'fg', b'#110022')
        return

    def test_itemconfigure_foreground(self):
        self.check_itemconfigure(b'foreground', b'#110022')
        return

    def test_itemconfigure_selectbackground(self):
        self.check_itemconfigure(b'selectbackground', b'#110022')
        return

    def test_itemconfigure_selectforeground(self):
        self.check_itemconfigure(b'selectforeground', b'#654321')
        return

    def test_box(self):
        lb = self.create()
        lb.insert(0, *(b'el%d' % i for i in range(8)))
        lb.pack()
        self.assertIsBoundingBox(lb.bbox(0))
        self.assertIsNone(lb.bbox(-1))
        self.assertIsNone(lb.bbox(10))
        self.assertRaises(TclError, lb.bbox, b'noindex')
        self.assertRaises(TclError, lb.bbox, None)
        self.assertRaises(TypeError, lb.bbox)
        self.assertRaises(TypeError, lb.bbox, 0, 1)
        return

    def test_curselection(self):
        lb = self.create()
        lb.insert(0, *(b'el%d' % i for i in range(8)))
        lb.selection_clear(0, tkinter.END)
        lb.selection_set(2, 4)
        lb.selection_set(6)
        self.assertEqual(lb.curselection(), (2, 3, 4, 6))
        self.assertRaises(TypeError, lb.curselection, 0)
        return

    def test_get(self):
        lb = self.create()
        lb.insert(0, *(b'el%d' % i for i in range(8)))
        self.assertEqual(lb.get(0), b'el0')
        self.assertEqual(lb.get(3), b'el3')
        self.assertEqual(lb.get(b'end'), b'el7')
        self.assertEqual(lb.get(8), b'')
        self.assertEqual(lb.get(-1), b'')
        self.assertEqual(lb.get(3, 5), (b'el3', b'el4', b'el5'))
        self.assertEqual(lb.get(5, b'end'), (b'el5', b'el6', b'el7'))
        self.assertEqual(lb.get(5, 0), ())
        self.assertEqual(lb.get(0, 0), (b'el0',))
        self.assertRaises(TclError, lb.get, b'noindex')
        self.assertRaises(TclError, lb.get, None)
        self.assertRaises(TypeError, lb.get)
        self.assertRaises(TclError, lb.get, b'end', b'noindex')
        self.assertRaises(TypeError, lb.get, 1, 2, 3)
        self.assertRaises(TclError, lb.get, 2.4)
        return


@add_standard_options(PixelSizeTests, StandardOptionsTests)
class ScaleTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'background', b'bigincrement', b'borderwidth', b'command', b'cursor', b'digits', b'font', b'foreground', b'from', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'label', b'length', b'orient', b'relief', b'repeatdelay', b'repeatinterval', b'resolution', b'showvalue', b'sliderlength', b'sliderrelief', b'state', b'takefocus', b'tickinterval', b'to', b'troughcolor', b'variable', b'width')
    default_orient = b'vertical'

    def create(self, **kwargs):
        return tkinter.Scale(self.root, **kwargs)

    def test_bigincrement(self):
        widget = self.create()
        self.checkFloatParam(widget, b'bigincrement', 12.4, 23.6, -5)
        return

    def test_digits(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'digits', 5, 0)
        return

    def test_from(self):
        widget = self.create()
        self.checkFloatParam(widget, b'from', 100, 14.9, 15.1, conv=round)
        return

    def test_label(self):
        widget = self.create()
        self.checkParam(widget, b'label', b'any string')
        self.checkParam(widget, b'label', b'')
        return

    def test_length(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'length', 130, 131.2, 135.6, b'5i')
        return

    def test_resolution(self):
        widget = self.create()
        self.checkFloatParam(widget, b'resolution', 4.2, 0, 6.7, -2)
        return

    def test_showvalue(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'showvalue')
        return

    def test_sliderlength(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'sliderlength', 10, 11.2, 15.6, -3, b'3m')
        return

    def test_sliderrelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'sliderrelief')
        return

    def test_tickinterval(self):
        widget = self.create()
        self.checkFloatParam(widget, b'tickinterval', 1, 4.3, 7.6, 0, conv=round)
        self.checkParam(widget, b'tickinterval', -2, expected=2, conv=round)
        return

    def test_to(self):
        widget = self.create()
        self.checkFloatParam(widget, b'to', 300, 14.9, 15.1, -10, conv=round)
        return


@add_standard_options(PixelSizeTests, StandardOptionsTests)
class ScrollbarTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'activerelief', b'background', b'borderwidth', b'command', b'cursor', b'elementborderwidth', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'jump', b'orient', b'relief', b'repeatdelay', b'repeatinterval', b'takefocus', b'troughcolor', b'width')
    _conv_pixels = staticmethod(int_round)
    _stringify = True
    default_orient = b'vertical'

    def create(self, **kwargs):
        return tkinter.Scrollbar(self.root, **kwargs)

    def test_activerelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'activerelief')
        return

    def test_elementborderwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'elementborderwidth', 4.3, 5.6, -2, b'1m')
        return

    def test_orient(self):
        widget = self.create()
        self.checkEnumParam(widget, b'orient', b'vertical', b'horizontal', errmsg=b'bad orientation "{}": must be vertical or horizontal')
        return

    def test_activate(self):
        sb = self.create()
        for e in (b'arrow1', b'slider', b'arrow2'):
            sb.activate(e)

        sb.activate(b'')
        self.assertRaises(TypeError, sb.activate)
        self.assertRaises(TypeError, sb.activate, b'arrow1', b'arrow2')
        return

    def test_set(self):
        sb = self.create()
        sb.set(0.2, 0.4)
        self.assertEqual(sb.get(), (0.2, 0.4))
        self.assertRaises(TclError, sb.set, b'abc', b'def')
        self.assertRaises(TclError, sb.set, 0.6, b'def')
        self.assertRaises(TclError, sb.set, 0.6, None)
        self.assertRaises(TclError, sb.set, 0.6)
        self.assertRaises(TclError, sb.set, 0.6, 0.7, 0.8)
        return


@add_standard_options(StandardOptionsTests)
class PanedWindowTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'background', b'borderwidth', b'cursor', b'handlepad', b'handlesize', b'height', b'opaqueresize', b'orient', b'proxybackground', b'proxyborderwidth', b'proxyrelief', b'relief', b'sashcursor', b'sashpad', b'sashrelief', b'sashwidth', b'showhandle', b'width')
    default_orient = b'horizontal'

    def create(self, **kwargs):
        return tkinter.PanedWindow(self.root, **kwargs)

    def test_handlepad(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'handlepad', 5, 6.4, 7.6, -3, b'1m')
        return

    def test_handlesize(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'handlesize', 8, 9.4, 10.6, -3, b'2m', conv=noconv)
        return

    def test_height(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'height', 100, 101.2, 102.6, -100, 0, b'1i', conv=noconv)
        return

    def test_opaqueresize(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'opaqueresize')
        return

    @requires_tcl(8, 6, 5)
    def test_proxybackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'proxybackground')
        return

    @requires_tcl(8, 6, 5)
    def test_proxyborderwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'proxyborderwidth', 0, 1.3, 2.9, 6, -2, b'10p', conv=noconv)
        return

    @requires_tcl(8, 6, 5)
    def test_proxyrelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'proxyrelief')
        return

    def test_sashcursor(self):
        widget = self.create()
        self.checkCursorParam(widget, b'sashcursor')
        return

    def test_sashpad(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'sashpad', 8, 1.3, 2.6, -2, b'2m')
        return

    def test_sashrelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'sashrelief')
        return

    def test_sashwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'sashwidth', 10, 11.1, 15.6, -3, b'1m', conv=noconv)
        return

    def test_showhandle(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'showhandle')
        return

    def test_width(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'width', 402, 403.4, 404.6, -402, 0, b'5i', conv=noconv)
        return

    def create2(self):
        p = self.create()
        b = tkinter.Button(p)
        c = tkinter.Button(p)
        p.add(b)
        p.add(c)
        return (p, b, c)

    def test_paneconfigure(self):
        p, b, c = self.create2()
        self.assertRaises(TypeError, p.paneconfigure)
        d = p.paneconfigure(b)
        self.assertIsInstance(d, dict)
        for k, v in d.items():
            self.assertEqual(len(v), 5)
            self.assertEqual(v, p.paneconfigure(b, k))
            self.assertEqual(v[4], p.panecget(b, k))

        return

    def check_paneconfigure(self, p, b, name, value, expected, stringify=False):
        conv = lambda x: x
        if not self.wantobjects or stringify:
            expected = str(expected)
        if self.wantobjects and stringify:
            conv = str
        p.paneconfigure(b, **{name: value})
        self.assertEqual(conv(p.paneconfigure(b, name)[4]), expected)
        self.assertEqual(conv(p.panecget(b, name)), expected)
        return

    def check_paneconfigure_bad(self, p, b, name, msg):
        with self.assertRaisesRegexp(TclError, msg):
            p.paneconfigure(b, **{name: b'badValue'})
        return

    def test_paneconfigure_after(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'after', c, str(c))
        self.check_paneconfigure_bad(p, b, b'after', b'bad window path name "badValue"')
        return

    def test_paneconfigure_before(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'before', c, str(c))
        self.check_paneconfigure_bad(p, b, b'before', b'bad window path name "badValue"')
        return

    def test_paneconfigure_height(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'height', 10, 10, stringify=get_tk_patchlevel() < (8, 5, 11))
        self.check_paneconfigure_bad(p, b, b'height', b'bad screen distance "badValue"')
        return

    @requires_tcl(8, 5)
    def test_paneconfigure_hide(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'hide', False, 0)
        self.check_paneconfigure_bad(p, b, b'hide', b'expected boolean value but got "badValue"')
        return

    def test_paneconfigure_minsize(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'minsize', 10, 10)
        self.check_paneconfigure_bad(p, b, b'minsize', b'bad screen distance "badValue"')
        return

    def test_paneconfigure_padx(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'padx', 1.3, 1)
        self.check_paneconfigure_bad(p, b, b'padx', b'bad screen distance "badValue"')
        return

    def test_paneconfigure_pady(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'pady', 1.3, 1)
        self.check_paneconfigure_bad(p, b, b'pady', b'bad screen distance "badValue"')
        return

    def test_paneconfigure_sticky(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'sticky', b'nsew', b'nesw')
        self.check_paneconfigure_bad(p, b, b'sticky', b'bad stickyness value "badValue": must be a string containing zero or more of n, e, s, and w')
        return

    @requires_tcl(8, 5)
    def test_paneconfigure_stretch(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'stretch', b'alw', b'always')
        self.check_paneconfigure_bad(p, b, b'stretch', b'bad stretch "badValue": must be always, first, last, middle, or never')
        return

    def test_paneconfigure_width(self):
        p, b, c = self.create2()
        self.check_paneconfigure(p, b, b'width', 10, 10, stringify=get_tk_patchlevel() < (8, 5, 11))
        self.check_paneconfigure_bad(p, b, b'width', b'bad screen distance "badValue"')
        return


@add_standard_options(StandardOptionsTests)
class MenuTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'activebackground', b'activeborderwidth', b'activeforeground', b'background', b'borderwidth', b'cursor', b'disabledforeground', b'font', b'foreground', b'postcommand', b'relief', b'selectcolor', b'takefocus', b'tearoff', b'tearoffcommand', b'title', b'type')
    _conv_pixels = noconv_meth

    def create(self, **kwargs):
        return tkinter.Menu(self.root, **kwargs)

    def test_postcommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'postcommand')
        return

    def test_tearoff(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'tearoff')
        return

    def test_tearoffcommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'tearoffcommand')
        return

    def test_title(self):
        widget = self.create()
        self.checkParam(widget, b'title', b'any string')
        return

    def test_type(self):
        widget = self.create()
        self.checkEnumParam(widget, b'type', b'normal', b'tearoff', b'menubar')
        return

    def test_entryconfigure(self):
        m1 = self.create()
        m1.add_command(label=b'test')
        self.assertRaises(TypeError, m1.entryconfigure)
        with self.assertRaisesRegexp(TclError, b'bad menu entry index "foo"'):
            m1.entryconfigure(b'foo')
        d = m1.entryconfigure(1)
        self.assertIsInstance(d, dict)
        for k, v in d.items():
            self.assertIsInstance(k, str)
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 5)
            self.assertEqual(v[0], k)
            self.assertEqual(m1.entrycget(1, k), v[4])

        m1.destroy()
        return

    def test_entryconfigure_label(self):
        m1 = self.create()
        m1.add_command(label=b'test')
        self.assertEqual(m1.entrycget(1, b'label'), b'test')
        m1.entryconfigure(1, label=b'changed')
        self.assertEqual(m1.entrycget(1, b'label'), b'changed')
        return

    def test_entryconfigure_variable(self):
        m1 = self.create()
        v1 = tkinter.BooleanVar(self.root)
        v2 = tkinter.BooleanVar(self.root)
        m1.add_checkbutton(variable=v1, onvalue=True, offvalue=False, label=b'Nonsense')
        self.assertEqual(str(m1.entrycget(1, b'variable')), str(v1))
        m1.entryconfigure(1, variable=v2)
        self.assertEqual(str(m1.entrycget(1, b'variable')), str(v2))
        return


@add_standard_options(PixelSizeTests, StandardOptionsTests)
class MessageTest(AbstractWidgetTest, unittest.TestCase):
    OPTIONS = (b'anchor', b'aspect', b'background', b'borderwidth', b'cursor', b'font', b'foreground', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'justify', b'padx', b'pady', b'relief', b'takefocus', b'text', b'textvariable', b'width')
    _conv_pad_pixels = noconv_meth

    def create(self, **kwargs):
        return tkinter.Message(self.root, **kwargs)

    def test_aspect(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'aspect', 250, 0, -300)
        return


tests_gui = [
 ButtonTest, CanvasTest, CheckbuttonTest, EntryTest, 
 FrameTest, LabelFrameTest, 
 LabelTest, ListboxTest, 
 MenubuttonTest, MenuTest, MessageTest, OptionMenuTest, 
 PanedWindowTest, 
 RadiobuttonTest, ScaleTest, ScrollbarTest, 
 SpinboxTest, TextTest, ToplevelTest]
if __name__ == b'__main__':
    run_unittest(*tests_gui)
