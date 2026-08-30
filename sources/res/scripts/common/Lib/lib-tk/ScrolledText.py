__all__ = [
 b'ScrolledText']
from Tkinter import Frame, Text, Scrollbar, Pack, Grid, Place
from Tkconstants import RIGHT, LEFT, Y, BOTH

class ScrolledText(Text):

    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)
        kw.update({b'yscrollcommand': (self.vbar.set)})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar[b'command'] = self.yview
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() + vars(Grid).keys() + vars(Place).keys()
        methods = set(methods).difference(text_meths)
        for m in methods:
            if m[0] != b'_' and m != b'config' and m != b'configure':
                setattr(self, m, getattr(self.frame, m))

        return

    def __str__(self):
        return str(self.frame)


def example():
    import __main__
    from Tkconstants import END
    stext = ScrolledText(bg=b'white', height=10)
    stext.insert(END, __main__.__doc__)
    stext.pack(fill=BOTH, side=LEFT, expand=True)
    stext.focus_set()
    stext.mainloop()
    return


if __name__ == b'__main__':
    example()
