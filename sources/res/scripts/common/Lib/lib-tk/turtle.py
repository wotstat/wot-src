_ver = b'turtle 1.0b1 - for Python 2.6   -  30. 5. 2008, 18:08'
import Tkinter as TK, types, math, time, os
from os.path import isfile, split, join
from copy import deepcopy
from math import *
_tg_classes = [
 6, 7, 8, 
 9, 10, 11, 12, 13, 14]
_tg_screen_functions = [15, 16, 17, 18, 
 19, 20, 21, 22, 23, 
 24, 25, 26, 27, 28, 29, 
 30, 
 31, 32, 33, 
 34, 35, 36, 37, 38, 
 39, 40]
_tg_turtle_functions = [41, 42, 43, 44, 45, 
 46, 47, 48, 49, 50, 51, 
 52, 53, 54, 55, 56, 
 57, 58, 
 59, 60, 61, 62, 63, 64, 
 65, 66, 67, 68, 69, 70, 71, 
 72, 
 73, 74, 75, 76, 77, 78, 
 79, 80, 81, 82, 83, 84, 85, 
 86, 87, 
 88, 89, 90, 91, 
 92, 93, 94, 95, 96, 
 97, 98, 99, 100, 101, 
 102, 
 103, 104, 105, 106, 107, 108, 36, 
 109, 110, 111, 112, 113, 
 39, 
 40, 114, 115, 116]
_tg_utilities = [b'write_docstringdict', b'done', b'mainloop']
_math_functions = [120, 121, 122, 123, 124, 125, 126, 
 127, 128, 129, 130, 131, 132, 133, 
 134, 135, 
 136, 137, 138, 139, 140, 141, 142, 143, 144]
__all__ = _tg_classes + _tg_screen_functions + _tg_turtle_functions + _tg_utilities + [b'Terminator'] + _math_functions
_alias_list = [
 15, 42, 45, 58, 70, 74, 78, 84, 
 86, 91, 92, 94, 95, 104, 
 109, 
 112, 113]
_CFG = {b'width': 0.5, b'height': 0.75, 
   b'canvwidth': 400, 
   b'canvheight': 300, 
   b'leftright': None, 
   b'topbottom': None, 
   b'mode': b'standard', 
   b'colormode': 1.0, 
   b'delay': 10, 
   b'undobuffersize': 1000, 
   b'shape': b'classic', 
   b'pencolor': b'black', 
   b'fillcolor': b'black', 
   b'resizemode': b'noresize', 
   b'visible': True, 
   b'language': b'english', 
   b'exampleturtle': b'turtle', 
   b'examplescreen': b'screen', 
   b'title': b'Python Turtle Graphics', 
   b'using_IDLE': False}

def config_dict(filename):
    f = open(filename, b'r')
    cfglines = f.readlines()
    f.close()
    cfgdict = {}
    for line in cfglines:
        line = line.strip()
        if not line or line.startswith(b'#'):
            continue
        try:
            key, value = line.split(b'=')
        except ValueError:
            print b'Bad line in config-file %s:\n%s' % (filename, line)
            continue

        key = key.strip()
        value = value.strip()
        if value in (b'True', b'False', b'None', b"''", b'""'):
            value = eval(value)
        else:
            try:
                if b'.' in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                pass

        cfgdict[key] = value

    return cfgdict


def readconfig(cfgdict):
    default_cfg = b'turtle.cfg'
    cfgdict1 = {}
    cfgdict2 = {}
    if isfile(default_cfg):
        cfgdict1 = config_dict(default_cfg)
    if b'importconfig' in cfgdict1:
        default_cfg = b'turtle_%s.cfg' % cfgdict1[b'importconfig']
    try:
        head, tail = split(__file__)
        cfg_file2 = join(head, default_cfg)
    except BaseException:
        cfg_file2 = b''

    if isfile(cfg_file2):
        cfgdict2 = config_dict(cfg_file2)
    _CFG.update(cfgdict2)
    _CFG.update(cfgdict1)
    return


try:
    readconfig(_CFG)
except BaseException:
    print b'No configfile read, reason unknown'

class Vec2D(tuple):

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    def __add__(self, other):
        return Vec2D(self[0] + other[0], self[1] + other[1])

    def __mul__(self, other):
        if isinstance(other, Vec2D):
            return self[0] * other[0] + self[1] * other[1]
        return Vec2D(self[0] * other, self[1] * other)

    def __rmul__(self, other):
        if isinstance(other, (int, long, float)):
            return Vec2D(self[0] * other, self[1] * other)
        return

    def __sub__(self, other):
        return Vec2D(self[0] - other[0], self[1] - other[1])

    def __neg__(self):
        return Vec2D(-self[0], -self[1])

    def __abs__(self):
        return (self[0] ** 2 + self[1] ** 2) ** 0.5

    def rotate(self, angle):
        perp = Vec2D(-self[1], self[0])
        angle = angle * math.pi / 180.0
        c, s = math.cos(angle), math.sin(angle)
        return Vec2D(self[0] * c + perp[0] * s, self[1] * c + perp[1] * s)

    def __getnewargs__(self):
        return (self[0], self[1])

    def __repr__(self):
        return b'(%.2f,%.2f)' % self


def __methodDict(cls, _dict):
    baseList = list(cls.__bases__)
    baseList.reverse()
    for _super in baseList:
        __methodDict(_super, _dict)

    for key, value in cls.__dict__.items():
        if type(value) == types.FunctionType:
            _dict[key] = value

    return


def __methods(cls):
    _dict = {}
    __methodDict(cls, _dict)
    return _dict.keys()


__stringBody = b'def %(method)s(self, *args, **kw): return ' + b'self.%(attribute)s.%(method)s(*args, **kw)'

def __forwardmethods(fromClass, toClass, toPart, exclude=()):
    _dict = {}
    __methodDict(toClass, _dict)
    for ex in _dict.keys():
        if ex[:1] == b'_' or ex[-1:] == b'_':
            del _dict[ex]

    for ex in exclude:
        if ex in _dict:
            del _dict[ex]

    for ex in __methods(fromClass):
        if ex in _dict:
            del _dict[ex]

    for method, func in _dict.items():
        d = {b'method': method, b'func': func}
        if type(toPart) == types.StringType:
            execString = __stringBody % {b'method': method, b'attribute': toPart}
        exec execString in d
        fromClass.__dict__[method] = d[method]

    return


