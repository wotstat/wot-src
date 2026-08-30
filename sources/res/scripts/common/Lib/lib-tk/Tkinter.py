__version__ = b'$Revision: 81008 $'
import sys
if sys.platform == b'win32':
    import FixTk
import _tkinter
tkinter = _tkinter
TclError = _tkinter.TclError
from types import *
from Tkconstants import *
import re
wantobjects = 1
TkVersion = float(_tkinter.TK_VERSION)
TclVersion = float(_tkinter.TCL_VERSION)
READABLE = _tkinter.READABLE
WRITABLE = _tkinter.WRITABLE
EXCEPTION = _tkinter.EXCEPTION
try:
    _tkinter.createfilehandler
except AttributeError:
    _tkinter.createfilehandler = None

try:
    _tkinter.deletefilehandler
except AttributeError:
    _tkinter.deletefilehandler = None

_magic_re = re.compile(b'([\\\\{}])')
_space_re = re.compile(b'([\\s])')

def _join(value):
    return (b' ').join(map(_stringify, value))


def _stringify(value):
    if isinstance(value, (list, tuple)):
        if len(value) == 1:
            value = _stringify(value[0])
            if _magic_re.search(value):
                value = b'{%s}' % value
        else:
            value = b'{%s}' % _join(value)
    else:
        if isinstance(value, str):
            value = unicode(value, b'utf-8')
        elif not isinstance(value, unicode):
            value = str(value)
        if not value:
            value = b'{}'
        elif _magic_re.search(value):
            value = _magic_re.sub(b'\\\\\\1', value)
            value = value.replace(b'\n', b'\\n')
            value = _space_re.sub(b'\\\\\\1', value)
            if value[0] == b'"':
                value = b'\\' + value
        elif value[0] == b'"' or _space_re.search(value):
            value = b'{%s}' % value
    return value


def _flatten(tuple):
    res = ()
    for item in tuple:
        if type(item) in (TupleType, ListType):
            res = res + _flatten(item)
        elif item is not None:
            res = res + (item,)

    return res


try:
    _flatten = _tkinter._flatten
except AttributeError:
    pass

def _cnfmerge(cnfs):
    if type(cnfs) is DictionaryType:
        return cnfs
    else:
        if type(cnfs) in (NoneType, StringType):
            return cnfs
        cnf = {}
        for c in _flatten(cnfs):
            try:
                cnf.update(c)
            except (AttributeError, TypeError) as msg:
                print b'_cnfmerge: fallback due to:', msg
                for k, v in c.items():
                    cnf[k] = v

        return cnf

    return


try:
    _cnfmerge = _tkinter._cnfmerge
except AttributeError:
    pass

def _splitdict(tk, v, cut_minus=True, conv=None):
    t = tk.splitlist(v)
    if len(t) % 2:
        raise RuntimeError(b'Tcl list representing a dict is expected to contain an even number of elements')
    it = iter(t)
    dict = {}
    for key, value in zip(it, it):
        key = str(key)
        if cut_minus and key[0] == b'-':
            key = key[1:]
        if conv:
            value = conv(value)
        dict[key] = value

    return dict


class Event():
    pass


_support_default_root = 1
_default_root = None

def NoDefaultRoot():
    global _default_root
    global _support_default_root
    _support_default_root = 0
    _default_root = None
    del _default_root
    return


def _tkerror(err):
    return


def _exit(code=0):
    try:
        code = int(code)
    except ValueError:
        pass

    raise SystemExit, code
    return


_varnum = 0

class Variable():
    _default = b''
    _tclCommands = None

    def __init__(self, master=None, value=None, name=None):
        global _varnum
        if not master:
            master = _default_root
        self._root = master._root()
        self._tk = master.tk
        if name:
            self._name = name
        else:
            self._name = b'PY_VAR' + repr(_varnum)
            _varnum += 1
        if value is not None:
            self.set(value)
        elif not self._tk.getboolean(self._tk.call(b'info', b'exists', self._name)):
            self.set(self._default)
        return

    def __del__(self):
        if self._tk is None:
            return
        else:
            if self._tk.getboolean(self._tk.call(b'info', b'exists', self._name)):
                self._tk.globalunsetvar(self._name)
            if self._tclCommands is not None:
                for name in self._tclCommands:
                    self._tk.deletecommand(name)

                self._tclCommands = None
            return

    def __str__(self):
        return self._name

    def set(self, value):
        return self._tk.globalsetvar(self._name, value)

    def get(self):
        return self._tk.globalgetvar(self._name)

    def trace_variable(self, mode, callback):
        f = CallWrapper(callback, None, self._root).__call__
        cbname = repr(id(f))
        try:
            callback = callback.im_func
        except AttributeError:
            pass

        try:
            cbname = cbname + callback.__name__
        except AttributeError:
            pass

        self._tk.createcommand(cbname, f)
        if self._tclCommands is None:
            self._tclCommands = []
        self._tclCommands.append(cbname)
        self._tk.call(b'trace', b'variable', self._name, mode, cbname)
        return cbname

    trace = trace_variable

    def trace_vdelete(self, mode, cbname):
        self._tk.call(b'trace', b'vdelete', self._name, mode, cbname)
        cbname = self._tk.splitlist(cbname)[0]
        for m, ca in self.trace_vinfo():
            if self._tk.splitlist(ca)[0] == cbname:
                break
        else:
            self._tk.deletecommand(cbname)
            try:
                self._tclCommands.remove(cbname)
            except ValueError:
                pass

        return

    def trace_vinfo(self):
        return map(self._tk.splitlist, self._tk.splitlist(self._tk.call(b'trace', b'vinfo', self._name)))

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__ and self._name == other._name


class StringVar(Variable):
    _default = b''

    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)
        return

    def get(self):
        value = self._tk.globalgetvar(self._name)
        if isinstance(value, basestring):
            return value
        return str(value)


class IntVar(Variable):
    _default = 0

    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)
        return

    def set(self, value):
        if isinstance(value, bool):
            value = int(value)
        return Variable.set(self, value)

    def get(self):
        return getint(self._tk.globalgetvar(self._name))


class DoubleVar(Variable):
    _default = 0.0

    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)
        return

    def get(self):
        return getdouble(self._tk.globalgetvar(self._name))


class BooleanVar(Variable):
    _default = False

    def __init__(self, master=None, value=None, name=None):
        Variable.__init__(self, master, value, name)
        return

    def set(self, value):
        return self._tk.globalsetvar(self._name, self._tk.getboolean(value))

    def get(self):
        return self._tk.getboolean(self._tk.globalgetvar(self._name))


def mainloop(n=0):
    _default_root.tk.mainloop(n)
    return


getint = int
getdouble = float

def getboolean(s):
    return _default_root.tk.getboolean(s)


