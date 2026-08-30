import sys, os, platform, re, imp
from Tkinter import *
import tkSimpleDialog, tkMessageBox, webbrowser
from idlelib.MultiCall import MultiCallCreator
from idlelib import WindowList
from idlelib import SearchDialog
from idlelib import GrepDialog
from idlelib import ReplaceDialog
from idlelib import PyParse
from idlelib.configHandler import idleConf
from idlelib import aboutDialog, textView, configDialog
from idlelib import macosxSupport
from idlelib import help
TK_TABWIDTH_DEFAULT = 8
_py_version = b' (%s)' % platform.python_version()

def _sphinx_version():
    major, minor, micro, level, serial = sys.version_info
    release = b'%s%s' % (major, minor)
    if micro:
        release += b'%s' % (micro,)
    if level == b'candidate':
        release += b'rc%s' % (serial,)
    elif level != b'final':
        release += b'%s%s' % (level[0], serial)
    return release


def _find_module(fullname, path=None):
    file = None
    for tgt in fullname.split(b'.'):
        if file is not None:
            file.close()
        file, filename, descr = imp.find_module(tgt, path)
        if descr[2] == imp.PY_SOURCE:
            break
        module = imp.load_module(tgt, file, filename, descr)
        try:
            path = module.__path__
        except AttributeError:
            raise ImportError, b'No source for module ' + module.__name__

    if descr[2] != imp.PY_SOURCE:
        m = __import__(fullname)
        try:
            filename = m.__file__
        except AttributeError:
            pass
        else:
            file = None
            base, ext = os.path.splitext(filename)
            if ext == b'.pyc':
                ext = b'.py'
            filename = base + ext
            descr = (filename, None, imp.PY_SOURCE)

    return (
     file, filename, descr)


class HelpDialog(object):

    def __init__(self):
        self.parent = None
        self.dlg = None
        return

    def display(self, parent, near=None):
        import warnings as w
        w.warn(b'EditorWindow.HelpDialog is no longer used by Idle.\nIt will be removed in 3.6 or later.\nIt has been replaced by private help.HelpWindow\n', DeprecationWarning, stacklevel=2)
        if self.dlg is None:
            self.show_dialog(parent)
        if near:
            self.nearwindow(near)
        return

    def show_dialog(self, parent):
        self.parent = parent
        fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), b'help.txt')
        self.dlg = dlg = textView.view_file(parent, b'Help', fn, modal=False)
        dlg.bind(b'<Destroy>', self.destroy, b'+')
        return

    def nearwindow(self, near):
        dlg = self.dlg
        geom = (near.winfo_rootx() + 10, near.winfo_rooty() + 10)
        dlg.withdraw()
        dlg.geometry(b'=+%d+%d' % geom)
        dlg.deiconify()
        dlg.lift()
        return

    def destroy(self, ev=None):
        self.dlg = None
        self.parent = None
        return


helpDialog = HelpDialog()

