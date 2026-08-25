import os, Tkinter
from Tkinter import *
from Tkinter import _flatten, _cnfmerge
if TkVersion < 3.999:
    raise ImportError, b'This version of Tix.py requires Tk 4.0 or higher'
import _tkinter
WINDOW = b'window'
TEXT = b'text'
STATUS = b'status'
IMMEDIATE = b'immediate'
IMAGE = b'image'
IMAGETEXT = b'imagetext'
BALLOON = b'balloon'
AUTO = b'auto'
ACROSSTOP = b'acrosstop'
ASCII = b'ascii'
CELL = b'cell'
COLUMN = b'column'
DECREASING = b'decreasing'
INCREASING = b'increasing'
INTEGER = b'integer'
MAIN = b'main'
MAX = b'max'
REAL = b'real'
ROW = b'row'
S_REGION = b's-region'
X_REGION = b'x-region'
Y_REGION = b'y-region'
TCL_DONT_WAIT = 2
TCL_WINDOW_EVENTS = 4
TCL_FILE_EVENTS = 8
TCL_TIMER_EVENTS = 16
TCL_IDLE_EVENTS = 32
TCL_ALL_EVENTS = 0

class tixCommand:

    def tix_addbitmapdir(self, directory):
        return self.tk.call(b'tix', b'addbitmapdir', directory)

    def tix_cget(self, option):
        return self.tk.call(b'tix', b'cget', option)

    def tix_configure(self, cnf=None, **kw):
        if kw:
            cnf = _cnfmerge((cnf, kw))
        elif cnf:
            cnf = _cnfmerge(cnf)
        if cnf is None:
            return self._getconfigure(b'tix', b'configure')
        else:
            if isinstance(cnf, StringType):
                return self._getconfigure1(b'tix', b'configure', b'-' + cnf)
            return self.tk.call((b'tix', b'configure') + self._options(cnf))

    def tix_filedialog(self, dlgclass=None):
        if dlgclass is not None:
            return self.tk.call(b'tix', b'filedialog', dlgclass)
        else:
            return self.tk.call(b'tix', b'filedialog')
            return

    def tix_getbitmap(self, name):
        return self.tk.call(b'tix', b'getbitmap', name)

    def tix_getimage(self, name):
        return self.tk.call(b'tix', b'getimage', name)

    def tix_option_get(self, name):
        return self.tk.call(b'tix', b'option', b'get', name)

    def tix_resetoptions(self, newScheme, newFontSet, newScmPrio=None):
        if newScmPrio is not None:
            return self.tk.call(b'tix', b'resetoptions', newScheme, newFontSet, newScmPrio)
        else:
            return self.tk.call(b'tix', b'resetoptions', newScheme, newFontSet)
            return


class Tk(Tkinter.Tk, tixCommand):

    def __init__(self, screenName=None, baseName=None, className=b'Tix'):
        Tkinter.Tk.__init__(self, screenName, baseName, className)
        tixlib = os.environ.get(b'TIX_LIBRARY')
        self.tk.eval(b'global auto_path; lappend auto_path [file dir [info nameof]]')
        if tixlib is not None:
            self.tk.eval(b'global auto_path; lappend auto_path {%s}' % tixlib)
            self.tk.eval(b'global tcl_pkgPath; lappend tcl_pkgPath {%s}' % tixlib)
        self.tk.eval(b'package require Tix')
        return

    def destroy(self):
        self.protocol(b'WM_DELETE_WINDOW', b'')
        Tkinter.Tk.destroy(self)
        return


class Form:

    def config(self, cnf={}, **kw):
        self.tk.call(b'tixForm', self._w, *self._options(cnf, kw))
        return

    form = config

    def __setitem__(self, key, value):
        Form.form(self, {key: value})
        return

    def check(self):
        return self.tk.call(b'tixForm', b'check', self._w)

    def forget(self):
        self.tk.call(b'tixForm', b'forget', self._w)
        return

    def grid(self, xsize=0, ysize=0):
        if not xsize and not ysize:
            x = self.tk.call(b'tixForm', b'grid', self._w)
            y = self.tk.splitlist(x)
            z = ()
            for x in y:
                z = z + (self.tk.getint(x),)

            return z
        return self.tk.call(b'tixForm', b'grid', self._w, xsize, ysize)

    def info(self, option=None):
        if not option:
            return self.tk.call(b'tixForm', b'info', self._w)
        if option[0] != b'-':
            option = b'-' + option
        return self.tk.call(b'tixForm', b'info', self._w, option)

    def slaves(self):
        return map(self._nametowidget, self.tk.splitlist(self.tk.call(b'tixForm', b'slaves', self._w)))


Tkinter.Widget.__bases__ = Tkinter.Widget.__bases__ + (Form,)