class Misc():
    _tclCommands = None

    def destroy(self):
        if self._tclCommands is not None:
            for name in self._tclCommands:
                self.tk.deletecommand(name)

            self._tclCommands = None
        return

    def deletecommand(self, name):
        self.tk.deletecommand(name)
        try:
            self._tclCommands.remove(name)
        except ValueError:
            pass

        return

    def tk_strictMotif(self, boolean=None):
        return self.tk.getboolean(self.tk.call(b'set', b'tk_strictMotif', boolean))

    def tk_bisque(self):
        self.tk.call(b'tk_bisque')
        return

    def tk_setPalette(self, *args, **kw):
        self.tk.call((b'tk_setPalette',) + _flatten(args) + _flatten(kw.items()))
        return

    def tk_menuBar(self, *args):
        import warnings
        warnings.warn(b'tk_menuBar() does nothing and will be removed in 3.6', DeprecationWarning, stacklevel=2)
        return

    def wait_variable(self, name=b'PY_VAR'):
        self.tk.call(b'tkwait', b'variable', name)
        return

    waitvar = wait_variable

    def wait_window(self, window=None):
        if window is None:
            window = self
        self.tk.call(b'tkwait', b'window', window._w)
        return

    def wait_visibility(self, window=None):
        if window is None:
            window = self
        self.tk.call(b'tkwait', b'visibility', window._w)
        return

    def setvar(self, name=b'PY_VAR', value=b'1'):
        self.tk.setvar(name, value)
        return

    def getvar(self, name=b'PY_VAR'):
        return self.tk.getvar(name)

    getint = int
    getdouble = float

    def getboolean(self, s):
        return self.tk.getboolean(s)

    def focus_set(self):
        self.tk.call(b'focus', self._w)
        return

    focus = focus_set

    def focus_force(self):
        self.tk.call(b'focus', b'-force', self._w)
        return

    def focus_get(self):
        name = self.tk.call(b'focus')
        if name == b'none' or not name:
            return None
        return self._nametowidget(name)

    def focus_displayof(self):
        name = self.tk.call(b'focus', b'-displayof', self._w)
        if name == b'none' or not name:
            return None
        return self._nametowidget(name)

    def focus_lastfor(self):
        name = self.tk.call(b'focus', b'-lastfor', self._w)
        if name == b'none' or not name:
            return None
        return self._nametowidget(name)

    def tk_focusFollowsMouse(self):
        self.tk.call(b'tk_focusFollowsMouse')
        return

    def tk_focusNext(self):
        name = self.tk.call(b'tk_focusNext', self._w)
        if not name:
            return None
        else:
            return self._nametowidget(name)

    def tk_focusPrev(self):
        name = self.tk.call(b'tk_focusPrev', self._w)
        if not name:
            return None
        else:
            return self._nametowidget(name)

    def after(self, ms, func=None, *args):
        if not func:
            self.tk.call(b'after', ms)
            return
        else:

            def callit():
                try:
                    func(*args)
                finally:
                    try:
                        self.deletecommand(name)
                    except TclError:
                        pass

                return

            callit.__name__ = func.__name__
            name = self._register(callit)
            return self.tk.call(b'after', ms, name)
            return

    def after_idle(self, func, *args):
        return self.after(b'idle', func, *args)

    def after_cancel(self, id):
        if not id:
            raise ValueError(b'id must be a valid identifier returned from after or after_idle')
        try:
            data = self.tk.call(b'after', b'info', id)
            script = self.tk.splitlist(data)[0]
            self.deletecommand(script)
        except TclError:
            pass

        self.tk.call(b'after', b'cancel', id)
        return

    def bell(self, displayof=0):
        self.tk.call((b'bell',) + self._displayof(displayof))
        return

    def clipboard_get(self, **kw):
        if b'type' not in kw and self._windowingsystem == b'x11':
            try:
                kw[b'type'] = b'UTF8_STRING'
                return self.tk.call((b'clipboard', b'get') + self._options(kw))
            except TclError:
                del kw[b'type']

        return self.tk.call((b'clipboard', b'get') + self._options(kw))

    def clipboard_clear(self, **kw):
        if b'displayof' not in kw:
            kw[b'displayof'] = self._w
        self.tk.call((b'clipboard', b'clear') + self._options(kw))
        return

    def clipboard_append(self, string, **kw):
        if b'displayof' not in kw:
            kw[b'displayof'] = self._w
        self.tk.call((b'clipboard', b'append') + self._options(kw) + (b'--', string))
        return

    def grab_current(self):
        name = self.tk.call(b'grab', b'current', self._w)
        if not name:
            return None
        else:
            return self._nametowidget(name)

    def grab_release(self):
        self.tk.call(b'grab', b'release', self._w)
        return

    def grab_set(self):
        self.tk.call(b'grab', b'set', self._w)
        return

    def grab_set_global(self):
        self.tk.call(b'grab', b'set', b'-global', self._w)
        return

    def grab_status(self):
        status = self.tk.call(b'grab', b'status', self._w)
        if status == b'none':
            status = None
        return status

    def option_add(self, pattern, value, priority=None):
        self.tk.call(b'option', b'add', pattern, value, priority)
        return

    def option_clear(self):
        self.tk.call(b'option', b'clear')
        return

    def option_get(self, name, className):
        return self.tk.call(b'option', b'get', self._w, name, className)

    def option_readfile(self, fileName, priority=None):
        self.tk.call(b'option', b'readfile', fileName, priority)
        return

    def selection_clear(self, **kw):
        if b'displayof' not in kw:
            kw[b'displayof'] = self._w
        self.tk.call((b'selection', b'clear') + self._options(kw))
        return

    def selection_get(self, **kw):
        if b'displayof' not in kw:
            kw[b'displayof'] = self._w
        if b'type' not in kw and self._windowingsystem == b'x11':
            try:
                kw[b'type'] = b'UTF8_STRING'
                return self.tk.call((b'selection', b'get') + self._options(kw))
            except TclError:
                del kw[b'type']

        return self.tk.call((b'selection', b'get') + self._options(kw))

    def selection_handle(self, command, **kw):
        name = self._register(command)
        self.tk.call((b'selection', b'handle') + self._options(kw) + (self._w, name))
        return

    def selection_own(self, **kw):
        self.tk.call((b'selection', b'own') + self._options(kw) + (self._w,))
        return

    def selection_own_get(self, **kw):
        if b'displayof' not in kw:
            kw[b'displayof'] = self._w
        name = self.tk.call((b'selection', b'own') + self._options(kw))
        if not name:
            return None
        else:
            return self._nametowidget(name)

    def send(self, interp, cmd, *args):
        return self.tk.call((b'send', interp, cmd) + args)

    def lower(self, belowThis=None):
        self.tk.call(b'lower', self._w, belowThis)
        return

    def tkraise(self, aboveThis=None):
        self.tk.call(b'raise', self._w, aboveThis)
        return

    lift = tkraise

    def colormodel(self, value=None):
        return self.tk.call(b'tk', b'colormodel', self._w, value)

    def winfo_atom(self, name, displayof=0):
        args = (b'winfo', b'atom') + self._displayof(displayof) + (name,)
        return getint(self.tk.call(args))

    def winfo_atomname(self, id, displayof=0):
        args = (b'winfo', b'atomname') + self._displayof(displayof) + (id,)
        return self.tk.call(args)

    def winfo_cells(self):
        return getint(self.tk.call(b'winfo', b'cells', self._w))

    def winfo_children(self):
        result = []
        for child in self.tk.splitlist(self.tk.call(b'winfo', b'children', self._w)):
            try:
                result.append(self._nametowidget(child))
            except KeyError:
                pass

        return result

    def winfo_class(self):
        return self.tk.call(b'winfo', b'class', self._w)

    def winfo_colormapfull(self):
        return self.tk.getboolean(self.tk.call(b'winfo', b'colormapfull', self._w))

    def winfo_containing(self, rootX, rootY, displayof=0):
        args = (b'winfo', b'containing') + self._displayof(displayof) + (rootX, rootY)
        name = self.tk.call(args)
        if not name:
            return None
        else:
            return self._nametowidget(name)

    def winfo_depth(self):
        return getint(self.tk.call(b'winfo', b'depth', self._w))

    def winfo_exists(self):
        return getint(self.tk.call(b'winfo', b'exists', self._w))

    def winfo_fpixels(self, number):
        return getdouble(self.tk.call(b'winfo', b'fpixels', self._w, number))

    def winfo_geometry(self):
        return self.tk.call(b'winfo', b'geometry', self._w)

    def winfo_height(self):
        return getint(self.tk.call(b'winfo', b'height', self._w))

    def winfo_id(self):
        return int(self.tk.call(b'winfo', b'id', self._w), 0)

    def winfo_interps(self, displayof=0):
        args = (b'winfo', b'interps') + self._displayof(displayof)
        return self.tk.splitlist(self.tk.call(args))

    def winfo_ismapped(self):
        return getint(self.tk.call(b'winfo', b'ismapped', self._w))

    def winfo_manager(self):
        return self.tk.call(b'winfo', b'manager', self._w)

    def winfo_name(self):
        return self.tk.call(b'winfo', b'name', self._w)

    def winfo_parent(self):
        return self.tk.call(b'winfo', b'parent', self._w)

    def winfo_pathname(self, id, displayof=0):
        args = (b'winfo', b'pathname') + self._displayof(displayof) + (id,)
        return self.tk.call(args)

    def winfo_pixels(self, number):
        return getint(self.tk.call(b'winfo', b'pixels', self._w, number))

    def winfo_pointerx(self):
        return getint(self.tk.call(b'winfo', b'pointerx', self._w))

    def winfo_pointerxy(self):
        return self._getints(self.tk.call(b'winfo', b'pointerxy', self._w))

    def winfo_pointery(self):
        return getint(self.tk.call(b'winfo', b'pointery', self._w))

    def winfo_reqheight(self):
        return getint(self.tk.call(b'winfo', b'reqheight', self._w))

    def winfo_reqwidth(self):
        return getint(self.tk.call(b'winfo', b'reqwidth', self._w))

    def winfo_rgb(self, color):
        return self._getints(self.tk.call(b'winfo', b'rgb', self._w, color))

    def winfo_rootx(self):
        return getint(self.tk.call(b'winfo', b'rootx', self._w))

    def winfo_rooty(self):
        return getint(self.tk.call(b'winfo', b'rooty', self._w))

    def winfo_screen(self):
        return self.tk.call(b'winfo', b'screen', self._w)

    def winfo_screencells(self):
        return getint(self.tk.call(b'winfo', b'screencells', self._w))

    def winfo_screendepth(self):
        return getint(self.tk.call(b'winfo', b'screendepth', self._w))

    def winfo_screenheight(self):
        return getint(self.tk.call(b'winfo', b'screenheight', self._w))

    def winfo_screenmmheight(self):
        return getint(self.tk.call(b'winfo', b'screenmmheight', self._w))

    def winfo_screenmmwidth(self):
        return getint(self.tk.call(b'winfo', b'screenmmwidth', self._w))

    def winfo_screenvisual(self):
        return self.tk.call(b'winfo', b'screenvisual', self._w)

    def winfo_screenwidth(self):
        return getint(self.tk.call(b'winfo', b'screenwidth', self._w))

    def winfo_server(self):
        return self.tk.call(b'winfo', b'server', self._w)

    def winfo_toplevel(self):
        return self._nametowidget(self.tk.call(b'winfo', b'toplevel', self._w))

    def winfo_viewable(self):
        return getint(self.tk.call(b'winfo', b'viewable', self._w))

    def winfo_visual(self):
        return self.tk.call(b'winfo', b'visual', self._w)

    def winfo_visualid(self):
        return self.tk.call(b'winfo', b'visualid', self._w)

    def winfo_visualsavailable(self, includeids=0):
        data = self.tk.split(self.tk.call(b'winfo', b'visualsavailable', self._w, includeids and b'includeids' or None))
        if type(data) is StringType:
            data = [
             self.tk.split(data)]
        return map(self.__winfo_parseitem, data)

    def __winfo_parseitem(self, t):
        return t[:1] + tuple(map(self.__winfo_getint, t[1:]))

    def __winfo_getint(self, x):
        return int(x, 0)

    def winfo_vrootheight(self):
        return getint(self.tk.call(b'winfo', b'vrootheight', self._w))

    def winfo_vrootwidth(self):
        return getint(self.tk.call(b'winfo', b'vrootwidth', self._w))

    def winfo_vrootx(self):
        return getint(self.tk.call(b'winfo', b'vrootx', self._w))

    def winfo_vrooty(self):
        return getint(self.tk.call(b'winfo', b'vrooty', self._w))

    def winfo_width(self):
        return getint(self.tk.call(b'winfo', b'width', self._w))

    def winfo_x(self):
        return getint(self.tk.call(b'winfo', b'x', self._w))

    def winfo_y(self):
        return getint(self.tk.call(b'winfo', b'y', self._w))

    def update(self):
        self.tk.call(b'update')
        return

    def update_idletasks(self):
        self.tk.call(b'update', b'idletasks')
        return

    def bindtags(self, tagList=None):
        if tagList is None:
            return self.tk.splitlist(self.tk.call(b'bindtags', self._w))
        else:
            self.tk.call(b'bindtags', self._w, tagList)
            return

    def _bind(self, what, sequence, func, add, needcleanup=1):
        if type(func) is StringType:
            self.tk.call(what + (sequence, func))
        else:
            if func:
                funcid = self._register(func, self._substitute, needcleanup)
                cmd = b'%sif {"[%s %s]" == "break"} break\n' % (
                 add and b'+' or b'',
                 funcid, self._subst_format_str)
                self.tk.call(what + (sequence, cmd))
                return funcid
            else:
                if sequence:
                    return self.tk.call(what + (sequence,))
                return self.tk.splitlist(self.tk.call(what))

        return

    def bind(self, sequence=None, func=None, add=None):
        return self._bind((b'bind', self._w), sequence, func, add)

    def unbind(self, sequence, funcid=None):
        self.tk.call(b'bind', self._w, sequence, b'')
        if funcid:
            self.deletecommand(funcid)
        return

    def bind_all(self, sequence=None, func=None, add=None):
        return self._bind((b'bind', b'all'), sequence, func, add, 0)

    def unbind_all(self, sequence):
        self.tk.call(b'bind', b'all', sequence, b'')
        return

    def bind_class(self, className, sequence=None, func=None, add=None):
        return self._bind((b'bind', className), sequence, func, add, 0)

    def unbind_class(self, className, sequence):
        self.tk.call(b'bind', className, sequence, b'')
        return

    def mainloop(self, n=0):
        self.tk.mainloop(n)
        return

    def quit(self):
        self.tk.quit()
        return

    def _getints(self, string):
        if string:
            return tuple(map(getint, self.tk.splitlist(string)))
        return

    def _getdoubles(self, string):
        if string:
            return tuple(map(getdouble, self.tk.splitlist(string)))
        return

    def _getboolean(self, string):
        if string:
            return self.tk.getboolean(string)
        return

    def _displayof(self, displayof):
        if displayof:
            return (b'-displayof', displayof)
        else:
            if displayof is None:
                return (b'-displayof', self._w)
            return ()

    @property
    def _windowingsystem(self):
        try:
            return self._root()._windowingsystem_cached
        except AttributeError:
            ws = self._root()._windowingsystem_cached = self.tk.call(b'tk', b'windowingsystem')
            return ws

        return

    def _options(self, cnf, kw=None):
        if kw:
            cnf = _cnfmerge((cnf, kw))
        else:
            cnf = _cnfmerge(cnf)
        res = ()
        for k, v in cnf.items():
            if v is not None:
                if k[-1] == b'_':
                    k = k[:-1]
                if hasattr(v, b'__call__'):
                    v = self._register(v)
                elif isinstance(v, (tuple, list)):
                    nv = []
                    for item in v:
                        if not isinstance(item, (basestring, int, long)):
                            break
                        elif isinstance(item, (int, long)):
                            nv.append(b'%d' % item)
                        else:
                            nv.append(_stringify(item))
                    else:
                        v = (b' ').join(nv)

                res = res + (b'-' + k, v)

        return res

    def nametowidget(self, name):
        name = str(name).split(b'.')
        w = self
        if not name[0]:
            w = w._root()
            name = name[1:]
        for n in name:
            if not n:
                break
            w = w.children[n]

        return w

    _nametowidget = nametowidget

    def _register(self, func, subst=None, needcleanup=1):
        f = CallWrapper(func, subst, self).__call__
        name = repr(id(f))
        try:
            func = func.im_func
        except AttributeError:
            pass

        try:
            name = name + func.__name__
        except AttributeError:
            pass

        self.tk.createcommand(name, f)
        if needcleanup:
            if self._tclCommands is None:
                self._tclCommands = []
            self._tclCommands.append(name)
        return name

    register = _register

    def _root(self):
        w = self
        while w.master:
            w = w.master

        return w

    _subst_format = (b'%#', b'%b', b'%f', b'%h', b'%k', b'%s', b'%t', b'%w', b'%x', b'%y', b'%A', b'%E', b'%K', b'%N', b'%W', b'%T', b'%X', b'%Y', b'%D')
    _subst_format_str = (b' ').join(_subst_format)

    def _substitute(self, *args):
        if len(args) != len(self._subst_format):
            return args
        getboolean = self.tk.getboolean
        getint = int

        def getint_event(s):
            try:
                return int(s)
            except ValueError:
                return s

            return

        nsign, b, f, h, k, s, t, w, x, y, A, E, K, N, W, T, X, Y, D = args
        e = Event()
        e.serial = getint(nsign)
        e.num = getint_event(b)
        try:
            e.focus = getboolean(f)
        except TclError:
            pass

        e.height = getint_event(h)
        e.keycode = getint_event(k)
        e.state = getint_event(s)
        e.time = getint_event(t)
        e.width = getint_event(w)
        e.x = getint_event(x)
        e.y = getint_event(y)
        e.char = A
        try:
            e.send_event = getboolean(E)
        except TclError:
            pass

        e.keysym = K
        e.keysym_num = getint_event(N)
        e.type = T
        try:
            e.widget = self._nametowidget(W)
        except KeyError:
            e.widget = W

        e.x_root = getint_event(X)
        e.y_root = getint_event(Y)
        try:
            e.delta = getint(D)
        except ValueError:
            e.delta = 0

        return (
         e,)

    def _report_exception(self):
        import sys
        exc, val, tb = sys.exc_type, sys.exc_value, sys.exc_traceback
        root = self._root()
        root.report_callback_exception(exc, val, tb)
        return

    def _getconfigure(self, *args):
        cnf = {}
        for x in self.tk.splitlist(self.tk.call(*args)):
            x = self.tk.splitlist(x)
            cnf[x[0][1:]] = (x[0][1:],) + x[1:]

        return cnf

    def _getconfigure1(self, *args):
        x = self.tk.splitlist(self.tk.call(*args))
        return (x[0][1:],) + x[1:]

    def _configure(self, cmd, cnf, kw):
        if kw:
            cnf = _cnfmerge((cnf, kw))
        elif cnf:
            cnf = _cnfmerge(cnf)
        if cnf is None:
            return self._getconfigure(_flatten((self._w, cmd)))
        else:
            if type(cnf) is StringType:
                return self._getconfigure1(_flatten((self._w, cmd, b'-' + cnf)))
            self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
            return

    def configure(self, cnf=None, **kw):
        return self._configure(b'configure', cnf, kw)

    config = configure

    def cget(self, key):
        return self.tk.call(self._w, b'cget', b'-' + key)

    __getitem__ = cget

    def __setitem__(self, key, value):
        self.configure({key: value})
        return

    def __contains__(self, key):
        raise TypeError(b"Tkinter objects don't support 'in' tests.")
        return

    def keys(self):
        splitlist = self.tk.splitlist
        return [splitlist(x)[0][1:] for x in splitlist(self.tk.call(self._w, b'configure'))]

    def __str__(self):
        return self._w

    _noarg_ = [
     b'_noarg_']

    def pack_propagate(self, flag=_noarg_):
        if flag is Misc._noarg_:
            return self._getboolean(self.tk.call(b'pack', b'propagate', self._w))
        self.tk.call(b'pack', b'propagate', self._w, flag)
        return

    propagate = pack_propagate

    def pack_slaves(self):
        return map(self._nametowidget, self.tk.splitlist(self.tk.call(b'pack', b'slaves', self._w)))

    slaves = pack_slaves

    def place_slaves(self):
        return map(self._nametowidget, self.tk.splitlist(self.tk.call(b'place', b'slaves', self._w)))

    def grid_bbox(self, column=None, row=None, col2=None, row2=None):
        args = (
         b'grid', b'bbox', self._w)
        if column is not None and row is not None:
            args = args + (column, row)
        if col2 is not None and row2 is not None:
            args = args + (col2, row2)
        return self._getints(self.tk.call(*args)) or None

    bbox = grid_bbox

    def _gridconvvalue(self, value):
        if isinstance(value, (str, _tkinter.Tcl_Obj)):
            try:
                svalue = str(value)
                if not svalue:
                    return None
                if b'.' in svalue:
                    return getdouble(svalue)
                return getint(svalue)
            except ValueError:
                pass

        return value

    def _grid_configure(self, command, index, cnf, kw):
        if type(cnf) is StringType and not kw:
            if cnf[-1:] == b'_':
                cnf = cnf[:-1]
            if cnf[:1] != b'-':
                cnf = b'-' + cnf
            options = (
             cnf,)
        else:
            options = self._options(cnf, kw)
        if not options:
            return _splitdict(self.tk, self.tk.call(b'grid', command, self._w, index), conv=self._gridconvvalue)
        res = self.tk.call((
         b'grid', command, self._w, index) + options)
        if len(options) == 1:
            return self._gridconvvalue(res)
        return

    def grid_columnconfigure(self, index, cnf={}, **kw):
        return self._grid_configure(b'columnconfigure', index, cnf, kw)

    columnconfigure = grid_columnconfigure

    def grid_location(self, x, y):
        return self._getints(self.tk.call(b'grid', b'location', self._w, x, y)) or None

    def grid_propagate(self, flag=_noarg_):
        if flag is Misc._noarg_:
            return self._getboolean(self.tk.call(b'grid', b'propagate', self._w))
        self.tk.call(b'grid', b'propagate', self._w, flag)
        return

    def grid_rowconfigure(self, index, cnf={}, **kw):
        return self._grid_configure(b'rowconfigure', index, cnf, kw)

    rowconfigure = grid_rowconfigure

    def grid_size(self):
        return self._getints(self.tk.call(b'grid', b'size', self._w)) or None

    size = grid_size

    def grid_slaves(self, row=None, column=None):
        args = ()
        if row is not None:
            args = args + (b'-row', row)
        if column is not None:
            args = args + (b'-column', column)
        return map(self._nametowidget, self.tk.splitlist(self.tk.call((
         b'grid', b'slaves', self._w) + args)))

    def event_add(self, virtual, *sequences):
        args = (
         b'event', b'add', virtual) + sequences
        self.tk.call(args)
        return

    def event_delete(self, virtual, *sequences):
        args = (
         b'event', b'delete', virtual) + sequences
        self.tk.call(args)
        return

    def event_generate(self, sequence, **kw):
        args = (
         b'event', b'generate', self._w, sequence)
        for k, v in kw.items():
            args = args + (b'-%s' % k, str(v))

        self.tk.call(args)
        return

    def event_info(self, virtual=None):
        return self.tk.splitlist(self.tk.call(b'event', b'info', virtual))

    def image_names(self):
        return self.tk.splitlist(self.tk.call(b'image', b'names'))

    def image_types(self):
        return self.tk.splitlist(self.tk.call(b'image', b'types'))


