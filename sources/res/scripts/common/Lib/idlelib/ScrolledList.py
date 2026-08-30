from Tkinter import *
from idlelib import macosxSupport

class ScrolledList:
    default = b'(None)'

    def __init__(self, master, **options):
        self.master = master
        self.frame = frame = Frame(master)
        self.frame.pack(fill=b'both', expand=1)
        self.vbar = vbar = Scrollbar(frame, name=b'vbar')
        self.vbar.pack(side=b'right', fill=b'y')
        self.listbox = listbox = Listbox(frame, exportselection=0, background=b'white')
        if options:
            listbox.configure(options)
        listbox.pack(expand=1, fill=b'both')
        vbar[b'command'] = listbox.yview
        listbox[b'yscrollcommand'] = vbar.set
        listbox.bind(b'<ButtonRelease-1>', self.click_event)
        listbox.bind(b'<Double-ButtonRelease-1>', self.double_click_event)
        if macosxSupport.isAquaTk():
            listbox.bind(b'<ButtonPress-2>', self.popup_event)
            listbox.bind(b'<Control-Button-1>', self.popup_event)
        else:
            listbox.bind(b'<ButtonPress-3>', self.popup_event)
        listbox.bind(b'<Key-Up>', self.up_event)
        listbox.bind(b'<Key-Down>', self.down_event)
        self.clear()
        return

    def close(self):
        self.frame.destroy()
        return

    def clear(self):
        self.listbox.delete(0, b'end')
        self.empty = 1
        self.listbox.insert(b'end', self.default)
        return

    def append(self, item):
        if self.empty:
            self.listbox.delete(0, b'end')
            self.empty = 0
        self.listbox.insert(b'end', str(item))
        return

    def get(self, index):
        return self.listbox.get(index)

    def click_event(self, event):
        self.listbox.activate(b'@%d,%d' % (event.x, event.y))
        index = self.listbox.index(b'active')
        self.select(index)
        self.on_select(index)
        return b'break'

    def double_click_event(self, event):
        index = self.listbox.index(b'active')
        self.select(index)
        self.on_double(index)
        return b'break'

    menu = None

    def popup_event(self, event):
        if not self.menu:
            self.make_menu()
        menu = self.menu
        self.listbox.activate(b'@%d,%d' % (event.x, event.y))
        index = self.listbox.index(b'active')
        self.select(index)
        menu.tk_popup(event.x_root, event.y_root)
        return

    def make_menu(self):
        menu = Menu(self.listbox, tearoff=0)
        self.menu = menu
        self.fill_menu()
        return

    def up_event(self, event):
        index = self.listbox.index(b'active')
        if self.listbox.selection_includes(index):
            index = index - 1
        else:
            index = self.listbox.size() - 1
        if index < 0:
            self.listbox.bell()
        else:
            self.select(index)
            self.on_select(index)
        return b'break'

    def down_event(self, event):
        index = self.listbox.index(b'active')
        if self.listbox.selection_includes(index):
            index = index + 1
        else:
            index = 0
        if index >= self.listbox.size():
            self.listbox.bell()
        else:
            self.select(index)
            self.on_select(index)
        return b'break'

    def select(self, index):
        self.listbox.focus_set()
        self.listbox.activate(index)
        self.listbox.selection_clear(0, b'end')
        self.listbox.selection_set(index)
        self.listbox.see(index)
        return

    def fill_menu(self):
        return

    def on_select(self, index):
        return

    def on_double(self, index):
        return


def _scrolled_list(parent):
    root = Tk()
    root.title(b'Test ScrolledList')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))

    class MyScrolledList(ScrolledList):

        def fill_menu(self):
            self.menu.add_command(label=b'right click')
            return

        def on_select(self, index):
            print b'select', self.get(index)
            return

        def on_double(self, index):
            print b'double', self.get(index)
            return

    scrolled_list = MyScrolledList(root)
    for i in range(30):
        scrolled_list.append(b'Item %02d' % i)

    root.mainloop()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_scrolled_list)
