import os, bdb
from Tkinter import *
from idlelib.WindowList import ListedToplevel
from idlelib.ScrolledList import ScrolledList
from idlelib import macosxSupport

class Idb(bdb.Bdb):

    def __init__(self, gui):
        self.gui = gui
        bdb.Bdb.__init__(self)
        return

    def user_line(self, frame):
        if self.in_rpc_code(frame):
            self.set_step()
            return
        message = self.__frame2message(frame)
        try:
            self.gui.interaction(message, frame)
        except TclError:
            pass

        return

    def user_exception(self, frame, info):
        if self.in_rpc_code(frame):
            self.set_step()
            return
        message = self.__frame2message(frame)
        self.gui.interaction(message, frame, info)
        return

    def in_rpc_code(self, frame):
        if frame.f_code.co_filename.count(b'rpc.py'):
            return True
        else:
            prev_frame = frame.f_back
            if prev_frame.f_code.co_filename.count(b'Debugger.py'):
                return False
            return self.in_rpc_code(prev_frame)

        return

    def __frame2message(self, frame):
        code = frame.f_code
        filename = code.co_filename
        lineno = frame.f_lineno
        basename = os.path.basename(filename)
        message = b'%s:%s' % (basename, lineno)
        if code.co_name != b'?':
            message = b'%s: %s()' % (message, code.co_name)
        return message


