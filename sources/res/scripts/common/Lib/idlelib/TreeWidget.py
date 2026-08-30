import os
from Tkinter import *
import imp
from idlelib import ZoomHeight
from idlelib.configHandler import idleConf
ICONDIR = b'Icons'
try:
    _icondir = os.path.join(os.path.dirname(__file__), ICONDIR)
except NameError:
    _icondir = ICONDIR

if os.path.isdir(_icondir):
    ICONDIR = _icondir
elif not os.path.isdir(ICONDIR):
    raise RuntimeError, b"can't find icon directory (%r)" % (ICONDIR,)

def listicons(icondir=ICONDIR):
    root = Tk()
    import glob
    list = glob.glob(os.path.join(icondir, b'*.gif'))
    list.sort()
    images = []
    row = column = 0
    for file in list:
        name = os.path.splitext(os.path.basename(file))[0]
        image = PhotoImage(file=file, master=root)
        images.append(image)
        label = Label(root, image=image, bd=1, relief=b'raised')
        label.grid(row=row, column=column)
        label = Label(root, text=name)
        label.grid(row=row + 1, column=column)
        column = column + 1
        if column >= 10:
            row = row + 2
            column = 0

    root.images = images
    return


class TreeNode:

    def __init__(self, canvas, parent, item):
        self.canvas = canvas
        self.parent = parent
        self.item = item
        self.state = b'collapsed'
        self.selected = False
        self.children = []
        self.x = self.y = None
        self.iconimages = {}
        return

    def destroy(self):
        for c in self.children[:]:
            self.children.remove(c)
            c.destroy()

        self.parent = None
        return

    def geticonimage(self, name):
        try:
            return self.iconimages[name]
        except KeyError:
            pass

        file, ext = os.path.splitext(name)
        ext = ext or b'.gif'
        fullname = os.path.join(ICONDIR, file + ext)
        image = PhotoImage(master=self.canvas, file=fullname)
        self.iconimages[name] = image
        return image

    def select(self, event=None):
        if self.selected:
            return
        self.deselectall()
        self.selected = True
        self.canvas.delete(self.image_id)
        self.drawicon()
        self.drawtext()
        return

    def deselect(self, event=None):
        if not self.selected:
            return
        self.selected = False
        self.canvas.delete(self.image_id)
        self.drawicon()
        self.drawtext()
        return

    def deselectall(self):
        if self.parent:
            self.parent.deselectall()
        else:
            self.deselecttree()
        return

    def deselecttree(self):
        if self.selected:
            self.deselect()
        for child in self.children:
            child.deselecttree()

        return

    def flip(self, event=None):
        if self.state == b'expanded':
            self.collapse()
        else:
            self.expand()
        self.item.OnDoubleClick()
        return b'break'

    def expand(self, event=None):
        if not self.item._IsExpandable():
            return
        if self.state != b'expanded':
            self.state = b'expanded'
            self.update()
            self.view()
        return

    def collapse(self, event=None):
        if self.state != b'collapsed':
            self.state = b'collapsed'
            self.update()
        return

    def view(self):
        top = self.y - 2
        bottom = self.lastvisiblechild().y + 17
        height = bottom - top
        visible_top = self.canvas.canvasy(0)
        visible_height = self.canvas.winfo_height()
        visible_bottom = self.canvas.canvasy(visible_height)
        if visible_top <= top and bottom <= visible_bottom:
            return
        x0, y0, x1, y1 = self.canvas._getints(self.canvas[b'scrollregion'])
        if top >= visible_top and height <= visible_height:
            fraction = top + height - visible_height
        else:
            fraction = top
        fraction = float(fraction) / y1
        self.canvas.yview_moveto(fraction)
        return

    def lastvisiblechild(self):
        if self.children and self.state == b'expanded':
            return self.children[-1].lastvisiblechild()
        else:
            return self

        return

    def update(self):
        if self.parent:
            self.parent.update()
        else:
            oldcursor = self.canvas[b'cursor']
            self.canvas[b'cursor'] = b'watch'
            self.canvas.update()
            self.canvas.delete(ALL)
            self.draw(7, 2)
            x0, y0, x1, y1 = self.canvas.bbox(ALL)
            self.canvas.configure(scrollregion=(0, 0, x1, y1))
            self.canvas[b'cursor'] = oldcursor
        return

    def draw(self, x, y):
        dy = 20
        self.x, self.y = x, y
        self.drawicon()
        self.drawtext()
        if self.state != b'expanded':
            return y + dy
        if not self.children:
            sublist = self.item._GetSubList()
            if not sublist:
                return y + 17
            for item in sublist:
                child = self.__class__(self.canvas, self, item)
                self.children.append(child)

        cx = x + 20
        cy = y + dy
        cylast = 0
        for child in self.children:
            cylast = cy
            self.canvas.create_line(x + 9, cy + 7, cx, cy + 7, fill=b'gray50')
            cy = child.draw(cx, cy)
            if child.item._IsExpandable():
                if child.state == b'expanded':
                    iconname = b'minusnode'
                    callback = child.collapse
                else:
                    iconname = b'plusnode'
                    callback = child.expand
                image = self.geticonimage(iconname)
                id = self.canvas.create_image(x + 9, cylast + 7, image=image)
                self.canvas.tag_bind(id, b'<1>', callback)
                self.canvas.tag_bind(id, b'<Double-1>', (lambda x: None))

        id = self.canvas.create_line(x + 9, y + 10, x + 9, cylast + 7, fill=b'gray50')
        self.canvas.tag_lower(id)
        return cy

    def drawicon(self):
        if self.selected:
            imagename = self.item.GetSelectedIconName() or self.item.GetIconName() or b'openfolder'
        else:
            imagename = self.item.GetIconName() or b'folder'
        image = self.geticonimage(imagename)
        id = self.canvas.create_image(self.x, self.y, anchor=b'nw', image=image)
        self.image_id = id
        self.canvas.tag_bind(id, b'<1>', self.select)
        self.canvas.tag_bind(id, b'<Double-1>', self.flip)
        return

    def drawtext(self):
        textx = self.x + 20 - 1
        texty = self.y - 4
        labeltext = self.item.GetLabelText()
        if labeltext:
            id = self.canvas.create_text(textx, texty, anchor=b'nw', text=labeltext)
            self.canvas.tag_bind(id, b'<1>', self.select)
            self.canvas.tag_bind(id, b'<Double-1>', self.flip)
            x0, y0, x1, y1 = self.canvas.bbox(id)
            textx = max(x1, 200) + 10
        text = self.item.GetText() or b'<no text>'
        try:
            self.entry
        except AttributeError:
            pass
        else:
            self.edit_finish()

        try:
            self.label
        except AttributeError:
            self.label = Label(self.canvas, text=text, bd=0, padx=2, pady=2)

        theme = idleConf.CurrentTheme()
        if self.selected:
            self.label.configure(idleConf.GetHighlight(theme, b'hilite'))
        else:
            self.label.configure(idleConf.GetHighlight(theme, b'normal'))
        id = self.canvas.create_window(textx, texty, anchor=b'nw', window=self.label)
        self.label.bind(b'<1>', self.select_or_edit)
        self.label.bind(b'<Double-1>', self.flip)
        self.text_id = id
        return

    def select_or_edit(self, event=None):
        if self.selected and self.item.IsEditable():
            self.edit(event)
        else:
            self.select(event)
        return

    def edit(self, event=None):
        self.entry = Entry(self.label, bd=0, highlightthickness=1, width=0)
        self.entry.insert(0, self.label[b'text'])
        self.entry.selection_range(0, END)
        self.entry.pack(ipadx=5)
        self.entry.focus_set()
        self.entry.bind(b'<Return>', self.edit_finish)
        self.entry.bind(b'<Escape>', self.edit_cancel)
        return

    def edit_finish(self, event=None):
        try:
            entry = self.entry
            del self.entry
        except AttributeError:
            return

        text = entry.get()
        entry.destroy()
        if text and text != self.item.GetText():
            self.item.SetText(text)
        text = self.item.GetText()
        self.label[b'text'] = text
        self.drawtext()
        self.canvas.focus_set()
        return

    def edit_cancel(self, event=None):
        try:
            entry = self.entry
            del self.entry
        except AttributeError:
            return

        entry.destroy()
        self.drawtext()
        self.canvas.focus_set()
        return