class ScrolledCanvas(TK.Frame):

    def __init__(self, master, width=500, height=350, canvwidth=600, canvheight=500):
        TK.Frame.__init__(self, master, width=width, height=height)
        self._rootwindow = self.winfo_toplevel()
        self.width, self.height = width, height
        self.canvwidth, self.canvheight = canvwidth, canvheight
        self.bg = b'white'
        self._canvas = TK.Canvas(master, width=width, height=height, bg=self.bg, relief=TK.SUNKEN, borderwidth=2)
        self.hscroll = TK.Scrollbar(master, command=self._canvas.xview, orient=TK.HORIZONTAL)
        self.vscroll = TK.Scrollbar(master, command=self._canvas.yview)
        self._canvas.configure(xscrollcommand=self.hscroll.set, yscrollcommand=self.vscroll.set)
        self.rowconfigure(0, weight=1, minsize=0)
        self.columnconfigure(0, weight=1, minsize=0)
        self._canvas.grid(padx=1, in_=self, pady=1, row=0, column=0, rowspan=1, columnspan=1, sticky=b'news')
        self.vscroll.grid(padx=1, in_=self, pady=1, row=0, column=1, rowspan=1, columnspan=1, sticky=b'news')
        self.hscroll.grid(padx=1, in_=self, pady=1, row=1, column=0, rowspan=1, columnspan=1, sticky=b'news')
        self.reset()
        self._rootwindow.bind(b'<Configure>', self.onResize)
        return

    def reset(self, canvwidth=None, canvheight=None, bg=None):
        if canvwidth:
            self.canvwidth = canvwidth
        if canvheight:
            self.canvheight = canvheight
        if bg:
            self.bg = bg
        self._canvas.config(bg=bg, scrollregion=(
         -self.canvwidth // 2, -self.canvheight // 2,
         self.canvwidth // 2, self.canvheight // 2))
        self._canvas.xview_moveto(0.5 * (self.canvwidth - self.width + 30) / self.canvwidth)
        self._canvas.yview_moveto(0.5 * (self.canvheight - self.height + 30) / self.canvheight)
        self.adjustScrolls()
        return

    def adjustScrolls(self):
        cwidth = self._canvas.winfo_width()
        cheight = self._canvas.winfo_height()
        self._canvas.xview_moveto(0.5 * (self.canvwidth - cwidth) / self.canvwidth)
        self._canvas.yview_moveto(0.5 * (self.canvheight - cheight) / self.canvheight)
        if cwidth < self.canvwidth or cheight < self.canvheight:
            self.hscroll.grid(padx=1, in_=self, pady=1, row=1, column=0, rowspan=1, columnspan=1, sticky=b'news')
            self.vscroll.grid(padx=1, in_=self, pady=1, row=0, column=1, rowspan=1, columnspan=1, sticky=b'news')
        else:
            self.hscroll.grid_forget()
            self.vscroll.grid_forget()
        return

    def onResize(self, event):
        self.adjustScrolls()
        return

    def bbox(self, *args):
        return self._canvas.bbox(*args)

    def cget(self, *args, **kwargs):
        return self._canvas.cget(*args, **kwargs)

    def config(self, *args, **kwargs):
        self._canvas.config(*args, **kwargs)
        return

    def bind(self, *args, **kwargs):
        self._canvas.bind(*args, **kwargs)
        return

    def unbind(self, *args, **kwargs):
        self._canvas.unbind(*args, **kwargs)
        return

    def focus_force(self):
        self._canvas.focus_force()
        return


__forwardmethods(ScrolledCanvas, TK.Canvas, b'_canvas')

class _Root(TK.Tk):

    def __init__(self):
        TK.Tk.__init__(self)
        return

    def setupcanvas(self, width, height, cwidth, cheight):
        self._canvas = ScrolledCanvas(self, width, height, cwidth, cheight)
        self._canvas.pack(expand=1, fill=b'both')
        return

    def _getcanvas(self):
        return self._canvas

    def set_geometry(self, width, height, startx, starty):
        self.geometry(b'%dx%d%+d%+d' % (width, height, startx, starty))
        return

    def ondestroy(self, destroy):
        self.wm_protocol(b'WM_DELETE_WINDOW', destroy)
        return

    def win_width(self):
        return self.winfo_screenwidth()

    def win_height(self):
        return self.winfo_screenheight()


Canvas = TK.Canvas

class TurtleScreenBase(object):

    @staticmethod
    def _blankimage():
        img = TK.PhotoImage(width=1, height=1)
        img.blank()
        return img

    @staticmethod
    def _image(filename):
        return TK.PhotoImage(file=filename)

    def __init__(self, cv):
        self.cv = cv
        if isinstance(cv, ScrolledCanvas):
            w = self.cv.canvwidth
            h = self.cv.canvheight
        else:
            w = int(self.cv.cget(b'width'))
            h = int(self.cv.cget(b'height'))
            self.cv.config(scrollregion=(-w // 2, -h // 2, w // 2, h // 2))
        self.canvwidth = w
        self.canvheight = h
        self.xscale = self.yscale = 1.0
        return

    def _createpoly(self):
        return self.cv.create_polygon((0, 0, 0, 0, 0, 0), fill=b'', outline=b'')

    def _drawpoly(self, polyitem, coordlist, fill=None, outline=None, width=None, top=False):
        cl = []
        for x, y in coordlist:
            cl.append(x * self.xscale)
            cl.append(-y * self.yscale)

        self.cv.coords(polyitem, *cl)
        if fill is not None:
            self.cv.itemconfigure(polyitem, fill=fill)
        if outline is not None:
            self.cv.itemconfigure(polyitem, outline=outline)
        if width is not None:
            self.cv.itemconfigure(polyitem, width=width)
        if top:
            self.cv.tag_raise(polyitem)
        return

    def _createline(self):
        return self.cv.create_line(0, 0, 0, 0, fill=b'', width=2, capstyle=TK.ROUND)

    def _drawline(self, lineitem, coordlist=None, fill=None, width=None, top=False):
        if coordlist is not None:
            cl = []
            for x, y in coordlist:
                cl.append(x * self.xscale)
                cl.append(-y * self.yscale)

            self.cv.coords(lineitem, *cl)
        if fill is not None:
            self.cv.itemconfigure(lineitem, fill=fill)
        if width is not None:
            self.cv.itemconfigure(lineitem, width=width)
        if top:
            self.cv.tag_raise(lineitem)
        return

    def _delete(self, item):
        self.cv.delete(item)
        return

    def _update(self):
        self.cv.update()
        return

    def _delay(self, delay):
        self.cv.after(delay)
        return

    def _iscolorstring(self, color):
        try:
            rgb = self.cv.winfo_rgb(color)
            ok = True
        except TK.TclError:
            ok = False

        return ok

    def _bgcolor(self, color=None):
        if color is not None:
            self.cv.config(bg=color)
            self._update()
        else:
            return self.cv.cget(b'bg')
        return

    def _write(self, pos, txt, align, font, pencolor):
        x, y = pos
        x = x * self.xscale
        y = y * self.yscale
        anchor = {b'left': b'sw', b'center': b's', b'right': b'se'}
        item = self.cv.create_text(x - 1, -y, text=txt, anchor=anchor[align], fill=pencolor, font=font)
        x0, y0, x1, y1 = self.cv.bbox(item)
        self.cv.update()
        return (item, x1 - 1)

    def _onclick(self, item, fun, num=1, add=None):
        if fun is None:
            self.cv.tag_unbind(item, b'<Button-%s>' % num)
        else:

            def eventfun(event):
                x, y = self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale
                fun(x, y)
                return

            self.cv.tag_bind(item, b'<Button-%s>' % num, eventfun, add)
        return

    def _onrelease(self, item, fun, num=1, add=None):
        if fun is None:
            self.cv.tag_unbind(item, b'<Button%s-ButtonRelease>' % num)
        else:

            def eventfun(event):
                x, y = self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale
                fun(x, y)
                return

            self.cv.tag_bind(item, b'<Button%s-ButtonRelease>' % num, eventfun, add)
        return

    def _ondrag(self, item, fun, num=1, add=None):
        if fun is None:
            self.cv.tag_unbind(item, b'<Button%s-Motion>' % num)
        else:

            def eventfun(event):
                try:
                    x, y = self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale
                    fun(x, y)
                except BaseException:
                    pass

                return

            self.cv.tag_bind(item, b'<Button%s-Motion>' % num, eventfun, add)
        return

    def _onscreenclick(self, fun, num=1, add=None):
        if fun is None:
            self.cv.unbind(b'<Button-%s>' % num)
        else:

            def eventfun(event):
                x, y = self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale
                fun(x, y)
                return

            self.cv.bind(b'<Button-%s>' % num, eventfun, add)
        return

    def _onkey(self, fun, key):
        if fun is None:
            self.cv.unbind(b'<KeyRelease-%s>' % key, None)
        else:

            def eventfun(event):
                fun()
                return

            self.cv.bind(b'<KeyRelease-%s>' % key, eventfun)
        return

    def _listen(self):
        self.cv.focus_force()
        return

    def _ontimer(self, fun, t):
        if t == 0:
            self.cv.after_idle(fun)
        else:
            self.cv.after(t, fun)
        return

    def _createimage(self, image):
        return self.cv.create_image(0, 0, image=image)

    def _drawimage(self, item, pos, image):
        x, y = pos
        self.cv.coords(item, (x * self.xscale, -y * self.yscale))
        self.cv.itemconfig(item, image=image)
        return

    def _setbgpic(self, item, image):
        self.cv.itemconfig(item, image=image)
        self.cv.tag_lower(item)
        return

    def _type(self, item):
        return self.cv.type(item)

    def _pointlist(self, item):
        cl = self.cv.coords(item)
        pl = [(cl[i], -cl[i + 1]) for i in range(0, len(cl), 2)]
        return pl

    def _setscrollregion(self, srx1, sry1, srx2, sry2):
        self.cv.config(scrollregion=(srx1, sry1, srx2, sry2))
        return

    def _rescale(self, xscalefactor, yscalefactor):
        items = self.cv.find_all()
        for item in items:
            coordinates = self.cv.coords(item)
            newcoordlist = []
            while coordinates:
                x, y = coordinates[:2]
                newcoordlist.append(x * xscalefactor)
                newcoordlist.append(y * yscalefactor)
                coordinates = coordinates[2:]

            self.cv.coords(item, *newcoordlist)

        return

    def _resize(self, canvwidth=None, canvheight=None, bg=None):
        if not isinstance(self.cv, ScrolledCanvas):
            return (self.canvwidth, self.canvheight)
        else:
            if canvwidth is canvheight is bg is None:
                return (self.cv.canvwidth, self.cv.canvheight)
            if canvwidth is not None:
                self.canvwidth = canvwidth
            if canvheight is not None:
                self.canvheight = canvheight
            self.cv.reset(canvwidth, canvheight, bg)
            return

    def _window_size(self):
        width = self.cv.winfo_width()
        if width <= 1:
            width = self.cv[b'width']
        height = self.cv.winfo_height()
        if height <= 1:
            height = self.cv[b'height']
        return (
         width, height)


class Terminator(Exception):
    pass


class TurtleGraphicsError(Exception):
    pass


class Shape(object):

    def __init__(self, type_, data=None):
        self._type = type_
        if type_ == b'polygon':
            if isinstance(data, list):
                data = tuple(data)
        elif type_ == b'image':
            if isinstance(data, basestring):
                if data.lower().endswith(b'.gif') and isfile(data):
                    data = TurtleScreen._image(data)
        elif type_ == b'compound':
            data = []
        else:
            raise TurtleGraphicsError(b'There is no shape type %s' % type_)
        self._data = data
        return

    def addcomponent(self, poly, fill, outline=None):
        if self._type != b'compound':
            raise TurtleGraphicsError(b'Cannot add component to %s Shape' % self._type)
        if outline is None:
            outline = fill
        self._data.append([poly, fill, outline])
        return


class Tbuffer(object):

    def __init__(self, bufsize=10):
        self.bufsize = bufsize
        self.buffer = [[None]] * bufsize
        self.ptr = -1
        self.cumulate = False
        return

    def reset(self, bufsize=None):
        if bufsize is None:
            for i in range(self.bufsize):
                self.buffer[i] = [
                 None]

        else:
            self.bufsize = bufsize
            self.buffer = [[None]] * bufsize
        self.ptr = -1
        return

    def push(self, item):
        if self.bufsize > 0:
            if not self.cumulate:
                self.ptr = (self.ptr + 1) % self.bufsize
                self.buffer[self.ptr] = item
            else:
                self.buffer[self.ptr].append(item)
        return

    def pop(self):
        if self.bufsize > 0:
            item = self.buffer[self.ptr]
            if item is None:
                return
            self.buffer[self.ptr] = [None]
            self.ptr = (self.ptr - 1) % self.bufsize
            return item
        return

    def nr_of_items(self):
        return self.bufsize - self.buffer.count([None])

    def __repr__(self):
        return str(self.buffer) + b' ' + str(self.ptr)


class TurtleScreen(TurtleScreenBase):
    _RUNNING = True

    def __init__(self, cv, mode=_CFG[b'mode'], colormode=_CFG[b'colormode'], delay=_CFG[b'delay']):
        self._shapes = {b'arrow': (Shape(b'polygon', ((-10, 0), (10, 0), (0, 10)))), 
           b'turtle': (Shape(b'polygon', ((0, 16), (-2, 14), (-1, 10), (-4, 7),
                     (-7, 9), (-9, 8), (-6, 5), (-7, 1), (-5, -3), (-8, -6),
                     (-6, -8), (-4, -5), (0, -7), (4, -5), (6, -8), (8, -6),
                     (5, -3), (7, 1), (6, 5), (9, 8), (7, 9), (4, 7), (1, 10),
                     (2, 14)))), 
           b'circle': (Shape(b'polygon', ((10, 0), (9.51, 3.09), (8.09, 5.88),
                     (5.88, 8.09), (3.09, 9.51), (0, 10), (-3.09, 9.51),
                     (-5.88, 8.09), (-8.09, 5.88), (-9.51, 3.09), (-10, 0),
                     (-9.51, -3.09), (-8.09, -5.88), (-5.88, -8.09),
                     (-3.09, -9.51), (-0.0, -10.0), (3.09, -9.51),
                     (5.88, -8.09), (8.09, -5.88), (9.51, -3.09)))), 
           b'square': (Shape(b'polygon', ((10, -10), (10, 10), (-10, 10),
                     (-10, -10)))), 
           b'triangle': (Shape(b'polygon', ((10, -5.77), (0, 11.55),
                       (-10, -5.77)))), 
           b'classic': (Shape(b'polygon', ((0, 0), (-5, -9), (0, -7), (5, -9)))), 
           b'blank': (Shape(b'image', self._blankimage()))}
        self._bgpics = {b'nopic': b''}
        TurtleScreenBase.__init__(self, cv)
        self._mode = mode
        self._delayvalue = delay
        self._colormode = _CFG[b'colormode']
        self._keys = []
        self.clear()
        return

    def clear(self):
        self._delayvalue = _CFG[b'delay']
        self._colormode = _CFG[b'colormode']
        self._delete(b'all')
        self._bgpic = self._createimage(b'')
        self._bgpicname = b'nopic'
        self._tracing = 1
        self._updatecounter = 0
        self._turtles = []
        self.bgcolor(b'white')
        for btn in (1, 2, 3):
            self.onclick(None, btn)

        for key in self._keys[:]:
            self.onkey(None, key)

        Turtle._pen = None
        return

    def mode(self, mode=None):
        if mode is None:
            return self._mode
        else:
            mode = mode.lower()
            if mode not in (b'standard', b'logo', b'world'):
                raise TurtleGraphicsError(b'No turtle-graphics-mode %s' % mode)
            self._mode = mode
            if mode in (b'standard', b'logo'):
                self._setscrollregion(-self.canvwidth // 2, -self.canvheight // 2, self.canvwidth // 2, self.canvheight // 2)
                self.xscale = self.yscale = 1.0
            self.reset()
            return

    def setworldcoordinates(self, llx, lly, urx, ury):
        if self.mode() != b'world':
            self.mode(b'world')
        xspan = float(urx - llx)
        yspan = float(ury - lly)
        wx, wy = self._window_size()
        self.screensize(wx - 20, wy - 20)
        oldxscale, oldyscale = self.xscale, self.yscale
        self.xscale = self.canvwidth / xspan
        self.yscale = self.canvheight / yspan
        srx1 = llx * self.xscale
        sry1 = -ury * self.yscale
        srx2 = self.canvwidth + srx1
        sry2 = self.canvheight + sry1
        self._setscrollregion(srx1, sry1, srx2, sry2)
        self._rescale(self.xscale / oldxscale, self.yscale / oldyscale)
        self.update()
        return

    def register_shape(self, name, shape=None):
        if shape is None:
            if name.lower().endswith(b'.gif'):
                shape = Shape(b'image', self._image(name))
            else:
                raise TurtleGraphicsError(b'Bad arguments for register_shape.\n' + b'Use  help(register_shape)')
        elif isinstance(shape, tuple):
            shape = Shape(b'polygon', shape)
        self._shapes[name] = shape
        return

    def _colorstr(self, color):
        if len(color) == 1:
            color = color[0]
        if isinstance(color, basestring):
            if self._iscolorstring(color) or color == b'':
                return color
            raise TurtleGraphicsError(b'bad color string: %s' % str(color))
        try:
            r, g, b = color
        except (TypeError, ValueError):
            raise TurtleGraphicsError(b'bad color arguments: %s' % str(color))

        if self._colormode == 1.0:
            r, g, b = [round(255.0 * x) for x in (r, g, b)]
        if not ((0 <= r <= 255) and 0 <= g <= 255) and 0 <= b <= 255:
            raise TurtleGraphicsError(b'bad color sequence: %s' % str(color))
        return b'#%02x%02x%02x' % (r, g, b)

    def _color(self, cstr):
        if not cstr.startswith(b'#'):
            return cstr
        if len(cstr) == 7:
            cl = [int(cstr[i:i + 2], 16) for i in (1, 3, 5)]
        elif len(cstr) == 4:
            cl = [16 * int(cstr[h], 16) for h in cstr[1:]]
        else:
            raise TurtleGraphicsError(b'bad colorstring: %s' % cstr)
        return tuple([c * self._colormode / 255 for c in cl])

    def colormode(self, cmode=None):
        if cmode is None:
            return self._colormode
        else:
            if cmode == 1.0:
                self._colormode = float(cmode)
            elif cmode == 255:
                self._colormode = int(cmode)
            return

    def reset(self):
        for turtle in self._turtles:
            turtle._setmode(self._mode)
            turtle.reset()

        return

    def turtles(self):
        return self._turtles

    def bgcolor(self, *args):
        if args:
            color = self._colorstr(args)
        else:
            color = None
        color = self._bgcolor(color)
        if color is not None:
            color = self._color(color)
        return color

    def tracer(self, n=None, delay=None):
        if n is None:
            return self._tracing
        else:
            self._tracing = int(n)
            self._updatecounter = 0
            if delay is not None:
                self._delayvalue = int(delay)
            if self._tracing:
                self.update()
            return

    def delay(self, delay=None):
        if delay is None:
            return self._delayvalue
        else:
            self._delayvalue = int(delay)
            return

    def _incrementudc(self):
        if not TurtleScreen._RUNNING:
            TurtleScreen._RUNNING = True
            raise Terminator
        if self._tracing > 0:
            self._updatecounter += 1
            self._updatecounter %= self._tracing
        return

    def update(self):
        tracing = self._tracing
        self._tracing = True
        for t in self.turtles():
            t._update_data()
            t._drawturtle()

        self._tracing = tracing
        self._update()
        return

    def window_width(self):
        return self._window_size()[0]

    def window_height(self):
        return self._window_size()[1]

    def getcanvas(self):
        return self.cv

    def getshapes(self):
        return sorted(self._shapes.keys())

    def onclick(self, fun, btn=1, add=None):
        self._onscreenclick(fun, btn, add)
        return

    def onkey(self, fun, key):
        if fun is None:
            if key in self._keys:
                self._keys.remove(key)
        elif key not in self._keys:
            self._keys.append(key)
        self._onkey(fun, key)
        return

    def listen(self, xdummy=None, ydummy=None):
        self._listen()
        return

    def ontimer(self, fun, t=0):
        self._ontimer(fun, t)
        return

    def bgpic(self, picname=None):
        if picname is None:
            return self._bgpicname
        else:
            if picname not in self._bgpics:
                self._bgpics[picname] = self._image(picname)
            self._setbgpic(self._bgpic, self._bgpics[picname])
            self._bgpicname = picname
            return

    def screensize(self, canvwidth=None, canvheight=None, bg=None):
        return self._resize(canvwidth, canvheight, bg)

    onscreenclick = onclick
    resetscreen = reset
    clearscreen = clear
    addshape = register_shape


class TNavigator(object):
    START_ORIENTATION = {b'standard': (Vec2D(1.0, 0.0)), 
       b'world': (Vec2D(1.0, 0.0)), 
       b'logo': (Vec2D(0.0, 1.0))}
    DEFAULT_MODE = b'standard'
    DEFAULT_ANGLEOFFSET = 0
    DEFAULT_ANGLEORIENT = 1

    def __init__(self, mode=DEFAULT_MODE):
        self._angleOffset = self.DEFAULT_ANGLEOFFSET
        self._angleOrient = self.DEFAULT_ANGLEORIENT
        self._mode = mode
        self.undobuffer = None
        self.degrees()
        self._mode = None
        self._setmode(mode)
        TNavigator.reset(self)
        return

    def reset(self):
        self._position = Vec2D(0.0, 0.0)
        self._orient = TNavigator.START_ORIENTATION[self._mode]
        return

    def _setmode(self, mode=None):
        if mode is None:
            return self._mode
        else:
            if mode not in (b'standard', b'logo', b'world'):
                return
            self._mode = mode
            if mode in (b'standard', b'world'):
                self._angleOffset = 0
                self._angleOrient = 1
            else:
                self._angleOffset = self._fullcircle / 4.0
                self._angleOrient = -1
            return

    def _setDegreesPerAU(self, fullcircle):
        self._fullcircle = fullcircle
        self._degreesPerAU = 360 / fullcircle
        if self._mode == b'standard':
            self._angleOffset = 0
        else:
            self._angleOffset = fullcircle / 4.0
        return

    def degrees(self, fullcircle=360.0):
        self._setDegreesPerAU(fullcircle)
        return

    def radians(self):
        self._setDegreesPerAU(2 * math.pi)
        return

    def _go(self, distance):
        ende = self._position + self._orient * distance
        self._goto(ende)
        return

    def _rotate(self, angle):
        angle *= self._degreesPerAU
        self._orient = self._orient.rotate(angle)
        return

    def _goto(self, end):
        self._position = end
        return

    def forward(self, distance):
        self._go(distance)
        return

    def back(self, distance):
        self._go(-distance)
        return

    def right(self, angle):
        self._rotate(-angle)
        return

    def left(self, angle):
        self._rotate(angle)
        return

    def pos(self):
        return self._position

    def xcor(self):
        return self._position[0]

    def ycor(self):
        return self._position[1]

    def goto(self, x, y=None):
        if y is None:
            self._goto(Vec2D(*x))
        else:
            self._goto(Vec2D(x, y))
        return

    def home(self):
        self.goto(0, 0)
        self.setheading(0)
        return

    def setx(self, x):
        self._goto(Vec2D(x, self._position[1]))
        return

    def sety(self, y):
        self._goto(Vec2D(self._position[0], y))
        return

    def distance(self, x, y=None):
        if y is not None:
            pos = Vec2D(x, y)
        if isinstance(x, Vec2D):
            pos = x
        elif isinstance(x, tuple):
            pos = Vec2D(*x)
        elif isinstance(x, TNavigator):
            pos = x._position
        return abs(pos - self._position)

    def towards(self, x, y=None):
        if y is not None:
            pos = Vec2D(x, y)
        if isinstance(x, Vec2D):
            pos = x
        elif isinstance(x, tuple):
            pos = Vec2D(*x)
        elif isinstance(x, TNavigator):
            pos = x._position
        x, y = pos - self._position
        result = round(math.atan2(y, x) * 180.0 / math.pi, 10) % 360.0
        result /= self._degreesPerAU
        return (self._angleOffset + self._angleOrient * result) % self._fullcircle

    def heading(self):
        x, y = self._orient
        result = round(math.atan2(y, x) * 180.0 / math.pi, 10) % 360.0
        result /= self._degreesPerAU
        return (self._angleOffset + self._angleOrient * result) % self._fullcircle

    def setheading(self, to_angle):
        angle = (to_angle - self.heading()) * self._angleOrient
        full = self._fullcircle
        angle = (angle + full / 2.0) % full - full / 2.0
        self._rotate(angle)
        return

    def circle(self, radius, extent=None, steps=None):
        if self.undobuffer:
            self.undobuffer.push([b'seq'])
            self.undobuffer.cumulate = True
        speed = self.speed()
        if extent is None:
            extent = self._fullcircle
        if steps is None:
            frac = abs(extent) / self._fullcircle
            steps = 1 + int(min(11 + abs(radius) / 6.0, 59.0) * frac)
        w = 1.0 * extent / steps
        w2 = 0.5 * w
        l = 2.0 * radius * math.sin(w2 * math.pi / 180.0 * self._degreesPerAU)
        if radius < 0:
            l, w, w2 = -l, -w, -w2
        tr = self.tracer()
        dl = self._delay()
        if speed == 0:
            self.tracer(0, 0)
        else:
            self.speed(0)
        self._rotate(w2)
        for i in range(steps):
            self.speed(speed)
            self._go(l)
            self.speed(0)
            self._rotate(w)

        self._rotate(-w2)
        if speed == 0:
            self.tracer(tr, dl)
        self.speed(speed)
        if self.undobuffer:
            self.undobuffer.cumulate = False
        return

    def speed(self, s=0):
        return

    def tracer(self, a=None, b=None):
        return

    def _delay(self, n=None):
        return

    fd = forward
    bk = back
    backward = back
    rt = right
    lt = left
    position = pos
    setpos = goto
    setposition = goto
    seth = setheading


class TPen(object):

    def __init__(self, resizemode=_CFG[b'resizemode']):
        self._resizemode = resizemode
        self.undobuffer = None
        TPen._reset(self)
        return

    def _reset(self, pencolor=_CFG[b'pencolor'], fillcolor=_CFG[b'fillcolor']):
        self._pensize = 1
        self._shown = True
        self._pencolor = pencolor
        self._fillcolor = fillcolor
        self._drawing = True
        self._speed = 3
        self._stretchfactor = (1, 1)
        self._tilt = 0
        self._outlinewidth = 1
        return

    def resizemode(self, rmode=None):
        if rmode is None:
            return self._resizemode
        else:
            rmode = rmode.lower()
            if rmode in (b'auto', b'user', b'noresize'):
                self.pen(resizemode=rmode)
            return

    def pensize(self, width=None):
        if width is None:
            return self._pensize
        else:
            self.pen(pensize=width)
            return

    def penup(self):
        if not self._drawing:
            return
        self.pen(pendown=False)
        return

    def pendown(self):
        if self._drawing:
            return
        self.pen(pendown=True)
        return

    def isdown(self):
        return self._drawing

    def speed(self, speed=None):
        speeds = {b'fastest': 0, b'fast': 10, b'normal': 6, b'slow': 3, b'slowest': 1}
        if speed is None:
            return self._speed
        else:
            if speed in speeds:
                speed = speeds[speed]
            elif 0.5 < speed < 10.5:
                speed = int(round(speed))
            else:
                speed = 0
            self.pen(speed=speed)
            return

    def color(self, *args):
        if args:
            l = len(args)
            if l == 1:
                pcolor = fcolor = args[0]
            elif l == 2:
                pcolor, fcolor = args
            elif l == 3:
                pcolor = fcolor = args
            pcolor = self._colorstr(pcolor)
            fcolor = self._colorstr(fcolor)
            self.pen(pencolor=pcolor, fillcolor=fcolor)
        else:
            return (
             self._color(self._pencolor), self._color(self._fillcolor))
        return

    def pencolor(self, *args):
        if args:
            color = self._colorstr(args)
            if color == self._pencolor:
                return
            self.pen(pencolor=color)
        else:
            return self._color(self._pencolor)
        return

    def fillcolor(self, *args):
        if args:
            color = self._colorstr(args)
            if color == self._fillcolor:
                return
            self.pen(fillcolor=color)
        else:
            return self._color(self._fillcolor)
        return

    def showturtle(self):
        self.pen(shown=True)
        return

    def hideturtle(self):
        self.pen(shown=False)
        return

    def isvisible(self):
        return self._shown

    def pen(self, pen=None, **pendict):
        _pd = {b'shown': (self._shown), b'pendown': (self._drawing), 
           b'pencolor': (self._pencolor), 
           b'fillcolor': (self._fillcolor), 
           b'pensize': (self._pensize), 
           b'speed': (self._speed), 
           b'resizemode': (self._resizemode), 
           b'stretchfactor': (self._stretchfactor), 
           b'outline': (self._outlinewidth), 
           b'tilt': (self._tilt)}
        if not (pen or pendict):
            return _pd
        if isinstance(pen, dict):
            p = pen
        else:
            p = {}
        p.update(pendict)
        _p_buf = {}
        for key in p:
            _p_buf[key] = _pd[key]

        if self.undobuffer:
            self.undobuffer.push((b'pen', _p_buf))
        newLine = False
        if b'pendown' in p:
            if self._drawing != p[b'pendown']:
                newLine = True
        if b'pencolor' in p:
            if isinstance(p[b'pencolor'], tuple):
                p[b'pencolor'] = self._colorstr((p[b'pencolor'],))
            if self._pencolor != p[b'pencolor']:
                newLine = True
        if b'pensize' in p:
            if self._pensize != p[b'pensize']:
                newLine = True
        if newLine:
            self._newLine()
        if b'pendown' in p:
            self._drawing = p[b'pendown']
        if b'pencolor' in p:
            self._pencolor = p[b'pencolor']
        if b'pensize' in p:
            self._pensize = p[b'pensize']
        if b'fillcolor' in p:
            if isinstance(p[b'fillcolor'], tuple):
                p[b'fillcolor'] = self._colorstr((p[b'fillcolor'],))
            self._fillcolor = p[b'fillcolor']
        if b'speed' in p:
            self._speed = p[b'speed']
        if b'resizemode' in p:
            self._resizemode = p[b'resizemode']
        if b'stretchfactor' in p:
            sf = p[b'stretchfactor']
            if isinstance(sf, (int, long, float)):
                sf = (
                 sf, sf)
            self._stretchfactor = sf
        if b'outline' in p:
            self._outlinewidth = p[b'outline']
        if b'shown' in p:
            self._shown = p[b'shown']
        if b'tilt' in p:
            self._tilt = p[b'tilt']
        self._update()
        return

    def _newLine(self, usePos=True):
        return

    def _update(self, count=True, forced=False):
        return

    def _color(self, args):
        return

    def _colorstr(self, args):
        return

    width = pensize
    up = penup
    pu = penup
    pd = pendown
    down = pendown
    st = showturtle
    ht = hideturtle


class _TurtleImage(object):

    def __init__(self, screen, shapeIndex):
        self.screen = screen
        self._type = None
        self._setshape(shapeIndex)
        return

    def _setshape(self, shapeIndex):
        screen = self.screen
        self.shapeIndex = shapeIndex
        if self._type == b'polygon' == screen._shapes[shapeIndex]._type:
            return
        if self._type == b'image' == screen._shapes[shapeIndex]._type:
            return
        if self._type in (b'image', b'polygon'):
            screen._delete(self._item)
        elif self._type == b'compound':
            for item in self._item:
                screen._delete(item)

        self._type = screen._shapes[shapeIndex]._type
        if self._type == b'polygon':
            self._item = screen._createpoly()
        elif self._type == b'image':
            self._item = screen._createimage(screen._shapes[b'blank']._data)
        elif self._type == b'compound':
            self._item = [screen._createpoly() for item in screen._shapes[shapeIndex]._data]
        return


class RawTurtle(TPen, TNavigator):
    screens = []

    def __init__(self, canvas=None, shape=_CFG[b'shape'], undobuffersize=_CFG[b'undobuffersize'], visible=_CFG[b'visible']):
        if isinstance(canvas, _Screen):
            self.screen = canvas
        elif isinstance(canvas, TurtleScreen):
            if canvas not in RawTurtle.screens:
                RawTurtle.screens.append(canvas)
            self.screen = canvas
        elif isinstance(canvas, (ScrolledCanvas, Canvas)):
            for screen in RawTurtle.screens:
                if screen.cv == canvas:
                    self.screen = screen
                    break
            else:
                self.screen = TurtleScreen(canvas)
                RawTurtle.screens.append(self.screen)

        else:
            raise TurtleGraphicsError(b'bad canvas argument %s' % canvas)
        screen = self.screen
        TNavigator.__init__(self, screen.mode())
        TPen.__init__(self)
        screen._turtles.append(self)
        self.drawingLineItem = screen._createline()
        self.turtle = _TurtleImage(screen, shape)
        self._poly = None
        self._creatingPoly = False
        self._fillitem = self._fillpath = None
        self._shown = visible
        self._hidden_from_screen = False
        self.currentLineItem = screen._createline()
        self.currentLine = [self._position]
        self.items = [self.currentLineItem]
        self.stampItems = []
        self._undobuffersize = undobuffersize
        self.undobuffer = Tbuffer(undobuffersize)
        self._update()
        return

    def reset(self):
        TNavigator.reset(self)
        TPen._reset(self)
        self._clear()
        self._drawturtle()
        self._update()
        return

    def setundobuffer(self, size):
        if size is None or size <= 0:
            self.undobuffer = None
        else:
            self.undobuffer = Tbuffer(size)
        return

    def undobufferentries(self):
        if self.undobuffer is None:
            return 0
        else:
            return self.undobuffer.nr_of_items()

    def _clear(self):
        self._fillitem = self._fillpath = None
        for item in self.items:
            self.screen._delete(item)

        self.currentLineItem = self.screen._createline()
        self.currentLine = []
        if self._drawing:
            self.currentLine.append(self._position)
        self.items = [
         self.currentLineItem]
        self.clearstamps()
        self.setundobuffer(self._undobuffersize)
        return

    def clear(self):
        self._clear()
        self._update()
        return

    def _update_data(self):
        self.screen._incrementudc()
        if self.screen._updatecounter != 0:
            return
        if len(self.currentLine) > 1:
            self.screen._drawline(self.currentLineItem, self.currentLine, self._pencolor, self._pensize)
        return

    def _update(self):
        screen = self.screen
        if screen._tracing == 0:
            return
        if screen._tracing == 1:
            self._update_data()
            self._drawturtle()
            screen._update()
            screen._delay(screen._delayvalue)
        else:
            self._update_data()
            if screen._updatecounter == 0:
                for t in screen.turtles():
                    t._drawturtle()

                screen._update()
        return

    def tracer(self, flag=None, delay=None):
        return self.screen.tracer(flag, delay)

    def _color(self, args):
        return self.screen._color(args)

    def _colorstr(self, args):
        return self.screen._colorstr(args)

    def _cc(self, args):
        if isinstance(args, basestring):
            return args
        try:
            r, g, b = args
        except (TypeError, ValueError):
            raise TurtleGraphicsError(b'bad color arguments: %s' % str(args))

        if self.screen._colormode == 1.0:
            r, g, b = [round(255.0 * x) for x in (r, g, b)]
        if not ((0 <= r <= 255) and 0 <= g <= 255) and 0 <= b <= 255:
            raise TurtleGraphicsError(b'bad color sequence: %s' % str(args))
        return b'#%02x%02x%02x' % (r, g, b)

    def clone(self):
        screen = self.screen
        self._newLine(self._drawing)
        turtle = self.turtle
        self.screen = None
        self.turtle = None
        q = deepcopy(self)
        self.screen = screen
        self.turtle = turtle
        q.screen = screen
        q.turtle = _TurtleImage(screen, self.turtle.shapeIndex)
        screen._turtles.append(q)
        ttype = screen._shapes[self.turtle.shapeIndex]._type
        if ttype == b'polygon':
            q.turtle._item = screen._createpoly()
        elif ttype == b'image':
            q.turtle._item = screen._createimage(screen._shapes[b'blank']._data)
        elif ttype == b'compound':
            q.turtle._item = [screen._createpoly() for item in screen._shapes[self.turtle.shapeIndex]._data]
        q.currentLineItem = screen._createline()
        q._update()
        return q

    def shape(self, name=None):
        if name is None:
            return self.turtle.shapeIndex
        else:
            if name not in self.screen.getshapes():
                raise TurtleGraphicsError(b'There is no shape named %s' % name)
            self.turtle._setshape(name)
            self._update()
            return

    def shapesize(self, stretch_wid=None, stretch_len=None, outline=None):
        if stretch_wid is stretch_len is outline is None:
            stretch_wid, stretch_len = self._stretchfactor
            return (
             stretch_wid, stretch_len, self._outlinewidth)
        else:
            if stretch_wid is not None:
                if stretch_len is None:
                    stretchfactor = (
                     stretch_wid, stretch_wid)
                else:
                    stretchfactor = (
                     stretch_wid, stretch_len)
            elif stretch_len is not None:
                stretchfactor = (
                 self._stretchfactor[0], stretch_len)
            else:
                stretchfactor = self._stretchfactor
            if outline is None:
                outline = self._outlinewidth
            self.pen(resizemode=b'user', stretchfactor=stretchfactor, outline=outline)
            return

    def settiltangle(self, angle):
        tilt = -angle * self._degreesPerAU * self._angleOrient
        tilt = tilt * math.pi / 180.0 % (2 * math.pi)
        self.pen(resizemode=b'user', tilt=tilt)
        return

    def tiltangle(self):
        tilt = -self._tilt * (180.0 / math.pi) * self._angleOrient
        return tilt / self._degreesPerAU % self._fullcircle

    def tilt(self, angle):
        self.settiltangle(angle + self.tiltangle())
        return

    def _polytrafo(self, poly):
        screen = self.screen
        p0, p1 = self._position
        e0, e1 = self._orient
        e = Vec2D(e0, e1 * screen.yscale / screen.xscale)
        e0, e1 = 1.0 / abs(e) * e
        return [(p0 + (e1 * x + e0 * y) / screen.xscale, p1 + (-e0 * x + e1 * y) / screen.yscale) for x, y in poly]

    def _drawturtle(self):
        screen = self.screen
        shape = screen._shapes[self.turtle.shapeIndex]
        ttype = shape._type
        titem = self.turtle._item
        if self._shown and screen._updatecounter == 0 and screen._tracing > 0:
            self._hidden_from_screen = False
            tshape = shape._data
            if ttype == b'polygon':
                if self._resizemode == b'noresize':
                    w = 1
                    shape = tshape
                else:
                    if self._resizemode == b'auto':
                        lx = ly = max(1, self._pensize / 5.0)
                        w = self._pensize
                        tiltangle = 0
                    elif self._resizemode == b'user':
                        lx, ly = self._stretchfactor
                        w = self._outlinewidth
                        tiltangle = self._tilt
                    shape = [(lx * x, ly * y) for x, y in tshape]
                    t0, t1 = math.sin(tiltangle), math.cos(tiltangle)
                    shape = [(t1 * x + t0 * y, -t0 * x + t1 * y) for x, y in shape]
                shape = self._polytrafo(shape)
                fc, oc = self._fillcolor, self._pencolor
                screen._drawpoly(titem, shape, fill=fc, outline=oc, width=w, top=True)
            elif ttype == b'image':
                screen._drawimage(titem, self._position, tshape)
            elif ttype == b'compound':
                lx, ly = self._stretchfactor
                w = self._outlinewidth
                for item, (poly, fc, oc) in zip(titem, tshape):
                    poly = [(lx * x, ly * y) for x, y in poly]
                    poly = self._polytrafo(poly)
                    screen._drawpoly(item, poly, fill=self._cc(fc), outline=self._cc(oc), width=w, top=True)

        elif self._hidden_from_screen:
            return
        if ttype == b'polygon':
            screen._drawpoly(titem, ((0, 0), (0, 0), (0, 0)), b'', b'')
        elif ttype == b'image':
            screen._drawimage(titem, self._position, screen._shapes[b'blank']._data)
        elif ttype == b'compound':
            for item in titem:
                screen._drawpoly(item, ((0, 0), (0, 0), (0, 0)), b'', b'')

        self._hidden_from_screen = True
        return

    def stamp(self):
        screen = self.screen
        shape = screen._shapes[self.turtle.shapeIndex]
        ttype = shape._type
        tshape = shape._data
        if ttype == b'polygon':
            stitem = screen._createpoly()
            if self._resizemode == b'noresize':
                w = 1
                shape = tshape
            else:
                if self._resizemode == b'auto':
                    lx = ly = max(1, self._pensize / 5.0)
                    w = self._pensize
                    tiltangle = 0
                elif self._resizemode == b'user':
                    lx, ly = self._stretchfactor
                    w = self._outlinewidth
                    tiltangle = self._tilt
                shape = [(lx * x, ly * y) for x, y in tshape]
                t0, t1 = math.sin(tiltangle), math.cos(tiltangle)
                shape = [(t1 * x + t0 * y, -t0 * x + t1 * y) for x, y in shape]
            shape = self._polytrafo(shape)
            fc, oc = self._fillcolor, self._pencolor
            screen._drawpoly(stitem, shape, fill=fc, outline=oc, width=w, top=True)
        elif ttype == b'image':
            stitem = screen._createimage(b'')
            screen._drawimage(stitem, self._position, tshape)
        elif ttype == b'compound':
            stitem = []
            for element in tshape:
                item = screen._createpoly()
                stitem.append(item)

            stitem = tuple(stitem)
            lx, ly = self._stretchfactor
            w = self._outlinewidth
            for item, (poly, fc, oc) in zip(stitem, tshape):
                poly = [(lx * x, ly * y) for x, y in poly]
                poly = self._polytrafo(poly)
                screen._drawpoly(item, poly, fill=self._cc(fc), outline=self._cc(oc), width=w, top=True)

        self.stampItems.append(stitem)
        self.undobuffer.push((b'stamp', stitem))
        return stitem

    def _clearstamp(self, stampid):
        if stampid in self.stampItems:
            if isinstance(stampid, tuple):
                for subitem in stampid:
                    self.screen._delete(subitem)

            else:
                self.screen._delete(stampid)
            self.stampItems.remove(stampid)
        item = (
         b'stamp', stampid)
        buf = self.undobuffer
        if item not in buf.buffer:
            return
        else:
            index = buf.buffer.index(item)
            buf.buffer.remove(item)
            if index <= buf.ptr:
                buf.ptr = (buf.ptr - 1) % buf.bufsize
            buf.buffer.insert((buf.ptr + 1) % buf.bufsize, [None])
            return

    def clearstamp(self, stampid):
        self._clearstamp(stampid)
        self._update()
        return

    def clearstamps(self, n=None):
        if n is None:
            toDelete = self.stampItems[:]
        elif n >= 0:
            toDelete = self.stampItems[:n]
        else:
            toDelete = self.stampItems[n:]
        for item in toDelete:
            self._clearstamp(item)

        self._update()
        return

    def _goto(self, end):
        go_modes = (
         self._drawing,
         self._pencolor,
         self._pensize,
         isinstance(self._fillpath, list))
        screen = self.screen
        undo_entry = (b'go', self._position, end, go_modes,
         (
          self.currentLineItem,
          self.currentLine[:],
          screen._pointlist(self.currentLineItem),
          self.items[:]))
        if self.undobuffer:
            self.undobuffer.push(undo_entry)
        start = self._position
        if self._speed and screen._tracing == 1:
            diff = end - start
            diffsq = (diff[0] * screen.xscale) ** 2 + (diff[1] * screen.yscale) ** 2
            nhops = 1 + int(diffsq ** 0.5 / (3 * 1.1 ** self._speed * self._speed))
            delta = diff * (1.0 / nhops)
            for n in range(1, nhops):
                if n == 1:
                    top = True
                else:
                    top = False
                self._position = start + delta * n
                if self._drawing:
                    screen._drawline(self.drawingLineItem, (
                     start, self._position), self._pencolor, self._pensize, top)
                self._update()

            if self._drawing:
                screen._drawline(self.drawingLineItem, ((0, 0), (0, 0)), fill=b'', width=self._pensize)
        if self._drawing:
            self.currentLine.append(end)
        if isinstance(self._fillpath, list):
            self._fillpath.append(end)
        self._position = end
        if self._creatingPoly:
            self._poly.append(end)
        if len(self.currentLine) > 42:
            self._newLine()
        self._update()
        return

    def _undogoto(self, entry):
        old, new, go_modes, coodata = entry
        drawing, pc, ps, filling = go_modes
        cLI, cL, pl, items = coodata
        screen = self.screen
        if abs(self._position - new) > 0.5:
            print b'undogoto: HALLO-DA-STIMMT-WAS-NICHT!'
        self.currentLineItem = cLI
        self.currentLine = cL
        if pl == [(0, 0), (0, 0)]:
            usepc = b''
        else:
            usepc = pc
        screen._drawline(cLI, pl, fill=usepc, width=ps)
        todelete = [i for i in self.items if i not in items and screen._type(i) == b'line']
        for i in todelete:
            screen._delete(i)
            self.items.remove(i)

        start = old
        if self._speed and screen._tracing == 1:
            diff = old - new
            diffsq = (diff[0] * screen.xscale) ** 2 + (diff[1] * screen.yscale) ** 2
            nhops = 1 + int(diffsq ** 0.5 / (3 * 1.1 ** self._speed * self._speed))
            delta = diff * (1.0 / nhops)
            for n in range(1, nhops):
                if n == 1:
                    top = True
                else:
                    top = False
                self._position = new + delta * n
                if drawing:
                    screen._drawline(self.drawingLineItem, (
                     start, self._position), pc, ps, top)
                self._update()

            if drawing:
                screen._drawline(self.drawingLineItem, ((0, 0), (0, 0)), fill=b'', width=ps)
        self._position = old
        if self._creatingPoly:
            if len(self._poly) > 0:
                self._poly.pop()
            if self._poly == []:
                self._creatingPoly = False
                self._poly = None
        if filling:
            if self._fillpath == []:
                self._fillpath = None
                print b'Unwahrscheinlich in _undogoto!'
            elif self._fillpath is not None:
                self._fillpath.pop()
        self._update()
        return

    def _rotate(self, angle):
        if self.undobuffer:
            self.undobuffer.push((b'rot', angle, self._degreesPerAU))
        angle *= self._degreesPerAU
        neworient = self._orient.rotate(angle)
        tracing = self.screen._tracing
        if tracing == 1 and self._speed > 0:
            anglevel = 3.0 * self._speed
            steps = 1 + int(abs(angle) / anglevel)
            delta = 1.0 * angle / steps
            for _ in range(steps):
                self._orient = self._orient.rotate(delta)
                self._update()

        self._orient = neworient
        self._update()
        return

    def _newLine(self, usePos=True):
        if len(self.currentLine) > 1:
            self.screen._drawline(self.currentLineItem, self.currentLine, self._pencolor, self._pensize)
            self.currentLineItem = self.screen._createline()
            self.items.append(self.currentLineItem)
        else:
            self.screen._drawline(self.currentLineItem, top=True)
        self.currentLine = []
        if usePos:
            self.currentLine = [
             self._position]
        return

    def fill(self, flag=None):
        filling = isinstance(self._fillpath, list)
        if flag is None:
            return filling
        else:
            screen = self.screen
            entry1 = entry2 = ()
            if filling:
                if len(self._fillpath) > 2:
                    self.screen._drawpoly(self._fillitem, self._fillpath, fill=self._fillcolor)
                    entry1 = (b'dofill', self._fillitem)
            if flag:
                self._fillitem = self.screen._createpoly()
                self.items.append(self._fillitem)
                self._fillpath = [self._position]
                entry2 = (b'beginfill', self._fillitem)
                self._newLine()
            else:
                self._fillitem = self._fillpath = None
            if self.undobuffer:
                if entry1 == ():
                    if entry2 != ():
                        self.undobuffer.push(entry2)
                elif entry2 == ():
                    self.undobuffer.push(entry1)
                else:
                    self.undobuffer.push([b'seq', entry1, entry2])
            self._update()
            return

    def begin_fill(self):
        self.fill(True)
        return

    def end_fill(self):
        self.fill(False)
        return

    def dot(self, size=None, *color):
        if not color:
            if isinstance(size, (basestring, tuple)):
                color = self._colorstr(size)
                size = self._pensize + max(self._pensize, 4)
            else:
                color = self._pencolor
                if not size:
                    size = self._pensize + max(self._pensize, 4)
        elif size is None:
            size = self._pensize + max(self._pensize, 4)
        color = self._colorstr(color)
        if hasattr(self.screen, b'_dot'):
            item = self.screen._dot(self._position, size, color)
            self.items.append(item)
            if self.undobuffer:
                self.undobuffer.push((b'dot', item))
        else:
            pen = self.pen()
            if self.undobuffer:
                self.undobuffer.push([b'seq'])
                self.undobuffer.cumulate = True
            try:
                if self.resizemode() == b'auto':
                    self.ht()
                self.pendown()
                self.pensize(size)
                self.pencolor(color)
                self.forward(0)
            finally:
                self.pen(pen)

            if self.undobuffer:
                self.undobuffer.cumulate = False
        return

    def _write(self, txt, align, font):
        item, end = self.screen._write(self._position, txt, align, font, self._pencolor)
        self.items.append(item)
        if self.undobuffer:
            self.undobuffer.push((b'wri', item))
        return end

    def write(self, arg, move=False, align=b'left', font=(b'Arial', 8, b'normal')):
        if self.undobuffer:
            self.undobuffer.push([b'seq'])
            self.undobuffer.cumulate = True
        end = self._write(str(arg), align.lower(), font)
        if move:
            x, y = self.pos()
            self.setpos(end, y)
        if self.undobuffer:
            self.undobuffer.cumulate = False
        return

    def begin_poly(self):
        self._poly = [
         self._position]
        self._creatingPoly = True
        return

    def end_poly(self):
        self._creatingPoly = False
        return

    def get_poly(self):
        if self._poly is not None:
            return tuple(self._poly)
        else:
            return

    def getscreen(self):
        return self.screen

    def getturtle(self):
        return self

    getpen = getturtle

    def window_width(self):
        return self.screen._window_size()[0]

    def window_height(self):
        return self.screen._window_size()[1]

    def _delay(self, delay=None):
        return self.screen.delay(delay)

    def onclick(self, fun, btn=1, add=None):
        self.screen._onclick(self.turtle._item, fun, btn, add)
        self._update()
        return

    def onrelease(self, fun, btn=1, add=None):
        self.screen._onrelease(self.turtle._item, fun, btn, add)
        self._update()
        return

    def ondrag(self, fun, btn=1, add=None):
        self.screen._ondrag(self.turtle._item, fun, btn, add)
        return

    def _undo(self, action, data):
        if self.undobuffer is None:
            return
        else:
            if action == b'rot':
                angle, degPAU = data
                self._rotate(-angle * degPAU / self._degreesPerAU)
                dummy = self.undobuffer.pop()
            elif action == b'stamp':
                stitem = data[0]
                self.clearstamp(stitem)
            elif action == b'go':
                self._undogoto(data)
            elif action in (b'wri', b'dot'):
                item = data[0]
                self.screen._delete(item)
                self.items.remove(item)
            elif action == b'dofill':
                item = data[0]
                self.screen._drawpoly(item, ((0, 0), (0, 0), (0, 0)), fill=b'', outline=b'')
            elif action == b'beginfill':
                item = data[0]
                self._fillitem = self._fillpath = None
                self.screen._delete(item)
                self.items.remove(item)
            elif action == b'pen':
                TPen.pen(self, data[0])
                self.undobuffer.pop()
            return

    def undo(self):
        if self.undobuffer is None:
            return
        else:
            item = self.undobuffer.pop()
            action = item[0]
            data = item[1:]
            if action == b'seq':
                while data:
                    item = data.pop()
                    self._undo(item[0], item[1:])

            else:
                self._undo(action, data)
            return

    turtlesize = shapesize


RawPen = RawTurtle

def Screen():
    if Turtle._screen is None:
        Turtle._screen = _Screen()
    return Turtle._screen


class _Screen(TurtleScreen):
    _root = None
    _canvas = None
    _title = _CFG[b'title']

    def __init__(self):
        if _Screen._root is None:
            _Screen._root = self._root = _Root()
            self._root.title(_Screen._title)
            self._root.ondestroy(self._destroy)
        if _Screen._canvas is None:
            width = _CFG[b'width']
            height = _CFG[b'height']
            canvwidth = _CFG[b'canvwidth']
            canvheight = _CFG[b'canvheight']
            leftright = _CFG[b'leftright']
            topbottom = _CFG[b'topbottom']
            self._root.setupcanvas(width, height, canvwidth, canvheight)
            _Screen._canvas = self._root._getcanvas()
            TurtleScreen.__init__(self, _Screen._canvas)
            self.setup(width, height, leftright, topbottom)
        return

    def setup(self, width=_CFG[b'width'], height=_CFG[b'height'], startx=_CFG[b'leftright'], starty=_CFG[b'topbottom']):
        if not hasattr(self._root, b'set_geometry'):
            return
        else:
            sw = self._root.win_width()
            sh = self._root.win_height()
            if isinstance(width, float) and 0 <= width <= 1:
                width = sw * width
            if startx is None:
                startx = (sw - width) / 2
            if isinstance(height, float) and 0 <= height <= 1:
                height = sh * height
            if starty is None:
                starty = (sh - height) / 2
            self._root.set_geometry(width, height, startx, starty)
            self.update()
            return

    def title(self, titlestring):
        if _Screen._root is not None:
            _Screen._root.title(titlestring)
        _Screen._title = titlestring
        return

    def _destroy(self):
        root = self._root
        if root is _Screen._root:
            Turtle._pen = None
            Turtle._screen = None
            _Screen._root = None
            _Screen._canvas = None
        TurtleScreen._RUNNING = False
        root.destroy()
        return

    def bye(self):
        self._destroy()
        return

    def exitonclick(self):

        def exitGracefully(x, y):
            self.bye()
            return

        self.onclick(exitGracefully)
        if _CFG[b'using_IDLE']:
            return
        try:
            mainloop()
        except AttributeError:
            exit(0)

        return


class Turtle(RawTurtle):
    _pen = None
    _screen = None

    def __init__(self, shape=_CFG[b'shape'], undobuffersize=_CFG[b'undobuffersize'], visible=_CFG[b'visible']):
        if Turtle._screen is None:
            Turtle._screen = Screen()
        RawTurtle.__init__(self, Turtle._screen, shape=shape, undobuffersize=undobuffersize, visible=visible)
        return


Pen = Turtle

def write_docstringdict(filename=b'turtle_docstringdict'):
    docsdict = {}
    for methodname in _tg_screen_functions:
        key = b'_Screen.' + methodname
        docsdict[key] = eval(key).__doc__

    for methodname in _tg_turtle_functions:
        key = b'Turtle.' + methodname
        docsdict[key] = eval(key).__doc__

    f = open(b'%s.py' % filename, b'w')
    keys = sorted([x for x in docsdict.keys() if x.split(b'.')[1] not in _alias_list])
    f.write(b'docsdict = {\n\n')
    for key in keys[:-1]:
        f.write(b'%s :\n' % repr(key))
        f.write(b'        """%s\n""",\n\n' % docsdict[key])

    key = keys[-1]
    f.write(b'%s :\n' % repr(key))
    f.write(b'        """%s\n"""\n\n' % docsdict[key])
    f.write(b'}\n')
    f.close()
    return


def read_docstrings(lang):
    modname = b'turtle_docstringdict_%(language)s' % {b'language': (lang.lower())}
    module = __import__(modname)
    docsdict = module.docsdict
    for key in docsdict:
        try:
            eval(key).im_func.__doc__ = docsdict[key]
        except BaseException:
            print b'Bad docstring-entry: %s' % key

    return


_LANGUAGE = _CFG[b'language']
try:
    if _LANGUAGE != b'english':
        read_docstrings(_LANGUAGE)
except ImportError:
    print b'Cannot find docsdict for', _LANGUAGE
except BaseException:
    print b'Unknown Error when trying to import %s-docstring-dictionary' % _LANGUAGE

def getmethparlist(ob):
    argText1 = argText2 = b''
    if type(ob) == types.MethodType:
        fob = ob.im_func
        argOffset = 1
    else:
        fob = ob
        argOffset = 0
    if type(fob) in [types.FunctionType, types.LambdaType]:
        try:
            counter = fob.func_code.co_argcount
            items2 = list(fob.func_code.co_varnames[argOffset:counter])
            realArgs = fob.func_code.co_varnames[argOffset:counter]
            defaults = fob.func_defaults or []
            defaults = list(map((lambda name: b'=%s' % repr(name)), defaults))
            defaults = [b''] * (len(realArgs) - len(defaults)) + defaults
            items1 = map((lambda arg, dflt: arg + dflt), realArgs, defaults)
            if fob.func_code.co_flags & 4:
                items1.append(b'*' + fob.func_code.co_varnames[counter])
                items2.append(b'*' + fob.func_code.co_varnames[counter])
                counter += 1
            if fob.func_code.co_flags & 8:
                items1.append(b'**' + fob.func_code.co_varnames[counter])
                items2.append(b'**' + fob.func_code.co_varnames[counter])
            argText1 = (b', ').join(items1)
            argText1 = b'(%s)' % argText1
            argText2 = (b', ').join(items2)
            argText2 = b'(%s)' % argText2
        except:
            pass

    return (
     argText1, argText2)


def _turtle_docrevise(docstr):
    import re
    if docstr is None:
        return
    else:
        turtlename = _CFG[b'exampleturtle']
        newdocstr = docstr.replace(b'%s.' % turtlename, b'')
        parexp = re.compile(b' \\(.+ %s\\):' % turtlename)
        newdocstr = parexp.sub(b':', newdocstr)
        return newdocstr


def _screen_docrevise(docstr):
    import re
    if docstr is None:
        return
    else:
        screenname = _CFG[b'examplescreen']
        newdocstr = docstr.replace(b'%s.' % screenname, b'')
        parexp = re.compile(b' \\(.+ %s\\):' % screenname)
        newdocstr = parexp.sub(b':', newdocstr)
        return newdocstr


__func_body = b'def {name}{paramslist}:\n    if {obj} is None:\n        if not TurtleScreen._RUNNING:\n            TurtleScreen._RUNNING = True\n            raise Terminator\n        {obj} = {init}\n    try:\n        return {obj}.{name}{argslist}\n    except TK.TclError:\n        if not TurtleScreen._RUNNING:\n            TurtleScreen._RUNNING = True\n            raise Terminator\n        raise\n'

def _make_global_funcs(functions, cls, obj, init, docrevise):
    for methodname in functions:
        method = getattr(cls, methodname)
        pl1, pl2 = getmethparlist(method)
        if pl1 == b'':
            print b'>>>>>>', pl1, pl2
            continue
        defstr = __func_body.format(obj=obj, init=init, name=methodname, paramslist=pl1, argslist=pl2)
        exec defstr in globals()
        globals()[methodname].__doc__ = docrevise(method.__doc__)

    return


_make_global_funcs(_tg_screen_functions, _Screen, b'Turtle._screen', b'Screen()', _screen_docrevise)
_make_global_funcs(_tg_turtle_functions, Turtle, b'Turtle._pen', b'Turtle()', _turtle_docrevise)
done = mainloop = TK.mainloop
if __name__ == b'__main__':

    def switchpen():
        if isdown():
            pu()
        else:
            pd()
        return


    def demo1():
        reset()
        tracer(True)
        up()
        backward(100)
        down()
        width(3)
        for i in range(3):
            if i == 2:
                fill(1)
            for _ in range(4):
                forward(20)
                left(90)

            if i == 2:
                color(b'maroon')
                fill(0)
            up()
            forward(30)
            down()

        width(1)
        color(b'black')
        tracer(False)
        up()
        right(90)
        forward(100)
        right(90)
        forward(100)
        right(180)
        down()
        write(b'startstart', 1)
        write(u'start', 1)
        color(b'red')
        for i in range(5):
            forward(20)
            left(90)
            forward(20)
            right(90)

        tracer(True)
        fill(1)
        for i in range(5):
            forward(20)
            left(90)
            forward(20)
            right(90)

        fill(0)
        return


    def demo2():
        speed(1)
        st()
        pensize(3)
        setheading(towards(0, 0))
        radius = distance(0, 0) / 2.0
        rt(90)
        for _ in range(18):
            switchpen()
            circle(radius, 10)

        write(b'wait a moment...')
        while undobufferentries():
            undo()

        reset()
        lt(90)
        colormode(255)
        laenge = 10
        pencolor(b'green')
        pensize(3)
        lt(180)
        for i in range(-2, 16):
            if i > 0:
                begin_fill()
                fillcolor(255 - 15 * i, 0, 15 * i)
            for _ in range(3):
                fd(laenge)
                lt(120)

            laenge += 10
            lt(15)
            speed((speed() + 1) % 12)

        end_fill()
        lt(120)
        pu()
        fd(70)
        rt(30)
        pd()
        color(b'red', b'yellow')
        speed(0)
        fill(1)
        for _ in range(4):
            circle(50, 90)
            rt(90)
            fd(30)
            rt(90)

        fill(0)
        lt(90)
        pu()
        fd(30)
        pd()
        shape(b'turtle')
        tri = getturtle()
        tri.resizemode(b'auto')
        turtle = Turtle()
        turtle.resizemode(u'auto')
        turtle.shape(b'turtle')
        turtle.reset()
        turtle.left(90)
        turtle.speed(0)
        turtle.up()
        turtle.goto(280, 40)
        turtle.lt(30)
        turtle.down()
        turtle.speed(6)
        turtle.color(b'blue', u'orange')
        turtle.pensize(2)
        tri.speed(6)
        setheading(towards(turtle))
        count = 1
        while tri.distance(turtle) > 4:
            turtle.fd(3.5)
            turtle.lt(0.6)
            tri.setheading(tri.towards(turtle))
            tri.fd(4)
            if count % 20 == 0:
                turtle.stamp()
                tri.stamp()
                switchpen()
            count += 1

        tri.write(b'CAUGHT! ', font=(b'Arial', 16, b'bold'), align=u'right')
        tri.pencolor(b'black')
        tri.pencolor(u'red')

        def baba(xdummy, ydummy):
            clearscreen()
            bye()
            return

        time.sleep(2)
        while undobufferentries():
            tri.undo()
            turtle.undo()

        tri.fd(50)
        tri.write(b'  Click me!', font=(b'Courier', 12, b'bold'))
        tri.onclick(baba, 1)
        return


    demo1()
    demo2()
    exitonclick()
