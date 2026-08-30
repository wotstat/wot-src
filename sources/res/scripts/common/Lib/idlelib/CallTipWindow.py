from Tkinter import Toplevel, Label, LEFT, SOLID, TclError
HIDE_VIRTUAL_EVENT_NAME = b'<<calltipwindow-hide>>'
HIDE_SEQUENCES = (b'<Key-Escape>', b'<FocusOut>')
CHECKHIDE_VIRTUAL_EVENT_NAME = b'<<calltipwindow-checkhide>>'
CHECKHIDE_SEQUENCES = (b'<KeyRelease>', b'<ButtonRelease>')
CHECKHIDE_TIME = 100
MARK_RIGHT = b'calltipwindowregion_right'

class CallTip:

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = self.label = None
        self.parenline = self.parencol = None
        self.lastline = None
        self.hideid = self.checkhideid = None
        self.checkhide_after_id = None
        return

    def position_window(self):
        curline = int(self.widget.index(b'insert').split(b'.')[0])
        if curline == self.lastline:
            return
        self.lastline = curline
        self.widget.see(b'insert')
        if curline == self.parenline:
            box = self.widget.bbox(b'%d.%d' % (self.parenline,
             self.parencol))
        else:
            box = self.widget.bbox(b'%d.0' % curline)
        if not box:
            box = list(self.widget.bbox(b'insert'))
            box[0] = 0
            box[2] = 0
        x = box[0] + self.widget.winfo_rootx() + 2
        y = box[1] + box[3] + self.widget.winfo_rooty()
        self.tipwindow.wm_geometry(b'+%d+%d' % (x, y))
        return

    def showtip(self, text, parenleft, parenright):
        self.text = text
        if self.tipwindow or not self.text:
            return
        self.widget.mark_set(MARK_RIGHT, parenright)
        self.parenline, self.parencol = map(int, self.widget.index(parenleft).split(b'.'))
        self.tipwindow = tw = Toplevel(self.widget)
        self.position_window()
        tw.wm_overrideredirect(1)
        try:
            tw.tk.call(b'::tk::unsupported::MacWindowStyle', b'style', tw._w, b'help', b'noActivates')
        except TclError:
            pass

        self.label = Label(tw, text=self.text, justify=LEFT, background=b'#ffffe0', relief=SOLID, borderwidth=1, font=self.widget[b'font'])
        self.label.pack()
        tw.update_idletasks()
        tw.lift()
        self.checkhideid = self.widget.bind(CHECKHIDE_VIRTUAL_EVENT_NAME, self.checkhide_event)
        for seq in CHECKHIDE_SEQUENCES:
            self.widget.event_add(CHECKHIDE_VIRTUAL_EVENT_NAME, seq)

        self.widget.after(CHECKHIDE_TIME, self.checkhide_event)
        self.hideid = self.widget.bind(HIDE_VIRTUAL_EVENT_NAME, self.hide_event)
        for seq in HIDE_SEQUENCES:
            self.widget.event_add(HIDE_VIRTUAL_EVENT_NAME, seq)

        return

    def checkhide_event(self, event=None):
        if not self.tipwindow:
            return
        else:
            curline, curcol = map(int, self.widget.index(b'insert').split(b'.'))
            if curline < self.parenline or curline == self.parenline and curcol <= self.parencol or self.widget.compare(b'insert', b'>', MARK_RIGHT):
                self.hidetip()
            else:
                self.position_window()
                if self.checkhide_after_id is not None:
                    self.widget.after_cancel(self.checkhide_after_id)
                self.checkhide_after_id = self.widget.after(CHECKHIDE_TIME, self.checkhide_event)
            return

    def hide_event(self, event):
        if not self.tipwindow:
            return
        self.hidetip()
        return

    def hidetip(self):
        if not self.tipwindow:
            return
        else:
            for seq in CHECKHIDE_SEQUENCES:
                self.widget.event_delete(CHECKHIDE_VIRTUAL_EVENT_NAME, seq)

            self.widget.unbind(CHECKHIDE_VIRTUAL_EVENT_NAME, self.checkhideid)
            self.checkhideid = None
            for seq in HIDE_SEQUENCES:
                self.widget.event_delete(HIDE_VIRTUAL_EVENT_NAME, seq)

            self.widget.unbind(HIDE_VIRTUAL_EVENT_NAME, self.hideid)
            self.hideid = None
            self.label.destroy()
            self.label = None
            self.tipwindow.destroy()
            self.tipwindow = None
            self.widget.mark_unset(MARK_RIGHT)
            self.parenline = self.parencol = self.lastline = None
            return

    def is_active(self):
        return bool(self.tipwindow)


def _calltip_window(parent):
    from Tkinter import Toplevel, Text, LEFT, BOTH
    top = Toplevel(parent)
    top.title(b'Test calltips')
    top.geometry(b'200x100+%d+%d' % (parent.winfo_rootx() + 200,
     parent.winfo_rooty() + 150))
    text = Text(top)
    text.pack(side=LEFT, fill=BOTH, expand=1)
    text.insert(b'insert', b'string.split')
    top.update()
    calltip = CallTip(text)

    def calltip_show(event):
        calltip.showtip(b'(s=Hello world)', b'insert', b'end')
        return

    def calltip_hide(event):
        calltip.hidetip()
        return

    text.event_add(b'<<calltip-show>>', b'(')
    text.event_add(b'<<calltip-hide>>', b')')
    text.bind(b'<<calltip-show>>', calltip_show)
    text.bind(b'<<calltip-hide>>', calltip_hide)
    text.focus_set()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_calltip_window)