class EditorWindow(object):
    from idlelib.Percolator import Percolator
    from idlelib.ColorDelegator import ColorDelegator
    from idlelib.UndoDelegator import UndoDelegator
    from idlelib.IOBinding import IOBinding, filesystemencoding, encoding
    from idlelib import Bindings
    from Tkinter import Toplevel
    from idlelib.MultiStatusBar import MultiStatusBar
    help_url = None

    def __init__(self, flist=None, filename=None, key=None, root=None):
        if EditorWindow.help_url is None:
            dochome = os.path.join(sys.prefix, b'Doc', b'index.html')
            if sys.platform.count(b'linux'):
                pyver = b'python-docs-' + b'%s.%s.%s' % sys.version_info[:3]
                if os.path.isdir(b'/var/www/html/python/'):
                    dochome = b'/var/www/html/python/index.html'
                else:
                    basepath = b'/usr/share/doc/'
                    dochome = os.path.join(basepath, pyver, b'Doc', b'index.html')
            elif sys.platform[:3] == b'win':
                chmfile = os.path.join(sys.prefix, b'Doc', b'Python%s.chm' % _sphinx_version())
                if os.path.isfile(chmfile):
                    dochome = chmfile
            elif sys.platform == b'darwin':
                dochome = os.path.join(sys.prefix, b'Resources/English.lproj/Documentation/index.html')
            dochome = os.path.normpath(dochome)
            if os.path.isfile(dochome):
                EditorWindow.help_url = dochome
                if sys.platform == b'darwin':
                    EditorWindow.help_url = b'file://' + EditorWindow.help_url
            else:
                EditorWindow.help_url = b'https://docs.python.org/%d.%d/' % sys.version_info[:2]
        self.flist = flist
        root = root or flist.root
        self.root = root
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = b'>>> '

        self.menubar = Menu(root)
        self.top = top = WindowList.ListedToplevel(root, menu=self.menubar)
        if flist:
            self.tkinter_vars = flist.vars
            self.top.instance_dict = flist.inversedict
        else:
            self.tkinter_vars = {}
            self.top.instance_dict = {}
        self.recent_files_path = os.path.join(idleConf.GetUserCfgDir(), b'recent-files.lst')
        self.text_frame = text_frame = Frame(top)
        self.vbar = vbar = Scrollbar(text_frame, name=b'vbar')
        self.width = idleConf.GetOption(b'main', b'EditorWindow', b'width', type=b'int')
        text_options = {b'name': b'text', 
           b'padx': 5, 
           b'wrap': b'none', 
           b'highlightthickness': 0, 
           b'width': (self.width), 
           b'height': (idleConf.GetOption(b'main', b'EditorWindow', b'height', type=b'int'))}
        if TkVersion >= 8.5:
            text_options[b'tabstyle'] = b'wordprocessor'
        self.text = text = MultiCallCreator(Text)(text_frame, **text_options)
        self.top.focused_widget = self.text
        self.createmenubar()
        self.apply_bindings()
        self.top.protocol(b'WM_DELETE_WINDOW', self.close)
        self.top.bind(b'<<close-window>>', self.close_event)
        if macosxSupport.isAquaTk():
            text.bind(b'<<close-window>>', self.close_event)
            text.bind(b'<Control-Button-1>', self.right_menu_event)
            text.bind(b'<2>', self.right_menu_event)
        else:
            text.bind(b'<3>', self.right_menu_event)
        text.bind(b'<<cut>>', self.cut)
        text.bind(b'<<copy>>', self.copy)
        text.bind(b'<<paste>>', self.paste)
        text.bind(b'<<center-insert>>', self.center_insert_event)
        text.bind(b'<<help>>', self.help_dialog)
        text.bind(b'<<python-docs>>', self.python_docs)
        text.bind(b'<<about-idle>>', self.about_dialog)
        text.bind(b'<<open-config-dialog>>', self.config_dialog)
        text.bind(b'<<open-module>>', self.open_module)
        text.bind(b'<<do-nothing>>', (lambda event: b'break'))
        text.bind(b'<<select-all>>', self.select_all)
        text.bind(b'<<remove-selection>>', self.remove_selection)
        text.bind(b'<<find>>', self.find_event)
        text.bind(b'<<find-again>>', self.find_again_event)
        text.bind(b'<<find-in-files>>', self.find_in_files_event)
        text.bind(b'<<find-selection>>', self.find_selection_event)
        text.bind(b'<<replace>>', self.replace_event)
        text.bind(b'<<goto-line>>', self.goto_line_event)
        text.bind(b'<<smart-backspace>>', self.smart_backspace_event)
        text.bind(b'<<newline-and-indent>>', self.newline_and_indent_event)
        text.bind(b'<<smart-indent>>', self.smart_indent_event)
        text.bind(b'<<indent-region>>', self.indent_region_event)
        text.bind(b'<<dedent-region>>', self.dedent_region_event)
        text.bind(b'<<comment-region>>', self.comment_region_event)
        text.bind(b'<<uncomment-region>>', self.uncomment_region_event)
        text.bind(b'<<tabify-region>>', self.tabify_region_event)
        text.bind(b'<<untabify-region>>', self.untabify_region_event)
        text.bind(b'<<toggle-tabs>>', self.toggle_tabs_event)
        text.bind(b'<<change-indentwidth>>', self.change_indentwidth_event)
        text.bind(b'<Left>', self.move_at_edge_if_selection(0))
        text.bind(b'<Right>', self.move_at_edge_if_selection(1))
        text.bind(b'<<del-word-left>>', self.del_word_left)
        text.bind(b'<<del-word-right>>', self.del_word_right)
        text.bind(b'<<beginning-of-line>>', self.home_callback)
        if flist:
            flist.inversedict[self] = key
            if key:
                flist.dict[key] = self
            text.bind(b'<<open-new-window>>', self.new_callback)
            text.bind(b'<<close-all-windows>>', self.flist.close_all_callback)
            text.bind(b'<<open-class-browser>>', self.open_class_browser)
            text.bind(b'<<open-path-browser>>', self.open_path_browser)
        self.set_status_bar()
        vbar[b'command'] = text.yview
        vbar.pack(side=RIGHT, fill=Y)
        text[b'yscrollcommand'] = vbar.set
        text[b'font'] = idleConf.GetFont(self.root, b'main', b'EditorWindow')
        text_frame.pack(side=LEFT, fill=BOTH, expand=1)
        text.pack(side=TOP, fill=BOTH, expand=1)
        text.focus_set()
        usespaces = idleConf.GetOption(b'main', b'Indent', b'use-spaces', type=b'bool')
        self.usetabs = not usespaces
        self.tabwidth = 8
        self.indentwidth = self.tabwidth
        self.set_notabs_indentwidth()
        self.context_use_ps1 = False
        self.num_context_lines = (50, 500, 5000000)
        self.per = per = self.Percolator(text)
        self.undo = undo = self.UndoDelegator()
        per.insertfilter(undo)
        text.undo_block_start = undo.undo_block_start
        text.undo_block_stop = undo.undo_block_stop
        undo.set_saved_change_hook(self.saved_change_hook)
        self.io = io = self.IOBinding(self)
        io.set_filename_change_hook(self.filename_change_hook)
        self.recent_files_menu = Menu(self.menubar, tearoff=0)
        self.menudict[b'file'].insert_cascade(3, label=b'Recent Files', underline=0, menu=self.recent_files_menu)
        self.update_recent_files_list()
        self.color = None
        if filename:
            if os.path.exists(filename) and not os.path.isdir(filename):
                io.loadfile(filename)
            else:
                io.set_filename(filename)
        self.ResetColorizer()
        self.saved_change_hook()
        self.set_indentation_params(self.ispythonsource(filename))
        self.load_extensions()
        menu = self.menudict.get(b'windows')
        if menu:
            end = menu.index(b'end')
            if end is None:
                end = -1
            if end >= 0:
                menu.add_separator()
                end = end + 1
            self.wmenu_end = end
            WindowList.register_callback(self.postwindowsmenu)
        self.askyesno = tkMessageBox.askyesno
        self.askinteger = tkSimpleDialog.askinteger
        self.showerror = tkMessageBox.showerror
        return

    def _filename_to_unicode(self, filename):
        if isinstance(filename, unicode) or not filename:
            return filename
        try:
            return filename.decode(self.filesystemencoding)
        except UnicodeDecodeError:
            try:
                return filename.decode(self.encoding)
            except UnicodeDecodeError:
                return filename.decode(b'iso8859-1')

        return

    def new_callback(self, event):
        dirname, basename = self.io.defaultfilename()
        self.flist.new(dirname)
        return b'break'

    def home_callback(self, event):
        if event.state & 4 != 0 and event.keysym == b'Home':
            return
        if self.text.index(b'iomark') and self.text.compare(b'iomark', b'<=', b'insert lineend') and self.text.compare(b'insert linestart', b'<=', b'iomark'):
            insertpt = int(self.text.index(b'iomark').split(b'.')[1])
        else:
            line = self.text.get(b'insert linestart', b'insert lineend')
            for insertpt in xrange(len(line)):
                if line[insertpt] not in (b' ', b'\t'):
                    break
            else:
                insertpt = len(line)

        lineat = int(self.text.index(b'insert').split(b'.')[1])
        if insertpt == lineat:
            insertpt = 0
        dest = b'insert linestart+' + str(insertpt) + b'c'
        if event.state & 1 == 0:
            self.text.tag_remove(b'sel', b'1.0', b'end')
        else:
            if not self.text.index(b'sel.first'):
                self.text.mark_set(b'my_anchor', b'insert')
            elif self.text.compare(self.text.index(b'sel.first'), b'<', self.text.index(b'insert')):
                self.text.mark_set(b'my_anchor', b'sel.first')
            else:
                self.text.mark_set(b'my_anchor', b'sel.last')
            first = self.text.index(dest)
            last = self.text.index(b'my_anchor')
            if self.text.compare(first, b'>', last):
                first, last = last, first
            self.text.tag_remove(b'sel', b'1.0', b'end')
            self.text.tag_add(b'sel', first, last)
        self.text.mark_set(b'insert', dest)
        self.text.see(b'insert')
        return b'break'

    def set_status_bar(self):
        self.status_bar = self.MultiStatusBar(self.top)
        sep = Frame(self.top, height=1, borderwidth=1, background=b'grey75')
        if sys.platform == b'darwin':
            self.status_bar.set_label(b'_padding1', b'    ', side=RIGHT)
        self.status_bar.set_label(b'column', b'Col: ?', side=RIGHT)
        self.status_bar.set_label(b'line', b'Ln: ?', side=RIGHT)
        self.status_bar.pack(side=BOTTOM, fill=X)
        sep.pack(side=BOTTOM, fill=X)
        self.text.bind(b'<<set-line-and-column>>', self.set_line_and_column)
        self.text.event_add(b'<<set-line-and-column>>', b'<KeyRelease>', b'<ButtonRelease>')
        self.text.after_idle(self.set_line_and_column)
        return

    def set_line_and_column(self, event=None):
        line, column = self.text.index(INSERT).split(b'.')
        self.status_bar.set_label(b'column', b'Col: %s' % column)
        self.status_bar.set_label(b'line', b'Ln: %s' % line)
        return

    menu_specs = [
     124, 
     125, 
     126, 
     127, 
     128, 
     129, 
     130]

    def createmenubar(self):
        mbar = self.menubar
        self.menudict = menudict = {}
        for name, label in self.menu_specs:
            underline, label = prepstr(label)
            menudict[name] = menu = Menu(mbar, name=name, tearoff=0)
            mbar.add_cascade(label=label, menu=menu, underline=underline)

        if macosxSupport.isCarbonTk():
            menudict[b'application'] = menu = Menu(mbar, name=b'apple', tearoff=0)
            mbar.add_cascade(label=b'IDLE', menu=menu)
        self.fill_menus()
        self.base_helpmenu_length = self.menudict[b'help'].index(END)
        self.reset_help_menu_entries()
        return

    def postwindowsmenu(self):
        menu = self.menudict[b'windows']
        end = menu.index(b'end')
        if end is None:
            end = -1
        if end > self.wmenu_end:
            menu.delete(self.wmenu_end + 1, end)
        WindowList.add_windows_to_menu(menu)
        return

    rmenu = None

    def right_menu_event(self, event):
        self.text.mark_set(b'insert', b'@%d,%d' % (event.x, event.y))
        if not self.rmenu:
            self.make_rmenu()
        rmenu = self.rmenu
        self.event = event
        iswin = sys.platform[:3] == b'win'
        if iswin:
            self.text.config(cursor=b'arrow')
        for item in self.rmenu_specs:
            try:
                label, eventname, verify_state = item
            except ValueError:
                continue

            if verify_state is None:
                continue
            state = getattr(self, verify_state)()
            rmenu.entryconfigure(label, state=state)

        rmenu.tk_popup(event.x_root, event.y_root)
        if iswin:
            self.text.config(cursor=b'ibeam')
        return

    rmenu_specs = [
     (b'Close', b'<<close-window>>', None)]

    def make_rmenu(self):
        rmenu = Menu(self.text, tearoff=0)
        for item in self.rmenu_specs:
            label, eventname = item[0], item[1]
            if label is not None:

                def command(text=self.text, eventname=eventname):
                    text.event_generate(eventname)
                    return

                rmenu.add_command(label=label, command=command)
            else:
                rmenu.add_separator()

        self.rmenu = rmenu
        return

    def rmenu_check_cut(self):
        return self.rmenu_check_copy()

    def rmenu_check_copy(self):
        try:
            indx = self.text.index(b'sel.first')
        except TclError:
            return b'disabled'

        if indx:
            return b'normal'
        else:
            return b'disabled'

        return

    def rmenu_check_paste(self):
        try:
            self.text.tk.call(b'tk::GetSelection', self.text, b'CLIPBOARD')
        except TclError:
            return b'disabled'

        return b'normal'
        return

    def about_dialog(self, event=None):
        aboutDialog.AboutDialog(self.top, b'About IDLE')
        return

    def config_dialog(self, event=None):
        configDialog.ConfigDialog(self.top, b'Settings')
        return

    def help_dialog(self, event=None):
        if self.root:
            parent = self.root
        else:
            parent = self.top
        help.show_idlehelp(parent)
        return

    def python_docs(self, event=None):
        if sys.platform[:3] == b'win':
            try:
                os.startfile(self.help_url)
            except WindowsError as why:
                tkMessageBox.showerror(title=b'Document Start Failure', message=str(why), parent=self.text)

        else:
            webbrowser.open(self.help_url)
        return b'break'

    def cut(self, event):
        self.text.event_generate(b'<<Cut>>')
        return b'break'

    def copy(self, event):
        if not self.text.tag_ranges(b'sel'):
            return
        self.text.event_generate(b'<<Copy>>')
        return b'break'

    def paste(self, event):
        self.text.event_generate(b'<<Paste>>')
        self.text.see(b'insert')
        return b'break'

    def select_all(self, event=None):
        self.text.tag_add(b'sel', b'1.0', b'end-1c')
        self.text.mark_set(b'insert', b'1.0')
        self.text.see(b'insert')
        return b'break'

    def remove_selection(self, event=None):
        self.text.tag_remove(b'sel', b'1.0', b'end')
        self.text.see(b'insert')
        return

    def move_at_edge_if_selection(self, edge_index):
        self_text_index = self.text.index
        self_text_mark_set = self.text.mark_set
        edges_table = (b'sel.first+1c', b'sel.last-1c')

        def move_at_edge(event):
            if event.state & 5 == 0:
                try:
                    self_text_index(b'sel.first')
                    self_text_mark_set(b'insert', edges_table[edge_index])
                except TclError:
                    pass

            return

        return move_at_edge

    def del_word_left(self, event):
        self.text.event_generate(b'<Meta-Delete>')
        return b'break'

    def del_word_right(self, event):
        self.text.event_generate(b'<Meta-d>')
        return b'break'

    def find_event(self, event):
        SearchDialog.find(self.text)
        return b'break'

    def find_again_event(self, event):
        SearchDialog.find_again(self.text)
        return b'break'

    def find_selection_event(self, event):
        SearchDialog.find_selection(self.text)
        return b'break'

    def find_in_files_event(self, event):
        GrepDialog.grep(self.text, self.io, self.flist)
        return b'break'

    def replace_event(self, event):
        ReplaceDialog.replace(self.text)
        return b'break'

    def goto_line_event(self, event):
        text = self.text
        lineno = tkSimpleDialog.askinteger(b'Goto', b'Go to line number:', parent=text)
        if lineno is None:
            return b'break'
        else:
            if lineno <= 0:
                text.bell()
                return b'break'
            text.mark_set(b'insert', b'%d.0' % lineno)
            text.see(b'insert')
            return

    def open_module(self, event=None):
        try:
            name = self.text.get(b'sel.first', b'sel.last')
        except TclError:
            name = b''
        else:
            name = name.strip()

        name = tkSimpleDialog.askstring(b'Module', b'Enter the name of a Python module\nto search on sys.path and open:', parent=self.text, initialvalue=name)
        if name:
            name = name.strip()
        if not name:
            return
        try:
            f, file_path, (suffix, mode, mtype) = _find_module(name)
        except (NameError, ImportError) as msg:
            tkMessageBox.showerror(b'Import error', str(msg), parent=self.text)
            return

        if mtype != imp.PY_SOURCE:
            tkMessageBox.showerror(b'Unsupported type', b'%s is not a source module' % name, parent=self.text)
            return
        if f:
            f.close()
        if self.flist:
            self.flist.open(file_path)
        else:
            self.io.loadfile(file_path)
        return file_path

    def open_class_browser(self, event=None):
        filename = self.io.filename
        if not (self.__class__.__name__ == b'PyShellEditorWindow' and filename):
            filename = self.open_module()
            if filename is None:
                return
        head, tail = os.path.split(filename)
        base, ext = os.path.splitext(tail)
        from idlelib import ClassBrowser
        ClassBrowser.ClassBrowser(self.flist, base, [head])
        return

    def open_path_browser(self, event=None):
        from idlelib import PathBrowser
        PathBrowser.PathBrowser(self.flist)
        return

    def gotoline(self, lineno):
        if lineno is not None and lineno > 0:
            self.text.mark_set(b'insert', b'%d.0' % lineno)
            self.text.tag_remove(b'sel', b'1.0', b'end')
            self.text.tag_add(b'sel', b'insert', b'insert +1l')
            self.center()
        return

    def ispythonsource(self, filename):
        if not filename or os.path.isdir(filename):
            return True
        base, ext = os.path.splitext(os.path.basename(filename))
        if os.path.normcase(ext) in (b'.py', b'.pyw'):
            return True
        try:
            f = open(filename)
            line = f.readline()
            f.close()
        except IOError:
            return False

        return line.startswith(b'#!') and line.find(b'python') >= 0

    def close_hook(self):
        if self.flist:
            self.flist.unregister_maybe_terminate(self)
            self.flist = None
        return

    def set_close_hook(self, close_hook):
        self.close_hook = close_hook
        return

    def filename_change_hook(self):
        if self.flist:
            self.flist.filename_changed_edit(self)
        self.saved_change_hook()
        self.top.update_windowlist_registry(self)
        self.ResetColorizer()
        return

    def _addcolorizer(self):
        if self.color:
            return
        if self.ispythonsource(self.io.filename):
            self.color = self.ColorDelegator()
        if self.color:
            self.per.removefilter(self.undo)
            self.per.insertfilter(self.color)
            self.per.insertfilter(self.undo)
        return

    def _rmcolorizer(self):
        if not self.color:
            return
        else:
            self.color.removecolors()
            self.per.removefilter(self.color)
            self.color = None
            return

    def ResetColorizer(self):
        self._rmcolorizer()
        self._addcolorizer()
        theme = idleConf.CurrentTheme()
        normal_colors = idleConf.GetHighlight(theme, b'normal')
        cursor_color = idleConf.GetHighlight(theme, b'cursor', fgBg=b'fg')
        select_colors = idleConf.GetHighlight(theme, b'hilite')
        self.text.config(foreground=normal_colors[b'foreground'], background=normal_colors[b'background'], insertbackground=cursor_color, selectforeground=select_colors[b'foreground'], selectbackground=select_colors[b'background'])
        if TkVersion >= 8.5:
            self.text.config(inactiveselectbackground=select_colors[b'background'])
        return

    def ResetFont(self):
        self.text[b'font'] = idleConf.GetFont(self.root, b'main', b'EditorWindow')
        return

    def RemoveKeybindings(self):
        self.Bindings.default_keydefs = keydefs = idleConf.GetCurrentKeySet()
        for event, keylist in keydefs.items():
            self.text.event_delete(event, *keylist)

        for extensionName in self.get_standard_extension_names():
            xkeydefs = idleConf.GetExtensionBindings(extensionName)
            if xkeydefs:
                for event, keylist in xkeydefs.items():
                    self.text.event_delete(event, *keylist)

        return

    def ApplyKeybindings(self):
        self.Bindings.default_keydefs = keydefs = idleConf.GetCurrentKeySet()
        self.apply_bindings()
        for extensionName in self.get_standard_extension_names():
            xkeydefs = idleConf.GetExtensionBindings(extensionName)
            if xkeydefs:
                self.apply_bindings(xkeydefs)

        menuEventDict = {}
        for menu in self.Bindings.menudefs:
            menuEventDict[menu[0]] = {}
            for item in menu[1]:
                if item:
                    menuEventDict[menu[0]][prepstr(item[0])[1]] = item[1]

        for menubarItem in self.menudict.keys():
            menu = self.menudict[menubarItem]
            end = menu.index(END)
            if end is None:
                continue
            end += 1
            for index in range(0, end):
                if menu.type(index) == b'command':
                    accel = menu.entrycget(index, b'accelerator')
                    if accel:
                        itemName = menu.entrycget(index, b'label')
                        event = b''
                        if menubarItem in menuEventDict:
                            if itemName in menuEventDict[menubarItem]:
                                event = menuEventDict[menubarItem][itemName]
                        if event:
                            accel = get_accelerator(keydefs, event)
                            menu.entryconfig(index, accelerator=accel)

        return

    def set_notabs_indentwidth(self):
        if not self.usetabs:
            self.indentwidth = idleConf.GetOption(b'main', b'Indent', b'num-spaces', type=b'int')
        return

    def reset_help_menu_entries(self):
        help_list = idleConf.GetAllExtraHelpSourcesList()
        helpmenu = self.menudict[b'help']
        helpmenu_length = helpmenu.index(END)
        if helpmenu_length > self.base_helpmenu_length:
            helpmenu.delete(self.base_helpmenu_length + 1, helpmenu_length)
        if help_list:
            helpmenu.add_separator()
            for entry in help_list:
                cmd = self.__extra_help_callback(entry[1])
                helpmenu.add_command(label=entry[0], command=cmd)

        self.menudict[b'help'] = helpmenu
        return

    def __extra_help_callback(self, helpfile):

        def display_extra_help(helpfile=helpfile):
            if not helpfile.startswith((b'www', b'http')):
                helpfile = os.path.normpath(helpfile)
            if sys.platform[:3] == b'win':
                try:
                    os.startfile(helpfile)
                except WindowsError as why:
                    tkMessageBox.showerror(title=b'Document Start Failure', message=str(why), parent=self.text)

            else:
                webbrowser.open(helpfile)
            return

        return display_extra_help

    def update_recent_files_list(self, new_file=None):
        rf_list = []
        if os.path.exists(self.recent_files_path):
            with open(self.recent_files_path, b'r') as rf_list_file:
                rf_list = rf_list_file.readlines()
        if new_file:
            new_file = os.path.abspath(new_file) + b'\n'
            if new_file in rf_list:
                rf_list.remove(new_file)
            rf_list.insert(0, new_file)
        bad_paths = []
        for path in rf_list:
            if b'\x00' in path or not os.path.exists(path[0:-1]):
                bad_paths.append(path)

        rf_list = [path for path in rf_list if path not in bad_paths]
        ulchars = b'1234567890ABCDEFGHIJK'
        rf_list = rf_list[0:len(ulchars)]
        try:
            with open(self.recent_files_path, b'w') as rf_file:
                rf_file.writelines(rf_list)
        except IOError as err:
            if not getattr(self.root, b'recentfilelist_error_displayed', False):
                self.root.recentfilelist_error_displayed = True
                tkMessageBox.showwarning(title=b'IDLE Warning', message=b'Cannot update File menu Recent Files list. Your operating system says:\n%s\nSelect OK and IDLE will continue without updating.' % str(err), parent=self.text)

        for instance in self.top.instance_dict.keys():
            menu = instance.recent_files_menu
            menu.delete(0, END)
            for i, file_name in enumerate(rf_list):
                file_name = file_name.rstrip()
                ufile_name = self._filename_to_unicode(file_name)
                callback = instance.__recent_file_callback(file_name)
                menu.add_command(label=ulchars[i] + b' ' + ufile_name, command=callback, underline=0)

        return

    def __recent_file_callback(self, file_name):

        def open_recent_file(fn_closure=file_name):
            self.io.open(editFile=fn_closure)
            return

        return open_recent_file

    def saved_change_hook(self):
        short = self.short_title()
        long = self.long_title()
        if short and long:
            title = short + b' - ' + long + _py_version
        elif short:
            title = short
        elif long:
            title = long
        else:
            title = b'Untitled'
        icon = short or long or title
        if not self.get_saved():
            title = b'*%s*' % title
            icon = b'*%s' % icon
        self.top.wm_title(title)
        self.top.wm_iconname(icon)
        return

    def get_saved(self):
        return self.undo.get_saved()

    def set_saved(self, flag):
        self.undo.set_saved(flag)
        return

    def reset_undo(self):
        self.undo.reset_undo()
        return

    def short_title(self):
        filename = self.io.filename
        if filename:
            filename = os.path.basename(filename)
        else:
            filename = b'Untitled'
        return self._filename_to_unicode(filename)

    def long_title(self):
        return self._filename_to_unicode(self.io.filename or b'')

    def center_insert_event(self, event):
        self.center()
        return

    def center(self, mark=b'insert'):
        text = self.text
        top, bot = self.getwindowlines()
        lineno = self.getlineno(mark)
        height = bot - top
        newtop = max(1, lineno - height // 2)
        text.yview(float(newtop))
        return

    def getwindowlines(self):
        text = self.text
        top = self.getlineno(b'@0,0')
        bot = self.getlineno(b'@0,65535')
        if top == bot and text.winfo_height() == 1:
            height = int(text[b'height'])
            bot = top + height - 1
        return (
         top, bot)

    def getlineno(self, mark=b'insert'):
        text = self.text
        return int(float(text.index(mark)))

    def get_geometry(self):
        geom = self.top.wm_geometry()
        m = re.match(b'(\\d+)x(\\d+)\\+(-?\\d+)\\+(-?\\d+)', geom)
        tuple = map(int, m.groups())
        return tuple

    def close_event(self, event):
        self.close()
        return

    def maybesave(self):
        if self.io:
            if not self.get_saved():
                if self.top.state() != b'normal':
                    self.top.deiconify()
                self.top.lower()
                self.top.lift()
            return self.io.maybesave()
        return

    def close(self):
        reply = self.maybesave()
        if str(reply) != b'cancel':
            self._close()
        return reply

    def _close(self):
        if self.io.filename:
            self.update_recent_files_list(new_file=self.io.filename)
        WindowList.unregister_callback(self.postwindowsmenu)
        self.unload_extensions()
        self.io.close()
        self.io = None
        self.undo = None
        if self.color:
            self.color.close(False)
            self.color = None
        self.text = None
        self.tkinter_vars = None
        self.per.close()
        self.per = None
        self.top.destroy()
        if self.close_hook:
            self.close_hook()
        return

    def load_extensions(self):
        self.extensions = {}
        self.load_standard_extensions()
        return

    def unload_extensions(self):
        for ins in self.extensions.values():
            if hasattr(ins, b'close'):
                ins.close()

        self.extensions = {}
        return

    def load_standard_extensions(self):
        for name in self.get_standard_extension_names():
            try:
                self.load_extension(name)
            except:
                print b'Failed to load extension', repr(name)
                import traceback
                traceback.print_exc()

        return

    def get_standard_extension_names(self):
        return idleConf.GetExtensions(editor_only=True)

    def load_extension(self, name):
        try:
            mod = __import__(name, globals(), locals(), [])
        except ImportError:
            print b'\nFailed to import extension: ', name
            return

        cls = getattr(mod, name)
        keydefs = idleConf.GetExtensionBindings(name)
        if hasattr(cls, b'menudefs'):
            self.fill_menus(cls.menudefs, keydefs)
        ins = cls(self)
        self.extensions[name] = ins
        if keydefs:
            self.apply_bindings(keydefs)
            for vevent in keydefs.keys():
                methodname = vevent.replace(b'-', b'_')
                while methodname[:1] == b'<':
                    methodname = methodname[1:]

                while methodname[-1:] == b'>':
                    methodname = methodname[:-1]

                methodname = methodname + b'_event'
                if hasattr(ins, methodname):
                    self.text.bind(vevent, getattr(ins, methodname))

        return

    def apply_bindings(self, keydefs=None):
        if keydefs is None:
            keydefs = self.Bindings.default_keydefs
        text = self.text
        text.keydefs = keydefs
        for event, keylist in keydefs.items():
            if keylist:
                text.event_add(event, *keylist)

        return

    def fill_menus(self, menudefs=None, keydefs=None):
        if menudefs is None:
            menudefs = self.Bindings.menudefs
        if keydefs is None:
            keydefs = self.Bindings.default_keydefs
        menudict = self.menudict
        text = self.text
        for mname, entrylist in menudefs:
            menu = menudict.get(mname)
            if not menu:
                continue
            for entry in entrylist:
                if not entry:
                    menu.add_separator()
                else:
                    label, eventname = entry
                    checkbutton = label[:1] == b'!'
                    if checkbutton:
                        label = label[1:]
                    underline, label = prepstr(label)
                    accelerator = get_accelerator(keydefs, eventname)

                    def command(text=text, eventname=eventname):
                        text.event_generate(eventname)
                        return

                    if checkbutton:
                        var = self.get_var_obj(eventname, BooleanVar)
                        menu.add_checkbutton(label=label, underline=underline, command=command, accelerator=accelerator, variable=var)
                    else:
                        menu.add_command(label=label, underline=underline, command=command, accelerator=accelerator)

        return

    def getvar(self, name):
        var = self.get_var_obj(name)
        if var:
            value = var.get()
            return value
        raise NameError, name
        return

    def setvar(self, name, value, vartype=None):
        var = self.get_var_obj(name, vartype)
        if var:
            var.set(value)
        else:
            raise NameError, name
        return

    def get_var_obj(self, name, vartype=None):
        var = self.tkinter_vars.get(name)
        if not var and vartype:
            self.tkinter_vars[name] = var = vartype(self.text)
        return var

    def is_char_in_string(self, text_index):
        if self.color:
            return self.text.tag_prevrange(b'TODO', text_index) or b'STRING' in self.text.tag_names(text_index)
        else:
            return 1

        return

    def get_selection_indices(self):
        try:
            first = self.text.index(b'sel.first')
            last = self.text.index(b'sel.last')
            return (first, last)
        except TclError:
            return (None, None)

        return

    def get_tabwidth(self):
        current = self.text[b'tabs'] or TK_TABWIDTH_DEFAULT
        return int(current)

    def set_tabwidth(self, newtabwidth):
        text = self.text
        if self.get_tabwidth() != newtabwidth:
            pixels = text.tk.call(b'font', b'measure', text[b'font'], b'-displayof', text.master, b'n' * newtabwidth)
            text.configure(tabs=pixels)
        return

    def set_indentation_params(self, ispythonsource, guess=True):
        if guess and ispythonsource:
            i = self.guess_indent()
            if 2 <= i <= 8:
                self.indentwidth = i
            if self.indentwidth != self.tabwidth:
                self.usetabs = False
        self.set_tabwidth(self.tabwidth)
        return

    def smart_backspace_event(self, event):
        text = self.text
        first, last = self.get_selection_indices()
        if first and last:
            text.delete(first, last)
            text.mark_set(b'insert', first)
            return b'break'
        chars = text.get(b'insert linestart', b'insert')
        if chars == b'':
            if text.compare(b'insert', b'>', b'1.0'):
                text.delete(b'insert-1c')
            else:
                text.bell()
            return b'break'
        if chars[-1] not in b' \t':
            text.delete(b'insert-1c')
            return b'break'
        tabwidth = self.tabwidth
        have = len(chars.expandtabs(tabwidth))
        want = (have - 1) // self.indentwidth * self.indentwidth
        if self.context_use_ps1:
            last_line_of_prompt = sys.ps1.split(b'\n')[-1]
        else:
            last_line_of_prompt = b''
        ncharsdeleted = 0
        while 1:
            if chars == last_line_of_prompt:
                break
            chars = chars[:-1]
            ncharsdeleted = ncharsdeleted + 1
            have = len(chars.expandtabs(tabwidth))
            if have <= want or chars[-1] not in b' \t':
                break

        text.undo_block_start()
        text.delete(b'insert-%dc' % ncharsdeleted, b'insert')
        if have < want:
            text.insert(b'insert', b' ' * (want - have))
        text.undo_block_stop()
        return b'break'

    def smart_indent_event(self, event):
        text = self.text
        first, last = self.get_selection_indices()
        text.undo_block_start()
        try:
            if first and last:
                if index2line(first) != index2line(last):
                    return self.indent_region_event(event)
                text.delete(first, last)
                text.mark_set(b'insert', first)
            prefix = text.get(b'insert linestart', b'insert')
            raw, effective = classifyws(prefix, self.tabwidth)
            if raw == len(prefix):
                self.reindent_to(effective + self.indentwidth)
            else:
                if self.usetabs:
                    pad = b'\t'
                else:
                    effective = len(prefix.expandtabs(self.tabwidth))
                    n = self.indentwidth
                    pad = b' ' * (n - effective % n)
                text.insert(b'insert', pad)
            text.see(b'insert')
            return b'break'
        finally:
            text.undo_block_stop()

        return

    def newline_and_indent_event(self, event):
        text = self.text
        first, last = self.get_selection_indices()
        text.undo_block_start()
        try:
            if first and last:
                text.delete(first, last)
                text.mark_set(b'insert', first)
            line = text.get(b'insert linestart', b'insert')
            i, n = 0, len(line)
            while i < n and line[i] in b' \t':
                i = i + 1

            if i == n:
                text.insert(b'insert linestart', b'\n')
                return b'break'
            indent = line[:i]
            i = 0
            last_line_of_prompt = sys.ps1.split(b'\n')[-1]
            while line and line[-1] in b' \t' and line != last_line_of_prompt:
                line = line[:-1]
                i = i + 1

            if i:
                text.delete(b'insert - %d chars' % i, b'insert')
            while text.get(b'insert') in b' \t':
                text.delete(b'insert')

            text.insert(b'insert', b'\n')
            lno = index2line(text.index(b'insert'))
            y = PyParse.Parser(self.indentwidth, self.tabwidth)
            if not self.context_use_ps1:
                for context in self.num_context_lines:
                    startat = max(lno - context, 1)
                    startatindex = repr(startat) + b'.0'
                    rawtext = text.get(startatindex, b'insert')
                    y.set_str(rawtext)
                    bod = y.find_good_parse_start(self.context_use_ps1, self._build_char_in_string_func(startatindex))
                    if bod is not None or startat == 1:
                        break

                y.set_lo(bod or 0)
            else:
                r = text.tag_prevrange(b'console', b'insert')
                if r:
                    startatindex = r[1]
                else:
                    startatindex = b'1.0'
                rawtext = text.get(startatindex, b'insert')
                y.set_str(rawtext)
                y.set_lo(0)
            c = y.get_continuation_type()
            if c != PyParse.C_NONE:
                if c == PyParse.C_STRING_FIRST_LINE:
                    pass
                elif c == PyParse.C_STRING_NEXT_LINES:
                    text.insert(b'insert', indent)
                elif c == PyParse.C_BRACKET:
                    self.reindent_to(y.compute_bracket_indent())
                elif c == PyParse.C_BACKSLASH:
                    if y.get_num_lines_in_stmt() > 1:
                        text.insert(b'insert', indent)
                    else:
                        self.reindent_to(y.compute_backslash_indent())
                return b'break'
            indent = y.get_base_indent_string()
            text.insert(b'insert', indent)
            if y.is_block_opener():
                self.smart_indent_event(event)
            elif indent and y.is_block_closer():
                self.smart_backspace_event(event)
            return b'break'
        finally:
            text.see(b'insert')
            text.undo_block_stop()

        return

    def _build_char_in_string_func(self, startindex):

        def inner(offset, _startindex=startindex, _icis=self.is_char_in_string):
            return _icis(_startindex + b'+%dc' % offset)

        return inner

    def indent_region_event(self, event):
        head, tail, chars, lines = self.get_region()
        for pos in range(len(lines)):
            line = lines[pos]
            if line:
                raw, effective = classifyws(line, self.tabwidth)
                effective = effective + self.indentwidth
                lines[pos] = self._make_blanks(effective) + line[raw:]

        self.set_region(head, tail, chars, lines)
        return b'break'

    def dedent_region_event(self, event):
        head, tail, chars, lines = self.get_region()
        for pos in range(len(lines)):
            line = lines[pos]
            if line:
                raw, effective = classifyws(line, self.tabwidth)
                effective = max(effective - self.indentwidth, 0)
                lines[pos] = self._make_blanks(effective) + line[raw:]

        self.set_region(head, tail, chars, lines)
        return b'break'

    def comment_region_event(self, event):
        head, tail, chars, lines = self.get_region()
        for pos in range(len(lines) - 1):
            line = lines[pos]
            lines[pos] = b'##' + line

        self.set_region(head, tail, chars, lines)
        return

    def uncomment_region_event(self, event):
        head, tail, chars, lines = self.get_region()
        for pos in range(len(lines)):
            line = lines[pos]
            if not line:
                continue
            if line[:2] == b'##':
                line = line[2:]
            elif line[:1] == b'#':
                line = line[1:]
            lines[pos] = line

        self.set_region(head, tail, chars, lines)
        return

    def tabify_region_event(self, event):
        head, tail, chars, lines = self.get_region()
        tabwidth = self._asktabwidth()
        if tabwidth is None:
            return
        else:
            for pos in range(len(lines)):
                line = lines[pos]
                if line:
                    raw, effective = classifyws(line, tabwidth)
                    ntabs, nspaces = divmod(effective, tabwidth)
                    lines[pos] = b'\t' * ntabs + b' ' * nspaces + line[raw:]

            self.set_region(head, tail, chars, lines)
            return

    def untabify_region_event(self, event):
        head, tail, chars, lines = self.get_region()
        tabwidth = self._asktabwidth()
        if tabwidth is None:
            return
        else:
            for pos in range(len(lines)):
                lines[pos] = lines[pos].expandtabs(tabwidth)

            self.set_region(head, tail, chars, lines)
            return

    def toggle_tabs_event(self, event):
        if self.askyesno(b'Toggle tabs', b'Turn tabs ' + (b'on', b'off')[self.usetabs] + b'?\nIndent width ' + (b'will be', b'remains at')[self.usetabs] + b' 8.' + b'\n Note: a tab is always 8 columns', parent=self.text):
            self.usetabs = not self.usetabs
            self.indentwidth = 8
        return b'break'

    def change_indentwidth_event(self, event):
        new = self.askinteger(b'Indent width', b'New indent width (2-16)\n(Always use 8 when using tabs)', parent=self.text, initialvalue=self.indentwidth, minvalue=2, maxvalue=16)
        if new and new != self.indentwidth and not self.usetabs:
            self.indentwidth = new
        return b'break'

    def get_region(self):
        text = self.text
        first, last = self.get_selection_indices()
        if first and last:
            head = text.index(first + b' linestart')
            tail = text.index(last + b'-1c lineend +1c')
        else:
            head = text.index(b'insert linestart')
            tail = text.index(b'insert lineend +1c')
        chars = text.get(head, tail)
        lines = chars.split(b'\n')
        return (head, tail, chars, lines)

    def set_region(self, head, tail, chars, lines):
        text = self.text
        newchars = (b'\n').join(lines)
        if newchars == chars:
            text.bell()
            return
        text.tag_remove(b'sel', b'1.0', b'end')
        text.mark_set(b'insert', head)
        text.undo_block_start()
        text.delete(head, tail)
        text.insert(head, newchars)
        text.undo_block_stop()
        text.tag_add(b'sel', head, b'insert')
        return

    def _make_blanks(self, n):
        if self.usetabs:
            ntabs, nspaces = divmod(n, self.tabwidth)
            return b'\t' * ntabs + b' ' * nspaces
        else:
            return b' ' * n

        return

    def reindent_to(self, column):
        text = self.text
        text.undo_block_start()
        if text.compare(b'insert linestart', b'!=', b'insert'):
            text.delete(b'insert linestart', b'insert')
        if column:
            text.insert(b'insert', self._make_blanks(column))
        text.undo_block_stop()
        return

    def _asktabwidth(self):
        return self.askinteger(b'Tab width', b'Columns per tab? (2-16)', parent=self.text, initialvalue=self.indentwidth, minvalue=2, maxvalue=16)

    def guess_indent(self):
        opener, indented = IndentSearcher(self.text, self.tabwidth).run()
        if opener and indented:
            raw, indentsmall = classifyws(opener, self.tabwidth)
            raw, indentlarge = classifyws(indented, self.tabwidth)
        else:
            indentsmall = indentlarge = 0
        return indentlarge - indentsmall


def index2line(index):
    return int(float(index))


def classifyws(s, tabwidth):
    raw = effective = 0
    for ch in s:
        if ch == b' ':
            raw = raw + 1
            effective = effective + 1
        elif ch == b'\t':
            raw = raw + 1
            effective = (effective // tabwidth + 1) * tabwidth
        else:
            break

    return (
     raw, effective)


import tokenize
_tokenize = tokenize
del tokenize

class IndentSearcher(object):

    def __init__(self, text, tabwidth):
        self.text = text
        self.tabwidth = tabwidth
        self.i = self.finished = 0
        self.blkopenline = self.indentedline = None
        return

    def readline(self):
        if self.finished:
            return b''
        i = self.i = self.i + 1
        mark = repr(i) + b'.0'
        if self.text.compare(mark, b'>=', b'end'):
            return b''
        return self.text.get(mark, mark + b' lineend+1c')

    def tokeneater(self, type, token, start, end, line, INDENT=_tokenize.INDENT, NAME=_tokenize.NAME, OPENERS=(b'class', b'def', b'for', b'if', b'try', b'while')):
        if self.finished:
            pass
        elif type == NAME and token in OPENERS:
            self.blkopenline = line
        elif type == INDENT and self.blkopenline:
            self.indentedline = line
            self.finished = 1
        return

    def run(self):
        save_tabsize = _tokenize.tabsize
        _tokenize.tabsize = self.tabwidth
        try:
            try:
                _tokenize.tokenize(self.readline, self.tokeneater)
            except (_tokenize.TokenError, SyntaxError):
                pass

        finally:
            _tokenize.tabsize = save_tabsize

        return (
         self.blkopenline, self.indentedline)


def prepstr(s):
    i = s.find(b'_')
    if i >= 0:
        s = s[:i] + s[i + 1:]
    return (
     i, s)


keynames = {b'bracketleft': b'[', 
   b'bracketright': b']', 
   b'slash': b'/'}

def get_accelerator(keydefs, eventname):
    keylist = keydefs.get(eventname)
    if not keylist or macosxSupport.isCocoaTk() and eventname in {
     b'<<open-module>>',
     b'<<goto-line>>',
     b'<<change-indentwidth>>'}:
        return b''
    s = keylist[0]
    s = re.sub(b'-[a-z]\\b', (lambda m: m.group().upper()), s)
    s = re.sub(b'\\b\\w+\\b', (lambda m: keynames.get(m.group(), m.group())), s)
    s = re.sub(b'Key-', b'', s)
    s = re.sub(b'Cancel', b'Ctrl-Break', s)
    s = re.sub(b'Control-', b'Ctrl-', s)
    s = re.sub(b'-', b'+', s)
    s = re.sub(b'><', b' ', s)
    s = re.sub(b'<', b'', s)
    s = re.sub(b'>', b'', s)
    return s


def fixwordbreaks(root):
    tk = root.tk
    tk.call(b'tcl_wordBreakAfter', b'a b', 0)
    tk.call(b'set', b'tcl_wordchars', b'[a-zA-Z0-9_]')
    tk.call(b'set', b'tcl_nonwordchars', b'[^a-zA-Z0-9_]')
    return


def _editor_window(parent):
    root = parent
    fixwordbreaks(root)
    if sys.argv[1:]:
        filename = sys.argv[1]
    else:
        filename = None
    macosxSupport.setupApp(root, None)
    edit = EditorWindow(root=root, filename=filename)
    edit.text.bind(b'<<close-all-windows>>', edit.close_event)
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_editor_window)