class CallWrapper():

    def __init__(self, func, subst, widget):
        self.func = func
        self.subst = subst
        self.widget = widget
        return

    def __call__(self, *args):
        try:
            if self.subst:
                args = self.subst(*args)
            return self.func(*args)
        except SystemExit as msg:
            raise SystemExit, msg
        except:
            self.widget._report_exception()

        return


class XView():

    def xview(self, *args):
        res = self.tk.call(self._w, b'xview', *args)
        if not args:
            return self._getdoubles(res)
        return

    def xview_moveto(self, fraction):
        self.tk.call(self._w, b'xview', b'moveto', fraction)
        return

    def xview_scroll(self, number, what):
        self.tk.call(self._w, b'xview', b'scroll', number, what)
        return


class YView():

    def yview(self, *args):
        res = self.tk.call(self._w, b'yview', *args)
        if not args:
            return self._getdoubles(res)
        return

    def yview_moveto(self, fraction):
        self.tk.call(self._w, b'yview', b'moveto', fraction)
        return

    def yview_scroll(self, number, what):
        self.tk.call(self._w, b'yview', b'scroll', number, what)
        return


class Wm():

    def wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None):
        return self._getints(self.tk.call(b'wm', b'aspect', self._w, minNumer, minDenom, maxNumer, maxDenom))

    aspect = wm_aspect

    def wm_attributes(self, *args):
        args = (
         b'wm', b'attributes', self._w) + args
        return self.tk.call(args)

    attributes = wm_attributes

    def wm_client(self, name=None):
        return self.tk.call(b'wm', b'client', self._w, name)

    client = wm_client

    def wm_colormapwindows(self, *wlist):
        if len(wlist) > 1:
            wlist = (
             wlist,)
        args = (
         b'wm', b'colormapwindows', self._w) + wlist
        if wlist:
            self.tk.call(args)
        else:
            return map(self._nametowidget, self.tk.splitlist(self.tk.call(args)))
        return

    colormapwindows = wm_colormapwindows

    def wm_command(self, value=None):
        return self.tk.call(b'wm', b'command', self._w, value)

    command = wm_command

    def wm_deiconify(self):
        return self.tk.call(b'wm', b'deiconify', self._w)

    deiconify = wm_deiconify

    def wm_focusmodel(self, model=None):
        return self.tk.call(b'wm', b'focusmodel', self._w, model)

    focusmodel = wm_focusmodel

    def wm_frame(self):
        return self.tk.call(b'wm', b'frame', self._w)

    frame = wm_frame

    def wm_geometry(self, newGeometry=None):
        return self.tk.call(b'wm', b'geometry', self._w, newGeometry)

    geometry = wm_geometry

    def wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None):
        return self._getints(self.tk.call(b'wm', b'grid', self._w, baseWidth, baseHeight, widthInc, heightInc))

    grid = wm_grid

    def wm_group(self, pathName=None):
        return self.tk.call(b'wm', b'group', self._w, pathName)

    group = wm_group

    def wm_iconbitmap(self, bitmap=None, default=None):
        if default:
            return self.tk.call(b'wm', b'iconbitmap', self._w, b'-default', default)
        else:
            return self.tk.call(b'wm', b'iconbitmap', self._w, bitmap)

        return

    iconbitmap = wm_iconbitmap

    def wm_iconify(self):
        return self.tk.call(b'wm', b'iconify', self._w)

    iconify = wm_iconify

    def wm_iconmask(self, bitmap=None):
        return self.tk.call(b'wm', b'iconmask', self._w, bitmap)

    iconmask = wm_iconmask

    def wm_iconname(self, newName=None):
        return self.tk.call(b'wm', b'iconname', self._w, newName)

    iconname = wm_iconname

    def wm_iconposition(self, x=None, y=None):
        return self._getints(self.tk.call(b'wm', b'iconposition', self._w, x, y))

    iconposition = wm_iconposition

    def wm_iconwindow(self, pathName=None):
        return self.tk.call(b'wm', b'iconwindow', self._w, pathName)

    iconwindow = wm_iconwindow

    def wm_maxsize(self, width=None, height=None):
        return self._getints(self.tk.call(b'wm', b'maxsize', self._w, width, height))

    maxsize = wm_maxsize

    def wm_minsize(self, width=None, height=None):
        return self._getints(self.tk.call(b'wm', b'minsize', self._w, width, height))

    minsize = wm_minsize

    def wm_overrideredirect(self, boolean=None):
        return self._getboolean(self.tk.call(b'wm', b'overrideredirect', self._w, boolean))

    overrideredirect = wm_overrideredirect

    def wm_positionfrom(self, who=None):
        return self.tk.call(b'wm', b'positionfrom', self._w, who)

    positionfrom = wm_positionfrom

    def wm_protocol(self, name=None, func=None):
        if hasattr(func, b'__call__'):
            command = self._register(func)
        else:
            command = func
        return self.tk.call(b'wm', b'protocol', self._w, name, command)

    protocol = wm_protocol

    def wm_resizable(self, width=None, height=None):
        return self.tk.call(b'wm', b'resizable', self._w, width, height)

    resizable = wm_resizable

    def wm_sizefrom(self, who=None):
        return self.tk.call(b'wm', b'sizefrom', self._w, who)

    sizefrom = wm_sizefrom

    def wm_state(self, newstate=None):
        return self.tk.call(b'wm', b'state', self._w, newstate)

    state = wm_state

    def wm_title(self, string=None):
        return self.tk.call(b'wm', b'title', self._w, string)

    title = wm_title

    def wm_transient(self, master=None):
        return self.tk.call(b'wm', b'transient', self._w, master)

    transient = wm_transient

    def wm_withdraw(self):
        return self.tk.call(b'wm', b'withdraw', self._w)

    withdraw = wm_withdraw


