import string
from Tkinter import *
from idlelib.Delegator import Delegator

class UndoDelegator(Delegator):
    max_undo = 1000

    def __init__(self):
        Delegator.__init__(self)
        self.reset_undo()
        return

    def setdelegate(self, delegate):
        if self.delegate is not None:
            self.unbind(b'<<undo>>')
            self.unbind(b'<<redo>>')
            self.unbind(b'<<dump-undo-state>>')
        Delegator.setdelegate(self, delegate)
        if delegate is not None:
            self.bind(b'<<undo>>', self.undo_event)
            self.bind(b'<<redo>>', self.redo_event)
            self.bind(b'<<dump-undo-state>>', self.dump_event)
        return

    def dump_event(self, event):
        from pprint import pprint
        pprint(self.undolist[:self.pointer])
        print b'pointer:', self.pointer,
        print b'saved:', self.saved,
        print b'can_merge:', self.can_merge,
        print b'get_saved():', self.get_saved()
        pprint(self.undolist[self.pointer:])
        return b'break'

    def reset_undo(self):
        self.was_saved = -1
        self.pointer = 0
        self.undolist = []
        self.undoblock = 0
        self.set_saved(1)
        return

    def set_saved(self, flag):
        if flag:
            self.saved = self.pointer
        else:
            self.saved = -1
        self.can_merge = False
        self.check_saved()
        return

    def get_saved(self):
        return self.saved == self.pointer

    saved_change_hook = None

    def set_saved_change_hook(self, hook):
        self.saved_change_hook = hook
        return

    was_saved = -1

    def check_saved(self):
        is_saved = self.get_saved()
        if is_saved != self.was_saved:
            self.was_saved = is_saved
            if self.saved_change_hook:
                self.saved_change_hook()
        return

    def insert(self, index, chars, tags=None):
        self.addcmd(InsertCommand(index, chars, tags))
        return

    def delete(self, index1, index2=None):
        self.addcmd(DeleteCommand(index1, index2))
        return

    def undo_block_start(self):
        if self.undoblock == 0:
            self.undoblock = CommandSequence()
        self.undoblock.bump_depth()
        return

    def undo_block_stop(self):
        if self.undoblock.bump_depth(-1) == 0:
            cmd = self.undoblock
            self.undoblock = 0
            if len(cmd) > 0:
                if len(cmd) == 1:
                    cmd = cmd.getcmd(0)
                self.addcmd(cmd, 0)
        return

    def addcmd(self, cmd, execute=True):
        if execute:
            cmd.do(self.delegate)
        if self.undoblock != 0:
            self.undoblock.append(cmd)
            return
        if self.can_merge and self.pointer > 0:
            lastcmd = self.undolist[self.pointer - 1]
            if lastcmd.merge(cmd):
                return
        self.undolist[(self.pointer):] = [
         cmd]
        if self.saved > self.pointer:
            self.saved = -1
        self.pointer = self.pointer + 1
        if len(self.undolist) > self.max_undo:
            del self.undolist[0]
            self.pointer = self.pointer - 1
            if self.saved >= 0:
                self.saved = self.saved - 1
        self.can_merge = True
        self.check_saved()
        return

    def undo_event(self, event):
        if self.pointer == 0:
            self.bell()
            return b'break'
        cmd = self.undolist[self.pointer - 1]
        cmd.undo(self.delegate)
        self.pointer = self.pointer - 1
        self.can_merge = False
        self.check_saved()
        return b'break'

    def redo_event(self, event):
        if self.pointer >= len(self.undolist):
            self.bell()
            return b'break'
        cmd = self.undolist[self.pointer]
        cmd.redo(self.delegate)
        self.pointer = self.pointer + 1
        self.can_merge = False
        self.check_saved()
        return b'break'


class Command:
    tags = None

    def __init__(self, index1, index2, chars, tags=None):
        self.marks_before = {}
        self.marks_after = {}
        self.index1 = index1
        self.index2 = index2
        self.chars = chars
        if tags:
            self.tags = tags
        return

    def __repr__(self):
        s = self.__class__.__name__
        t = (self.index1, self.index2, self.chars, self.tags)
        if self.tags is None:
            t = t[:-1]
        return s + repr(t)

    def do(self, text):
        return

    def redo(self, text):
        return

    def undo(self, text):
        return

    def merge(self, cmd):
        return 0

    def save_marks(self, text):
        marks = {}
        for name in text.mark_names():
            if name != b'insert' and name != b'current':
                marks[name] = text.index(name)

        return marks

    def set_marks(self, text, marks):
        for name, index in marks.items():
            text.mark_set(name, index)

        return


