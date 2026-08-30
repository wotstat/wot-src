from Tkinter import *
from Dialog import Dialog
import os, fnmatch
dialogstates = {}

class FileDialog:
    title = b'File Selection Dialog'

    def __init__(self, master, title=None):
        if title is None:
            title = self.title
        self.master = master
        self.directory = None
        self.top = Toplevel(master)
        self.top.title(title)
        self.top.iconname(title)
        self.botframe = Frame(self.top)
        self.botframe.pack(side=BOTTOM, fill=X)
        self.selection = Entry(self.top)
        self.selection.pack(side=BOTTOM, fill=X)
        self.selection.bind(b'<Return>', self.ok_event)
        self.filter = Entry(self.top)
        self.filter.pack(side=TOP, fill=X)
        self.filter.bind(b'<Return>', self.filter_command)
        self.midframe = Frame(self.top)
        self.midframe.pack(expand=YES, fill=BOTH)
        self.filesbar = Scrollbar(self.midframe)
        self.filesbar.pack(side=RIGHT, fill=Y)
        self.files = Listbox(self.midframe, exportselection=0, yscrollcommand=(
         self.filesbar, b'set'))
        self.files.pack(side=RIGHT, expand=YES, fill=BOTH)
        btags = self.files.bindtags()
        self.files.bindtags(btags[1:] + btags[:1])
        self.files.bind(b'<ButtonRelease-1>', self.files_select_event)
        self.files.bind(b'<Double-ButtonRelease-1>', self.files_double_event)
        self.filesbar.config(command=(self.files, b'yview'))
        self.dirsbar = Scrollbar(self.midframe)
        self.dirsbar.pack(side=LEFT, fill=Y)
        self.dirs = Listbox(self.midframe, exportselection=0, yscrollcommand=(
         self.dirsbar, b'set'))
        self.dirs.pack(side=LEFT, expand=YES, fill=BOTH)
        self.dirsbar.config(command=(self.dirs, b'yview'))
        btags = self.dirs.bindtags()
        self.dirs.bindtags(btags[1:] + btags[:1])
        self.dirs.bind(b'<ButtonRelease-1>', self.dirs_select_event)
        self.dirs.bind(b'<Double-ButtonRelease-1>', self.dirs_double_event)
        self.ok_button = Button(self.botframe, text=b'OK', command=self.ok_command)
        self.ok_button.pack(side=LEFT)
        self.filter_button = Button(self.botframe, text=b'Filter', command=self.filter_command)
        self.filter_button.pack(side=LEFT, expand=YES)
        self.cancel_button = Button(self.botframe, text=b'Cancel', command=self.cancel_command)
        self.cancel_button.pack(side=RIGHT)
        self.top.protocol(b'WM_DELETE_WINDOW', self.cancel_command)
        self.top.bind(b'<Alt-w>', self.cancel_command)
        self.top.bind(b'<Alt-W>', self.cancel_command)
        return

    def go(self, dir_or_file=os.curdir, pattern=b'*', default=b'', key=None):
        if key and key in dialogstates:
            self.directory, pattern = dialogstates[key]
        else:
            dir_or_file = os.path.expanduser(dir_or_file)
            if os.path.isdir(dir_or_file):
                self.directory = dir_or_file
            else:
                self.directory, default = os.path.split(dir_or_file)
        self.set_filter(self.directory, pattern)
        self.set_selection(default)
        self.filter_command()
        self.selection.focus_set()
        self.top.wait_visibility()
        self.top.grab_set()
        self.how = None
        self.master.mainloop()
        if key:
            directory, pattern = self.get_filter()
            if self.how:
                directory = os.path.dirname(self.how)
            dialogstates[key] = (
             directory, pattern)
        self.top.destroy()
        return self.how

    def quit(self, how=None):
        self.how = how
        self.master.quit()
        return

    def dirs_double_event(self, event):
        self.filter_command()
        return

    def dirs_select_event(self, event):
        dir, pat = self.get_filter()
        subdir = self.dirs.get(b'active')
        dir = os.path.normpath(os.path.join(self.directory, subdir))
        self.set_filter(dir, pat)
        return

    def files_double_event(self, event):
        self.ok_command()
        return

    def files_select_event(self, event):
        file = self.files.get(b'active')
        self.set_selection(file)
        return

    def ok_event(self, event):
        self.ok_command()
        return

    def ok_command(self):
        self.quit(self.get_selection())
        return

    def filter_command(self, event=None):
        dir, pat = self.get_filter()
        try:
            names = os.listdir(dir)
        except os.error:
            self.master.bell()
            return

        self.directory = dir
        self.set_filter(dir, pat)
        names.sort()
        subdirs = [os.pardir]
        matchingfiles = []
        for name in names:
            fullname = os.path.join(dir, name)
            if os.path.isdir(fullname):
                subdirs.append(name)
            elif fnmatch.fnmatch(name, pat):
                matchingfiles.append(name)

        self.dirs.delete(0, END)
        for name in subdirs:
            self.dirs.insert(END, name)

        self.files.delete(0, END)
        for name in matchingfiles:
            self.files.insert(END, name)

        head, tail = os.path.split(self.get_selection())
        if tail == os.curdir:
            tail = b''
        self.set_selection(tail)
        return

    def get_filter(self):
        filter = self.filter.get()
        filter = os.path.expanduser(filter)
        if filter[-1:] == os.sep or os.path.isdir(filter):
            filter = os.path.join(filter, b'*')
        return os.path.split(filter)

    def get_selection(self):
        file = self.selection.get()
        file = os.path.expanduser(file)
        return file

    def cancel_command(self, event=None):
        self.quit()
        return

    def set_filter(self, dir, pat):
        if not os.path.isabs(dir):
            try:
                pwd = os.getcwd()
            except os.error:
                pwd = None

            if pwd:
                dir = os.path.join(pwd, dir)
                dir = os.path.normpath(dir)
        self.filter.delete(0, END)
        self.filter.insert(END, os.path.join(dir or os.curdir, pat or b'*'))
        return

    def set_selection(self, file):
        self.selection.delete(0, END)
        self.selection.insert(END, os.path.join(self.directory, file))
        return


class LoadFileDialog(FileDialog):
    title = b'Load File Selection Dialog'

    def ok_command(self):
        file = self.get_selection()
        if not os.path.isfile(file):
            self.master.bell()
        else:
            self.quit(file)
        return


class SaveFileDialog(FileDialog):
    title = b'Save File Selection Dialog'

    def ok_command(self):
        file = self.get_selection()
        if os.path.exists(file):
            if os.path.isdir(file):
                self.master.bell()
                return
            d = Dialog(self.top, title=b'Overwrite Existing File Question', text=b'Overwrite existing file %r?' % (file,), bitmap=b'questhead', default=1, strings=(b'Yes', b'Cancel'))
            if d.num != 0:
                return
        else:
            head, tail = os.path.split(file)
            if not os.path.isdir(head):
                self.master.bell()
                return
        self.quit(file)
        return


def test():
    root = Tk()
    root.withdraw()
    fd = LoadFileDialog(root)
    loadfile = fd.go(key=b'test')
    fd = SaveFileDialog(root)
    savefile = fd.go(key=b'test')
    print loadfile, savefile
    return


if __name__ == b'__main__':
    test()
