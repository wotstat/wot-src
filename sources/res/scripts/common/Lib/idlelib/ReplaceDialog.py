from Tkinter import *
from idlelib import SearchEngine
from idlelib.SearchDialogBase import SearchDialogBase
import re

def replace(text):
    root = text._root()
    engine = SearchEngine.get(root)
    if not hasattr(engine, b'_replacedialog'):
        engine._replacedialog = ReplaceDialog(root, engine)
    dialog = engine._replacedialog
    dialog.open(text)
    return


class ReplaceDialog(SearchDialogBase):
    title = b'Replace Dialog'
    icon = b'Replace'

    def __init__(self, root, engine):
        SearchDialogBase.__init__(self, root, engine)
        self.replvar = StringVar(root)
        return

    def open(self, text):
        SearchDialogBase.open(self, text)
        try:
            first = text.index(b'sel.first')
        except TclError:
            first = None

        try:
            last = text.index(b'sel.last')
        except TclError:
            last = None

        first = first or text.index(b'insert')
        last = last or first
        self.show_hit(first, last)
        self.ok = 1
        return

    def create_entries(self):
        SearchDialogBase.create_entries(self)
        self.replent = self.make_entry(b'Replace with:', self.replvar)[0]
        return

    def create_command_buttons(self):
        SearchDialogBase.create_command_buttons(self)
        self.make_button(b'Find', self.find_it)
        self.make_button(b'Replace', self.replace_it)
        self.make_button(b'Replace+Find', self.default_command, 1)
        self.make_button(b'Replace All', self.replace_all)
        return

    def find_it(self, event=None):
        self.do_find(0)
        return

    def replace_it(self, event=None):
        if self.do_find(self.ok):
            self.do_replace()
        return

    def default_command(self, event=None):
        if self.do_find(self.ok):
            if self.do_replace():
                self.do_find(0)
        return

    def _replace_expand(self, m, repl):
        if self.engine.isre():
            try:
                new = m.expand(repl)
            except re.error:
                self.engine.report_error(repl, b'Invalid Replace Expression')
                new = None

        else:
            new = repl
        return new

    def replace_all(self, event=None):
        prog = self.engine.getprog()
        if not prog:
            return
        else:
            repl = self.replvar.get()
            text = self.text
            res = self.engine.search_text(text, prog)
            if not res:
                text.bell()
                return
            text.tag_remove(b'sel', b'1.0', b'end')
            text.tag_remove(b'hit', b'1.0', b'end')
            line = res[0]
            col = res[1].start()
            if self.engine.iswrap():
                line = 1
                col = 0
            ok = 1
            first = last = None
            text.undo_block_start()
            while 1:
                res = self.engine.search_forward(text, prog, line, col, 0, ok)
                if not res:
                    break
                line, m = res
                chars = text.get(b'%d.0' % line, b'%d.0' % (line + 1))
                orig = m.group()
                new = self._replace_expand(m, repl)
                if new is None:
                    break
                i, j = m.span()
                first = b'%d.%d' % (line, i)
                last = b'%d.%d' % (line, j)
                if new == orig:
                    text.mark_set(b'insert', last)
                else:
                    text.mark_set(b'insert', first)
                    if first != last:
                        text.delete(first, last)
                    if new:
                        text.insert(first, new)
                col = i + len(new)
                ok = 0

            text.undo_block_stop()
            if first and last:
                self.show_hit(first, last)
            self.close()
            return

    def do_find(self, ok=0):
        if not self.engine.getprog():
            return False
        else:
            text = self.text
            res = self.engine.search_text(text, None, ok)
            if not res:
                text.bell()
                return False
            line, m = res
            i, j = m.span()
            first = b'%d.%d' % (line, i)
            last = b'%d.%d' % (line, j)
            self.show_hit(first, last)
            self.ok = 1
            return True

    def do_replace(self):
        prog = self.engine.getprog()
        if not prog:
            return False
        else:
            text = self.text
            try:
                first = pos = text.index(b'sel.first')
                last = text.index(b'sel.last')
            except TclError:
                pos = None

            if not pos:
                first = last = pos = text.index(b'insert')
            line, col = SearchEngine.get_line_col(pos)
            chars = text.get(b'%d.0' % line, b'%d.0' % (line + 1))
            m = prog.match(chars, col)
            if not prog:
                return False
            new = self._replace_expand(m, self.replvar.get())
            if new is None:
                return False
            text.mark_set(b'insert', first)
            text.undo_block_start()
            if m.group():
                text.delete(first, last)
            if new:
                text.insert(first, new)
            text.undo_block_stop()
            self.show_hit(first, text.index(b'insert'))
            self.ok = 0
            return True

    def show_hit(self, first, last):
        text = self.text
        text.mark_set(b'insert', first)
        text.tag_remove(b'sel', b'1.0', b'end')
        text.tag_add(b'sel', first, last)
        text.tag_remove(b'hit', b'1.0', b'end')
        if first == last:
            text.tag_add(b'hit', first)
        else:
            text.tag_add(b'hit', first, last)
        text.see(b'insert')
        text.update_idletasks()
        return

    def close(self, event=None):
        SearchDialogBase.close(self, event)
        self.text.tag_remove(b'hit', b'1.0', b'end')
        return


def _replace_dialog(parent):
    root = Tk()
    root.title(b'Test ReplaceDialog')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))

    def undo_block_start():
        return

    def undo_block_stop():
        return

    text = Text(root)
    text.undo_block_start = undo_block_start
    text.undo_block_stop = undo_block_stop
    text.pack()
    text.insert(b'insert', b'This is a sample string.\n' * 10)

    def show_replace():
        text.tag_add(SEL, b'1.0', END)
        replace(text)
        text.tag_remove(SEL, b'1.0', END)
        return

    button = Button(root, text=b'Replace', command=show_replace)
    button.pack()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_replace_dialog)
