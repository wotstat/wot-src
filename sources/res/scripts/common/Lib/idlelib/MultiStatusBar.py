from Tkinter import *

class MultiStatusBar(Frame):

    def __init__(self, master=None, **kw):
        if master is None:
            master = Tk()
        Frame.__init__(self, master, **kw)
        self.labels = {}
        return

    def set_label(self, name, text=b'', side=LEFT, width=0):
        if name not in self.labels:
            label = Label(self, borderwidth=0, anchor=W)
            label.pack(side=side, pady=0, padx=4)
            self.labels[name] = label
        else:
            label = self.labels[name]
        if width != 0:
            label.config(width=width)
        label.config(text=text)
        return


def _multistatus_bar(parent):
    root = Tk()
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))
    root.title(b'Test multistatus bar')
    frame = Frame(root)
    text = Text(frame)
    text.pack()
    msb = MultiStatusBar(frame)
    msb.set_label(b'one', b'hello')
    msb.set_label(b'two', b'world')
    msb.pack(side=BOTTOM, fill=X)

    def change():
        msb.set_label(b'one', b'foo')
        msb.set_label(b'two', b'bar')
        return

    button = Button(root, text=b'Update status', command=change)
    button.pack(side=BOTTOM)
    frame.pack()
    frame.mainloop()
    root.mainloop()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_multistatus_bar)