class TixWidget(Tkinter.Widget):

    def __init__(self, master=None, widgetName=None, static_options=None, cnf={}, kw={}):
        if kw:
            cnf = _cnfmerge((cnf, kw))
        else:
            cnf = _cnfmerge(cnf)
        extra = ()
        if static_options:
            static_options.append(b'options')
        else:
            static_options = [
             b'options']
        for k, v in cnf.items()[:]:
            if k in static_options:
                extra = extra + (b'-' + k, v)
                del cnf[k]

        self.widgetName = widgetName
        Widget._setup(self, master, cnf)
        if widgetName:
            self.tk.call(widgetName, self._w, *extra)
        if cnf:
            Widget.config(self, cnf)
        self.subwidget_list = {}
        return

    def __getattr__(self, name):
        if name in self.subwidget_list:
            return self.subwidget_list[name]
        raise AttributeError, name
        return

    def set_silent(self, value):
        self.tk.call(b'tixSetSilent', self._w, value)
        return

    def subwidget(self, name):
        n = self._subwidget_name(name)
        if not n:
            raise TclError, b'Subwidget ' + name + b' not child of ' + self._name
        n = n[len(self._w) + 1:]
        return self._nametowidget(n)

    def subwidgets_all(self):
        names = self._subwidget_names()
        if not names:
            return []
        retlist = []
        for name in names:
            name = name[len(self._w) + 1:]
            try:
                retlist.append(self._nametowidget(name))
            except:
                pass

        return retlist

    def _subwidget_name(self, name):
        try:
            return self.tk.call(self._w, b'subwidget', name)
        except TclError:
            return

        return

    def _subwidget_names(self):
        try:
            x = self.tk.call(self._w, b'subwidgets', b'-all')
            return self.tk.splitlist(x)
        except TclError:
            return

        return

    def config_all(self, option, value):
        if option == b'':
            return
        if not isinstance(option, StringType):
            option = repr(option)
        if not isinstance(value, StringType):
            value = repr(value)
        names = self._subwidget_names()
        for name in names:
            self.tk.call(name, b'configure', b'-' + option, value)

        return

    def image_create(self, imgtype, cnf={}, master=None, **kw):
        if not master:
            master = Tkinter._default_root
            if not master:
                raise RuntimeError, b'Too early to create image'
        if kw and cnf:
            cnf = _cnfmerge((cnf, kw))
        elif kw:
            cnf = kw
        options = ()
        for k, v in cnf.items():
            if hasattr(v, b'__call__'):
                v = self._register(v)
            options = options + (b'-' + k, v)

        return master.tk.call((b'image', b'create', imgtype) + options)

    def image_delete(self, imgname):
        try:
            self.tk.call(b'image', b'delete', imgname)
        except TclError:
            pass

        return


class TixSubWidget(TixWidget):

    def __init__(self, master, name, destroy_physically=1, check_intermediate=1):
        if check_intermediate:
            path = master._subwidget_name(name)
            try:
                path = path[len(master._w) + 1:]
                plist = path.split(b'.')
            except:
                plist = []

        if not check_intermediate:
            TixWidget.__init__(self, master, None, None, {b'name': name})
        else:
            parent = master
            for i in range(len(plist) - 1):
                n = (b'.').join(plist[:i + 1])
                try:
                    w = master._nametowidget(n)
                    parent = w
                except KeyError:
                    parent = TixSubWidget(parent, plist[i], destroy_physically=0, check_intermediate=0)

            if plist:
                name = plist[-1]
            TixWidget.__init__(self, parent, None, None, {b'name': name})
        self.destroy_physically = destroy_physically
        return

    def destroy(self):
        for c in self.children.values():
            c.destroy()

        if self._name in self.master.children:
            del self.master.children[self._name]
        if self._name in self.master.subwidget_list:
            del self.master.subwidget_list[self._name]
        if self.destroy_physically:
            self.tk.call(b'destroy', self._w)
        return


class DisplayStyle:

    def __init__(self, itemtype, cnf={}, **kw):
        if b'refwindow' in kw:
            master = kw[b'refwindow']
        elif b'refwindow' in cnf:
            master = cnf[b'refwindow']
        else:
            master = Tkinter._default_root
            if not master:
                raise RuntimeError(b'Too early to create display style: no root window')
        self.tk = master.tk
        self.stylename = self.tk.call(b'tixDisplayStyle', itemtype, *self._options(cnf, kw))
        return

    def __str__(self):
        return self.stylename

    def _options(self, cnf, kw):
        if kw and cnf:
            cnf = _cnfmerge((cnf, kw))
        elif kw:
            cnf = kw
        opts = ()
        for k, v in cnf.items():
            opts = opts + (b'-' + k, v)

        return opts

    def delete(self):
        self.tk.call(self.stylename, b'delete')
        return

    def __setitem__(self, key, value):
        self.tk.call(self.stylename, b'configure', b'-%s' % key, value)
        return

    def config(self, cnf={}, **kw):
        return self._getconfigure(self.stylename, b'configure', *self._options(cnf, kw))

    def __getitem__(self, key):
        return self.tk.call(self.stylename, b'cget', b'-%s' % key)


