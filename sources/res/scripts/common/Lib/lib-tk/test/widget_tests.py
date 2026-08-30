import unittest, sys, Tkinter as tkinter
from ttk import Scale
from test_ttk.support import AbstractTkTest, tcl_version, requires_tcl, get_tk_patchlevel, pixels_conv, tcl_obj_eq
import test.test_support
noconv = noconv_meth = False
if get_tk_patchlevel() < (8, 5, 11):
    noconv = str
noconv_meth = noconv and staticmethod(noconv)

def int_round(x):
    return int(round(x))


pixels_round = int_round
if get_tk_patchlevel()[:3] == (8, 5, 11):
    pixels_round = int
_sentinel = object()

class AbstractWidgetTest(AbstractTkTest):
    _conv_pixels = staticmethod(pixels_round)
    _conv_pad_pixels = None
    _stringify = False

    @property
    def scaling(self):
        try:
            return self._scaling
        except AttributeError:
            self._scaling = float(self.root.call(b'tk', b'scaling'))
            return self._scaling

        return

    def _str(self, value):
        if not self._stringify and self.wantobjects and tcl_version >= (8, 6):
            return value
        if isinstance(value, tuple):
            return (b' ').join(map(self._str, value))
        return str(value)

    def assertEqual2(self, actual, expected, msg=None, eq=object.__eq__):
        if eq(actual, expected):
            return
        self.assertEqual(actual, expected, msg)
        return

    def checkParam(self, widget, name, value, expected=_sentinel, conv=False, eq=None):
        widget[name] = value
        if expected is _sentinel:
            expected = value
        if conv:
            expected = conv(expected)
        if self._stringify or not self.wantobjects:
            if isinstance(expected, tuple):
                expected = tkinter._join(expected)
            else:
                expected = str(expected)
        if eq is None:
            eq = tcl_obj_eq
        self.assertEqual2(widget[name], expected, eq=eq)
        self.assertEqual2(widget.cget(name), expected, eq=eq)
        if not isinstance(widget, Scale):
            t = widget.configure(name)
            self.assertEqual(len(t), 5)
            self.assertEqual2(t[4], expected, eq=eq)
        return

    def checkInvalidParam(self, widget, name, value, errmsg=None, keep_orig=True):
        orig = widget[name]
        if errmsg is not None:
            errmsg = errmsg.format(value)
        with self.assertRaises(tkinter.TclError) as cm:
            widget[name] = value
        if errmsg is not None:
            self.assertEqual(str(cm.exception), errmsg)
        if keep_orig:
            self.assertEqual(widget[name], orig)
        else:
            widget[name] = orig
        with self.assertRaises(tkinter.TclError) as cm:
            widget.configure({name: value})
        if errmsg is not None:
            self.assertEqual(str(cm.exception), errmsg)
        if keep_orig:
            self.assertEqual(widget[name], orig)
        else:
            widget[name] = orig
        return

    def checkParams(self, widget, name, *values, **kwargs):
        for value in values:
            self.checkParam(widget, name, value, **kwargs)

        return

    def checkIntegerParam(self, widget, name, *values, **kwargs):
        self.checkParams(widget, name, *values, **kwargs)
        self.checkInvalidParam(widget, name, b'', errmsg=b'expected integer but got ""')
        self.checkInvalidParam(widget, name, b'10p', errmsg=b'expected integer but got "10p"')
        self.checkInvalidParam(widget, name, 3.2, errmsg=b'expected integer but got "3.2"')
        return

    def checkFloatParam(self, widget, name, *values, **kwargs):
        if b'conv' in kwargs:
            conv = kwargs.pop(b'conv')
        else:
            conv = float
        for value in values:
            self.checkParam(widget, name, value, conv=conv, **kwargs)

        self.checkInvalidParam(widget, name, b'', errmsg=b'expected floating-point number but got ""')
        self.checkInvalidParam(widget, name, b'spam', errmsg=b'expected floating-point number but got "spam"')
        return

    def checkBooleanParam(self, widget, name):
        for value in (False, 0, b'false', b'no', b'off'):
            self.checkParam(widget, name, value, expected=0)

        for value in (True, 1, b'true', b'yes', b'on'):
            self.checkParam(widget, name, value, expected=1)

        self.checkInvalidParam(widget, name, b'', errmsg=b'expected boolean value but got ""')
        self.checkInvalidParam(widget, name, b'spam', errmsg=b'expected boolean value but got "spam"')
        return

    def checkColorParam(self, widget, name, allow_empty=None, **kwargs):
        self.checkParams(widget, name, b'#ff0000', b'#00ff00', b'#0000ff', b'#123456', b'red', b'green', b'blue', b'white', b'black', b'grey', **kwargs)
        self.checkInvalidParam(widget, name, b'spam', errmsg=b'unknown color name "spam"')
        return

    def checkCursorParam(self, widget, name, **kwargs):
        self.checkParams(widget, name, b'arrow', b'watch', b'cross', b'', **kwargs)
        if tcl_version >= (8, 5):
            self.checkParam(widget, name, b'none')
        self.checkInvalidParam(widget, name, b'spam', errmsg=b'bad cursor spec "spam"')
        return

    def checkCommandParam(self, widget, name):

        def command(*args):
            return

        widget[name] = command
        self.assertTrue(widget[name])
        self.checkParams(widget, name, b'')
        return

    def checkEnumParam(self, widget, name, *values, **kwargs):
        if b'errmsg' in kwargs:
            errmsg = kwargs.pop(b'errmsg')
        else:
            errmsg = None
        self.checkParams(widget, name, *values, **kwargs)
        if errmsg is None:
            errmsg2 = b' %s "{}": must be %s%s or %s' % (
             name,
             (b', ').join(values[:-1]),
             b',' if len(values) > 2 else b'',
             values[-1])
            self.checkInvalidParam(widget, name, b'', errmsg=b'ambiguous' + errmsg2)
            errmsg = b'bad' + errmsg2
        self.checkInvalidParam(widget, name, b'spam', errmsg=errmsg)
        return

    def checkPixelsParam(self, widget, name, *values, **kwargs):
        if b'conv' in kwargs:
            conv = kwargs.pop(b'conv')
        else:
            conv = None
        if conv is None:
            conv = self._conv_pixels
        if b'keep_orig' in kwargs:
            keep_orig = kwargs.pop(b'keep_orig')
        else:
            keep_orig = True
        for value in values:
            expected = _sentinel
            conv1 = conv
            if isinstance(value, str):
                if conv1 and conv1 is not str:
                    expected = pixels_conv(value) * self.scaling
                    conv1 = int_round
            self.checkParam(widget, name, value, expected=expected, conv=conv1, **kwargs)

        self.checkInvalidParam(widget, name, b'6x', errmsg=b'bad screen distance "6x"', keep_orig=keep_orig)
        self.checkInvalidParam(widget, name, b'spam', errmsg=b'bad screen distance "spam"', keep_orig=keep_orig)
        return

    def checkReliefParam(self, widget, name):
        self.checkParams(widget, name, b'flat', b'groove', b'raised', b'ridge', b'solid', b'sunken')
        errmsg = b'bad relief "spam": must be flat, groove, raised, ridge, solid, or sunken'
        if tcl_version < (8, 6):
            errmsg = None
        self.checkInvalidParam(widget, name, b'spam', errmsg=errmsg)
        return

    def checkImageParam(self, widget, name):
        image = tkinter.PhotoImage(master=self.root, name=b'image1')
        self.checkParam(widget, name, image, conv=str)
        self.checkInvalidParam(widget, name, b'spam', errmsg=b'image "spam" doesn\'t exist')
        widget[name] = b''
        return

    def checkVariableParam(self, widget, name, var):
        self.checkParam(widget, name, var, conv=str)
        return

    def assertIsBoundingBox(self, bbox):
        self.assertIsNotNone(bbox)
        self.assertIsInstance(bbox, tuple)
        if len(bbox) != 4:
            self.fail(b'Invalid bounding box: %r' % (bbox,))
        for item in bbox:
            if not isinstance(item, int):
                self.fail(b'Invalid bounding box: %r' % (bbox,))
                break

        return

    def test_keys(self):
        widget = self.create()
        keys = widget.keys()
        if not isinstance(widget, Scale):
            self.assertEqual(sorted(keys), sorted(widget.configure()))
        for k in keys:
            widget[k]

        if test.test_support.verbose:
            aliases = {b'bd': b'borderwidth', b'bg': b'background', 
               b'fg': b'foreground', 
               b'invcmd': b'invalidcommand', 
               b'vcmd': b'validatecommand'}
            keys = set(keys)
            expected = set(self.OPTIONS)
            for k in sorted(keys - expected):
                if not (k in aliases and aliases[k] in keys and aliases[k] in expected):
                    print b'%s.OPTIONS doesn\'t contain "%s"' % (
                     self.__class__.__name__, k)

        return