class Tk(Misc, Wm):
    _w = b'.'

    def __init__(self, screenName=None, baseName=None, className=b'Tk', useTk=1, sync=0, use=None):
        self.master = None
        self.children = {}
        self._tkloaded = 0
        self.tk = None
        if baseName is None:
            import os
            baseName = os.path.basename(sys.argv[0])
            baseName, ext = os.path.splitext(baseName)
            if ext not in (b'.py', b'.pyc', b'.pyo'):
                baseName = baseName + ext
        interactive = 0
        self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
        if useTk:
            self._loadtk()
        if not sys.flags.ignore_environment:
            self.readprofile(baseName, className)
        return

    def loadtk(self):
        if not self._tkloaded:
            self.tk.loadtk()
            self._loadtk()
        return

    def _loadtk(self):
        global _default_root
        self._tkloaded = 1
        tk_version = self.tk.getvar(b'tk_version')
        if tk_version != _tkinter.TK_VERSION:
            raise RuntimeError, b"tk.h version (%s) doesn't match libtk.a version (%s)" % (
             _tkinter.TK_VERSION, tk_version)
        tcl_version = str(self.tk.getvar(b'tcl_version'))
        if tcl_version != _tkinter.TCL_VERSION:
            raise RuntimeError, b"tcl.h version (%s) doesn't match libtcl.a version (%s)" % (
             _tkinter.TCL_VERSION, tcl_version)
        if TkVersion < 4.0:
            raise RuntimeError, b'Tk 4.0 or higher is required; found Tk %s' % str(TkVersion)
        if self._tclCommands is None:
            self._tclCommands = []
        self.tk.createcommand(b'tkerror', _tkerror)
        self.tk.createcommand(b'exit', _exit)
        self._tclCommands.append(b'tkerror')
        self._tclCommands.append(b'exit')
        if _support_default_root and not _default_root:
            _default_root = self
        self.protocol(b'WM_DELETE_WINDOW', self.destroy)
        return

    def destroy(self):
        global _default_root
        for c in self.children.values():
            c.destroy()

        self.tk.call(b'destroy', self._w)
        Misc.destroy(self)
        if _support_default_root and _default_root is self:
            _default_root = None
        return

    def readprofile(self, baseName, className):
        import os
        if b'HOME' in os.environ:
            home = os.environ[b'HOME']
        else:
            home = os.curdir
        class_tcl = os.path.join(home, b'.%s.tcl' % className)
        class_py = os.path.join(home, b'.%s.py' % className)
        base_tcl = os.path.join(home, b'.%s.tcl' % baseName)
        base_py = os.path.join(home, b'.%s.py' % baseName)
        dir = {b'self': self}
        exec b'from Tkinter import *' in dir
        if os.path.isfile(class_tcl):
            self.tk.call(b'source', class_tcl)
        if os.path.isfile(class_py):
            execfile(class_py, dir)
        if os.path.isfile(base_tcl):
            self.tk.call(b'source', base_tcl)
        if os.path.isfile(base_py):
            execfile(base_py, dir)
        return

    def report_callback_exception(self, exc, val, tb):
        import traceback, sys
        print >> sys.stderr, b'Exception in Tkinter callback'
        sys.last_type = exc
        sys.last_value = val
        sys.last_traceback = tb
        traceback.print_exception(exc, val, tb)
        return

    def __getattr__(self, attr):
        return getattr(self.tk, attr)


