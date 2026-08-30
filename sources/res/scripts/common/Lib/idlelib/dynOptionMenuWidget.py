import copy
from Tkinter import OptionMenu, _setit, StringVar, Button

class DynOptionMenu(OptionMenu):

    def __init__(self, master, variable, value, *values, **kwargs):
        kwargsCopy = copy.copy(kwargs)
        if b'highlightthickness' in kwargs.keys():
            del kwargs[b'highlightthickness']
        OptionMenu.__init__(self, master, variable, value, *values, **kwargs)
        self.config(highlightthickness=kwargsCopy.get(b'highlightthickness'))
        self.variable = variable
        self.command = kwargs.get(b'command')
        return

    def SetMenu(self, valueList, value=None):
        self[b'menu'].delete(0, b'end')
        for item in valueList:
            self[b'menu'].add_command(label=item, command=_setit(self.variable, item, self.command))

        if value:
            self.variable.set(value)
        return


def _dyn_option_menu(parent):
    from Tkinter import Toplevel
    top = Toplevel()
    top.title(b'Tets dynamic option menu')
    top.geometry(b'200x100+%d+%d' % (parent.winfo_rootx() + 200,
     parent.winfo_rooty() + 150))
    top.focus_set()
    var = StringVar(top)
    var.set(b'Old option set')
    dyn = DynOptionMenu(top, var, b'old1', b'old2', b'old3', b'old4')
    dyn.pack()

    def update():
        dyn.SetMenu([b'new1', b'new2', b'new3', b'new4'], value=b'new option set')
        return

    button = Button(top, text=b'Change option set', command=update)
    button.pack()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_dyn_option_menu)
