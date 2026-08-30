from Tkinter import *
from idlelib import SearchEngine
from idlelib.SearchDialogBase import SearchDialogBase

def _setup(text):
    root = text._root()
    engine = SearchEngine.get(root)
    if not hasattr(engine, b'_searchdialog'):
        engine._searchdialog = SearchDialog(root, engine)
    return engine._searchdialog


def find(text):
    pat = text.get(b'sel.first', b'sel.last')
    return _setup(text).open(text, pat)


def find_again(text):
    return _setup(text).find_again(text)


def find_selection(text):
    return _setup(text).find_selection(text)


class SearchDialog(SearchDialogBase):

    def create_widgets(self):
        SearchDialogBase.create_widgets(self)
        self.make_button(b'Find Next', self.default_command, 1)
        return

    def default_command(self, event=None):
        if not self.engine.getprog():
            return
        self.find_again(self.text)
        return

    def find_again(self, text):
        if not self.engine.getpat():
            self.open(text)
            return False
        else:
            if not self.engine.getprog():
                return False
            res = self.engine.search_text(text)
            if res:
                line, m = res
                i, j = m.span()
                first = b'%d.%d' % (line, i)
                last = b'%d.%d' % (line, j)
                try:
                    selfirst = text.index(b'sel.first')
                    sellast = text.index(b'sel.last')
                    if selfirst == first and sellast == last:
                        text.bell()
                        return False
                except TclError:
                    pass

                text.tag_remove(b'sel', b'1.0', b'end')
                text.tag_add(b'sel', first, last)
                text.mark_set(b'insert', self.engine.isback() and first or last)
                text.see(b'insert')
                return True
            text.bell()
            return False

        return

    def find_selection(self, text):
        pat = text.get(b'sel.first', b'sel.last')
        if pat:
            self.engine.setcookedpat(pat)
        return self.find_again(text)


def _search_dialog(parent):
    root = Tk()
    root.title(b'Test SearchDialog')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))
    text = Text(root)
    text.pack()
    text.insert(b'insert', b'This is a sample string.\n' * 10)

    def show_find():
        text.tag_add(SEL, b'1.0', END)
        s = _setup(text)
        s.open(text)
        text.tag_remove(SEL, b'1.0', END)
        return

    button = Button(root, text=b'Search', command=show_find)
    button.pack()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_search_dialog)