class Debugger():
    vstack = vsource = vlocals = vglobals = None

    def __init__(self, pyshell, idb=None):
        if idb is None:
            idb = Idb(self)
        self.pyshell = pyshell
        self.idb = idb
        self.frame = None
        self.make_gui()
        self.interacting = 0
        self.nesting_level = 0
        return

    def run(self, *args):
        if self.nesting_level > 0:
            self.abort_loop()
            self.root.after(100, (lambda : self.run(*args)))
            return
        try:
            self.interacting = 1
            return self.idb.run(*args)
        finally:
            self.interacting = 0

        return

    def close(self, event=None):
        try:
            self.quit()
        except Exception:
            pass

        if self.interacting:
            self.top.bell()
            return
        else:
            if self.stackviewer:
                self.stackviewer.close()
                self.stackviewer = None
            self.pyshell.close_debugger()
            self.top.destroy()
            return

    def make_gui(self):
        pyshell = self.pyshell
        self.flist = pyshell.flist
        self.root = root = pyshell.root
        self.top = top = ListedToplevel(root)
        self.top.wm_title(b'Debug Control')
        self.top.wm_iconname(b'Debug')
        top.wm_protocol(b'WM_DELETE_WINDOW', self.close)
        self.top.bind(b'<Escape>', self.close)
        self.bframe = bframe = Frame(top)
        self.bframe.pack(anchor=b'w')
        self.buttons = bl = []
        self.bcont = b = Button(bframe, text=b'Go', command=self.cont)
        bl.append(b)
        self.bstep = b = Button(bframe, text=b'Step', command=self.step)
        bl.append(b)
        self.bnext = b = Button(bframe, text=b'Over', command=self.next)
        bl.append(b)
        self.bret = b = Button(bframe, text=b'Out', command=self.ret)
        bl.append(b)
        self.bret = b = Button(bframe, text=b'Quit', command=self.quit)
        bl.append(b)
        for b in bl:
            b.configure(state=b'disabled')
            b.pack(side=b'left')

        self.cframe = cframe = Frame(bframe)
        self.cframe.pack(side=b'left')
        if not self.vstack:
            self.__class__.vstack = BooleanVar(top)
            self.vstack.set(1)
        self.bstack = Checkbutton(cframe, text=b'Stack', command=self.show_stack, variable=self.vstack)
        self.bstack.grid(row=0, column=0)
        if not self.vsource:
            self.__class__.vsource = BooleanVar(top)
        self.bsource = Checkbutton(cframe, text=b'Source', command=self.show_source, variable=self.vsource)
        self.bsource.grid(row=0, column=1)
        if not self.vlocals:
            self.__class__.vlocals = BooleanVar(top)
            self.vlocals.set(1)
        self.blocals = Checkbutton(cframe, text=b'Locals', command=self.show_locals, variable=self.vlocals)
        self.blocals.grid(row=1, column=0)
        if not self.vglobals:
            self.__class__.vglobals = BooleanVar(top)
        self.bglobals = Checkbutton(cframe, text=b'Globals', command=self.show_globals, variable=self.vglobals)
        self.bglobals.grid(row=1, column=1)
        self.status = Label(top, anchor=b'w')
        self.status.pack(anchor=b'w')
        self.error = Label(top, anchor=b'w')
        self.error.pack(anchor=b'w', fill=b'x')
        self.errorbg = self.error.cget(b'background')
        self.fstack = Frame(top, height=1)
        self.fstack.pack(expand=1, fill=b'both')
        self.flocals = Frame(top)
        self.flocals.pack(expand=1, fill=b'both')
        self.fglobals = Frame(top, height=1)
        self.fglobals.pack(expand=1, fill=b'both')
        if self.vstack.get():
            self.show_stack()
        if self.vlocals.get():
            self.show_locals()
        if self.vglobals.get():
            self.show_globals()
        return

    def interaction(self, message, frame, info=None):
        self.frame = frame
        self.status.configure(text=message)
        if info:
            type, value, tb = info
            try:
                m1 = type.__name__
            except AttributeError:
                m1 = b'%s' % str(type)

            if value is not None:
                try:
                    m1 = b'%s: %s' % (m1, str(value))
                except:
                    pass

            bg = b'yellow'
        else:
            m1 = b''
            tb = None
            bg = self.errorbg
        self.error.configure(text=m1, background=bg)
        sv = self.stackviewer
        if sv:
            stack, i = self.idb.get_stack(self.frame, tb)
            sv.load_stack(stack, i)
        self.show_variables(1)
        if self.vsource.get():
            self.sync_source_line()
        for b in self.buttons:
            b.configure(state=b'normal')

        self.top.wakeup()
        self.nesting_level += 1
        self.root.tk.call(b'vwait', b'::idledebugwait')
        self.nesting_level -= 1
        for b in self.buttons:
            b.configure(state=b'disabled')

        self.status.configure(text=b'')
        self.error.configure(text=b'', background=self.errorbg)
        self.frame = None
        return

    def sync_source_line(self):
        frame = self.frame
        if not frame:
            return
        filename, lineno = self.__frame2fileline(frame)
        if filename[:1] + filename[-1:] != b'<>' and os.path.exists(filename):
            self.flist.gotofileline(filename, lineno)
        return

    def __frame2fileline(self, frame):
        code = frame.f_code
        filename = code.co_filename
        lineno = frame.f_lineno
        return (filename, lineno)

    def cont(self):
        self.idb.set_continue()
        self.abort_loop()
        return

    def step(self):
        self.idb.set_step()
        self.abort_loop()
        return

    def next(self):
        self.idb.set_next(self.frame)
        self.abort_loop()
        return

    def ret(self):
        self.idb.set_return(self.frame)
        self.abort_loop()
        return

    def quit(self):
        self.idb.set_quit()
        self.abort_loop()
        return

    def abort_loop(self):
        self.root.tk.call(b'set', b'::idledebugwait', b'1')
        return

    stackviewer = None

    def show_stack(self):
        if not self.stackviewer and self.vstack.get():
            self.stackviewer = sv = StackViewer(self.fstack, self.flist, self)
            if self.frame:
                stack, i = self.idb.get_stack(self.frame, None)
                sv.load_stack(stack, i)
        else:
            sv = self.stackviewer
            if sv and not self.vstack.get():
                self.stackviewer = None
                sv.close()
            self.fstack[b'height'] = 1
        return

    def show_source(self):
        if self.vsource.get():
            self.sync_source_line()
        return

    def show_frame(self, stackitem):
        self.frame = stackitem[0]
        self.show_variables()
        return

    localsviewer = None
    globalsviewer = None

    def show_locals(self):
        lv = self.localsviewer
        if self.vlocals.get():
            if not lv:
                self.localsviewer = NamespaceViewer(self.flocals, b'Locals')
        elif lv:
            self.localsviewer = None
            lv.close()
            self.flocals[b'height'] = 1
        self.show_variables()
        return

    def show_globals(self):
        gv = self.globalsviewer
        if self.vglobals.get():
            if not gv:
                self.globalsviewer = NamespaceViewer(self.fglobals, b'Globals')
        elif gv:
            self.globalsviewer = None
            gv.close()
            self.fglobals[b'height'] = 1
        self.show_variables()
        return

    def show_variables(self, force=0):
        lv = self.localsviewer
        gv = self.globalsviewer
        frame = self.frame
        if not frame:
            ldict = gdict = None
        else:
            ldict = frame.f_locals
            gdict = frame.f_globals
            if lv and gv and ldict is gdict:
                ldict = None
        if lv:
            lv.load_dict(ldict, force, self.pyshell.interp.rpcclt)
        if gv:
            gv.load_dict(gdict, force, self.pyshell.interp.rpcclt)
        return

    def set_breakpoint_here(self, filename, lineno):
        self.idb.set_break(filename, lineno)
        return

    def clear_breakpoint_here(self, filename, lineno):
        self.idb.clear_break(filename, lineno)
        return

    def clear_file_breaks(self, filename):
        self.idb.clear_all_file_breaks(filename)
        return

    def load_breakpoints(self):
        pyshell_edit_windows = self.pyshell.flist.inversedict.keys()
        for editwin in pyshell_edit_windows:
            filename = editwin.io.filename
            try:
                for lineno in editwin.breakpoints:
                    self.set_breakpoint_here(filename, lineno)

            except AttributeError:
                continue

        return


