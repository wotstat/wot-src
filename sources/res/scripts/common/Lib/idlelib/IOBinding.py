import codecs
from codecs import BOM_UTF8
import os, pipes, re, sys, tempfile
from Tkinter import *
import tkFileDialog, tkMessageBox
from SimpleDialog import SimpleDialog
from idlelib.configHandler import idleConf
try:
    import locale
    locale.setlocale(locale.LC_CTYPE, b'')
except (ImportError, locale.Error):
    pass

filesystemencoding = sys.getfilesystemencoding()
encoding = b'ascii'
if sys.platform == b'win32':
    try:
        encoding = locale.getdefaultlocale()[1]
        codecs.lookup(encoding)
    except LookupError:
        pass

else:
    try:
        encoding = locale.nl_langinfo(locale.CODESET)
        if encoding is None or encoding is b'':
            encoding = b'ascii'
        codecs.lookup(encoding)
    except (NameError, AttributeError, LookupError):
        try:
            encoding = locale.getdefaultlocale()[1]
            if encoding is None or encoding is b'':
                encoding = b'ascii'
            codecs.lookup(encoding)
        except (ValueError, LookupError):
            pass

encoding = encoding.lower()
coding_re = re.compile(b'^[ \\t\\f]*#.*?coding[:=][ \\t]*([-\\w.]+)')
blank_re = re.compile(b'^[ \\t\\f]*(?:[#\\r\\n]|$)')

class EncodingMessage(SimpleDialog):

    def __init__(self, master, enc):
        self.should_edit = False
        self.root = top = Toplevel(master)
        top.bind(b'<Return>', self.return_event)
        top.bind(b'<Escape>', self.do_ok)
        top.protocol(b'WM_DELETE_WINDOW', self.wm_delete_window)
        top.wm_title(b'I/O Warning')
        top.wm_iconname(b'I/O Warning')
        self.top = top
        l1 = Label(top, text=b'Non-ASCII found, yet no encoding declared. Add a line like')
        l1.pack(side=TOP, anchor=W)
        l2 = Entry(top, font=b'courier')
        l2.insert(0, b'# -*- coding: %s -*-' % enc)
        l2.pack(side=TOP, anchor=W, fill=X)
        l3 = Label(top, text=b'to your file\nSee Language Reference, 2.1.4 Encoding declarations.\nChoose OK to save this file as %s\nEdit your general options to silence this warning' % enc)
        l3.pack(side=TOP, anchor=W)
        buttons = Frame(top)
        buttons.pack(side=TOP, fill=X)
        self.default = self.cancel = 0
        b1 = Button(buttons, text=b'Ok', default=b'active', command=self.do_ok)
        b1.pack(side=LEFT, fill=BOTH, expand=1)
        b2 = Button(buttons, text=b'Edit my file', command=self.do_edit)
        b2.pack(side=LEFT, fill=BOTH, expand=1)
        self._set_transient(master)
        return

    def do_ok(self):
        self.done(0)
        return

    def do_edit(self):
        self.done(1)
        return


def coding_spec(str):
    lst = str.split(b'\n', 2)[:2]
    for line in lst:
        match = coding_re.match(line)
        if match is not None:
            break
        if not blank_re.match(line):
            return
    else:
        return

    name = match.group(1)
    import codecs
    try:
        codecs.lookup(name)
    except LookupError:
        raise LookupError, b'Unknown encoding ' + name

    return name


