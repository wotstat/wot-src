from Tkinter import *
from idlelib.EditorWindow import EditorWindow
import re, tkMessageBox
from idlelib import IOBinding

class OutputWindow(EditorWindow):

    def __init__(self, *args):
        EditorWindow.__init__(self, *args)
        self.text.bind(b'<<goto-file-line>>', self.goto_file_line)
        return

    def ispythonsource(self, filename):
        return 0

    def short_title(self):
        return b'Output'

    def maybesave(self):
        if self.get_saved():
            return b'yes'
        else:
            return b'no'

        return

    def write(self, s, tags=(), mark=b'insert'):
        if isinstance(s, str):
            try:
                s = unicode(s, IOBinding.encoding)
            except UnicodeError:
                pass

        self.text.insert(mark, s, tags)
        self.text.see(mark)
        self.text.update()
        return

    def writelines(self, lines):
        for line in lines:
            self.write(line)

        return

    def flush(self):
        return

    rmenu_specs = [
     27, 
     28, 
     29, 
     31, 
     32]
    file_line_pats = [
     19, 
     20, 
     21, 
     22, 
     23]
    file_line_progs = None

    def goto_file_line(self, event=None):
        if self.file_line_progs is None:
            l = []
            for pat in self.file_line_pats:
                l.append(re.compile(pat, re.IGNORECASE))

            self.file_line_progs = l
        line = self.text.get(b'insert linestart', b'insert lineend')
        result = self._file_line_helper(line)
        if not result:
            line = self.text.get(b'insert -1line linestart', b'insert -1line lineend')
            result = self._file_line_helper(line)
            if not result:
                tkMessageBox.showerror(b'No special line', b"The line you point at doesn't look like a valid file name followed by a line number.", parent=self.text)
                return
        filename, lineno = result
        edit = self.flist.open(filename)
        edit.gotoline(lineno)
        return

    def _file_line_helper(self, line):
        for prog in self.file_line_progs:
            match = prog.search(line)
            if match:
                filename, lineno = match.group(1, 2)
                try:
                    f = open(filename, b'r')
                    f.close()
                    break
                except IOError:
                    continue

        else:
            return

        try:
            return (
             filename, int(lineno))
        except TypeError:
            return

        return


class OnDemandOutputWindow:
    tagdefs = {b'stdout': {b'foreground': b'blue'}, b'stderr': {b'foreground': b'#007700'}}

    def __init__(self, flist):
        self.flist = flist
        self.owin = None
        return

    def write(self, s, tags, mark):
        if not self.owin:
            self.setup()
        self.owin.write(s, tags, mark)
        return

    def setup(self):
        self.owin = owin = OutputWindow(self.flist)
        text = owin.text
        for tag, cnf in self.tagdefs.items():
            if cnf:
                text.tag_configure(tag, **cnf)

        text.tag_raise(b'sel')
        self.write = self.owin.write
        return
