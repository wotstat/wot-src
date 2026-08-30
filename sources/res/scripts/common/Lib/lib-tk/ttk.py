__version__ = b'0.3.1'
__author__ = b'Guilherme Polo <ggpolo@gmail.com>'
__all__ = [
 2, 3, 4, 5, 6, 7, 
 8, 9, 10, 11, 12, 
 13, 14, 15, 16, 17, 
 18, 
 19, 20, 21, 
 22, 23, 
 24, 25]
import Tkinter
from Tkinter import _flatten, _join, _stringify, _splitdict
_REQUIRE_TILE = True if Tkinter.TkVersion < 8.5 else False

def _load_tile(master):
    if _REQUIRE_TILE:
        import os
        tilelib = os.environ.get(b'TILE_LIBRARY')
        if tilelib:
            master.tk.eval(b'global auto_path; lappend auto_path {%s}' % tilelib)
        master.tk.eval(b'package require tile')
        master._tile_loaded = True
    return


def _format_optvalue(value, script=False):
    if script:
        value = _stringify(value)
    elif isinstance(value, (list, tuple)):
        value = _join(value)
    return value


def _format_optdict(optdict, script=False, ignore=None):
    opts = []
    for opt, value in optdict.iteritems():
        if not ignore or opt not in ignore:
            opts.append(b'-%s' % opt)
            if value is not None:
                opts.append(_format_optvalue(value, script))

    return _flatten(opts)


def _mapdict_values(items):
    opt_val = []
    for item in items:
        state = item[:-1]
        val = item[-1]
        state[0]
        if len(state) == 1:
            state = state[0] or b''
        else:
            state = (b' ').join(state)
        opt_val.append(state)
        if val is not None:
            opt_val.append(val)

    return opt_val


def _format_mapdict(mapdict, script=False):
    opts = []
    for opt, value in mapdict.iteritems():
        opts.extend((b'-%s' % opt,
         _format_optvalue(_mapdict_values(value), script)))

    return _flatten(opts)


def _format_elemcreate(etype, script=False, *args, **kw):
    spec = None
    opts = ()
    if etype in (b'image', b'vsapi'):
        if etype == b'image':
            iname = args[0]
            imagespec = _join(_mapdict_values(args[1:]))
            spec = b'%s %s' % (iname, imagespec)
        else:
            class_name, part_id = args[:2]
            statemap = _join(_mapdict_values(args[2:]))
            spec = b'%s %s %s' % (class_name, part_id, statemap)
        opts = _format_optdict(kw, script)
    elif etype == b'from':
        spec = args[0]
        if len(args) > 1:
            opts = (
             _format_optvalue(args[1], script),)
    if script:
        spec = b'{%s}' % spec
        opts = (b' ').join(opts)
    return (spec, opts)


def _format_layoutlist(layout, indent=0, indent_size=2):
    script = []
    for layout_elem in layout:
        elem, opts = layout_elem
        opts = opts or {}
        fopts = (b' ').join(_format_optdict(opts, True, (b'children',)))
        head = b'%s%s%s' % (b' ' * indent, elem, b' %s' % fopts if fopts else b'')
        if b'children' in opts:
            script.append(head + b' -children {')
            indent += indent_size
            newscript, indent = _format_layoutlist(opts[b'children'], indent, indent_size)
            script.append(newscript)
            indent -= indent_size
            script.append(b'%s}' % (b' ' * indent))
        else:
            script.append(head)

    return (
     (b'\n').join(script), indent)


def _script_from_settings(settings):
    script = []
    for name, opts in settings.iteritems():
        if opts.get(b'configure'):
            s = (b' ').join(_format_optdict(opts[b'configure'], True))
            script.append(b'ttk::style configure %s %s;' % (name, s))
        if opts.get(b'map'):
            s = (b' ').join(_format_mapdict(opts[b'map'], True))
            script.append(b'ttk::style map %s %s;' % (name, s))
        if b'layout' in opts:
            if not opts[b'layout']:
                s = b'null'
            else:
                s, _ = _format_layoutlist(opts[b'layout'])
            script.append(b'ttk::style layout %s {\n%s\n}' % (name, s))
        if opts.get(b'element create'):
            eopts = opts[b'element create']
            etype = eopts[0]
            argc = 1
            while argc < len(eopts) and not hasattr(eopts[argc], b'iteritems'):
                argc += 1

            elemargs = eopts[1:argc]
            elemkw = eopts[argc] if argc < len(eopts) and eopts[argc] else {}
            spec, opts = _format_elemcreate(etype, True, *elemargs, **elemkw)
            script.append(b'ttk::style element create %s %s %s %s' % (
             name, etype, spec, opts))

    return (b'\n').join(script)