class IOBinding():

    def __init__(self, editwin):
        self.editwin = editwin
        self.text = editwin.text
        self.__id_open = self.text.bind(b'<<open-window-from-file>>', self.open)
        self.__id_save = self.text.bind(b'<<save-window>>', self.save)
        self.__id_saveas = self.text.bind(b'<<save-window-as-file>>', self.save_as)
        self.__id_savecopy = self.text.bind(b'<<save-copy-of-window-as-file>>', self.save_a_copy)
        self.fileencoding = None
        self.__id_print = self.text.bind(b'<<print-window>>', self.print_window)
        return

    def close(self):
        self.text.unbind(b'<<open-window-from-file>>', self.__id_open)
        self.text.unbind(b'<<save-window>>', self.__id_save)
        self.text.unbind(b'<<save-window-as-file>>', self.__id_saveas)
        self.text.unbind(b'<<save-copy-of-window-as-file>>', self.__id_savecopy)
        self.text.unbind(b'<<print-window>>', self.__id_print)
        self.editwin = None
        self.text = None
        self.filename_change_hook = None
        return

    def get_saved(self):
        return self.editwin.get_saved()

    def set_saved(self, flag):
        self.editwin.set_saved(flag)
        return

    def reset_undo(self):
        self.editwin.reset_undo()
        return

    filename_change_hook = None

    def set_filename_change_hook(self, hook):
        self.filename_change_hook = hook
        return

    filename = None
    dirname = None

    def set_filename(self, filename):
        if filename and os.path.isdir(filename):
            self.filename = None
            self.dirname = filename
        else:
            self.filename = filename
            self.dirname = None
            self.set_saved(1)
            if self.filename_change_hook:
                self.filename_change_hook()
        return

    def open(self, event=None, editFile=None):
        flist = self.editwin.flist
        if flist:
            if not editFile:
                filename = self.askopenfile()
            else:
                filename = editFile
            if filename:
                if self.editwin and not getattr(self.editwin, b'interp', None) and not self.filename and self.get_saved():
                    flist.open(filename, self.loadfile)
                else:
                    flist.open(filename)
            elif self.text:
                self.text.focus_set()
            return b'break'
        if self.get_saved():
            reply = self.maybesave()
            if reply == b'cancel':
                self.text.focus_set()
                return b'break'
        if not editFile:
            filename = self.askopenfile()
        else:
            filename = editFile
        if filename:
            self.loadfile(filename)
        else:
            self.text.focus_set()
        return b'break'

    eol = b'(\\r\\n)|\\n|\\r'
    eol_re = re.compile(eol)
    eol_convention = os.linesep

    def loadfile(self, filename):
        try:
            with open(filename, b'rb') as f:
                chars = f.read()
        except IOError as msg:
            tkMessageBox.showerror(b'I/O Error', str(msg), parent=self.text)
            return False

        chars = self.decode(chars)
        firsteol = self.eol_re.search(chars)
        if firsteol:
            self.eol_convention = firsteol.group(0)
            if isinstance(self.eol_convention, unicode):
                self.eol_convention = self.eol_convention.encode(b'ascii')
            chars = self.eol_re.sub(b'\\n', chars)
        self.text.delete(b'1.0', b'end')
        self.set_filename(None)
        self.text.insert(b'1.0', chars)
        self.reset_undo()
        self.set_filename(filename)
        self.text.mark_set(b'insert', b'1.0')
        self.text.yview(b'insert')
        self.updaterecentfileslist(filename)
        return True

    def decode(self, chars):
        if chars.startswith(BOM_UTF8):
            try:
                chars = chars[3:].decode(b'utf-8')
            except UnicodeError:
                return chars

            self.fileencoding = BOM_UTF8
            return chars
        try:
            enc = coding_spec(chars)
        except LookupError as name:
            tkMessageBox.showerror(title=b'Error loading the file', message=b"The encoding '%s' is not known to this Python installation. The file may not display correctly" % name, parent=self.text)
            enc = None

        if enc:
            try:
                return unicode(chars, enc)
            except UnicodeError:
                pass

        try:
            return unicode(chars, b'ascii')
        except UnicodeError:
            pass

        try:
            chars = unicode(chars, encoding)
            self.fileencoding = encoding
        except UnicodeError:
            pass

        return chars

    def maybesave(self):
        if self.get_saved():
            return b'yes'
        else:
            message = b'Do you want to save %s before closing?' % (self.filename or b'this untitled document')
            confirm = tkMessageBox.askyesnocancel(title=b'Save On Close', message=message, default=tkMessageBox.YES, parent=self.text)
            if confirm:
                reply = b'yes'
                self.save(None)
                if not self.get_saved():
                    reply = b'cancel'
            elif confirm is None:
                reply = b'cancel'
            else:
                reply = b'no'
            self.text.focus_set()
            return reply

    def save(self, event):
        if not self.filename:
            self.save_as(event)
        elif self.writefile(self.filename):
            self.set_saved(True)
            try:
                self.editwin.store_file_breaks()
            except AttributeError:
                pass

        self.text.focus_set()
        return b'break'

    def save_as(self, event):
        filename = self.asksavefile()
        if filename:
            if self.writefile(filename):
                self.set_filename(filename)
                self.set_saved(1)
                try:
                    self.editwin.store_file_breaks()
                except AttributeError:
                    pass

        self.text.focus_set()
        self.updaterecentfileslist(filename)
        return b'break'

    def save_a_copy(self, event):
        filename = self.asksavefile()
        if filename:
            self.writefile(filename)
        self.text.focus_set()
        self.updaterecentfileslist(filename)
        return b'break'

    def writefile(self, filename):
        self.fixlastline()
        chars = self.encode(self.text.get(b'1.0', b'end-1c'))
        if self.eol_convention != b'\n':
            chars = chars.replace(b'\n', self.eol_convention)
        try:
            with open(filename, b'wb') as f:
                f.write(chars)
                f.flush()
                os.fsync(f.fileno())
            return True
        except IOError as msg:
            tkMessageBox.showerror(b'I/O Error', str(msg), parent=self.text)
            return False

        return

    def encode(self, chars):
        if isinstance(chars, str):
            return chars
        else:
            try:
                return chars.encode(b'ascii')
            except UnicodeError:
                pass

            try:
                enc = coding_spec(chars)
                failed = None
            except LookupError as msg:
                failed = msg
                enc = None

            if enc:
                try:
                    return chars.encode(enc)
                except UnicodeError:
                    failed = b"Invalid encoding '%s'" % enc

            if failed:
                tkMessageBox.showerror(b'I/O Error', b'%s. Saving as UTF-8' % failed, parent=self.text)
            if self.fileencoding == BOM_UTF8 or failed:
                return BOM_UTF8 + chars.encode(b'utf-8')
            if self.fileencoding:
                try:
                    return chars.encode(self.fileencoding)
                except UnicodeError:
                    tkMessageBox.showerror(b'I/O Error', b"Cannot save this as '%s' anymore. Saving as UTF-8" % self.fileencoding, parent=self.text)
                    return BOM_UTF8 + chars.encode(b'utf-8')

            config_encoding = idleConf.GetOption(b'main', b'EditorWindow', b'encoding')
            if config_encoding == b'utf-8':
                return BOM_UTF8 + chars.encode(b'utf-8')
            ask_user = True
            try:
                chars = chars.encode(encoding)
                enc = encoding
                if config_encoding == b'locale':
                    ask_user = False
            except UnicodeError:
                chars = BOM_UTF8 + chars.encode(b'utf-8')
                enc = b'utf-8'

            if not ask_user:
                return chars
            dialog = EncodingMessage(self.editwin.top, enc)
            dialog.go()
            if dialog.num == 1:
                encline = b'# -*- coding: %s -*-\n' % enc
                firstline = self.text.get(b'1.0', b'2.0')
                if firstline.startswith(b'#!'):
                    self.text.insert(b'2.0', encline)
                else:
                    self.text.insert(b'1.0', encline)
                return self.encode(self.text.get(b'1.0', b'end-1c'))
            return chars

    def fixlastline(self):
        c = self.text.get(b'end-2c')
        if c != b'\n':
            self.text.insert(b'end-1c', b'\n')
        return

    def print_window(self, event):
        confirm = tkMessageBox.askokcancel(title=b'Print', message=b'Print to Default Printer', default=tkMessageBox.OK, parent=self.text)
        if not confirm:
            self.text.focus_set()
            return b'break'
        else:
            tempfilename = None
            saved = self.get_saved()
            if saved:
                filename = self.filename
            if not saved or filename is None:
                tfd, tempfilename = tempfile.mkstemp(prefix=b'IDLE_tmp_')
                filename = tempfilename
                os.close(tfd)
                if not self.writefile(tempfilename):
                    os.unlink(tempfilename)
                    return b'break'
            platform = os.name
            printPlatform = True
            if platform == b'posix':
                command = idleConf.GetOption(b'main', b'General', b'print-command-posix')
                command = command + b' 2>&1'
            elif platform == b'nt':
                command = idleConf.GetOption(b'main', b'General', b'print-command-win')
            else:
                printPlatform = False
            if printPlatform:
                command = command % pipes.quote(filename)
                pipe = os.popen(command, b'r')
                output = pipe.read().strip()
                status = pipe.close()
                if status:
                    output = b'Printing failed (exit status 0x%x)\n' % status + output
                if output:
                    output = b'Printing command: %s\n' % repr(command) + output
                    tkMessageBox.showerror(b'Print status', output, parent=self.text)
            else:
                message = b'Printing is not enabled for this platform: %s' % platform
                tkMessageBox.showinfo(b'Print status', message, parent=self.text)
            if tempfilename:
                os.unlink(tempfilename)
            return b'break'

    opendialog = None
    savedialog = None
    filetypes = [
     (b'Python files', b'*.py *.pyw', b'TEXT'),
     (b'Text files', b'*.txt', b'TEXT'),
     (b'All files', b'*')]
    defaultextension = b'.py' if sys.platform == b'darwin' else b''

    def askopenfile(self):
        dir, base = self.defaultfilename(b'open')
        if not self.opendialog:
            self.opendialog = tkFileDialog.Open(parent=self.text, filetypes=self.filetypes)
        filename = self.opendialog.show(initialdir=dir, initialfile=base)
        if isinstance(filename, unicode):
            filename = filename.encode(filesystemencoding)
        return filename

    def defaultfilename(self, mode=b'open'):
        if self.filename:
            return os.path.split(self.filename)
        else:
            if self.dirname:
                return (self.dirname, b'')
            try:
                pwd = os.getcwd()
            except os.error:
                pwd = b''

            return (
             pwd, b'')

        return

    def asksavefile(self):
        dir, base = self.defaultfilename(b'save')
        if not self.savedialog:
            self.savedialog = tkFileDialog.SaveAs(parent=self.text, filetypes=self.filetypes, defaultextension=self.defaultextension)
        filename = self.savedialog.show(initialdir=dir, initialfile=base)
        if isinstance(filename, unicode):
            filename = filename.encode(filesystemencoding)
        return filename

    def updaterecentfileslist(self, filename):
        self.editwin.update_recent_files_list(filename)
        return