class Balloon(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        static = [
         1, 2, 3, 4, 
         5]
        TixWidget.__init__(self, master, b'tixBalloon', static, cnf, kw)
        self.subwidget_list[b'label'] = _dummyLabel(self, b'label', destroy_physically=0)
        self.subwidget_list[b'message'] = _dummyLabel(self, b'message', destroy_physically=0)
        return

    def bind_widget(self, widget, cnf={}, **kw):
        self.tk.call(self._w, b'bind', widget._w, *self._options(cnf, kw))
        return

    def unbind_widget(self, widget):
        self.tk.call(self._w, b'unbind', widget._w)
        return


class ButtonBox(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixButtonBox', [
         b'orientation', b'options'], cnf, kw)
        return

    def add(self, name, cnf={}, **kw):
        btn = self.tk.call(self._w, b'add', name, *self._options(cnf, kw))
        self.subwidget_list[name] = _dummyButton(self, name)
        return btn

    def invoke(self, name):
        if name in self.subwidget_list:
            self.tk.call(self._w, b'invoke', name)
        return


class ComboBox(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixComboBox', [
         b'editable', b'dropdown', b'fancy', b'options'], cnf, kw)
        self.subwidget_list[b'label'] = _dummyLabel(self, b'label')
        self.subwidget_list[b'entry'] = _dummyEntry(self, b'entry')
        self.subwidget_list[b'arrow'] = _dummyButton(self, b'arrow')
        self.subwidget_list[b'slistbox'] = _dummyScrolledListBox(self, b'slistbox')
        try:
            self.subwidget_list[b'tick'] = _dummyButton(self, b'tick')
            self.subwidget_list[b'cross'] = _dummyButton(self, b'cross')
        except TypeError:
            pass

        return

    def add_history(self, str):
        self.tk.call(self._w, b'addhistory', str)
        return

    def append_history(self, str):
        self.tk.call(self._w, b'appendhistory', str)
        return

    def insert(self, index, str):
        self.tk.call(self._w, b'insert', index, str)
        return

    def pick(self, index):
        self.tk.call(self._w, b'pick', index)
        return


