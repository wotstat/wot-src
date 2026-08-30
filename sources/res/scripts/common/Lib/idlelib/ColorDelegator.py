import time, re, keyword, __builtin__
from idlelib.Delegator import Delegator
from idlelib.configHandler import idleConf
DEBUG = False

def any(name, alternates):
    return b'(?P<%s>' % name + (b'|').join(alternates) + b')'


def make_pat():
    kw = b'\\b' + any(b'KEYWORD', keyword.kwlist) + b'\\b'
    builtinlist = [str(name) for name in dir(__builtin__) if not name.startswith(b'_')]
    builtinlist.remove(b'print')
    builtin = b'([^.\'\\"\\\\#]\\b|^)' + any(b'BUILTIN', builtinlist) + b'\\b'
    comment = any(b'COMMENT', [b'#[^\\n]*'])
    stringprefix = b'(\\br|u|ur|R|U|UR|Ur|uR|b|B|br|Br|bR|BR)?'
    sqstring = stringprefix + b"'[^'\\\\\\n]*(\\\\.[^'\\\\\\n]*)*'?"
    dqstring = stringprefix + b'"[^"\\\\\\n]*(\\\\.[^"\\\\\\n]*)*"?'
    sq3string = stringprefix + b"'''[^'\\\\]*((\\\\.|'(?!''))[^'\\\\]*)*(''')?"
    dq3string = stringprefix + b'"""[^"\\\\]*((\\\\.|"(?!""))[^"\\\\]*)*(""")?'
    string = any(b'STRING', [sq3string, dq3string, sqstring, dqstring])
    return kw + b'|' + builtin + b'|' + comment + b'|' + string + b'|' + any(b'SYNC', [b'\\n'])


prog = re.compile(make_pat(), re.S)
idprog = re.compile(b'\\s+(\\w+)', re.S)