def Tcl(screenName=None, baseName=None, className=b'Tk', useTk=0):
    return Tk(screenName, baseName, className, useTk)


class Pack():

    def pack_configure(self, cnf={}, **kw):
        self.tk.call((
         b'pack', b'configure', self._w) + self._options(cnf, kw))
        return

    pack = configure = config = pack_configure

    def pack_forget(self):
        self.tk.call(b'pack', b'forget', self._w)
        return

    forget = pack_forget

    def pack_info(self):
        d = _splitdict(self.tk, self.tk.call(b'pack', b'info', self._w))
        if b'in' in d:
            d[b'in'] = self.nametowidget(d[b'in'])
        return d

    info = pack_info
    propagate = pack_propagate = Misc.pack_propagate
    slaves = pack_slaves = Misc.pack_slaves


class Place():

    def place_configure(self, cnf={}, **kw):
        self.tk.call((
         b'place', b'configure', self._w) + self._options(cnf, kw))
        return

    place = configure = config = place_configure

    def place_forget(self):
        self.tk.call(b'place', b'forget', self._w)
        return

    forget = place_forget

    def place_info(self):
        d = _splitdict(self.tk, self.tk.call(b'place', b'info', self._w))
        if b'in' in d:
            d[b'in'] = self.nametowidget(d[b'in'])
        return d

    info = place_info
    slaves = place_slaves = Misc.place_slaves


class Grid():

    def grid_configure(self, cnf={}, **kw):
        self.tk.call((
         b'grid', b'configure', self._w) + self._options(cnf, kw))
        return

    grid = configure = config = grid_configure
    bbox = grid_bbox = Misc.grid_bbox
    columnconfigure = grid_columnconfigure = Misc.grid_columnconfigure

    def grid_forget(self):
        self.tk.call(b'grid', b'forget', self._w)
        return

    forget = grid_forget

    def grid_remove(self):
        self.tk.call(b'grid', b'remove', self._w)
        return

    def grid_info(self):
        d = _splitdict(self.tk, self.tk.call(b'grid', b'info', self._w))
        if b'in' in d:
            d[b'in'] = self.nametowidget(d[b'in'])
        return d

    info = grid_info
    location = grid_location = Misc.grid_location
    propagate = grid_propagate = Misc.grid_propagate
    rowconfigure = grid_rowconfigure = Misc.grid_rowconfigure
    size = grid_size = Misc.grid_size
    slaves = grid_slaves = Misc.grid_slaves


class BaseWidget(Misc):

    def _setup(self, master, cnf):
        global _default_root
        if _support_default_root:
            if not master:
                if not _default_root:
                    _default_root = Tk()
                master = _default_root
        self.master = master
        self.tk = master.tk
        name = None
        if b'name' in cnf:
            name = cnf[b'name']
            del cnf[b'name']
        if not name:
            name = repr(id(self))
        self._name = name
        if master._w == b'.':
            self._w = b'.' + name
        else:
            self._w = master._w + b'.' + name
        self.children = {}
        if self._name in self.master.children:
            self.master.children[self._name].destroy()
        self.master.children[self._name] = self
        return

    def __init__(self, master, widgetName, cnf={}, kw={}, extra=()):
        if kw:
            cnf = _cnfmerge((cnf, kw))
        self.widgetName = widgetName
        BaseWidget._setup(self, master, cnf)
        if self._tclCommands is None:
            self._tclCommands = []
        classes = []
        for k in cnf.keys():
            if type(k) is ClassType:
                classes.append((k, cnf[k]))
                del cnf[k]

        self.tk.call((
         widgetName, self._w) + extra + self._options(cnf))
        for k, v in classes:
            k.configure(self, v)

        return

    def destroy(self):
        for c in self.children.values():
            c.destroy()

        self.tk.call(b'destroy', self._w)
        if self._name in self.master.children:
            del self.master.children[self._name]
        Misc.destroy(self)
        return

    def _do(self, name, args=()):
        return self.tk.call((self._w, name) + args)


class Widget(BaseWidget, Pack, Place, Grid):
    pass


class Toplevel(BaseWidget, Wm):

    def __init__(self, master=None, cnf={}, **kw):
        if kw:
            cnf = _cnfmerge((cnf, kw))
        extra = ()
        for wmkey in [1, 2, 3, 4, 
         5]:
            if wmkey in cnf:
                val = cnf[wmkey]
                if wmkey[-1] == b'_':
                    opt = b'-' + wmkey[:-1]
                else:
                    opt = b'-' + wmkey
                extra = extra + (opt, val)
                del cnf[wmkey]

        BaseWidget.__init__(self, master, b'toplevel', cnf, {}, extra)
        root = self._root()
        self.iconname(root.iconname())
        self.title(root.title())
        self.protocol(b'WM_DELETE_WINDOW', self.destroy)
        return


class Button(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'button', cnf, kw)
        return

    def tkButtonEnter(self, *dummy):
        self.tk.call(b'tkButtonEnter', self._w)
        return

    def tkButtonLeave(self, *dummy):
        self.tk.call(b'tkButtonLeave', self._w)
        return

    def tkButtonDown(self, *dummy):
        self.tk.call(b'tkButtonDown', self._w)
        return

    def tkButtonUp(self, *dummy):
        self.tk.call(b'tkButtonUp', self._w)
        return

    def tkButtonInvoke(self, *dummy):
        self.tk.call(b'tkButtonInvoke', self._w)
        return

    def flash(self):
        self.tk.call(self._w, b'flash')
        return

    def invoke(self):
        return self.tk.call(self._w, b'invoke')


def AtEnd():
    return b'end'


def AtInsert(*args):
    s = b'insert'
    for a in args:
        if a:
            s = s + (b' ' + a)

    return s


def AtSelFirst():
    return b'sel.first'


def AtSelLast():
    return b'sel.last'


def At(x, y=None):
    if y is None:
        return b'@%r' % (x,)
    else:
        return b'@%r,%r' % (x, y)
        return


class Canvas(Widget, XView, YView):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'canvas', cnf, kw)
        return

    def addtag(self, *args):
        self.tk.call((self._w, b'addtag') + args)
        return

    def addtag_above(self, newtag, tagOrId):
        self.addtag(newtag, b'above', tagOrId)
        return

    def addtag_all(self, newtag):
        self.addtag(newtag, b'all')
        return

    def addtag_below(self, newtag, tagOrId):
        self.addtag(newtag, b'below', tagOrId)
        return

    def addtag_closest(self, newtag, x, y, halo=None, start=None):
        self.addtag(newtag, b'closest', x, y, halo, start)
        return

    def addtag_enclosed(self, newtag, x1, y1, x2, y2):
        self.addtag(newtag, b'enclosed', x1, y1, x2, y2)
        return

    def addtag_overlapping(self, newtag, x1, y1, x2, y2):
        self.addtag(newtag, b'overlapping', x1, y1, x2, y2)
        return

    def addtag_withtag(self, newtag, tagOrId):
        self.addtag(newtag, b'withtag', tagOrId)
        return

    def bbox(self, *args):
        return self._getints(self.tk.call((self._w, b'bbox') + args)) or None

    def tag_unbind(self, tagOrId, sequence, funcid=None):
        self.tk.call(self._w, b'bind', tagOrId, sequence, b'')
        if funcid:
            self.deletecommand(funcid)
        return

    def tag_bind(self, tagOrId, sequence=None, func=None, add=None):
        return self._bind((self._w, b'bind', tagOrId), sequence, func, add)

    def canvasx(self, screenx, gridspacing=None):
        return getdouble(self.tk.call(self._w, b'canvasx', screenx, gridspacing))

    def canvasy(self, screeny, gridspacing=None):
        return getdouble(self.tk.call(self._w, b'canvasy', screeny, gridspacing))

    def coords(self, *args):
        return map(getdouble, self.tk.splitlist(self.tk.call((self._w, b'coords') + args)))

    def _create(self, itemType, args, kw):
        args = _flatten(args)
        cnf = args[-1]
        if type(cnf) in (DictionaryType, TupleType):
            args = args[:-1]
        else:
            cnf = {}
        return getint(self.tk.call(self._w, b'create', itemType, *(args + self._options(cnf, kw))))

    def create_arc(self, *args, **kw):
        return self._create(b'arc', args, kw)

    def create_bitmap(self, *args, **kw):
        return self._create(b'bitmap', args, kw)

    def create_image(self, *args, **kw):
        return self._create(b'image', args, kw)

    def create_line(self, *args, **kw):
        return self._create(b'line', args, kw)

    def create_oval(self, *args, **kw):
        return self._create(b'oval', args, kw)

    def create_polygon(self, *args, **kw):
        return self._create(b'polygon', args, kw)

    def create_rectangle(self, *args, **kw):
        return self._create(b'rectangle', args, kw)

    def create_text(self, *args, **kw):
        return self._create(b'text', args, kw)

    def create_window(self, *args, **kw):
        return self._create(b'window', args, kw)

    def dchars(self, *args):
        self.tk.call((self._w, b'dchars') + args)
        return

    def delete(self, *args):
        self.tk.call((self._w, b'delete') + args)
        return

    def dtag(self, *args):
        self.tk.call((self._w, b'dtag') + args)
        return

    def find(self, *args):
        return self._getints(self.tk.call((self._w, b'find') + args)) or ()

    def find_above(self, tagOrId):
        return self.find(b'above', tagOrId)

    def find_all(self):
        return self.find(b'all')

    def find_below(self, tagOrId):
        return self.find(b'below', tagOrId)

    def find_closest(self, x, y, halo=None, start=None):
        return self.find(b'closest', x, y, halo, start)

    def find_enclosed(self, x1, y1, x2, y2):
        return self.find(b'enclosed', x1, y1, x2, y2)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.find(b'overlapping', x1, y1, x2, y2)

    def find_withtag(self, tagOrId):
        return self.find(b'withtag', tagOrId)

    def focus(self, *args):
        return self.tk.call((self._w, b'focus') + args)

    def gettags(self, *args):
        return self.tk.splitlist(self.tk.call((self._w, b'gettags') + args))

    def icursor(self, *args):
        self.tk.call((self._w, b'icursor') + args)
        return

    def index(self, *args):
        return getint(self.tk.call((self._w, b'index') + args))

    def insert(self, *args):
        self.tk.call((self._w, b'insert') + args)
        return

    def itemcget(self, tagOrId, option):
        return self.tk.call((
         self._w, b'itemcget') + (tagOrId, b'-' + option))

    def itemconfigure(self, tagOrId, cnf=None, **kw):
        return self._configure((b'itemconfigure', tagOrId), cnf, kw)

    itemconfig = itemconfigure

    def tag_lower(self, *args):
        self.tk.call((self._w, b'lower') + args)
        return

    lower = tag_lower

    def move(self, *args):
        self.tk.call((self._w, b'move') + args)
        return

    def postscript(self, cnf={}, **kw):
        return self.tk.call((self._w, b'postscript') + self._options(cnf, kw))

    def tag_raise(self, *args):
        self.tk.call((self._w, b'raise') + args)
        return

    lift = tkraise = tag_raise

    def scale(self, *args):
        self.tk.call((self._w, b'scale') + args)
        return

    def scan_mark(self, x, y):
        self.tk.call(self._w, b'scan', b'mark', x, y)
        return

    def scan_dragto(self, x, y, gain=10):
        self.tk.call(self._w, b'scan', b'dragto', x, y, gain)
        return

    def select_adjust(self, tagOrId, index):
        self.tk.call(self._w, b'select', b'adjust', tagOrId, index)
        return

    def select_clear(self):
        self.tk.call(self._w, b'select', b'clear')
        return

    def select_from(self, tagOrId, index):
        self.tk.call(self._w, b'select', b'from', tagOrId, index)
        return

    def select_item(self):
        return self.tk.call(self._w, b'select', b'item') or None

    def select_to(self, tagOrId, index):
        self.tk.call(self._w, b'select', b'to', tagOrId, index)
        return

    def type(self, tagOrId):
        return self.tk.call(self._w, b'type', tagOrId) or None


