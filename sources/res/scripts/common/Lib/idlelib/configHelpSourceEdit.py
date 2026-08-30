import os, sys
from Tkinter import *
import tkMessageBox, tkFileDialog

class GetHelpSourceDialog(Toplevel):

    def __init__(self, parent, title, menuItem=b'', filePath=b'', _htest=False):
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        self.resizable(height=FALSE, width=FALSE)
        self.title(title)
        self.transient(parent)
        self.grab_set()
        self.protocol(b'WM_DELETE_WINDOW', self.Cancel)
        self.parent = parent
        self.result = None
        self.CreateWidgets()
        self.menu.set(menuItem)
        self.path.set(filePath)
        self.withdraw()
        self.update_idletasks()
        self.geometry(b'+%d+%d' % (
         parent.winfo_rootx() + (parent.winfo_width() / 2 - self.winfo_reqwidth() / 2),
         parent.winfo_rooty() + ((_htest or parent.winfo_height() / 2) - self.winfo_reqheight() / 2 if 1 else 150)))
        self.deiconify()
        self.bind(b'<Return>', self.Ok)
        self.wait_window()
        return

    def CreateWidgets(self):
        self.menu = StringVar(self)
        self.path = StringVar(self)
        self.fontSize = StringVar(self)
        self.frameMain = Frame(self, borderwidth=2, relief=GROOVE)
        self.frameMain.pack(side=TOP, expand=TRUE, fill=BOTH)
        labelMenu = Label(self.frameMain, anchor=W, justify=LEFT, text=b'Menu Item:')
        self.entryMenu = Entry(self.frameMain, textvariable=self.menu, width=30)
        self.entryMenu.focus_set()
        labelPath = Label(self.frameMain, anchor=W, justify=LEFT, text=b'Help File Path: Enter URL or browse for file')
        self.entryPath = Entry(self.frameMain, textvariable=self.path, width=40)
        self.entryMenu.focus_set()
        labelMenu.pack(anchor=W, padx=5, pady=3)
        self.entryMenu.pack(anchor=W, padx=5, pady=3)
        labelPath.pack(anchor=W, padx=5, pady=3)
        self.entryPath.pack(anchor=W, padx=5, pady=3)
        browseButton = Button(self.frameMain, text=b'Browse', width=8, command=self.browseFile)
        browseButton.pack(pady=3)
        frameButtons = Frame(self)
        frameButtons.pack(side=BOTTOM, fill=X)
        self.buttonOk = Button(frameButtons, text=b'OK', width=8, default=ACTIVE, command=self.Ok)
        self.buttonOk.grid(row=0, column=0, padx=5, pady=5)
        self.buttonCancel = Button(frameButtons, text=b'Cancel', width=8, command=self.Cancel)
        self.buttonCancel.grid(row=0, column=1, padx=5, pady=5)
        return

    def browseFile(self):
        filetypes = [
         19, 
         20, 
         21, 
         22, 
         23]
        path = self.path.get()
        if path:
            dir, base = os.path.split(path)
        else:
            base = None
            if sys.platform[:3] == b'win':
                dir = os.path.join(os.path.dirname(sys.executable), b'Doc')
                if not os.path.isdir(dir):
                    dir = os.getcwd()
            else:
                dir = os.getcwd()
        opendialog = tkFileDialog.Open(parent=self, filetypes=filetypes)
        file = opendialog.show(initialdir=dir, initialfile=base)
        if file:
            self.path.set(file)
        return

    def MenuOk(self):
        menuOk = True
        menu = self.menu.get()
        menu.strip()
        if not menu:
            tkMessageBox.showerror(title=b'Menu Item Error', message=b'No menu item specified', parent=self)
            self.entryMenu.focus_set()
            menuOk = False
        elif len(menu) > 30:
            tkMessageBox.showerror(title=b'Menu Item Error', message=b'Menu item too long:\nLimit 30 characters.', parent=self)
            self.entryMenu.focus_set()
            menuOk = False
        return menuOk

    def PathOk(self):
        pathOk = True
        path = self.path.get()
        path.strip()
        if not path:
            tkMessageBox.showerror(title=b'File Path Error', message=b'No help file path specified.', parent=self)
            self.entryPath.focus_set()
            pathOk = False
        elif path.startswith((b'www.', b'http')):
            pass
        elif path[:5] == b'file:':
            path = path[5:]
        if not os.path.exists(path):
            tkMessageBox.showerror(title=b'File Path Error', message=b'Help file path does not exist.', parent=self)
            self.entryPath.focus_set()
            pathOk = False
        return pathOk

    def Ok(self, event=None):
        if self.MenuOk() and self.PathOk():
            self.result = (
             self.menu.get().strip(),
             self.path.get().strip())
            if sys.platform == b'darwin':
                path = self.result[1]
                if path.startswith((b'www', b'file:', b'http:')):
                    pass
                else:
                    self.result = list(self.result)
                    self.result[1] = b'file://' + path
            self.grab_release()
            self.destroy()
        return

    def Cancel(self, event=None):
        self.result = None
        self.grab_release()
        self.destroy()
        return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(GetHelpSourceDialog)