class TreeItem:

    def __init__(self):
        return

    def GetText(self):
        return

    def GetLabelText(self):
        return

    expandable = None

    def _IsExpandable(self):
        if self.expandable is None:
            self.expandable = self.IsExpandable()
        return self.expandable

    def IsExpandable(self):
        return 1

    def _GetSubList(self):
        if not self.IsExpandable():
            return []
        sublist = self.GetSubList()
        if not sublist:
            self.expandable = 0
        return sublist

    def IsEditable(self):
        return

    def SetText(self, text):
        return

    def GetIconName(self):
        return

    def GetSelectedIconName(self):
        return

    def GetSubList(self):
        return

    def OnDoubleClick(self):
        return


class FileTreeItem(TreeItem):

    def __init__(self, path):
        self.path = path
        return

    def GetText(self):
        return os.path.basename(self.path) or self.path

    def IsEditable(self):
        return os.path.basename(self.path) != b''

    def SetText(self, text):
        newpath = os.path.dirname(self.path)
        newpath = os.path.join(newpath, text)
        if os.path.dirname(newpath) != os.path.dirname(self.path):
            return
        try:
            os.rename(self.path, newpath)
            self.path = newpath
        except os.error:
            pass

        return

    def GetIconName(self):
        if not self.IsExpandable():
            return b'python'
        return

    def IsExpandable(self):
        return os.path.isdir(self.path)

    def GetSubList(self):
        try:
            names = os.listdir(self.path)
        except os.error:
            return []

        names.sort(key=os.path.normcase)
        sublist = []
        for name in names:
            item = FileTreeItem(os.path.join(self.path, name))
            sublist.append(item)

        return sublist