class Control(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixControl', [b'options'], cnf, kw)
        self.subwidget_list[b'incr'] = _dummyButton(self, b'incr')
        self.subwidget_list[b'decr'] = _dummyButton(self, b'decr')
        self.subwidget_list[b'label'] = _dummyLabel(self, b'label')
        self.subwidget_list[b'entry'] = _dummyEntry(self, b'entry')
        return

    def decrement(self):
        self.tk.call(self._w, b'decr')
        return

    def increment(self):
        self.tk.call(self._w, b'incr')
        return

    def invoke(self):
        self.tk.call(self._w, b'invoke')
        return

    def update(self):
        self.tk.call(self._w, b'update')
        return


class DirList(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixDirList', [b'options'], cnf, kw)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return

    def chdir(self, dir):
        self.tk.call(self._w, b'chdir', dir)
        return


class DirTree(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixDirTree', [b'options'], cnf, kw)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return

    def chdir(self, dir):
        self.tk.call(self._w, b'chdir', dir)
        return


class DirSelectBox(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixDirSelectBox', [b'options'], cnf, kw)
        self.subwidget_list[b'dirlist'] = _dummyDirList(self, b'dirlist')
        self.subwidget_list[b'dircbx'] = _dummyFileComboBox(self, b'dircbx')
        return


class ExFileSelectBox(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixExFileSelectBox', [b'options'], cnf, kw)
        self.subwidget_list[b'cancel'] = _dummyButton(self, b'cancel')
        self.subwidget_list[b'ok'] = _dummyButton(self, b'ok')
        self.subwidget_list[b'hidden'] = _dummyCheckbutton(self, b'hidden')
        self.subwidget_list[b'types'] = _dummyComboBox(self, b'types')
        self.subwidget_list[b'dir'] = _dummyComboBox(self, b'dir')
        self.subwidget_list[b'dirlist'] = _dummyDirList(self, b'dirlist')
        self.subwidget_list[b'file'] = _dummyComboBox(self, b'file')
        self.subwidget_list[b'filelist'] = _dummyScrolledListBox(self, b'filelist')
        return

    def filter(self):
        self.tk.call(self._w, b'filter')
        return

    def invoke(self):
        self.tk.call(self._w, b'invoke')
        return


class DirSelectDialog(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixDirSelectDialog', [
         b'options'], cnf, kw)
        self.subwidget_list[b'dirbox'] = _dummyDirSelectBox(self, b'dirbox')
        return

    def popup(self):
        self.tk.call(self._w, b'popup')
        return

    def popdown(self):
        self.tk.call(self._w, b'popdown')
        return


class ExFileSelectDialog(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixExFileSelectDialog', [
         b'options'], cnf, kw)
        self.subwidget_list[b'fsbox'] = _dummyExFileSelectBox(self, b'fsbox')
        return

    def popup(self):
        self.tk.call(self._w, b'popup')
        return

    def popdown(self):
        self.tk.call(self._w, b'popdown')
        return


class FileSelectBox(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixFileSelectBox', [b'options'], cnf, kw)
        self.subwidget_list[b'dirlist'] = _dummyScrolledListBox(self, b'dirlist')
        self.subwidget_list[b'filelist'] = _dummyScrolledListBox(self, b'filelist')
        self.subwidget_list[b'filter'] = _dummyComboBox(self, b'filter')
        self.subwidget_list[b'selection'] = _dummyComboBox(self, b'selection')
        return

    def apply_filter(self):
        self.tk.call(self._w, b'filter')
        return

    def invoke(self):
        self.tk.call(self._w, b'invoke')
        return


class FileSelectDialog(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixFileSelectDialog', [
         b'options'], cnf, kw)
        self.subwidget_list[b'btns'] = _dummyStdButtonBox(self, b'btns')
        self.subwidget_list[b'fsbox'] = _dummyFileSelectBox(self, b'fsbox')
        return

    def popup(self):
        self.tk.call(self._w, b'popup')
        return

    def popdown(self):
        self.tk.call(self._w, b'popdown')
        return


class FileEntry(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixFileEntry', [
         b'dialogtype', b'options'], cnf, kw)
        self.subwidget_list[b'button'] = _dummyButton(self, b'button')
        self.subwidget_list[b'entry'] = _dummyEntry(self, b'entry')
        return

    def invoke(self):
        self.tk.call(self._w, b'invoke')
        return

    def file_dialog(self):
        return


class HList(TixWidget, XView, YView):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixHList', [
         b'columns', b'options'], cnf, kw)
        return

    def add(self, entry, cnf={}, **kw):
        return self.tk.call(self._w, b'add', entry, *self._options(cnf, kw))

    def add_child(self, parent=None, cnf={}, **kw):
        if not parent:
            parent = b''
        return self.tk.call(self._w, b'addchild', parent, *self._options(cnf, kw))

    def anchor_set(self, entry):
        self.tk.call(self._w, b'anchor', b'set', entry)
        return

    def anchor_clear(self):
        self.tk.call(self._w, b'anchor', b'clear')
        return

    def column_width(self, col=0, width=None, chars=None):
        if not chars:
            return self.tk.call(self._w, b'column', b'width', col, width)
        else:
            return self.tk.call(self._w, b'column', b'width', col, b'-char', chars)

        return

    def delete_all(self):
        self.tk.call(self._w, b'delete', b'all')
        return

    def delete_entry(self, entry):
        self.tk.call(self._w, b'delete', b'entry', entry)
        return

    def delete_offsprings(self, entry):
        self.tk.call(self._w, b'delete', b'offsprings', entry)
        return

    def delete_siblings(self, entry):
        self.tk.call(self._w, b'delete', b'siblings', entry)
        return

    def dragsite_set(self, index):
        self.tk.call(self._w, b'dragsite', b'set', index)
        return

    def dragsite_clear(self):
        self.tk.call(self._w, b'dragsite', b'clear')
        return

    def dropsite_set(self, index):
        self.tk.call(self._w, b'dropsite', b'set', index)
        return

    def dropsite_clear(self):
        self.tk.call(self._w, b'dropsite', b'clear')
        return

    def header_create(self, col, cnf={}, **kw):
        self.tk.call(self._w, b'header', b'create', col, *self._options(cnf, kw))
        return

    def header_configure(self, col, cnf={}, **kw):
        if cnf is None:
            return self._getconfigure(self._w, b'header', b'configure', col)
        else:
            self.tk.call(self._w, b'header', b'configure', col, *self._options(cnf, kw))
            return

    def header_cget(self, col, opt):
        return self.tk.call(self._w, b'header', b'cget', col, opt)

    def header_exists(self, col):
        return self.tk.getboolean(self.tk.call(self._w, b'header', b'exist', col))

    header_exist = header_exists

    def header_delete(self, col):
        self.tk.call(self._w, b'header', b'delete', col)
        return

    def header_size(self, col):
        return self.tk.call(self._w, b'header', b'size', col)

    def hide_entry(self, entry):
        self.tk.call(self._w, b'hide', b'entry', entry)
        return

    def indicator_create(self, entry, cnf={}, **kw):
        self.tk.call(self._w, b'indicator', b'create', entry, *self._options(cnf, kw))
        return

    def indicator_configure(self, entry, cnf={}, **kw):
        if cnf is None:
            return self._getconfigure(self._w, b'indicator', b'configure', entry)
        else:
            self.tk.call(self._w, b'indicator', b'configure', entry, *self._options(cnf, kw))
            return

    def indicator_cget(self, entry, opt):
        return self.tk.call(self._w, b'indicator', b'cget', entry, opt)

    def indicator_exists(self, entry):
        return self.tk.call(self._w, b'indicator', b'exists', entry)

    def indicator_delete(self, entry):
        self.tk.call(self._w, b'indicator', b'delete', entry)
        return

    def indicator_size(self, entry):
        return self.tk.call(self._w, b'indicator', b'size', entry)

    def info_anchor(self):
        return self.tk.call(self._w, b'info', b'anchor')

    def info_bbox(self, entry):
        return self._getints(self.tk.call(self._w, b'info', b'bbox', entry)) or None

    def info_children(self, entry=None):
        c = self.tk.call(self._w, b'info', b'children', entry)
        return self.tk.splitlist(c)

    def info_data(self, entry):
        return self.tk.call(self._w, b'info', b'data', entry)

    def info_dragsite(self):
        return self.tk.call(self._w, b'info', b'dragsite')

    def info_dropsite(self):
        return self.tk.call(self._w, b'info', b'dropsite')

    def info_exists(self, entry):
        return self.tk.call(self._w, b'info', b'exists', entry)

    def info_hidden(self, entry):
        return self.tk.call(self._w, b'info', b'hidden', entry)

    def info_next(self, entry):
        return self.tk.call(self._w, b'info', b'next', entry)

    def info_parent(self, entry):
        return self.tk.call(self._w, b'info', b'parent', entry)

    def info_prev(self, entry):
        return self.tk.call(self._w, b'info', b'prev', entry)

    def info_selection(self):
        c = self.tk.call(self._w, b'info', b'selection')
        return self.tk.splitlist(c)

    def item_cget(self, entry, col, opt):
        return self.tk.call(self._w, b'item', b'cget', entry, col, opt)

    def item_configure(self, entry, col, cnf={}, **kw):
        if cnf is None:
            return self._getconfigure(self._w, b'item', b'configure', entry, col)
        else:
            self.tk.call(self._w, b'item', b'configure', entry, col, *self._options(cnf, kw))
            return

    def item_create(self, entry, col, cnf={}, **kw):
        self.tk.call(self._w, b'item', b'create', entry, col, *self._options(cnf, kw))
        return

    def item_exists(self, entry, col):
        return self.tk.call(self._w, b'item', b'exists', entry, col)

    def item_delete(self, entry, col):
        self.tk.call(self._w, b'item', b'delete', entry, col)
        return

    def entrycget(self, entry, opt):
        return self.tk.call(self._w, b'entrycget', entry, opt)

    def entryconfigure(self, entry, cnf={}, **kw):
        if cnf is None:
            return self._getconfigure(self._w, b'entryconfigure', entry)
        else:
            self.tk.call(self._w, b'entryconfigure', entry, *self._options(cnf, kw))
            return

    def nearest(self, y):
        return self.tk.call(self._w, b'nearest', y)

    def see(self, entry):
        self.tk.call(self._w, b'see', entry)
        return

    def selection_clear(self, cnf={}, **kw):
        self.tk.call(self._w, b'selection', b'clear', *self._options(cnf, kw))
        return

    def selection_includes(self, entry):
        return self.tk.call(self._w, b'selection', b'includes', entry)

    def selection_set(self, first, last=None):
        self.tk.call(self._w, b'selection', b'set', first, last)
        return

    def show_entry(self, entry):
        return self.tk.call(self._w, b'show', b'entry', entry)