class ColorDelegator(Delegator):

    def __init__(self):
        Delegator.__init__(self)
        self.prog = prog
        self.idprog = idprog
        self.LoadTagDefs()
        return

    def setdelegate(self, delegate):
        if self.delegate is not None:
            self.unbind(b'<<toggle-auto-coloring>>')
        Delegator.setdelegate(self, delegate)
        if delegate is not None:
            self.config_colors()
            self.bind(b'<<toggle-auto-coloring>>', self.toggle_colorize_event)
            self.notify_range(b'1.0', b'end')
        else:
            self.stop_colorizing = True
            self.allow_colorizing = False
        return

    def config_colors(self):
        for tag, cnf in self.tagdefs.items():
            if cnf:
                self.tag_configure(tag, **cnf)

        self.tag_raise(b'sel')
        return

    def LoadTagDefs(self):
        theme = idleConf.CurrentTheme()
        self.tagdefs = {b'COMMENT': (idleConf.GetHighlight(theme, b'comment')), 
           b'KEYWORD': (idleConf.GetHighlight(theme, b'keyword')), 
           b'BUILTIN': (idleConf.GetHighlight(theme, b'builtin')), 
           b'STRING': (idleConf.GetHighlight(theme, b'string')), 
           b'DEFINITION': (idleConf.GetHighlight(theme, b'definition')), 
           b'SYNC': {b'background': None, b'foreground': None}, b'TODO': {b'background': None, b'foreground': None}, b'ERROR': (idleConf.GetHighlight(theme, b'error')), 
           b'hit': (idleConf.GetHighlight(theme, b'hit'))}
        if DEBUG:
            print b'tagdefs', self.tagdefs
        return

    def insert(self, index, chars, tags=None):
        index = self.index(index)
        self.delegate.insert(index, chars, tags)
        self.notify_range(index, index + b'+%dc' % len(chars))
        return

    def delete(self, index1, index2=None):
        index1 = self.index(index1)
        self.delegate.delete(index1, index2)
        self.notify_range(index1)
        return

    after_id = None
    allow_colorizing = True
    colorizing = False

    def notify_range(self, index1, index2=None):
        self.tag_add(b'TODO', index1, index2)
        if self.after_id:
            if DEBUG:
                print b'colorizing already scheduled'
            return
        if self.colorizing:
            self.stop_colorizing = True
            if DEBUG:
                print b'stop colorizing'
        if self.allow_colorizing:
            if DEBUG:
                print b'schedule colorizing'
            self.after_id = self.after(1, self.recolorize)
        return

    close_when_done = None

    def close(self, close_when_done=None):
        if self.after_id:
            after_id = self.after_id
            self.after_id = None
            if DEBUG:
                print b'cancel scheduled recolorizer'
            self.after_cancel(after_id)
        self.allow_colorizing = False
        self.stop_colorizing = True
        if close_when_done:
            if not self.colorizing:
                close_when_done.destroy()
            else:
                self.close_when_done = close_when_done
        return

    def toggle_colorize_event(self, event):
        if self.after_id:
            after_id = self.after_id
            self.after_id = None
            if DEBUG:
                print b'cancel scheduled recolorizer'
            self.after_cancel(after_id)
        if self.allow_colorizing and self.colorizing:
            if DEBUG:
                print b'stop colorizing'
            self.stop_colorizing = True
        self.allow_colorizing = not self.allow_colorizing
        if self.allow_colorizing and not self.colorizing:
            self.after_id = self.after(1, self.recolorize)
        if DEBUG:
            print b'auto colorizing turned',
            print self.allow_colorizing and b'on' or b'off'
        return b'break'

    def recolorize(self):
        self.after_id = None
        if not self.delegate:
            if DEBUG:
                print b'no delegate'
            return
        if not self.allow_colorizing:
            if DEBUG:
                print b'auto colorizing is off'
            return
        if self.colorizing:
            if DEBUG:
                print b'already colorizing'
            return
        try:
            self.stop_colorizing = False
            self.colorizing = True
            if DEBUG:
                print b'colorizing...'
            t0 = time.clock()
            self.recolorize_main()
            t1 = time.clock()
            if DEBUG:
                print b'%.3f seconds' % (t1 - t0)
        finally:
            self.colorizing = False

        if self.allow_colorizing and self.tag_nextrange(b'TODO', b'1.0'):
            if DEBUG:
                print b'reschedule colorizing'
            self.after_id = self.after(1, self.recolorize)
        if self.close_when_done:
            top = self.close_when_done
            self.close_when_done = None
            top.destroy()
        return

    def recolorize_main(self):
        next = b'1.0'
        while True:
            item = self.tag_nextrange(b'TODO', next)
            if not item:
                break
            head, tail = item
            self.tag_remove(b'SYNC', head, tail)
            item = self.tag_prevrange(b'SYNC', head)
            if item:
                head = item[1]
            else:
                head = b'1.0'
            chars = b''
            next = head
            lines_to_get = 1
            ok = False
            while not ok:
                mark = next
                next = self.index(mark + b'+%d lines linestart' % lines_to_get)
                lines_to_get = min(lines_to_get * 2, 100)
                ok = b'SYNC' in self.tag_names(next + b'-1c')
                line = self.get(mark, next)
                if not line:
                    return
                for tag in self.tagdefs.keys():
                    self.tag_remove(tag, mark, next)

                chars = chars + line
                m = self.prog.search(chars)
                while m:
                    for key, value in m.groupdict().items():
                        if value:
                            a, b = m.span(key)
                            self.tag_add(key, head + b'+%dc' % a, head + b'+%dc' % b)
                            if value in (b'def', b'class'):
                                m1 = self.idprog.match(chars, b)
                                if m1:
                                    a, b = m1.span(1)
                                    self.tag_add(b'DEFINITION', head + b'+%dc' % a, head + b'+%dc' % b)

                    m = self.prog.search(chars, m.end())

                if b'SYNC' in self.tag_names(next + b'-1c'):
                    head = next
                    chars = b''
                else:
                    ok = False
                if not ok:
                    self.tag_add(b'TODO', next)
                self.update()
                if self.stop_colorizing:
                    if DEBUG:
                        print b'colorizing stopped'
                    return

        return

    def removecolors(self):
        for tag in self.tagdefs.keys():
            self.tag_remove(tag, b'1.0', b'end')

        return


def _color_delegator(parent):
    from Tkinter import Toplevel, Text
    from idlelib.Percolator import Percolator
    top = Toplevel(parent)
    top.title(b'Test ColorDelegator')
    top.geometry(b'200x100+%d+%d' % (parent.winfo_rootx() + 200,
     parent.winfo_rooty() + 150))
    source = b"if somename: x = 'abc' # comment\nprint\n"
    text = Text(top, background=b'white')
    text.pack(expand=1, fill=b'both')
    text.insert(b'insert', source)
    text.focus_set()
    p = Percolator(text)
    d = ColorDelegator()
    p.insertfilter(d)
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_color_delegator)
