__version__ = b'0.9'
import Tkinter
NORMAL = b'normal'
ROMAN = b'roman'
BOLD = b'bold'
ITALIC = b'italic'

def nametofont(name):
    return Font(name=name, exists=True)


class Font:

    def _set(self, kw):
        options = []
        for k, v in kw.items():
            if not isinstance(v, basestring):
                v = str(v)
            options.append(b'-' + k)
            options.append(v)

        return tuple(options)

    def _get(self, args):
        options = []
        for k in args:
            options.append(b'-' + k)

        return tuple(options)

    def _mkdict(self, args):
        options = {}
        for i in range(0, len(args), 2):
            options[args[i][1:]] = args[i + 1]

        return options

    def __init__(self, root=None, font=None, name=None, exists=False, **options):
        if not root:
            root = Tkinter._default_root
        tk = getattr(root, b'tk', root)
        if font:
            font = tk.splitlist(tk.call(b'font', b'actual', font))
        else:
            font = self._set(options)
        if not name:
            name = b'font' + str(id(self))
        self.name = name
        if exists:
            self.delete_font = False
            if self.name not in tk.splitlist(tk.call(b'font', b'names')):
                raise Tkinter._tkinter.TclError, b'named font %s does not already exist' % (self.name,)
            if font:
                tk.call(b'font', b'configure', self.name, *font)
        else:
            tk.call(b'font', b'create', self.name, *font)
            self.delete_font = True
        self._tk = tk
        self._split = tk.splitlist
        self._call = tk.call
        return

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Font) and self.name == other.name

    def __getitem__(self, key):
        return self.cget(key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})
        return

    def __del__(self):
        try:
            if self.delete_font:
                self._call(b'font', b'delete', self.name)
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            pass

        return

    def copy(self):
        return Font(self._tk, **self.actual())

    def actual(self, option=None):
        if option:
            return self._call(b'font', b'actual', self.name, b'-' + option)
        else:
            return self._mkdict(self._split(self._call(b'font', b'actual', self.name)))

        return

    def cget(self, option):
        return self._call(b'font', b'config', self.name, b'-' + option)

    def config(self, **options):
        if options:
            self._call(b'font', b'config', self.name, *self._set(options))
        else:
            return self._mkdict(self._split(self._call(b'font', b'config', self.name)))
        return

    configure = config

    def measure(self, text):
        return int(self._call(b'font', b'measure', self.name, text))

    def metrics(self, *options):
        if options:
            return int(self._call(b'font', b'metrics', self.name, self._get(options)))
        else:
            res = self._split(self._call(b'font', b'metrics', self.name))
            options = {}
            for i in range(0, len(res), 2):
                options[res[i][1:]] = int(res[i + 1])

            return options

        return


def families(root=None):
    if not root:
        root = Tkinter._default_root
    return root.tk.splitlist(root.tk.call(b'font', b'families'))


def names(root=None):
    if not root:
        root = Tkinter._default_root
    return root.tk.splitlist(root.tk.call(b'font', b'names'))


if __name__ == b'__main__':
    root = Tkinter.Tk()
    f = Font(family=b'times', size=30, weight=NORMAL)
    print f.actual()
    print f.actual(b'family')
    print f.actual(b'weight')
    print f.config()
    print f.cget(b'family')
    print f.cget(b'weight')
    print names()
    print f.measure(b'hello'), f.metrics(b'linespace')
    print f.metrics()
    f = Font(font=(b'Courier', 20, b'bold'))
    print f.measure(b'hello'), f.metrics(b'linespace')
    w = Tkinter.Label(root, text=b'Hello, world', font=f)
    w.pack()
    w = Tkinter.Button(root, text=b'Quit!', command=root.destroy)
    w.pack()
    fb = Font(font=w[b'font']).copy()
    fb.config(weight=BOLD)
    w.config(font=fb)
    Tkinter.mainloop()