def _list_from_statespec(stuple):
    nval = []
    for val in stuple:
        typename = getattr(val, b'typename', None)
        if typename is None:
            nval.append(val)
        else:
            val = str(val)
            if typename == b'StateSpec':
                val = val.split()
            nval.append(val)

    it = iter(nval)
    return [_flatten(spec) for spec in zip(it, it)]


def _list_from_layouttuple(tk, ltuple):
    ltuple = tk.splitlist(ltuple)
    res = []
    indx = 0
    while indx < len(ltuple):
        name = ltuple[indx]
        opts = {}
        res.append((name, opts))
        indx += 1
        while indx < len(ltuple):
            opt, val = ltuple[indx:indx + 2]
            if not opt.startswith(b'-'):
                break
            opt = opt[1:]
            indx += 2
            if opt == b'children':
                val = _list_from_layouttuple(tk, val)
            opts[opt] = val

    return res


def _val_or_dict(tk, options, *args):
    options = _format_optdict(options)
    res = tk.call(*(args + options))
    if len(options) % 2:
        return res
    return _splitdict(tk, res, conv=_tclobj_to_py)


def _convert_stringval(value):
    value = unicode(value)
    try:
        value = int(value)
    except (ValueError, TypeError):
        pass

    return value


def _to_number(x):
    if isinstance(x, str):
        if b'.' in x:
            x = float(x)
        else:
            x = int(x)
    return x


def _tclobj_to_py(val):
    if val and hasattr(val, b'__len__') and not isinstance(val, basestring):
        if getattr(val[0], b'typename', None) == b'StateSpec':
            val = _list_from_statespec(val)
        else:
            val = map(_convert_stringval, val)
    elif hasattr(val, b'typename'):
        val = _convert_stringval(val)
    return val


def tclobjs_to_py(adict):
    for opt, val in adict.items():
        adict[opt] = _tclobj_to_py(val)

    return adict


def setup_master(master=None):
    if master is None:
        if Tkinter._support_default_root:
            master = Tkinter._default_root or Tkinter.Tk()
        else:
            raise RuntimeError(b'No master specified and Tkinter is configured to not support default root')
    return master


class Style(object):
    _name = b'ttk::style'

    def __init__(self, master=None):
        master = setup_master(master)
        if not getattr(master, b'_tile_loaded', False):
            _load_tile(master)
        self.master = master
        self.tk = self.master.tk
        return

    def configure(self, style, query_opt=None, **kw):
        if query_opt is not None:
            kw[query_opt] = None
        return _val_or_dict(self.tk, kw, self._name, b'configure', style)

    def map(self, style, query_opt=None, **kw):
        if query_opt is not None:
            return _list_from_statespec(self.tk.splitlist(self.tk.call(self._name, b'map', style, b'-%s' % query_opt)))
        else:
            return _splitdict(self.tk, self.tk.call(self._name, b'map', style, *_format_mapdict(kw)), conv=_tclobj_to_py)

    def lookup(self, style, option, state=None, default=None):
        state = (b' ').join(state) if state else b''
        return self.tk.call(self._name, b'lookup', style, b'-%s' % option, state, default)

    def layout(self, style, layoutspec=None):
        lspec = None
        if layoutspec:
            lspec = _format_layoutlist(layoutspec)[0]
        elif layoutspec is not None:
            lspec = b'null'
        return _list_from_layouttuple(self.tk, self.tk.call(self._name, b'layout', style, lspec))

    def element_create(self, elementname, etype, *args, **kw):
        spec, opts = _format_elemcreate(etype, False, *args, **kw)
        self.tk.call(self._name, b'element', b'create', elementname, etype, spec, *opts)
        return

    def element_names(self):
        return self.tk.splitlist(self.tk.call(self._name, b'element', b'names'))

    def element_options(self, elementname):
        return self.tk.splitlist(self.tk.call(self._name, b'element', b'options', elementname))

    def theme_create(self, themename, parent=None, settings=None):
        script = _script_from_settings(settings) if settings else b''
        if parent:
            self.tk.call(self._name, b'theme', b'create', themename, b'-parent', parent, b'-settings', script)
        else:
            self.tk.call(self._name, b'theme', b'create', themename, b'-settings', script)
        return

    def theme_settings(self, themename, settings):
        script = _script_from_settings(settings)
        self.tk.call(self._name, b'theme', b'settings', themename, script)
        return

    def theme_names(self):
        return self.tk.splitlist(self.tk.call(self._name, b'theme', b'names'))

    def theme_use(self, themename=None):
        if themename is None:
            return self.tk.eval(b'return $ttk::currentTheme')
        else:
            self.tk.call(b'ttk::setTheme', themename)
            return