class InsertCommand(Command):

    def __init__(self, index1, chars, tags=None):
        Command.__init__(self, index1, None, chars, tags)
        return

    def do(self, text):
        self.marks_before = self.save_marks(text)
        self.index1 = text.index(self.index1)
        if text.compare(self.index1, b'>', b'end-1c'):
            self.index1 = text.index(b'end-1c')
        text.insert(self.index1, self.chars, self.tags)
        self.index2 = text.index(b'%s+%dc' % (self.index1, len(self.chars)))
        self.marks_after = self.save_marks(text)
        return

    def redo(self, text):
        text.mark_set(b'insert', self.index1)
        text.insert(self.index1, self.chars, self.tags)
        self.set_marks(text, self.marks_after)
        text.see(b'insert')
        return

    def undo(self, text):
        text.mark_set(b'insert', self.index1)
        text.delete(self.index1, self.index2)
        self.set_marks(text, self.marks_before)
        text.see(b'insert')
        return

    def merge(self, cmd):
        if self.__class__ is not cmd.__class__:
            return False
        if self.index2 != cmd.index1:
            return False
        if self.tags != cmd.tags:
            return False
        if len(cmd.chars) != 1:
            return False
        if self.chars and self.classify(self.chars[-1]) != self.classify(cmd.chars):
            return False
        self.index2 = cmd.index2
        self.chars = self.chars + cmd.chars
        return True

    alphanumeric = string.ascii_letters + string.digits + b'_'

    def classify(self, c):
        if c in self.alphanumeric:
            return b'alphanumeric'
        if c == b'\n':
            return b'newline'
        return b'punctuation'


class DeleteCommand(Command):

    def __init__(self, index1, index2=None):
        Command.__init__(self, index1, index2, None, None)
        return

    def do(self, text):
        self.marks_before = self.save_marks(text)
        self.index1 = text.index(self.index1)
        if self.index2:
            self.index2 = text.index(self.index2)
        else:
            self.index2 = text.index(self.index1 + b' +1c')
        if text.compare(self.index2, b'>', b'end-1c'):
            self.index2 = text.index(b'end-1c')
        self.chars = text.get(self.index1, self.index2)
        text.delete(self.index1, self.index2)
        self.marks_after = self.save_marks(text)
        return

    def redo(self, text):
        text.mark_set(b'insert', self.index1)
        text.delete(self.index1, self.index2)
        self.set_marks(text, self.marks_after)
        text.see(b'insert')
        return

    def undo(self, text):
        text.mark_set(b'insert', self.index1)
        text.insert(self.index1, self.chars)
        self.set_marks(text, self.marks_before)
        text.see(b'insert')
        return


class CommandSequence(Command):

    def __init__(self):
        self.cmds = []
        self.depth = 0
        return

    def __repr__(self):
        s = self.__class__.__name__
        strs = []
        for cmd in self.cmds:
            strs.append(b'    %r' % (cmd,))

        return s + b'(\n' + (b',\n').join(strs) + b'\n)'

    def __len__(self):
        return len(self.cmds)

    def append(self, cmd):
        self.cmds.append(cmd)
        return

    def getcmd(self, i):
        return self.cmds[i]

    def redo(self, text):
        for cmd in self.cmds:
            cmd.redo(text)

        return

    def undo(self, text):
        cmds = self.cmds[:]
        cmds.reverse()
        for cmd in cmds:
            cmd.undo(text)

        return

    def bump_depth(self, incr=1):
        self.depth = self.depth + incr
        return self.depth


def _undo_delegator(parent):
    from idlelib.Percolator import Percolator
    root = Tk()
    root.title(b'Test UndoDelegator')
    width, height, x, y = list(map(int, re.split(b'[x+]', parent.geometry())))
    root.geometry(b'+%d+%d' % (x, y + 150))
    text = Text(root)
    text.config(height=10)
    text.pack()
    text.focus_set()
    p = Percolator(text)
    d = UndoDelegator()
    p.insertfilter(d)
    undo = Button(root, text=b'Undo', command=(lambda : d.undo_event(None)))
    undo.pack(side=b'left')
    redo = Button(root, text=b'Redo', command=(lambda : d.redo_event(None)))
    redo.pack(side=b'left')
    dump = Button(root, text=b'Dump', command=(lambda : d.dump_event(None)))
    dump.pack(side=b'left')
    root.mainloop()
    return


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(_undo_delegator)
