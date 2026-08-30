import string
__all__ = [
 b'Cmd']
PROMPT = b'(Cmd) '
IDENTCHARS = string.ascii_letters + string.digits + b'_'

class Cmd:
    prompt = PROMPT
    identchars = IDENTCHARS
    ruler = b'='
    lastcmd = b''
    intro = None
    doc_leader = b''
    doc_header = b'Documented commands (type help <topic>):'
    misc_header = b'Miscellaneous help topics:'
    undoc_header = b'Undocumented commands:'
    nohelp = b'*** No help on %s'
    use_rawinput = 1

    def __init__(self, completekey=b'tab', stdin=None, stdout=None):
        import sys
        if stdin is not None:
            self.stdin = stdin
        else:
            self.stdin = sys.stdin
        if stdout is not None:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout
        self.cmdqueue = []
        self.completekey = completekey
        return

    def cmdloop(self, intro=None):
        self.preloop()
        if self.use_rawinput and self.completekey:
            try:
                import readline
                self.old_completer = readline.get_completer()
                readline.set_completer(self.complete)
                readline.parse_and_bind(self.completekey + b': complete')
            except ImportError:
                pass

        try:
            if intro is not None:
                self.intro = intro
            if self.intro:
                self.stdout.write(str(self.intro) + b'\n')
            stop = None
            while not stop:
                if self.cmdqueue:
                    line = self.cmdqueue.pop(0)
                elif self.use_rawinput:
                    try:
                        line = raw_input(self.prompt)
                    except EOFError:
                        line = b'EOF'

                else:
                    self.stdout.write(self.prompt)
                    self.stdout.flush()
                    line = self.stdin.readline()
                    if not len(line):
                        line = b'EOF'
                    else:
                        line = line.rstrip(b'\r\n')
                line = self.precmd(line)
                stop = self.onecmd(line)
                stop = self.postcmd(stop, line)

            self.postloop()
        finally:
            if self.use_rawinput and self.completekey:
                try:
                    import readline
                    readline.set_completer(self.old_completer)
                except ImportError:
                    pass

        return

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        return stop

    def preloop(self):
        return

    def postloop(self):
        return

    def parseline(self, line):
        line = line.strip()
        if not line:
            return (None, None, line)
        else:
            if line[0] == b'?':
                line = b'help ' + line[1:]
            elif line[0] == b'!':
                if hasattr(self, b'do_shell'):
                    line = b'shell ' + line[1:]
                else:
                    return (
                     None, None, line)
            i, n = 0, len(line)
            while i < n and line[i] in self.identchars:
                i = i + 1

            cmd, arg = line[:i], line[i:].strip()
            return (cmd, arg, line)

    def onecmd(self, line):
        cmd, arg, line = self.parseline(line)
        if not line:
            return self.emptyline()
        else:
            if cmd is None:
                return self.default(line)
            else:
                self.lastcmd = line
                if line == b'EOF':
                    self.lastcmd = b''
                if cmd == b'':
                    return self.default(line)
                try:
                    func = getattr(self, b'do_' + cmd)
                except AttributeError:
                    return self.default(line)

                return func(arg)

            return

    def emptyline(self):
        if self.lastcmd:
            return self.onecmd(self.lastcmd)
        return

    def default(self, line):
        self.stdout.write(b'*** Unknown syntax: %s\n' % line)
        return

    def completedefault(self, *ignored):
        return []

    def completenames(self, text, *ignored):
        dotext = b'do_' + text
        return [a[3:] for a in self.get_names() if a.startswith(dotext)]

    def complete(self, text, state):
        if state == 0:
            import readline
            origline = readline.get_line_buffer()
            line = origline.lstrip()
            stripped = len(origline) - len(line)
            begidx = readline.get_begidx() - stripped
            endidx = readline.get_endidx() - stripped
            if begidx > 0:
                cmd, args, foo = self.parseline(line)
                if cmd == b'':
                    compfunc = self.completedefault
                else:
                    try:
                        compfunc = getattr(self, b'complete_' + cmd)
                    except AttributeError:
                        compfunc = self.completedefault

            else:
                compfunc = self.completenames
            self.completion_matches = compfunc(text, line, begidx, endidx)
        try:
            return self.completion_matches[state]
        except IndexError:
            return

        return

    def get_names(self):
        return dir(self.__class__)

    def complete_help(self, *args):
        commands = set(self.completenames(*args))
        topics = set(a[5:] for a in self.get_names() if a.startswith(b'help_' + args[0]))
        return list(commands | topics)

    def do_help(self, arg):
        if arg:
            try:
                func = getattr(self, b'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, b'do_' + arg).__doc__
                    if doc:
                        self.stdout.write(b'%s\n' % str(doc))
                        return
                except AttributeError:
                    pass

                self.stdout.write(b'%s\n' % str(self.nohelp % (arg,)))
                return

            func()
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == b'help_':
                    help[name[5:]] = 1

            names.sort()
            prevname = b''
            for name in names:
                if name[:3] == b'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd = name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)

            self.stdout.write(b'%s\n' % str(self.doc_leader))
            self.print_topics(self.doc_header, cmds_doc, 15, 80)
            self.print_topics(self.misc_header, help.keys(), 15, 80)
            self.print_topics(self.undoc_header, cmds_undoc, 15, 80)
        return

    def print_topics(self, header, cmds, cmdlen, maxcol):
        if cmds:
            self.stdout.write(b'%s\n' % str(header))
            if self.ruler:
                self.stdout.write(b'%s\n' % str(self.ruler * len(header)))
            self.columnize(cmds, maxcol - 1)
            self.stdout.write(b'\n')
        return

    def columnize(self, list, displaywidth=80):
        if not list:
            self.stdout.write(b'<empty>\n')
            return
        nonstrings = [i for i in range(len(list)) if not isinstance(list[i], str)]
        if nonstrings:
            raise TypeError, b'list[i] not a string for i in %s' % (b', ').join(map(str, nonstrings))
        size = len(list)
        if size == 1:
            self.stdout.write(b'%s\n' % str(list[0]))
            return
        for nrows in range(1, len(list)):
            ncols = (size + nrows - 1) // nrows
            colwidths = []
            totwidth = -2
            for col in range(ncols):
                colwidth = 0
                for row in range(nrows):
                    i = row + nrows * col
                    if i >= size:
                        break
                    x = list[i]
                    colwidth = max(colwidth, len(x))

                colwidths.append(colwidth)
                totwidth += colwidth + 2
                if totwidth > displaywidth:
                    break

            if totwidth <= displaywidth:
                break
        else:
            nrows = len(list)
            ncols = 1
            colwidths = [0]

        for row in range(nrows):
            texts = []
            for col in range(ncols):
                i = row + nrows * col
                if i >= size:
                    x = b''
                else:
                    x = list[i]
                texts.append(x)

            while texts and not texts[-1]:
                del texts[-1]

            for col in range(len(texts)):
                texts[col] = texts[col].ljust(colwidths[col])

            self.stdout.write(b'%s\n' % str((b'  ').join(texts)))

        return
