from warnings import warnpy3k
warnpy3k(b'the Canvas module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
from Tkinter import Canvas, _cnfmerge, _flatten

class CanvasItem:

    def __init__(self, canvas, itemType, *args, **kw):
        self.canvas = canvas
        self.id = canvas._create(itemType, args, kw)
        if not hasattr(canvas, b'items'):
            canvas.items = {}
        canvas.items[self.id] = self
        return

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return b'<%s, id=%d>' % (self.__class__.__name__, self.id)

    def delete(self):
        del self.canvas.items[self.id]
        self.canvas.delete(self.id)
        return

    def __getitem__(self, key):
        v = self.canvas.tk.split(self.canvas.tk.call(self.canvas._w, b'itemconfigure', self.id, b'-' + key))
        return v[4]

    cget = __getitem__

    def __setitem__(self, key, value):
        self.canvas.itemconfig(self.id, {key: value})
        return

    def keys(self):
        if not hasattr(self, b'_keys'):
            self._keys = map((lambda x, tk=self.canvas.tk: tk.splitlist(x)[0][1:]), self.canvas.tk.splitlist(self.canvas._do(b'itemconfigure', (
             self.id,))))
        return self._keys

    def has_key(self, key):
        return key in self.keys()

    def __contains__(self, key):
        return key in self.keys()

    def addtag(self, tag, option=b'withtag'):
        self.canvas.addtag(tag, option, self.id)
        return

    def bbox(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.id)
        return ((x1, y1), (x2, y2))

    def bind(self, sequence=None, command=None, add=None):
        return self.canvas.tag_bind(self.id, sequence, command, add)

    def unbind(self, sequence, funcid=None):
        self.canvas.tag_unbind(self.id, sequence, funcid)
        return

    def config(self, cnf={}, **kw):
        return self.canvas.itemconfig(self.id, _cnfmerge((cnf, kw)))

    def coords(self, pts=()):
        flat = ()
        for x, y in pts:
            flat = flat + (x, y)

        return self.canvas.coords(self.id, *flat)

    def dchars(self, first, last=None):
        self.canvas.dchars(self.id, first, last)
        return

    def dtag(self, ttd):
        self.canvas.dtag(self.id, ttd)
        return

    def focus(self):
        self.canvas.focus(self.id)
        return

    def gettags(self):
        return self.canvas.gettags(self.id)

    def icursor(self, index):
        self.canvas.icursor(self.id, index)
        return

    def index(self, index):
        return self.canvas.index(self.id, index)

    def insert(self, beforethis, string):
        self.canvas.insert(self.id, beforethis, string)
        return

    def lower(self, belowthis=None):
        self.canvas.tag_lower(self.id, belowthis)
        return

    def move(self, xamount, yamount):
        self.canvas.move(self.id, xamount, yamount)
        return

    def tkraise(self, abovethis=None):
        self.canvas.tag_raise(self.id, abovethis)
        return

    raise_ = tkraise

    def scale(self, xorigin, yorigin, xscale, yscale):
        self.canvas.scale(self.id, xorigin, yorigin, xscale, yscale)
        return

    def type(self):
        return self.canvas.type(self.id)


class Arc(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'arc', *args, **kw)
        return


class Bitmap(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'bitmap', *args, **kw)
        return


class ImageItem(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'image', *args, **kw)
        return


class Line(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'line', *args, **kw)
        return


class Oval(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'oval', *args, **kw)
        return


class Polygon(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'polygon', *args, **kw)
        return


class Rectangle(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'rectangle', *args, **kw)
        return


class CanvasText(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'text', *args, **kw)
        return


class Window(CanvasItem):

    def __init__(self, canvas, *args, **kw):
        CanvasItem.__init__(self, canvas, b'window', *args, **kw)
        return


class Group:

    def __init__(self, canvas, tag=None):
        if not tag:
            tag = b'Group%d' % id(self)
        self.tag = self.id = tag
        self.canvas = canvas
        self.canvas.dtag(self.tag)
        return

    def str(self):
        return self.tag

    __str__ = str

    def _do(self, cmd, *args):
        return self.canvas._do(cmd, (self.tag,) + _flatten(args))

    def addtag_above(self, tagOrId):
        self._do(b'addtag', b'above', tagOrId)
        return

    def addtag_all(self):
        self._do(b'addtag', b'all')
        return

    def addtag_below(self, tagOrId):
        self._do(b'addtag', b'below', tagOrId)
        return

    def addtag_closest(self, x, y, halo=None, start=None):
        self._do(b'addtag', b'closest', x, y, halo, start)
        return

    def addtag_enclosed(self, x1, y1, x2, y2):
        self._do(b'addtag', b'enclosed', x1, y1, x2, y2)
        return

    def addtag_overlapping(self, x1, y1, x2, y2):
        self._do(b'addtag', b'overlapping', x1, y1, x2, y2)
        return

    def addtag_withtag(self, tagOrId):
        self._do(b'addtag', b'withtag', tagOrId)
        return

    def bbox(self):
        return self.canvas._getints(self._do(b'bbox'))

    def bind(self, sequence=None, command=None, add=None):
        return self.canvas.tag_bind(self.id, sequence, command, add)

    def unbind(self, sequence, funcid=None):
        self.canvas.tag_unbind(self.id, sequence, funcid)
        return

    def coords(self, *pts):
        return self._do(b'coords', pts)

    def dchars(self, first, last=None):
        self._do(b'dchars', first, last)
        return

    def delete(self):
        self._do(b'delete')
        return

    def dtag(self, tagToDelete=None):
        self._do(b'dtag', tagToDelete)
        return

    def focus(self):
        self._do(b'focus')
        return

    def gettags(self):
        return self.canvas.tk.splitlist(self._do(b'gettags', self.tag))

    def icursor(self, index):
        return self._do(b'icursor', index)

    def index(self, index):
        return self.canvas.tk.getint(self._do(b'index', index))

    def insert(self, beforeThis, string):
        self._do(b'insert', beforeThis, string)
        return

    def config(self, cnf={}, **kw):
        return self.canvas.itemconfigure(self.tag, _cnfmerge((cnf, kw)))

    def lower(self, belowThis=None):
        self._do(b'lower', belowThis)
        return

    def move(self, xAmount, yAmount):
        self._do(b'move', xAmount, yAmount)
        return

    def tkraise(self, aboveThis=None):
        self._do(b'raise', aboveThis)
        return

    lift = tkraise

    def scale(self, xOrigin, yOrigin, xScale, yScale):
        self._do(b'scale', xOrigin, yOrigin, xScale, yScale)
        return

    def select_adjust(self, index):
        self.canvas._do(b'select', (b'adjust', self.tag, index))
        return

    def select_from(self, index):
        self.canvas._do(b'select', (b'from', self.tag, index))
        return

    def select_to(self, index):
        self.canvas._do(b'select', (b'to', self.tag, index))
        return

    def type(self):
        return self._do(b'type')