class InputOnly(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixInputOnly', None, cnf, kw)
        return


class LabelEntry(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixLabelEntry', [
         b'labelside', b'options'], cnf, kw)
        self.subwidget_list[b'label'] = _dummyLabel(self, b'label')
        self.subwidget_list[b'entry'] = _dummyEntry(self, b'entry')
        return


class LabelFrame(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixLabelFrame', [
         b'labelside', b'options'], cnf, kw)
        self.subwidget_list[b'label'] = _dummyLabel(self, b'label')
        self.subwidget_list[b'frame'] = _dummyFrame(self, b'frame')
        return


class ListNoteBook(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixListNoteBook', [b'options'], cnf, kw)
        self.subwidget_list[b'pane'] = _dummyPanedWindow(self, b'pane', destroy_physically=0)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'shlist'] = _dummyScrolledHList(self, b'shlist')
        return

    def add(self, name, cnf={}, **kw):
        self.tk.call(self._w, b'add', name, *self._options(cnf, kw))
        self.subwidget_list[name] = TixSubWidget(self, name)
        return self.subwidget_list[name]

    def page(self, name):
        return self.subwidget(name)

    def pages(self):
        names = self.tk.split(self.tk.call(self._w, b'pages'))
        ret = []
        for x in names:
            ret.append(self.subwidget(x))

        return ret

    def raise_page(self, name):
        self.tk.call(self._w, b'raise', name)
        return


class Meter(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixMeter', [
         b'options'], cnf, kw)
        return


class NoteBook(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixNoteBook', [b'options'], cnf, kw)
        self.subwidget_list[b'nbframe'] = TixSubWidget(self, b'nbframe', destroy_physically=0)
        return

    def add(self, name, cnf={}, **kw):
        self.tk.call(self._w, b'add', name, *self._options(cnf, kw))
        self.subwidget_list[name] = TixSubWidget(self, name)
        return self.subwidget_list[name]

    def delete(self, name):
        self.tk.call(self._w, b'delete', name)
        self.subwidget_list[name].destroy()
        del self.subwidget_list[name]
        return

    def page(self, name):
        return self.subwidget(name)

    def pages(self):
        names = self.tk.split(self.tk.call(self._w, b'pages'))
        ret = []
        for x in names:
            ret.append(self.subwidget(x))

        return ret

    def raise_page(self, name):
        self.tk.call(self._w, b'raise', name)
        return

    def raised(self):
        return self.tk.call(self._w, b'raised')


class NoteBookFrame(TixWidget):
    pass


class OptionMenu(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixOptionMenu', [
         b'labelside', b'options'], cnf, kw)
        self.subwidget_list[b'menubutton'] = _dummyMenubutton(self, b'menubutton')
        self.subwidget_list[b'menu'] = _dummyMenu(self, b'menu')
        return

    def add_command(self, name, cnf={}, **kw):
        self.tk.call(self._w, b'add', b'command', name, *self._options(cnf, kw))
        return

    def add_separator(self, name, cnf={}, **kw):
        self.tk.call(self._w, b'add', b'separator', name, *self._options(cnf, kw))
        return

    def delete(self, name):
        self.tk.call(self._w, b'delete', name)
        return

    def disable(self, name):
        self.tk.call(self._w, b'disable', name)
        return

    def enable(self, name):
        self.tk.call(self._w, b'enable', name)
        return