def _io_binding(parent):
    from Tkinter import Toplevel, Text
    root = Toplevel(parent)
    root.title(b'Test IOBinding')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))

    class MyEditWin:

        def __init__(self, text):
            self.text = text
            self.flist = None
            self.text.bind(b'<Control-o>', self.open)
            self.text.bind(b'<Control-p>', self.printer)
            self.text.bind(b'<Control-s>', self.save)
            self.text.bind(b'<Alt-s>', self.saveas)
            self.text.bind(b'<Control-c>', self.savecopy)
            return

        def get_saved(self):
            return 0

        def set_saved(self, flag):
            return

        def reset_undo(self):
            return

        def update_recent_files_list(self, filename):
            return

        def open(self, event):
            self.text.event_generate(b'<<open-window-from-file>>')
            return

        def printer(self, event):
            self.text.event_generate(b'<<print-window>>')
            return

        def save(self, event):
            self.text.event_generate(b'<<save-window>>')
            return

        def saveas(self, event):
            self.text.event_generate(b'<<save-window-as-file>>')
            return

        def savecopy(self, event):
            self.text.event_generate(b'<<save-copy-of-window-as-file>>')
            return

    text = Text(root)
    text.pack()
    text.focus_set()
    editwin = MyEditWin(text)
    IOBinding(editwin)
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_io_binding)
