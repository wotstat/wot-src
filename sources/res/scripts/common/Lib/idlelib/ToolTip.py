from Tkinter import *

class ToolTipBase:

    def __init__(self, button):
        self.button = button
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind(b'<Enter>', self.enter)
        self._id2 = self.button.bind(b'<Leave>', self.leave)
        self._id3 = self.button.bind(b'<ButtonPress>', self.leave)
        return

    def enter(self, event=None):
        self.schedule()
        return

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
        return

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(1500, self.showtip)
        return

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.button.after_cancel(id)
        return

    def showtip(self):
        if self.tipwindow:
            return
        x = self.button.winfo_rootx() + 20
        y = self.button.winfo_rooty() + self.button.winfo_height() + 1
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(1)
        tw.wm_geometry(b'+%d+%d' % (x, y))
        self.showcontents()
        return

    def showcontents(self, text=b'Your text here'):
        label = Label(self.tipwindow, text=text, justify=LEFT, background=b'#ffffe0', relief=SOLID, borderwidth=1)
        label.pack()
        return

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
        return


class ToolTip(ToolTipBase):

    def __init__(self, button, text):
        ToolTipBase.__init__(self, button)
        self.text = text
        return

    def showcontents(self):
        ToolTipBase.showcontents(self, self.text)
        return


class ListboxToolTip(ToolTipBase):

    def __init__(self, button, items):
        ToolTipBase.__init__(self, button)
        self.items = items
        return

    def showcontents(self):
        listbox = Listbox(self.tipwindow, background=b'#ffffe0')
        listbox.pack()
        for item in self.items:
            listbox.insert(END, item)

        return


def _tooltip(parent):
    root = Tk()
    root.title(b'Test tooltip')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))
    label = Label(root, text=b'Place your mouse over buttons')
    label.pack()
    button1 = Button(root, text=b'Button 1')
    button2 = Button(root, text=b'Button 2')
    button1.pack()
    button2.pack()
    ToolTip(button1, b'This is tooltip text for button1.')
    ListboxToolTip(button2, [b'This is', b'multiple line',
     b'tooltip text', b'for button2'])
    root.mainloop()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_tooltip)