class StackViewer(ScrolledList):

    def __init__(self, master, flist, gui):
        if macosxSupport.isAquaTk():
            ScrolledList.__init__(self, master)
        else:
            ScrolledList.__init__(self, master, width=80)
        self.flist = flist
        self.gui = gui
        self.stack = []
        return

    def load_stack(self, stack, index=None):
        self.stack = stack
        self.clear()
        for i in range(len(stack)):
            frame, lineno = stack[i]
            try:
                modname = frame.f_globals[b'__name__']
            except:
                modname = b'?'

            code = frame.f_code
            filename = code.co_filename
            funcname = code.co_name
            import linecache
            sourceline = linecache.getline(filename, lineno)
            import string
            sourceline = string.strip(sourceline)
            if funcname in (b'?', b'', None):
                item = b'%s, line %d: %s' % (modname, lineno, sourceline)
            else:
                item = b'%s.%s(), line %d: %s' % (modname, funcname,
                 lineno, sourceline)
            if i == index:
                item = b'> ' + item
            self.append(item)

        if index is not None:
            self.select(index)
        return

    def popup_event(self, event):
        if self.stack:
            return ScrolledList.popup_event(self, event)
        return

    def fill_menu(self):
        menu = self.menu
        menu.add_command(label=b'Go to source line', command=self.goto_source_line)
        menu.add_command(label=b'Show stack frame', command=self.show_stack_frame)
        return

    def on_select(self, index):
        if 0 <= index < len(self.stack):
            self.gui.show_frame(self.stack[index])
        return

    def on_double(self, index):
        self.show_source(index)
        return

    def goto_source_line(self):
        index = self.listbox.index(b'active')
        self.show_source(index)
        return

    def show_stack_frame(self):
        index = self.listbox.index(b'active')
        if 0 <= index < len(self.stack):
            self.gui.show_frame(self.stack[index])
        return

    def show_source(self, index):
        if not 0 <= index < len(self.stack):
            return
        frame, lineno = self.stack[index]
        code = frame.f_code
        filename = code.co_filename
        if os.path.isfile(filename):
            edit = self.flist.open(filename)
            if edit:
                edit.gotoline(lineno)
        return


class NamespaceViewer():

    def __init__(self, master, title, dict=None):
        width = 0
        height = 40
        if dict:
            height = 20 * len(dict)
        self.master = master
        self.title = title
        import repr
        self.repr = repr.Repr()
        self.repr.maxstring = 60
        self.repr.maxother = 60
        self.frame = frame = Frame(master)
        self.frame.pack(expand=1, fill=b'both')
        self.label = Label(frame, text=title, borderwidth=2, relief=b'groove')
        self.label.pack(fill=b'x')
        self.vbar = vbar = Scrollbar(frame, name=b'vbar')
        vbar.pack(side=b'right', fill=b'y')
        self.canvas = canvas = Canvas(frame, height=min(300, max(40, height)), scrollregion=(
         0, 0, width, height))
        canvas.pack(side=b'left', fill=b'both', expand=1)
        vbar[b'command'] = canvas.yview
        canvas[b'yscrollcommand'] = vbar.set
        self.subframe = subframe = Frame(canvas)
        self.sfid = canvas.create_window(0, 0, window=subframe, anchor=b'nw')
        self.load_dict(dict)
        return

    dict = -1

    def load_dict(self, dict, force=0, rpc_client=None):
        if dict is self.dict and not force:
            return
        else:
            subframe = self.subframe
            frame = self.frame
            for c in subframe.children.values():
                c.destroy()

            self.dict = None
            if not dict:
                l = Label(subframe, text=b'None')
                l.grid(row=0, column=0)
            else:
                names = dict.keys()
                names.sort()
                row = 0
                for name in names:
                    value = dict[name]
                    svalue = self.repr.repr(value)
                    if rpc_client:
                        svalue = svalue[1:-1]
                    l = Label(subframe, text=name)
                    l.grid(row=row, column=0, sticky=b'nw')
                    l = Entry(subframe, width=0, borderwidth=0)
                    l.insert(0, svalue)
                    l.grid(row=row, column=1, sticky=b'nw')
                    row = row + 1

            self.dict = dict
            subframe.update_idletasks()
            width = subframe.winfo_reqwidth()
            height = subframe.winfo_reqheight()
            canvas = self.canvas
            self.canvas[b'scrollregion'] = (0, 0, width, height)
            if height > 300:
                canvas[b'height'] = 300
                frame.pack(expand=1)
            else:
                canvas[b'height'] = height
                frame.pack(expand=0)
            return

    def close(self):
        self.frame.destroy()
        return