class StandardOptionsTests(object):
    STANDARD_OPTIONS = (b'activebackground', b'activeborderwidth', b'activeforeground', b'anchor', b'background', b'bitmap', b'borderwidth', b'compound', b'cursor', b'disabledforeground', b'exportselection', b'font', b'foreground', b'highlightbackground', b'highlightcolor', b'highlightthickness', b'image', b'insertbackground', b'insertborderwidth', b'insertofftime', b'insertontime', b'insertwidth', b'jump', b'justify', b'orient', b'padx', b'pady', b'relief', b'repeatdelay', b'repeatinterval', b'selectbackground', b'selectborderwidth', b'selectforeground', b'setgrid', b'takefocus', b'text', b'textvariable', b'troughcolor', b'underline', b'wraplength', b'xscrollcommand', b'yscrollcommand')

    def test_activebackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'activebackground')
        return

    def test_activeborderwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'activeborderwidth', 0, 1.3, 2.9, 6, -2, b'10p')
        return

    def test_activeforeground(self):
        widget = self.create()
        self.checkColorParam(widget, b'activeforeground')
        return

    def test_anchor(self):
        widget = self.create()
        self.checkEnumParam(widget, b'anchor', b'n', b'ne', b'e', b'se', b's', b'sw', b'w', b'nw', b'center')
        return

    def test_background(self):
        widget = self.create()
        self.checkColorParam(widget, b'background')
        if b'bg' in self.OPTIONS:
            self.checkColorParam(widget, b'bg')
        return

    def test_bitmap(self):
        widget = self.create()
        self.checkParam(widget, b'bitmap', b'questhead')
        self.checkParam(widget, b'bitmap', b'gray50')
        filename = test.test_support.findfile(b'python.xbm', subdir=b'imghdrdata')
        self.checkParam(widget, b'bitmap', b'@' + filename)
        if not (b'aqua' in self.root.tk.call(b'tk', b'windowingsystem') and b'AppKit' in self.root.winfo_server()):
            self.checkInvalidParam(widget, b'bitmap', b'spam', errmsg=b'bitmap "spam" not defined')
        return

    def test_borderwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'borderwidth', 0, 1.3, 2.6, 6, -2, b'10p')
        if b'bd' in self.OPTIONS:
            self.checkPixelsParam(widget, b'bd', 0, 1.3, 2.6, 6, -2, b'10p')
        return

    def test_compound(self):
        widget = self.create()
        self.checkEnumParam(widget, b'compound', b'bottom', b'center', b'left', b'none', b'right', b'top')
        return

    def test_cursor(self):
        widget = self.create()
        self.checkCursorParam(widget, b'cursor')
        return

    def test_disabledforeground(self):
        widget = self.create()
        self.checkColorParam(widget, b'disabledforeground')
        return

    def test_exportselection(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'exportselection')
        return

    def test_font(self):
        widget = self.create()
        self.checkParam(widget, b'font', b'-Adobe-Helvetica-Medium-R-Normal--*-120-*-*-*-*-*-*')
        self.checkInvalidParam(widget, b'font', b'', errmsg=b'font "" doesn\'t exist')
        return

    def test_foreground(self):
        widget = self.create()
        self.checkColorParam(widget, b'foreground')
        if b'fg' in self.OPTIONS:
            self.checkColorParam(widget, b'fg')
        return

    def test_highlightbackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'highlightbackground')
        return

    def test_highlightcolor(self):
        widget = self.create()
        self.checkColorParam(widget, b'highlightcolor')
        return

    def test_highlightthickness(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'highlightthickness', 0, 1.3, 2.6, 6, b'10p')
        self.checkParam(widget, b'highlightthickness', -2, expected=0, conv=self._conv_pixels)
        return

    @unittest.skipIf(sys.platform == b'darwin', b'crashes with Cocoa Tk (issue19733)')
    def test_image(self):
        widget = self.create()
        self.checkImageParam(widget, b'image')
        return

    def test_insertbackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'insertbackground')
        return

    def test_insertborderwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'insertborderwidth', 0, 1.3, 2.6, 6, -2, b'10p')
        return

    def test_insertofftime(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'insertofftime', 100)
        return

    def test_insertontime(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'insertontime', 100)
        return

    def test_insertwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'insertwidth', 1.3, 2.6, -2, b'10p')
        return

    def test_jump(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'jump')
        return

    def test_justify(self):
        widget = self.create()
        self.checkEnumParam(widget, b'justify', b'left', b'right', b'center', errmsg=b'bad justification "{}": must be left, right, or center')
        self.checkInvalidParam(widget, b'justify', b'', errmsg=b'ambiguous justification "": must be left, right, or center')
        return

    def test_orient(self):
        widget = self.create()
        self.assertEqual(str(widget[b'orient']), self.default_orient)
        self.checkEnumParam(widget, b'orient', b'horizontal', b'vertical')
        return

    def test_padx(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'padx', 3, 4.4, 5.6, -2, b'12m', conv=self._conv_pad_pixels)
        return

    def test_pady(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'pady', 3, 4.4, 5.6, -2, b'12m', conv=self._conv_pad_pixels)
        return

    def test_relief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'relief')
        return

    def test_repeatdelay(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'repeatdelay', -500, 500)
        return

    def test_repeatinterval(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'repeatinterval', -500, 500)
        return

    def test_selectbackground(self):
        widget = self.create()
        self.checkColorParam(widget, b'selectbackground')
        return

    def test_selectborderwidth(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'selectborderwidth', 1.3, 2.6, -2, b'10p')
        return

    def test_selectforeground(self):
        widget = self.create()
        self.checkColorParam(widget, b'selectforeground')
        return

    def test_setgrid(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'setgrid')
        return

    def test_state(self):
        widget = self.create()
        self.checkEnumParam(widget, b'state', b'active', b'disabled', b'normal')
        return

    def test_takefocus(self):
        widget = self.create()
        self.checkParams(widget, b'takefocus', b'0', b'1', b'')
        return

    def test_text(self):
        widget = self.create()
        self.checkParams(widget, b'text', b'', b'any string')
        return

    def test_textvariable(self):
        widget = self.create()
        var = tkinter.StringVar(self.root)
        self.checkVariableParam(widget, b'textvariable', var)
        return

    def test_troughcolor(self):
        widget = self.create()
        self.checkColorParam(widget, b'troughcolor')
        return

    def test_underline(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'underline', 0, 1, 10)
        return

    def test_wraplength(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'wraplength', 100)
        return

    def test_xscrollcommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'xscrollcommand')
        return

    def test_yscrollcommand(self):
        widget = self.create()
        self.checkCommandParam(widget, b'yscrollcommand')
        return

    def test_command(self):
        widget = self.create()
        self.checkCommandParam(widget, b'command')
        return

    def test_indicatoron(self):
        widget = self.create()
        self.checkBooleanParam(widget, b'indicatoron')
        return

    def test_offrelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'offrelief')
        return

    def test_overrelief(self):
        widget = self.create()
        self.checkReliefParam(widget, b'overrelief')
        return

    def test_selectcolor(self):
        widget = self.create()
        self.checkColorParam(widget, b'selectcolor')
        return

    def test_selectimage(self):
        widget = self.create()
        self.checkImageParam(widget, b'selectimage')
        return

    @requires_tcl(8, 5)
    def test_tristateimage(self):
        widget = self.create()
        self.checkImageParam(widget, b'tristateimage')
        return

    @requires_tcl(8, 5)
    def test_tristatevalue(self):
        widget = self.create()
        self.checkParam(widget, b'tristatevalue', b'unknowable')
        return

    def test_variable(self):
        widget = self.create()
        var = tkinter.DoubleVar(self.root)
        self.checkVariableParam(widget, b'variable', var)
        return