class Checkbutton(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'checkbutton', cnf, kw)
        return

    def deselect(self):
        self.tk.call(self._w, b'deselect')
        return

    def flash(self):
        self.tk.call(self._w, b'flash')
        return

    def invoke(self):
        return self.tk.call(self._w, b'invoke')

    def select(self):
        self.tk.call(self._w, b'select')
        return

    def toggle(self):
        self.tk.call(self._w, b'toggle')
        return


class Entry(Widget, XView):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'entry', cnf, kw)
        return

    def delete(self, first, last=None):
        self.tk.call(self._w, b'delete', first, last)
        return

    def get(self):
        return self.tk.call(self._w, b'get')

    def icursor(self, index):
        self.tk.call(self._w, b'icursor', index)
        return

    def index(self, index):
        return getint(self.tk.call(self._w, b'index', index))

    def insert(self, index, string):
        self.tk.call(self._w, b'insert', index, string)
        return

    def scan_mark(self, x):
        self.tk.call(self._w, b'scan', b'mark', x)
        return

    def scan_dragto(self, x):
        self.tk.call(self._w, b'scan', b'dragto', x)
        return

    def selection_adjust(self, index):
        self.tk.call(self._w, b'selection', b'adjust', index)
        return

    select_adjust = selection_adjust

    def selection_clear(self):
        self.tk.call(self._w, b'selection', b'clear')
        return

    select_clear = selection_clear

    def selection_from(self, index):
        self.tk.call(self._w, b'selection', b'from', index)
        return

    select_from = selection_from

    def selection_present(self):
        return self.tk.getboolean(self.tk.call(self._w, b'selection', b'present'))

    select_present = selection_present

    def selection_range(self, start, end):
        self.tk.call(self._w, b'selection', b'range', start, end)
        return

    select_range = selection_range

    def selection_to(self, index):
        self.tk.call(self._w, b'selection', b'to', index)
        return

    select_to = selection_to


class Frame(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        cnf = _cnfmerge((cnf, kw))
        extra = ()
        if b'class_' in cnf:
            extra = (
             b'-class', cnf[b'class_'])
            del cnf[b'class_']
        elif b'class' in cnf:
            extra = (
             b'-class', cnf[b'class'])
            del cnf[b'class']
        Widget.__init__(self, master, b'frame', cnf, {}, extra)
        return


class Label(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'label', cnf, kw)
        return


class Listbox(Widget, XView, YView):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'listbox', cnf, kw)
        return

    def activate(self, index):
        self.tk.call(self._w, b'activate', index)
        return

    def bbox(self, index):
        return self._getints(self.tk.call(self._w, b'bbox', index)) or None

    def curselection(self):
        return self._getints(self.tk.call(self._w, b'curselection')) or ()

    def delete(self, first, last=None):
        self.tk.call(self._w, b'delete', first, last)
        return

    def get(self, first, last=None):
        if last is not None:
            return self.tk.splitlist(self.tk.call(self._w, b'get', first, last))
        else:
            return self.tk.call(self._w, b'get', first)
            return

    def index(self, index):
        i = self.tk.call(self._w, b'index', index)
        if i == b'none':
            return None
        else:
            return getint(i)

    def insert(self, index, *elements):
        self.tk.call((self._w, b'insert', index) + elements)
        return

    def nearest(self, y):
        return getint(self.tk.call(self._w, b'nearest', y))

    def scan_mark(self, x, y):
        self.tk.call(self._w, b'scan', b'mark', x, y)
        return

    def scan_dragto(self, x, y):
        self.tk.call(self._w, b'scan', b'dragto', x, y)
        return

    def see(self, index):
        self.tk.call(self._w, b'see', index)
        return

    def selection_anchor(self, index):
        self.tk.call(self._w, b'selection', b'anchor', index)
        return

    select_anchor = selection_anchor

    def selection_clear(self, first, last=None):
        self.tk.call(self._w, b'selection', b'clear', first, last)
        return

    select_clear = selection_clear

    def selection_includes(self, index):
        return self.tk.getboolean(self.tk.call(self._w, b'selection', b'includes', index))

    select_includes = selection_includes

    def selection_set(self, first, last=None):
        self.tk.call(self._w, b'selection', b'set', first, last)
        return

    select_set = selection_set

    def size(self):
        return getint(self.tk.call(self._w, b'size'))

    def itemcget(self, index, option):
        return self.tk.call((
         self._w, b'itemcget') + (index, b'-' + option))

    def itemconfigure(self, index, cnf=None, **kw):
        return self._configure((b'itemconfigure', index), cnf, kw)

    itemconfig = itemconfigure


class Menu(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'menu', cnf, kw)
        return

    def tk_bindForTraversal(self):
        import warnings
        warnings.warn(b'tk_bindForTraversal() does nothing and will be removed in 3.6', DeprecationWarning, stacklevel=2)
        return

    def tk_mbPost(self):
        self.tk.call(b'tk_mbPost', self._w)
        return

    def tk_mbUnpost(self):
        self.tk.call(b'tk_mbUnpost')
        return

    def tk_traverseToMenu(self, char):
        self.tk.call(b'tk_traverseToMenu', self._w, char)
        return

    def tk_traverseWithinMenu(self, char):
        self.tk.call(b'tk_traverseWithinMenu', self._w, char)
        return

    def tk_getMenuButtons(self):
        return self.tk.call(b'tk_getMenuButtons', self._w)

    def tk_nextMenu(self, count):
        self.tk.call(b'tk_nextMenu', count)
        return

    def tk_nextMenuEntry(self, count):
        self.tk.call(b'tk_nextMenuEntry', count)
        return

    def tk_invokeMenu(self):
        self.tk.call(b'tk_invokeMenu', self._w)
        return

    def tk_firstMenu(self):
        self.tk.call(b'tk_firstMenu', self._w)
        return

    def tk_mbButtonDown(self):
        self.tk.call(b'tk_mbButtonDown', self._w)
        return

    def tk_popup(self, x, y, entry=b''):
        self.tk.call(b'tk_popup', self._w, x, y, entry)
        return

    def activate(self, index):
        self.tk.call(self._w, b'activate', index)
        return

    def add(self, itemType, cnf={}, **kw):
        self.tk.call((self._w, b'add', itemType) + self._options(cnf, kw))
        return

    def add_cascade(self, cnf={}, **kw):
        self.add(b'cascade', cnf or kw)
        return

    def add_checkbutton(self, cnf={}, **kw):
        self.add(b'checkbutton', cnf or kw)
        return

    def add_command(self, cnf={}, **kw):
        self.add(b'command', cnf or kw)
        return

    def add_radiobutton(self, cnf={}, **kw):
        self.add(b'radiobutton', cnf or kw)
        return

    def add_separator(self, cnf={}, **kw):
        self.add(b'separator', cnf or kw)
        return

    def insert(self, index, itemType, cnf={}, **kw):
        self.tk.call((self._w, b'insert', index, itemType) + self._options(cnf, kw))
        return

    def insert_cascade(self, index, cnf={}, **kw):
        self.insert(index, b'cascade', cnf or kw)
        return

    def insert_checkbutton(self, index, cnf={}, **kw):
        self.insert(index, b'checkbutton', cnf or kw)
        return

    def insert_command(self, index, cnf={}, **kw):
        self.insert(index, b'command', cnf or kw)
        return

    def insert_radiobutton(self, index, cnf={}, **kw):
        self.insert(index, b'radiobutton', cnf or kw)
        return

    def insert_separator(self, index, cnf={}, **kw):
        self.insert(index, b'separator', cnf or kw)
        return

    def delete(self, index1, index2=None):
        if index2 is None:
            index2 = index1
        num_index1, num_index2 = self.index(index1), self.index(index2)
        if num_index1 is None or num_index2 is None:
            num_index1, num_index2 = (0, -1)
        for i in range(num_index1, num_index2 + 1):
            if b'command' in self.entryconfig(i):
                c = str(self.entrycget(i, b'command'))
                if c:
                    self.deletecommand(c)

        self.tk.call(self._w, b'delete', index1, index2)
        return

    def entrycget(self, index, option):
        return self.tk.call(self._w, b'entrycget', index, b'-' + option)

    def entryconfigure(self, index, cnf=None, **kw):
        return self._configure((b'entryconfigure', index), cnf, kw)

    entryconfig = entryconfigure

    def index(self, index):
        i = self.tk.call(self._w, b'index', index)
        if i == b'none':
            return None
        else:
            return getint(i)

    def invoke(self, index):
        return self.tk.call(self._w, b'invoke', index)

    def post(self, x, y):
        self.tk.call(self._w, b'post', x, y)
        return

    def type(self, index):
        return self.tk.call(self._w, b'type', index)

    def unpost(self):
        self.tk.call(self._w, b'unpost')
        return

    def yposition(self, index):
        return getint(self.tk.call(self._w, b'yposition', index))


