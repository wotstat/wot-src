import re
from Tkinter import StringVar, BooleanVar, TclError
import tkMessageBox

def get(root):
    if not hasattr(root, b'_searchengine'):
        root._searchengine = SearchEngine(root)
    return root._searchengine


class SearchEngine:

    def __init__(self, root):
        self.root = root
        self.patvar = StringVar(root, b'')
        self.revar = BooleanVar(root, False)
        self.casevar = BooleanVar(root, False)
        self.wordvar = BooleanVar(root, False)
        self.wrapvar = BooleanVar(root, True)
        self.backvar = BooleanVar(root, False)
        return

    def getpat(self):
        return self.patvar.get()

    def setpat(self, pat):
        self.patvar.set(pat)
        return

    def isre(self):
        return self.revar.get()

    def iscase(self):
        return self.casevar.get()

    def isword(self):
        return self.wordvar.get()

    def iswrap(self):
        return self.wrapvar.get()

    def isback(self):
        return self.backvar.get()

    def setcookedpat(self, pat):
        if self.isre():
            pat = re.escape(pat)
        self.setpat(pat)
        return

    def getcookedpat(self):
        pat = self.getpat()
        if not self.isre():
            pat = re.escape(pat)
        if self.isword():
            pat = b'\\b%s\\b' % pat
        return pat

    def getprog(self):
        pat = self.getpat()
        if not pat:
            self.report_error(pat, b'Empty regular expression')
            return
        else:
            pat = self.getcookedpat()
            flags = 0
            if not self.iscase():
                flags = flags | re.IGNORECASE
            try:
                prog = re.compile(pat, flags)
            except re.error as what:
                args = what.args
                msg = args[0]
                col = args[1] if len(args) >= 2 else -1
                self.report_error(pat, msg, col)
                return

            return prog

    def report_error(self, pat, msg, col=-1):
        msg = b'Error: ' + str(msg)
        if pat:
            msg = msg + b'\nPattern: ' + str(pat)
        if col >= 0:
            msg = msg + b'\nOffset: ' + str(col)
        tkMessageBox.showerror(b'Regular expression error', msg, master=self.root)
        return

    def search_text(self, text, prog=None, ok=0):
        if not prog:
            prog = self.getprog()
            if not prog:
                return None
        wrap = self.wrapvar.get()
        first, last = get_selection(text)
        if self.isback():
            if ok:
                start = last
            else:
                start = first
            line, col = get_line_col(start)
            res = self.search_backward(text, prog, line, col, wrap, ok)
        else:
            if ok:
                start = first
            else:
                start = last
            line, col = get_line_col(start)
            res = self.search_forward(text, prog, line, col, wrap, ok)
        return res

    def search_forward(self, text, prog, line, col, wrap, ok=0):
        wrapped = 0
        startline = line
        chars = text.get(b'%d.0' % line, b'%d.0' % (line + 1))
        while chars:
            m = prog.search(chars[:-1], col)
            if m:
                if ok or m.end() > col:
                    return (line, m)
            line = line + 1
            if wrapped and line > startline:
                break
            col = 0
            ok = 1
            chars = text.get(b'%d.0' % line, b'%d.0' % (line + 1))
            if not chars and wrap:
                wrapped = 1
                wrap = 0
                line = 1
                chars = text.get(b'1.0', b'2.0')

        return

    def search_backward(self, text, prog, line, col, wrap, ok=0):
        wrapped = 0
        startline = line
        chars = text.get(b'%d.0' % line, b'%d.0' % (line + 1))
        while 1:
            m = search_reverse(prog, chars[:-1], col)
            if m:
                if ok or m.start() < col:
                    return (line, m)
            line = line - 1
            if wrapped and line < startline:
                break
            ok = 1
            if line <= 0:
                if not wrap:
                    break
                wrapped = 1
                wrap = 0
                pos = text.index(b'end-1c')
                line, col = map(int, pos.split(b'.'))
            chars = text.get(b'%d.0' % line, b'%d.0' % (line + 1))
            col = len(chars) - 1

        return


def search_reverse(prog, chars, col):
    m = prog.search(chars)
    if not m:
        return
    else:
        found = None
        i, j = m.span()
        while i < col and j <= col:
            found = m
            if i == j:
                j = j + 1
            m = prog.search(chars, j)
            if not m:
                break
            i, j = m.span()

        return found


def get_selection(text):
    try:
        first = text.index(b'sel.first')
        last = text.index(b'sel.last')
    except TclError:
        first = last = None

    if not first:
        first = text.index(b'insert')
    if not last:
        last = first
    return (
     first, last)


def get_line_col(index):
    line, col = map(int, index.split(b'.'))
    return (line, col)


if __name__ == b'__main__':
    import unittest
    unittest.main(b'idlelib.idle_test.test_searchengine', verbosity=2, exit=False)