class IntegerSizeTests(object):

    def test_height(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'height', 100, -100, 0)
        return

    def test_width(self):
        widget = self.create()
        self.checkIntegerParam(widget, b'width', 402, -402, 0)
        return


class PixelSizeTests(object):

    def test_height(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'height', 100, 101.2, 102.6, -100, 0, b'3c')
        return

    def test_width(self):
        widget = self.create()
        self.checkPixelsParam(widget, b'width', 402, 403.4, 404.6, -402, 0, b'5i')
        return


def add_standard_options(*source_classes):

    def decorator(cls):
        for option in cls.OPTIONS:
            methodname = b'test_' + option
            if not hasattr(cls, methodname):
                for source_class in source_classes:
                    if hasattr(source_class, methodname):
                        setattr(cls, methodname, getattr(source_class, methodname).im_func)
                        break
                else:

                    def test(self, option=option):
                        widget = self.create()
                        widget[option]
                        raise AssertionError(b'Option "%s" is not tested in %s' % (
                         option, cls.__name__))
                        return

                    test.__name__ = methodname
                    setattr(cls, methodname, test)

        return cls

    return decorator


def setUpModule():
    if test.test_support.verbose:
        tcl = tkinter.Tcl()
        print b'patchlevel =', tcl.call(b'info', b'patchlevel')
    return