class Widget(Tkinter.Widget):

    def __init__(self, master, widgetname, kw=None):
        master = setup_master(master)
        if not getattr(master, b'_tile_loaded', False):
            _load_tile(master)
        Tkinter.Widget.__init__(self, master, widgetname, kw=kw)
        return

    def identify(self, x, y):
        return self.tk.call(self._w, b'identify', x, y)

    def instate(self, statespec, callback=None, *args, **kw):
        ret = self.tk.getboolean(self.tk.call(self._w, b'instate', (b' ').join(statespec)))
        if ret and callback:
            return callback(*args, **kw)
        return ret

    def state(self, statespec=None):
        if statespec is not None:
            statespec = (b' ').join(statespec)
        return self.tk.splitlist(str(self.tk.call(self._w, b'state', statespec)))


class Button(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::button', kw)
        return

    def invoke(self):
        return self.tk.call(self._w, b'invoke')


class Checkbutton(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::checkbutton', kw)
        return

    def invoke(self):
        return self.tk.call(self._w, b'invoke')


class Entry(Widget, Tkinter.Entry):

    def __init__(self, master=None, widget=None, **kw):
        Widget.__init__(self, master, widget or b'ttk::entry', kw)
        return

    def bbox(self, index):
        return self._getints(self.tk.call(self._w, b'bbox', index))

    def identify(self, x, y):
        return self.tk.call(self._w, b'identify', x, y)

    def validate(self):
        return self.tk.getboolean(self.tk.call(self._w, b'validate'))


class Combobox(Entry):

    def __init__(self, master=None, **kw):
        Entry.__init__(self, master, b'ttk::combobox', **kw)
        return

    def current(self, newindex=None):
        if newindex is None:
            return self.tk.getint(self.tk.call(self._w, b'current'))
        else:
            return self.tk.call(self._w, b'current', newindex)

    def set(self, value):
        self.tk.call(self._w, b'set', value)
        return


class Frame(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::frame', kw)
        return


class Label(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::label', kw)
        return


class Labelframe(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::labelframe', kw)
        return


LabelFrame = Labelframe

class Menubutton(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::menubutton', kw)
        return


class Notebook(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::notebook', kw)
        return

    def add(self, child, **kw):
        self.tk.call(self._w, b'add', child, *_format_optdict(kw))
        return

    def forget(self, tab_id):
        self.tk.call(self._w, b'forget', tab_id)
        return

    def hide(self, tab_id):
        self.tk.call(self._w, b'hide', tab_id)
        return

    def identify(self, x, y):
        return self.tk.call(self._w, b'identify', x, y)

    def index(self, tab_id):
        return self.tk.getint(self.tk.call(self._w, b'index', tab_id))

    def insert(self, pos, child, **kw):
        self.tk.call(self._w, b'insert', pos, child, *_format_optdict(kw))
        return

    def select(self, tab_id=None):
        return self.tk.call(self._w, b'select', tab_id)

    def tab(self, tab_id, option=None, **kw):
        if option is not None:
            kw[option] = None
        return _val_or_dict(self.tk, kw, self._w, b'tab', tab_id)

    def tabs(self):
        return self.tk.splitlist(self.tk.call(self._w, b'tabs') or ())

    def enable_traversal(self):
        self.tk.call(b'ttk::notebook::enableTraversal', self._w)
        return


class Panedwindow(Widget, Tkinter.PanedWindow):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::panedwindow', kw)
        return

    forget = Tkinter.PanedWindow.forget

    def insert(self, pos, child, **kw):
        self.tk.call(self._w, b'insert', pos, child, *_format_optdict(kw))
        return

    def pane(self, pane, option=None, **kw):
        if option is not None:
            kw[option] = None
        return _val_or_dict(self.tk, kw, self._w, b'pane', pane)

    def sashpos(self, index, newpos=None):
        return self.tk.getint(self.tk.call(self._w, b'sashpos', index, newpos))


PanedWindow = Panedwindow

class Progressbar(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::progressbar', kw)
        return

    def start(self, interval=None):
        self.tk.call(self._w, b'start', interval)
        return

    def step(self, amount=None):
        self.tk.call(self._w, b'step', amount)
        return

    def stop(self):
        self.tk.call(self._w, b'stop')
        return


class Radiobutton(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::radiobutton', kw)
        return

    def invoke(self):
        return self.tk.call(self._w, b'invoke')


class Scale(Widget, Tkinter.Scale):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::scale', kw)
        return

    def configure(self, cnf=None, **kw):
        if cnf:
            kw.update(cnf)
        Widget.configure(self, **kw)
        if any([b'from' in kw, b'from_' in kw, b'to' in kw]):
            self.event_generate(b'<<RangeChanged>>')
        return

    def get(self, x=None, y=None):
        return self.tk.call(self._w, b'get', x, y)


class Scrollbar(Widget, Tkinter.Scrollbar):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::scrollbar', kw)
        return


class Separator(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::separator', kw)
        return


class Sizegrip(Widget):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::sizegrip', kw)
        return


class Treeview(Widget, Tkinter.XView, Tkinter.YView):

    def __init__(self, master=None, **kw):
        Widget.__init__(self, master, b'ttk::treeview', kw)
        return

    def bbox(self, item, column=None):
        return self._getints(self.tk.call(self._w, b'bbox', item, column)) or b''

    def get_children(self, item=None):
        return self.tk.splitlist(self.tk.call(self._w, b'children', item or b'') or ())

    def set_children(self, item, *newchildren):
        self.tk.call(self._w, b'children', item, newchildren)
        return

    def column(self, column, option=None, **kw):
        if option is not None:
            kw[option] = None
        return _val_or_dict(self.tk, kw, self._w, b'column', column)

    def delete(self, *items):
        self.tk.call(self._w, b'delete', items)
        return

    def detach(self, *items):
        self.tk.call(self._w, b'detach', items)
        return

    def exists(self, item):
        return self.tk.getboolean(self.tk.call(self._w, b'exists', item))

    def focus(self, item=None):
        return self.tk.call(self._w, b'focus', item)

    def heading(self, column, option=None, **kw):
        cmd = kw.get(b'command')
        if cmd and not isinstance(cmd, basestring):
            kw[b'command'] = self.master.register(cmd, self._substitute)
        if option is not None:
            kw[option] = None
        return _val_or_dict(self.tk, kw, self._w, b'heading', column)

    def identify(self, component, x, y):
        return self.tk.call(self._w, b'identify', component, x, y)

    def identify_row(self, y):
        return self.identify(b'row', 0, y)

    def identify_column(self, x):
        return self.identify(b'column', x, 0)

    def identify_region(self, x, y):
        return self.identify(b'region', x, y)

    def identify_element(self, x, y):
        return self.identify(b'element', x, y)

    def index(self, item):
        return self.tk.getint(self.tk.call(self._w, b'index', item))

    def insert(self, parent, index, iid=None, **kw):
        opts = _format_optdict(kw)
        if iid is not None:
            res = self.tk.call(self._w, b'insert', parent, index, b'-id', iid, *opts)
        else:
            res = self.tk.call(self._w, b'insert', parent, index, *opts)
        return res

    def item(self, item, option=None, **kw):
        if option is not None:
            kw[option] = None
        return _val_or_dict(self.tk, kw, self._w, b'item', item)

    def move(self, item, parent, index):
        self.tk.call(self._w, b'move', item, parent, index)
        return

    reattach = move

    def next(self, item):
        return self.tk.call(self._w, b'next', item)

    def parent(self, item):
        return self.tk.call(self._w, b'parent', item)

    def prev(self, item):
        return self.tk.call(self._w, b'prev', item)

    def see(self, item):
        self.tk.call(self._w, b'see', item)
        return

    def selection(self, selop=None, items=None):
        if isinstance(items, basestring):
            items = (
             items,)
        return self.tk.splitlist(self.tk.call(self._w, b'selection', selop, items))

    def selection_set(self, items):
        self.selection(b'set', items)
        return

    def selection_add(self, items):
        self.selection(b'add', items)
        return

    def selection_remove(self, items):
        self.selection(b'remove', items)
        return

    def selection_toggle(self, items):
        self.selection(b'toggle', items)
        return

    def set(self, item, column=None, value=None):
        res = self.tk.call(self._w, b'set', item, column, value)
        if column is None and value is None:
            return _splitdict(self.tk, res, cut_minus=False, conv=_tclobj_to_py)
        else:
            return res
            return

    def tag_bind(self, tagname, sequence=None, callback=None):
        self._bind((self._w, b'tag', b'bind', tagname), sequence, callback, add=0)
        return

    def tag_configure(self, tagname, option=None, **kw):
        if option is not None:
            kw[option] = None
        return _val_or_dict(self.tk, kw, self._w, b'tag', b'configure', tagname)

    def tag_has(self, tagname, item=None):
        if item is None:
            return self.tk.splitlist(self.tk.call(self._w, b'tag', b'has', tagname))
        else:
            return self.tk.getboolean(self.tk.call(self._w, b'tag', b'has', tagname, item))
            return


class LabeledScale(Frame, object):

    def __init__(self, master=None, variable=None, from_=0, to=10, **kw):
        self._label_top = kw.pop(b'compound', b'top') == b'top'
        Frame.__init__(self, master, **kw)
        self._variable = variable or Tkinter.IntVar(master)
        self._variable.set(from_)
        self._last_valid = from_
        self.label = Label(self)
        self.scale = Scale(self, variable=self._variable, from_=from_, to=to)
        self.scale.bind(b'<<RangeChanged>>', self._adjust)
        scale_side = b'bottom' if self._label_top else b'top'
        label_side = b'top' if scale_side == b'bottom' else b'bottom'
        self.scale.pack(side=scale_side, fill=b'x')
        tmp = Label(self).pack(side=label_side)
        self.label.place(anchor=b'n' if label_side == b'top' else b's')
        self.__tracecb = self._variable.trace_variable(b'w', self._adjust)
        self.bind(b'<Configure>', self._adjust)
        self.bind(b'<Map>', self._adjust)
        return

    def destroy(self):
        try:
            self._variable.trace_vdelete(b'w', self.__tracecb)
        except AttributeError:
            pass
        else:
            del self._variable

        Frame.destroy(self)
        self.label = None
        self.scale = None
        return

    def _adjust(self, *args):

        def adjust_label():
            self.update_idletasks()
            x, y = self.scale.coords()
            if self._label_top:
                y = self.scale.winfo_y() - self.label.winfo_reqheight()
            else:
                y = self.scale.winfo_reqheight() + self.label.winfo_reqheight()
            self.label.place_configure(x=x, y=y)
            return

        from_ = _to_number(self.scale[b'from'])
        to = _to_number(self.scale[b'to'])
        if to < from_:
            from_, to = to, from_
        newval = self._variable.get()
        if not from_ <= newval <= to:
            self.value = self._last_valid
            return
        self._last_valid = newval
        self.label[b'text'] = newval
        self.after_idle(adjust_label)
        return

    def _get_value(self):
        return self._variable.get()

    def _set_value(self, val):
        self._variable.set(val)
        return

    value = property(_get_value, _set_value)


class OptionMenu(Menubutton):

    def __init__(self, master, variable, default=None, *values, **kwargs):
        kw = {b'textvariable': variable, b'style': (kwargs.pop(b'style', None)), b'direction': (kwargs.pop(b'direction', None))}
        Menubutton.__init__(self, master, **kw)
        self[b'menu'] = Tkinter.Menu(self, tearoff=False)
        self._variable = variable
        self._callback = kwargs.pop(b'command', None)
        if kwargs:
            raise Tkinter.TclError(b'unknown option -%s' % kwargs.iterkeys().next())
        self.set_menu(default, *values)
        return

    def __getitem__(self, item):
        if item == b'menu':
            return self.nametowidget(Menubutton.__getitem__(self, item))
        return Menubutton.__getitem__(self, item)

    def set_menu(self, default=None, *values):
        menu = self[b'menu']
        menu.delete(0, b'end')
        for val in values:
            menu.add_radiobutton(label=val, command=Tkinter._setit(self._variable, val, self._callback), variable=self._variable)

        if default:
            self._variable.set(default)
        return

    def destroy(self):
        try:
            del self._variable
        except AttributeError:
            pass

        Menubutton.destroy(self)
        return