class Menubutton(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'menubutton', cnf, kw)
        return


class Message(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'message', cnf, kw)
        return


class Radiobutton(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'radiobutton', cnf, kw)
        return

    def deselect(self):
        self.tk.call(self._w, b'deselect')
        return

    def flash(self):
        self.tk.call(self._w, b'flash')
        return

    def invoke(self):
        return self.tk.call(self._w, b'invoke')

    def select(self):
        self.tk.call(self._w, b'select')
        return


class Scale(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'scale', cnf, kw)
        return

    def get(self):
        value = self.tk.call(self._w, b'get')
        try:
            return getint(value)
        except ValueError:
            return getdouble(value)

        return

    def set(self, value):
        self.tk.call(self._w, b'set', value)
        return

    def coords(self, value=None):
        return self._getints(self.tk.call(self._w, b'coords', value))

    def identify(self, x, y):
        return self.tk.call(self._w, b'identify', x, y)


class Scrollbar(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'scrollbar', cnf, kw)
        return

    def activate(self, index):
        self.tk.call(self._w, b'activate', index)
        return

    def delta(self, deltax, deltay):
        return getdouble(self.tk.call(self._w, b'delta', deltax, deltay))

    def fraction(self, x, y):
        return getdouble(self.tk.call(self._w, b'fraction', x, y))

    def identify(self, x, y):
        return self.tk.call(self._w, b'identify', x, y)

    def get(self):
        return self._getdoubles(self.tk.call(self._w, b'get'))

    def set(self, *args):
        self.tk.call((self._w, b'set') + args)
        return


class Text(Widget, XView, YView):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'text', cnf, kw)
        return

    def bbox(self, *args):
        return self._getints(self.tk.call((self._w, b'bbox') + args)) or None

    def tk_textSelectTo(self, index):
        self.tk.call(b'tk_textSelectTo', self._w, index)
        return

    def tk_textBackspace(self):
        self.tk.call(b'tk_textBackspace', self._w)
        return

    def tk_textIndexCloser(self, a, b, c):
        self.tk.call(b'tk_textIndexCloser', self._w, a, b, c)
        return

    def tk_textResetAnchor(self, index):
        self.tk.call(b'tk_textResetAnchor', self._w, index)
        return

    def compare(self, index1, op, index2):
        return self.tk.getboolean(self.tk.call(self._w, b'compare', index1, op, index2))

    def debug(self, boolean=None):
        if boolean is None:
            return self.tk.getboolean(self.tk.call(self._w, b'debug'))
        else:
            self.tk.call(self._w, b'debug', boolean)
            return

    def delete(self, index1, index2=None):
        self.tk.call(self._w, b'delete', index1, index2)
        return

    def dlineinfo(self, index):
        return self._getints(self.tk.call(self._w, b'dlineinfo', index))

    def dump(self, index1, index2=None, command=None, **kw):
        args = []
        func_name = None
        result = None
        if not command:
            result = []

            def append_triple(key, value, index, result=result):
                result.append((key, value, index))
                return

            command = append_triple
        try:
            if not isinstance(command, str):
                func_name = command = self._register(command)
            args += [b'-command', command]
            for key in kw:
                if kw[key]:
                    args.append(b'-' + key)

            args.append(index1)
            if index2:
                args.append(index2)
            self.tk.call(self._w, b'dump', *args)
            return result
        finally:
            if func_name:
                self.deletecommand(func_name)

        return

    def edit(self, *args):
        return self.tk.call(self._w, b'edit', *args)

    def edit_modified(self, arg=None):
        return self.edit(b'modified', arg)

    def edit_redo(self):
        return self.edit(b'redo')

    def edit_reset(self):
        return self.edit(b'reset')

    def edit_separator(self):
        return self.edit(b'separator')

    def edit_undo(self):
        return self.edit(b'undo')

    def get(self, index1, index2=None):
        return self.tk.call(self._w, b'get', index1, index2)

    def image_cget(self, index, option):
        if option[:1] != b'-':
            option = b'-' + option
        if option[-1:] == b'_':
            option = option[:-1]
        return self.tk.call(self._w, b'image', b'cget', index, option)

    def image_configure(self, index, cnf=None, **kw):
        return self._configure((b'image', b'configure', index), cnf, kw)

    def image_create(self, index, cnf={}, **kw):
        return self.tk.call(self._w, b'image', b'create', index, *self._options(cnf, kw))

    def image_names(self):
        return self.tk.call(self._w, b'image', b'names')

    def index(self, index):
        return str(self.tk.call(self._w, b'index', index))

    def insert(self, index, chars, *args):
        self.tk.call((self._w, b'insert', index, chars) + args)
        return

    def mark_gravity(self, markName, direction=None):
        return self.tk.call((
         self._w, b'mark', b'gravity', markName, direction))

    def mark_names(self):
        return self.tk.splitlist(self.tk.call(self._w, b'mark', b'names'))

    def mark_set(self, markName, index):
        self.tk.call(self._w, b'mark', b'set', markName, index)
        return

    def mark_unset(self, *markNames):
        self.tk.call((self._w, b'mark', b'unset') + markNames)
        return

    def mark_next(self, index):
        return self.tk.call(self._w, b'mark', b'next', index) or None

    def mark_previous(self, index):
        return self.tk.call(self._w, b'mark', b'previous', index) or None

    def scan_mark(self, x, y):
        self.tk.call(self._w, b'scan', b'mark', x, y)
        return

    def scan_dragto(self, x, y):
        self.tk.call(self._w, b'scan', b'dragto', x, y)
        return

    def search(self, pattern, index, stopindex=None, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None, elide=None):
        args = [
         self._w, b'search']
        if forwards:
            args.append(b'-forwards')
        if backwards:
            args.append(b'-backwards')
        if exact:
            args.append(b'-exact')
        if regexp:
            args.append(b'-regexp')
        if nocase:
            args.append(b'-nocase')
        if elide:
            args.append(b'-elide')
        if count:
            args.append(b'-count')
            args.append(count)
        if pattern and pattern[0] == b'-':
            args.append(b'--')
        args.append(pattern)
        args.append(index)
        if stopindex:
            args.append(stopindex)
        return str(self.tk.call(tuple(args)))

    def see(self, index):
        self.tk.call(self._w, b'see', index)
        return

    def tag_add(self, tagName, index1, *args):
        self.tk.call((
         self._w, b'tag', b'add', tagName, index1) + args)
        return

    def tag_unbind(self, tagName, sequence, funcid=None):
        self.tk.call(self._w, b'tag', b'bind', tagName, sequence, b'')
        if funcid:
            self.deletecommand(funcid)
        return

    def tag_bind(self, tagName, sequence, func, add=None):
        return self._bind((self._w, b'tag', b'bind', tagName), sequence, func, add)

    def tag_cget(self, tagName, option):
        if option[:1] != b'-':
            option = b'-' + option
        if option[-1:] == b'_':
            option = option[:-1]
        return self.tk.call(self._w, b'tag', b'cget', tagName, option)

    def tag_configure(self, tagName, cnf=None, **kw):
        return self._configure((b'tag', b'configure', tagName), cnf, kw)

    tag_config = tag_configure

    def tag_delete(self, *tagNames):
        self.tk.call((self._w, b'tag', b'delete') + tagNames)
        return

    def tag_lower(self, tagName, belowThis=None):
        self.tk.call(self._w, b'tag', b'lower', tagName, belowThis)
        return

    def tag_names(self, index=None):
        return self.tk.splitlist(self.tk.call(self._w, b'tag', b'names', index))

    def tag_nextrange(self, tagName, index1, index2=None):
        return self.tk.splitlist(self.tk.call(self._w, b'tag', b'nextrange', tagName, index1, index2))

    def tag_prevrange(self, tagName, index1, index2=None):
        return self.tk.splitlist(self.tk.call(self._w, b'tag', b'prevrange', tagName, index1, index2))

    def tag_raise(self, tagName, aboveThis=None):
        self.tk.call(self._w, b'tag', b'raise', tagName, aboveThis)
        return

    def tag_ranges(self, tagName):
        return self.tk.splitlist(self.tk.call(self._w, b'tag', b'ranges', tagName))

    def tag_remove(self, tagName, index1, index2=None):
        self.tk.call(self._w, b'tag', b'remove', tagName, index1, index2)
        return

    def window_cget(self, index, option):
        if option[:1] != b'-':
            option = b'-' + option
        if option[-1:] == b'_':
            option = option[:-1]
        return self.tk.call(self._w, b'window', b'cget', index, option)

    def window_configure(self, index, cnf=None, **kw):
        return self._configure((b'window', b'configure', index), cnf, kw)

    window_config = window_configure

    def window_create(self, index, cnf={}, **kw):
        self.tk.call((
         self._w, b'window', b'create', index) + self._options(cnf, kw))
        return

    def window_names(self):
        return self.tk.splitlist(self.tk.call(self._w, b'window', b'names'))

    def yview_pickplace(self, *what):
        self.tk.call((self._w, b'yview', b'-pickplace') + what)
        return


