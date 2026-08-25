from Tkinter import *

class Dialog(Toplevel):

    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        self.withdraw()
        if parent.winfo_viewable():
            self.transient(parent)
        if title:
            self.title(title)
        self.parent = parent
        self.result = None
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)
        self.buttonbox()
        if not self.initial_focus:
            self.initial_focus = self
        self.protocol(b'WM_DELETE_WINDOW', self.cancel)
        if self.parent is not None:
            self.geometry(b'+%d+%d' % (parent.winfo_rootx() + 50,
             parent.winfo_rooty() + 50))
        self.deiconify()
        self.initial_focus.focus_set()
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)
        return

    def destroy(self):
        self.initial_focus = None
        Toplevel.destroy(self)
        return

    def body(self, master):
        return

    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text=b'OK', width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text=b'Cancel', width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind(b'<Return>', self.ok)
        self.bind(b'<Escape>', self.cancel)
        box.pack()
        return

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return
        self.withdraw()
        self.update_idletasks()
        try:
            self.apply()
        finally:
            self.cancel()

        return

    def cancel(self, event=None):
        if self.parent is not None:
            self.parent.focus_set()
        self.destroy()
        return

    def validate(self):
        return 1

    def apply(self):
        return


class _QueryDialog(Dialog):

    def __init__(self, title, prompt, initialvalue=None, minvalue=None, maxvalue=None, parent=None):
        if not parent:
            import Tkinter
            parent = Tkinter._default_root
        self.prompt = prompt
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.initialvalue = initialvalue
        Dialog.__init__(self, parent, title)
        return

    def destroy(self):
        self.entry = None
        Dialog.destroy(self)
        return

    def body(self, master):
        w = Label(master, text=self.prompt, justify=LEFT)
        w.grid(row=0, padx=5, sticky=W)
        self.entry = Entry(master, name=b'entry')
        self.entry.grid(row=1, padx=5, sticky=W + E)
        if self.initialvalue is not None:
            self.entry.insert(0, self.initialvalue)
            self.entry.select_range(0, END)
        return self.entry

    def validate(self):
        import tkMessageBox
        try:
            result = self.getresult()
        except ValueError:
            tkMessageBox.showwarning(b'Illegal value', self.errormessage + b'\nPlease try again', parent=self)
            return 0

        if self.minvalue is not None and result < self.minvalue:
            tkMessageBox.showwarning(b'Too small', b'The allowed minimum value is %s. Please try again.' % self.minvalue, parent=self)
            return 0
        else:
            if self.maxvalue is not None and result > self.maxvalue:
                tkMessageBox.showwarning(b'Too large', b'The allowed maximum value is %s. Please try again.' % self.maxvalue, parent=self)
                return 0
            self.result = result
            return 1


class _QueryInteger(_QueryDialog):
    errormessage = b'Not an integer.'

    def getresult(self):
        return int(self.entry.get())


def askinteger(title, prompt, **kw):
    d = _QueryInteger(title, prompt, **kw)
    return d.result


class _QueryFloat(_QueryDialog):
    errormessage = b'Not a floating point value.'

    def getresult(self):
        return float(self.entry.get())


def askfloat(title, prompt, **kw):
    d = _QueryFloat(title, prompt, **kw)
    return d.result


class _QueryString(_QueryDialog):

    def __init__(self, *args, **kw):
        if b'show' in kw:
            self.__show = kw[b'show']
            del kw[b'show']
        else:
            self.__show = None
        _QueryDialog.__init__(self, *args, **kw)
        return

    def body(self, master):
        entry = _QueryDialog.body(self, master)
        if self.__show is not None:
            entry.configure(show=self.__show)
        return entry

    def getresult(self):
        return self.entry.get()


def askstring(title, prompt, **kw):
    d = _QueryString(title, prompt, **kw)
    return d.result


if __name__ == b'__main__':
    root = Tk()
    root.update()
    print askinteger(b'Spam', b'Egg count', initialvalue=144)
    print askfloat(b'Spam', b'Egg weight\n(in tons)', minvalue=1, maxvalue=100)
    print askstring(b'Spam', b'Egg label')