class PanedWindow(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixPanedWindow', [b'orientation', b'options'], cnf, kw)
        return

    def add(self, name, cnf={}, **kw):
        self.tk.call(self._w, b'add', name, *self._options(cnf, kw))
        self.subwidget_list[name] = TixSubWidget(self, name, check_intermediate=0)
        return self.subwidget_list[name]

    def delete(self, name):
        self.tk.call(self._w, b'delete', name)
        self.subwidget_list[name].destroy()
        del self.subwidget_list[name]
        return

    def forget(self, name):
        self.tk.call(self._w, b'forget', name)
        return

    def panecget(self, entry, opt):
        return self.tk.call(self._w, b'panecget', entry, opt)

    def paneconfigure(self, entry, cnf={}, **kw):
        if cnf is None:
            return self._getconfigure(self._w, b'paneconfigure', entry)
        else:
            self.tk.call(self._w, b'paneconfigure', entry, *self._options(cnf, kw))
            return

    def panes(self):
        names = self.tk.splitlist(self.tk.call(self._w, b'panes'))
        return [self.subwidget(x) for x in names]


class PopupMenu(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixPopupMenu', [b'options'], cnf, kw)
        self.subwidget_list[b'menubutton'] = _dummyMenubutton(self, b'menubutton')
        self.subwidget_list[b'menu'] = _dummyMenu(self, b'menu')
        return

    def bind_widget(self, widget):
        self.tk.call(self._w, b'bind', widget._w)
        return

    def unbind_widget(self, widget):
        self.tk.call(self._w, b'unbind', widget._w)
        return

    def post_widget(self, widget, x, y):
        self.tk.call(self._w, b'post', widget._w, x, y)
        return


class ResizeHandle(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        flags = [
         1, 2, 3, 4, 
         5, 6, 7, 
         8, 
         9]
        TixWidget.__init__(self, master, b'tixResizeHandle', flags, cnf, kw)
        return

    def attach_widget(self, widget):
        self.tk.call(self._w, b'attachwidget', widget._w)
        return

    def detach_widget(self, widget):
        self.tk.call(self._w, b'detachwidget', widget._w)
        return

    def hide(self, widget):
        self.tk.call(self._w, b'hide', widget._w)
        return

    def show(self, widget):
        self.tk.call(self._w, b'show', widget._w)
        return


class ScrolledHList(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixScrolledHList', [b'options'], cnf, kw)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class ScrolledListBox(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixScrolledListBox', [b'options'], cnf, kw)
        self.subwidget_list[b'listbox'] = _dummyListbox(self, b'listbox')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class ScrolledText(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixScrolledText', [b'options'], cnf, kw)
        self.subwidget_list[b'text'] = _dummyText(self, b'text')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class ScrolledTList(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixScrolledTList', [b'options'], cnf, kw)
        self.subwidget_list[b'tlist'] = _dummyTList(self, b'tlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class ScrolledWindow(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixScrolledWindow', [b'options'], cnf, kw)
        self.subwidget_list[b'window'] = _dummyFrame(self, b'window')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class Select(TixWidget):

    def __init__(self, master, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixSelect', [
         2, 3, 4, 5, 
         6], cnf, kw)
        self.subwidget_list[b'label'] = _dummyLabel(self, b'label')
        return

    def add(self, name, cnf={}, **kw):
        self.tk.call(self._w, b'add', name, *self._options(cnf, kw))
        self.subwidget_list[name] = _dummyButton(self, name)
        return self.subwidget_list[name]

    def invoke(self, name):
        self.tk.call(self._w, b'invoke', name)
        return


class Shell(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixShell', [b'options', b'title'], cnf, kw)
        return


class DialogShell(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixDialogShell', [
         2, 3, 4, 
         5, 6, 
         7, 
         8], cnf, kw)
        return

    def popdown(self):
        self.tk.call(self._w, b'popdown')
        return

    def popup(self):
        self.tk.call(self._w, b'popup')
        return

    def center(self):
        self.tk.call(self._w, b'center')
        return


class StdButtonBox(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixStdButtonBox', [
         b'orientation', b'options'], cnf, kw)
        self.subwidget_list[b'ok'] = _dummyButton(self, b'ok')
        self.subwidget_list[b'apply'] = _dummyButton(self, b'apply')
        self.subwidget_list[b'cancel'] = _dummyButton(self, b'cancel')
        self.subwidget_list[b'help'] = _dummyButton(self, b'help')
        return

    def invoke(self, name):
        if name in self.subwidget_list:
            self.tk.call(self._w, b'invoke', name)
        return


class TList(TixWidget, XView, YView):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixTList', [b'options'], cnf, kw)
        return

    def active_set(self, index):
        self.tk.call(self._w, b'active', b'set', index)
        return

    def active_clear(self):
        self.tk.call(self._w, b'active', b'clear')
        return

    def anchor_set(self, index):
        self.tk.call(self._w, b'anchor', b'set', index)
        return

    def anchor_clear(self):
        self.tk.call(self._w, b'anchor', b'clear')
        return

    def delete(self, from_, to=None):
        self.tk.call(self._w, b'delete', from_, to)
        return

    def dragsite_set(self, index):
        self.tk.call(self._w, b'dragsite', b'set', index)
        return

    def dragsite_clear(self):
        self.tk.call(self._w, b'dragsite', b'clear')
        return

    def dropsite_set(self, index):
        self.tk.call(self._w, b'dropsite', b'set', index)
        return

    def dropsite_clear(self):
        self.tk.call(self._w, b'dropsite', b'clear')
        return

    def insert(self, index, cnf={}, **kw):
        self.tk.call(self._w, b'insert', index, *self._options(cnf, kw))
        return

    def info_active(self):
        return self.tk.call(self._w, b'info', b'active')

    def info_anchor(self):
        return self.tk.call(self._w, b'info', b'anchor')

    def info_down(self, index):
        return self.tk.call(self._w, b'info', b'down', index)

    def info_left(self, index):
        return self.tk.call(self._w, b'info', b'left', index)

    def info_right(self, index):
        return self.tk.call(self._w, b'info', b'right', index)

    def info_selection(self):
        c = self.tk.call(self._w, b'info', b'selection')
        return self.tk.splitlist(c)

    def info_size(self):
        return self.tk.call(self._w, b'info', b'size')

    def info_up(self, index):
        return self.tk.call(self._w, b'info', b'up', index)

    def nearest(self, x, y):
        return self.tk.call(self._w, b'nearest', x, y)

    def see(self, index):
        self.tk.call(self._w, b'see', index)
        return

    def selection_clear(self, cnf={}, **kw):
        self.tk.call(self._w, b'selection', b'clear', *self._options(cnf, kw))
        return

    def selection_includes(self, index):
        return self.tk.call(self._w, b'selection', b'includes', index)

    def selection_set(self, first, last=None):
        self.tk.call(self._w, b'selection', b'set', first, last)
        return


class Tree(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixTree', [
         b'options'], cnf, kw)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return

    def autosetmode(self):
        self.tk.call(self._w, b'autosetmode')
        return

    def close(self, entrypath):
        self.tk.call(self._w, b'close', entrypath)
        return

    def getmode(self, entrypath):
        return self.tk.call(self._w, b'getmode', entrypath)

    def open(self, entrypath):
        self.tk.call(self._w, b'open', entrypath)
        return

    def setmode(self, entrypath, mode=b'none'):
        self.tk.call(self._w, b'setmode', entrypath, mode)
        return


class CheckList(TixWidget):

    def __init__(self, master=None, cnf={}, **kw):
        TixWidget.__init__(self, master, b'tixCheckList', [
         b'options', b'radio'], cnf, kw)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return

    def autosetmode(self):
        self.tk.call(self._w, b'autosetmode')
        return

    def close(self, entrypath):
        self.tk.call(self._w, b'close', entrypath)
        return

    def getmode(self, entrypath):
        return self.tk.call(self._w, b'getmode', entrypath)

    def open(self, entrypath):
        self.tk.call(self._w, b'open', entrypath)
        return

    def getselection(self, mode=b'on'):
        c = self.tk.split(self.tk.call(self._w, b'getselection', mode))
        return self.tk.splitlist(c)

    def getstatus(self, entrypath):
        return self.tk.call(self._w, b'getstatus', entrypath)

    def setstatus(self, entrypath, mode=b'on'):
        self.tk.call(self._w, b'setstatus', entrypath, mode)
        return


class _dummyButton(Button, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyCheckbutton(Checkbutton, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyEntry(Entry, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyFrame(Frame, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyLabel(Label, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyListbox(Listbox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyMenu(Menu, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyMenubutton(Menubutton, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyScrollbar(Scrollbar, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyText(Text, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyScrolledListBox(ScrolledListBox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'listbox'] = _dummyListbox(self, b'listbox')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class _dummyHList(HList, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyScrolledHList(ScrolledHList, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class _dummyTList(TList, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyComboBox(ComboBox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, [b'fancy', destroy_physically])
        self.subwidget_list[b'label'] = _dummyLabel(self, b'label')
        self.subwidget_list[b'entry'] = _dummyEntry(self, b'entry')
        self.subwidget_list[b'arrow'] = _dummyButton(self, b'arrow')
        self.subwidget_list[b'slistbox'] = _dummyScrolledListBox(self, b'slistbox')
        try:
            self.subwidget_list[b'tick'] = _dummyButton(self, b'tick')
            self.subwidget_list[b'cross'] = _dummyButton(self, b'cross')
        except TypeError:
            pass

        return


class _dummyDirList(DirList, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'hlist'] = _dummyHList(self, b'hlist')
        self.subwidget_list[b'vsb'] = _dummyScrollbar(self, b'vsb')
        self.subwidget_list[b'hsb'] = _dummyScrollbar(self, b'hsb')
        return


class _dummyDirSelectBox(DirSelectBox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'dirlist'] = _dummyDirList(self, b'dirlist')
        self.subwidget_list[b'dircbx'] = _dummyFileComboBox(self, b'dircbx')
        return


class _dummyExFileSelectBox(ExFileSelectBox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'cancel'] = _dummyButton(self, b'cancel')
        self.subwidget_list[b'ok'] = _dummyButton(self, b'ok')
        self.subwidget_list[b'hidden'] = _dummyCheckbutton(self, b'hidden')
        self.subwidget_list[b'types'] = _dummyComboBox(self, b'types')
        self.subwidget_list[b'dir'] = _dummyComboBox(self, b'dir')
        self.subwidget_list[b'dirlist'] = _dummyScrolledListBox(self, b'dirlist')
        self.subwidget_list[b'file'] = _dummyComboBox(self, b'file')
        self.subwidget_list[b'filelist'] = _dummyScrolledListBox(self, b'filelist')
        return


class _dummyFileSelectBox(FileSelectBox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'dirlist'] = _dummyScrolledListBox(self, b'dirlist')
        self.subwidget_list[b'filelist'] = _dummyScrolledListBox(self, b'filelist')
        self.subwidget_list[b'filter'] = _dummyComboBox(self, b'filter')
        self.subwidget_list[b'selection'] = _dummyComboBox(self, b'selection')
        return


class _dummyFileComboBox(ComboBox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'dircbx'] = _dummyComboBox(self, b'dircbx')
        return


class _dummyStdButtonBox(StdButtonBox, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        self.subwidget_list[b'ok'] = _dummyButton(self, b'ok')
        self.subwidget_list[b'apply'] = _dummyButton(self, b'apply')
        self.subwidget_list[b'cancel'] = _dummyButton(self, b'cancel')
        self.subwidget_list[b'help'] = _dummyButton(self, b'help')
        return


class _dummyNoteBookFrame(NoteBookFrame, TixSubWidget):

    def __init__(self, master, name, destroy_physically=0):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


class _dummyPanedWindow(PanedWindow, TixSubWidget):

    def __init__(self, master, name, destroy_physically=1):
        TixSubWidget.__init__(self, master, name, destroy_physically)
        return


def OptionName(widget):
    return widget.tk.call(b'tixOptionName', widget._w)


def FileTypeList(dict):
    s = b''
    for type in dict.keys():
        s = s + b'{{' + type + b'} {' + type + b' - ' + dict[type] + b'}} '

    return s


class CObjView(TixWidget):
    pass


class Grid(TixWidget, XView, YView):

    def __init__(self, master=None, cnf={}, **kw):
        static = []
        self.cnf = cnf
        TixWidget.__init__(self, master, b'tixGrid', static, cnf, kw)
        return

    def anchor_clear(self):
        self.tk.call(self, b'anchor', b'clear')
        return

    def anchor_get(self):
        return self._getints(self.tk.call(self, b'anchor', b'get'))

    def anchor_set(self, x, y):
        self.tk.call(self, b'anchor', b'set', x, y)
        return

    def delete_row(self, from_, to=None):
        if to is None:
            self.tk.call(self, b'delete', b'row', from_)
        else:
            self.tk.call(self, b'delete', b'row', from_, to)
        return

    def delete_column(self, from_, to=None):
        if to is None:
            self.tk.call(self, b'delete', b'column', from_)
        else:
            self.tk.call(self, b'delete', b'column', from_, to)
        return

    def edit_apply(self):
        self.tk.call(self, b'edit', b'apply')
        return

    def edit_set(self, x, y):
        self.tk.call(self, b'edit', b'set', x, y)
        return

    def entrycget(self, x, y, option):
        if option and option[0] != b'-':
            option = b'-' + option
        return self.tk.call(self, b'entrycget', x, y, option)

    def entryconfigure(self, x, y, cnf=None, **kw):
        return self._configure((b'entryconfigure', x, y), cnf, kw)

    def info_exists(self, x, y):
        return self._getboolean(self.tk.call(self, b'info', b'exists', x, y))

    def info_bbox(self, x, y):
        return self.tk.call(self, b'info', b'bbox', x, y)

    def move_column(self, from_, to, offset):
        self.tk.call(self, b'move', b'column', from_, to, offset)
        return

    def move_row(self, from_, to, offset):
        self.tk.call(self, b'move', b'row', from_, to, offset)
        return

    def nearest(self, x, y):
        return self._getints(self.tk.call(self, b'nearest', x, y))

    def set(self, x, y, itemtype=None, **kw):
        args = self._options(self.cnf, kw)
        if itemtype is not None:
            args = (
             b'-itemtype', itemtype) + args
        self.tk.call(self, b'set', x, y, *args)
        return

    def size_column(self, index, **kw):
        return self.tk.split(self.tk.call(self._w, b'size', b'column', index, *self._options({}, kw)))

    def size_row(self, index, **kw):
        return self.tk.split(self.tk.call(self, b'size', b'row', index, *self._options({}, kw)))

    def unset(self, x, y):
        self.tk.call(self._w, b'unset', x, y)
        return


class ScrolledGrid(Grid):

    def __init__(self, master=None, cnf={}, **kw):
        static = []
        self.cnf = cnf
        TixWidget.__init__(self, master, b'tixScrolledGrid', static, cnf, kw)
        return
