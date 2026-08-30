from Tkinter import *
from Tkinter import _cnfmerge
if TkVersion <= 3.6:
    DIALOG_ICON = b'warning'
else:
    DIALOG_ICON = b'questhead'

class Dialog(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        cnf = _cnfmerge((cnf, kw))
        self.widgetName = b'__dialog__'
        Widget._setup(self, master, cnf)
        self.num = self.tk.getint(self.tk.call(b'tk_dialog', self._w, cnf[b'title'], cnf[b'text'], cnf[b'bitmap'], cnf[b'default'], *cnf[b'strings']))
        try:
            Widget.destroy(self)
        except TclError:
            pass

        return

    def destroy(self):
        return


def _test():
    d = Dialog(None, {b'title': b'File Modified', b'text': b'File "Python.h" has been modified since the last time it was saved. Do you want to save it before exiting the application.', 
       b'bitmap': DIALOG_ICON, 
       b'default': 0, 
       b'strings': (b'Save File', b'Discard Changes', b'Return to Editor')})
    print d.num
    return


if __name__ == b'__main__':
    t = Button(None, {b'text': b'Test', b'command': _test, 
       Pack: {}})
    q = Button(None, {b'text': b'Quit', b'command': (t.quit), 
       Pack: {}})
    t.mainloop()