class _setit():

    def __init__(self, var, value, callback=None):
        self.__value = value
        self.__var = var
        self.__callback = callback
        return

    def __call__(self, *args):
        self.__var.set(self.__value)
        if self.__callback:
            self.__callback(self.__value, *args)
        return


class OptionMenu(Menubutton):

    def __init__(self, master, variable, value, *values, **kwargs):
        kw = {b'borderwidth': 2, b'textvariable': variable, b'indicatoron': 1, 
           b'relief': RAISED, b'anchor': b'c', b'highlightthickness': 2}
        Widget.__init__(self, master, b'menubutton', kw)
        self.widgetName = b'tk_optionMenu'
        menu = self.__menu = Menu(self, name=b'menu', tearoff=0)
        self.menuname = menu._w
        callback = kwargs.get(b'command')
        if b'command' in kwargs:
            del kwargs[b'command']
        if kwargs:
            raise TclError, b'unknown option -' + kwargs.keys()[0]
        menu.add_command(label=value, command=_setit(variable, value, callback))
        for v in values:
            menu.add_command(label=v, command=_setit(variable, v, callback))

        self[b'menu'] = menu
        return

    def __getitem__(self, name):
        if name == b'menu':
            return self.__menu
        return Widget.__getitem__(self, name)

    def destroy(self):
        Menubutton.destroy(self)
        self.__menu = None
        return


class Image():
    _last_id = 0

    def __init__(self, imgtype, name=None, cnf={}, master=None, **kw):
        self.name = None
        if not master:
            master = _default_root
            if not master:
                raise RuntimeError, b'Too early to create image'
        self.tk = getattr(master, b'tk', master)
        if not name:
            Image._last_id += 1
            name = b'pyimage%r' % (Image._last_id,)
            if name[0] == b'-':
                name = b'_' + name[1:]
        if kw and cnf:
            cnf = _cnfmerge((cnf, kw))
        elif kw:
            cnf = kw
        options = ()
        for k, v in cnf.items():
            if hasattr(v, b'__call__'):
                v = self._register(v)
            elif k in (b'data', b'maskdata'):
                v = self.tk._createbytearray(v)
            options = options + (b'-' + k, v)

        self.tk.call((b'image', b'create', imgtype, name) + options)
        self.name = name
        return

    def __str__(self):
        return self.name

    def __del__(self):
        if self.name:
            try:
                self.tk.call(b'image', b'delete', self.name)
            except TclError:
                pass

        return

    def __setitem__(self, key, value):
        self.tk.call(self.name, b'configure', b'-' + key, value)
        return

    def __getitem__(self, key):
        return self.tk.call(self.name, b'configure', b'-' + key)

    def configure(self, **kw):
        res = ()
        for k, v in _cnfmerge(kw).items():
            if v is not None:
                if k[-1] == b'_':
                    k = k[:-1]
                if hasattr(v, b'__call__'):
                    v = self._register(v)
                elif k in (b'data', b'maskdata'):
                    v = self.tk._createbytearray(v)
                res = res + (b'-' + k, v)

        self.tk.call((self.name, b'config') + res)
        return

    config = configure

    def height(self):
        return getint(self.tk.call(b'image', b'height', self.name))

    def type(self):
        return self.tk.call(b'image', b'type', self.name)

    def width(self):
        return getint(self.tk.call(b'image', b'width', self.name))


class PhotoImage(Image):

    def __init__(self, name=None, cnf={}, master=None, **kw):
        Image.__init__(self, b'photo', name, cnf, master, **kw)
        return

    def blank(self):
        self.tk.call(self.name, b'blank')
        return

    def cget(self, option):
        return self.tk.call(self.name, b'cget', b'-' + option)

    def __getitem__(self, key):
        return self.tk.call(self.name, b'cget', b'-' + key)

    def copy(self):
        destImage = PhotoImage(master=self.tk)
        self.tk.call(destImage, b'copy', self.name)
        return destImage

    def zoom(self, x, y=b''):
        destImage = PhotoImage(master=self.tk)
        if y == b'':
            y = x
        self.tk.call(destImage, b'copy', self.name, b'-zoom', x, y)
        return destImage

    def subsample(self, x, y=b''):
        destImage = PhotoImage(master=self.tk)
        if y == b'':
            y = x
        self.tk.call(destImage, b'copy', self.name, b'-subsample', x, y)
        return destImage

    def get(self, x, y):
        return self.tk.call(self.name, b'get', x, y)

    def put(self, data, to=None):
        args = (
         self.name, b'put', data)
        if to:
            if to[0] == b'-to':
                to = to[1:]
            args = args + (b'-to',) + tuple(to)
        self.tk.call(args)
        return

    def write(self, filename, format=None, from_coords=None):
        args = (
         self.name, b'write', filename)
        if format:
            args = args + (b'-format', format)
        if from_coords:
            args = args + (b'-from',) + tuple(from_coords)
        self.tk.call(args)
        return


class BitmapImage(Image):

    def __init__(self, name=None, cnf={}, master=None, **kw):
        Image.__init__(self, b'bitmap', name, cnf, master, **kw)
        return


def image_names():
    return _default_root.tk.splitlist(_default_root.tk.call(b'image', b'names'))


def image_types():
    return _default_root.tk.splitlist(_default_root.tk.call(b'image', b'types'))


class Spinbox(Widget, XView):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'spinbox', cnf, kw)
        return

    def bbox(self, index):
        return self._getints(self.tk.call(self._w, b'bbox', index)) or None

    def delete(self, first, last=None):
        return self.tk.call(self._w, b'delete', first, last)

    def get(self):
        return self.tk.call(self._w, b'get')

    def icursor(self, index):
        return self.tk.call(self._w, b'icursor', index)

    def identify(self, x, y):
        return self.tk.call(self._w, b'identify', x, y)

    def index(self, index):
        return self.tk.call(self._w, b'index', index)

    def insert(self, index, s):
        return self.tk.call(self._w, b'insert', index, s)

    def invoke(self, element):
        return self.tk.call(self._w, b'invoke', element)

    def scan(self, *args):
        return self._getints(self.tk.call((self._w, b'scan') + args)) or ()

    def scan_mark(self, x):
        return self.scan(b'mark', x)

    def scan_dragto(self, x):
        return self.scan(b'dragto', x)

    def selection(self, *args):
        return self._getints(self.tk.call((self._w, b'selection') + args)) or ()

    def selection_adjust(self, index):
        return self.selection(b'adjust', index)

    def selection_clear(self):
        return self.selection(b'clear')

    def selection_element(self, element=None):
        return self.tk.call(self._w, b'selection', b'element', element)


class LabelFrame(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'labelframe', cnf, kw)
        return


class PanedWindow(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'panedwindow', cnf, kw)
        return

    def add(self, child, **kw):
        self.tk.call((self._w, b'add', child) + self._options(kw))
        return

    def remove(self, child):
        self.tk.call(self._w, b'forget', child)
        return

    forget = remove

    def identify(self, x, y):
        return self.tk.call(self._w, b'identify', x, y)

    def proxy(self, *args):
        return self._getints(self.tk.call((self._w, b'proxy') + args)) or ()

    def proxy_coord(self):
        return self.proxy(b'coord')

    def proxy_forget(self):
        return self.proxy(b'forget')

    def proxy_place(self, x, y):
        return self.proxy(b'place', x, y)

    def sash(self, *args):
        return self._getints(self.tk.call((self._w, b'sash') + args)) or ()

    def sash_coord(self, index):
        return self.sash(b'coord', index)

    def sash_mark(self, index):
        return self.sash(b'mark', index)

    def sash_place(self, index, x, y):
        return self.sash(b'place', index, x, y)

    def panecget(self, child, option):
        return self.tk.call((
         self._w, b'panecget') + (child, b'-' + option))

    def paneconfigure(self, tagOrId, cnf=None, **kw):
        if cnf is None and not kw:
            return self._getconfigure(self._w, b'paneconfigure', tagOrId)
        else:
            if type(cnf) == StringType and not kw:
                return self._getconfigure1(self._w, b'paneconfigure', tagOrId, b'-' + cnf)
            self.tk.call((self._w, b'paneconfigure', tagOrId) + self._options(cnf, kw))
            return

    paneconfig = paneconfigure

    def panes(self):
        return self.tk.splitlist(self.tk.call(self._w, b'panes'))


class Studbutton(Button):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'studbutton', cnf, kw)
        self.bind(b'<Any-Enter>', self.tkButtonEnter)
        self.bind(b'<Any-Leave>', self.tkButtonLeave)
        self.bind(b'<1>', self.tkButtonDown)
        self.bind(b'<ButtonRelease-1>', self.tkButtonUp)
        return


class Tributton(Button):

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, b'tributton', cnf, kw)
        self.bind(b'<Any-Enter>', self.tkButtonEnter)
        self.bind(b'<Any-Leave>', self.tkButtonLeave)
        self.bind(b'<1>', self.tkButtonDown)
        self.bind(b'<ButtonRelease-1>', self.tkButtonUp)
        self[b'fg'] = self[b'bg']
        self[b'activebackground'] = self[b'bg']
        return


def _test():
    root = Tk()
    text = b'This is Tcl/Tk version %s' % TclVersion
    if TclVersion >= 8.1:
        try:
            text = text + unicode(b'\nThis should be a cedilla: \xe7', b'iso-8859-1')
        except NameError:
            pass

    label = Label(root, text=text)
    label.pack()
    test = Button(root, text=b'Click me!', command=(lambda root=root: root.test.configure(text=b'[%s]' % root.test[b'text'])))
    test.pack()
    root.test = test
    quit = Button(root, text=b'QUIT', command=root.destroy)
    quit.pack()
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()
    return


if __name__ == b'__main__':
    _test()