class ScrolledCanvas:

    def __init__(self, master, **opts):
        if b'yscrollincrement' not in opts:
            opts[b'yscrollincrement'] = 17
        self.master = master
        self.frame = Frame(master)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.canvas = Canvas(self.frame, **opts)
        self.canvas.grid(row=0, column=0, sticky=b'nsew')
        self.vbar = Scrollbar(self.frame, name=b'vbar')
        self.vbar.grid(row=0, column=1, sticky=b'nse')
        self.hbar = Scrollbar(self.frame, name=b'hbar', orient=b'horizontal')
        self.hbar.grid(row=1, column=0, sticky=b'ews')
        self.canvas[b'yscrollcommand'] = self.vbar.set
        self.vbar[b'command'] = self.canvas.yview
        self.canvas[b'xscrollcommand'] = self.hbar.set
        self.hbar[b'command'] = self.canvas.xview
        self.canvas.bind(b'<Key-Prior>', self.page_up)
        self.canvas.bind(b'<Key-Next>', self.page_down)
        self.canvas.bind(b'<Key-Up>', self.unit_up)
        self.canvas.bind(b'<Key-Down>', self.unit_down)
        self.canvas.bind(b'<Alt-Key-2>', self.zoom_height)
        self.canvas.focus_set()
        return

    def page_up(self, event):
        self.canvas.yview_scroll(-1, b'page')
        return b'break'

    def page_down(self, event):
        self.canvas.yview_scroll(1, b'page')
        return b'break'

    def unit_up(self, event):
        self.canvas.yview_scroll(-1, b'unit')
        return b'break'

    def unit_down(self, event):
        self.canvas.yview_scroll(1, b'unit')
        return b'break'

    def zoom_height(self, event):
        ZoomHeight.zoom_height(self.master)
        return b'break'


def _tree_widget(parent):
    root = Tk()
    root.title(b'Test TreeWidget')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))
    sc = ScrolledCanvas(root, bg=b'white', highlightthickness=0, takefocus=1)
    sc.frame.pack(expand=1, fill=b'both', side=LEFT)
    item = FileTreeItem(os.getcwd())
    node = TreeNode(sc.canvas, None, item)
    node.expand()
    root.mainloop()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_tree_widget)
