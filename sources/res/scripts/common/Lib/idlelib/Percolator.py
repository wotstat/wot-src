from idlelib.WidgetRedirector import WidgetRedirector
from idlelib.Delegator import Delegator

class Percolator:

    def __init__(self, text):
        self.text = text
        self.redir = WidgetRedirector(text)
        self.top = self.bottom = Delegator(text)
        self.bottom.insert = self.redir.register(b'insert', self.insert)
        self.bottom.delete = self.redir.register(b'delete', self.delete)
        self.filters = []
        return

    def close(self):
        while self.top is not self.bottom:
            self.removefilter(self.top)

        self.top = None
        self.bottom.setdelegate(None)
        self.bottom = None
        self.redir.close()
        self.redir = None
        self.text = None
        return

    def insert(self, index, chars, tags=None):
        self.top.insert(index, chars, tags)
        return

    def delete(self, index1, index2=None):
        self.top.delete(index1, index2)
        return

    def insertfilter(self, filter):
        filter.setdelegate(self.top)
        self.top = filter
        return

    def removefilter(self, filter):
        f = self.top
        if f is filter:
            self.top = filter.delegate
            filter.setdelegate(None)
        else:
            while f.delegate is not filter:
                f.resetcache()
                f = f.delegate

            f.setdelegate(filter.delegate)
            filter.setdelegate(None)
        return


def _percolator(parent):
    import Tkinter as tk, re

    class Tracer(Delegator):

        def __init__(self, name):
            self.name = name
            Delegator.__init__(self, None)
            return

        def insert(self, *args):
            print self.name, b': insert', args
            self.delegate.insert(*args)
            return

        def delete(self, *args):
            print self.name, b': delete', args
            self.delegate.delete(*args)
            return

    root = tk.Tk()
    root.title(b'Test Percolator')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))
    text = tk.Text(root)
    p = Percolator(text)
    t1 = Tracer(b't1')
    t2 = Tracer(b't2')

    def toggle1():
        if var1.get() == 0:
            var1.set(1)
            p.insertfilter(t1)
        elif var1.get() == 1:
            var1.set(0)
            p.removefilter(t1)
        return

    def toggle2():
        if var2.get() == 0:
            var2.set(1)
            p.insertfilter(t2)
        elif var2.get() == 1:
            var2.set(0)
            p.removefilter(t2)
        return

    text.pack()
    var1 = tk.IntVar()
    cb1 = tk.Checkbutton(root, text=b'Tracer1', command=toggle1, variable=var1)
    cb1.pack()
    var2 = tk.IntVar()
    cb2 = tk.Checkbutton(root, text=b'Tracer2', command=toggle2, variable=var2)
    cb2.pack()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_percolator)
