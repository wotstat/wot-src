__revision__ = b'$Id$'
import sys

class TextFile:
    default_options = {b'strip_comments': 1, b'skip_blanks': 1, 
       b'lstrip_ws': 0, 
       b'rstrip_ws': 1, 
       b'join_lines': 0, 
       b'collapse_join': 0}

    def __init__(self, filename=None, file=None, **options):
        if filename is None and file is None:
            raise RuntimeError, b"you must supply either or both of 'filename' and 'file'"
        for opt in self.default_options.keys():
            if opt in options:
                setattr(self, opt, options[opt])
            else:
                setattr(self, opt, self.default_options[opt])

        for opt in options.keys():
            if opt not in self.default_options:
                raise KeyError, b"invalid TextFile option '%s'" % opt

        if file is None:
            self.open(filename)
        else:
            self.filename = filename
            self.file = file
            self.current_line = 0
        self.linebuf = []
        return

    def open(self, filename):
        self.filename = filename
        self.file = open(self.filename, b'r')
        self.current_line = 0
        return

    def close(self):
        file = self.file
        self.file = None
        self.filename = None
        self.current_line = None
        file.close()
        return

    def gen_error(self, msg, line=None):
        outmsg = []
        if line is None:
            line = self.current_line
        outmsg.append(self.filename + b', ')
        if isinstance(line, (list, tuple)):
            outmsg.append(b'lines %d-%d: ' % tuple(line))
        else:
            outmsg.append(b'line %d: ' % line)
        outmsg.append(str(msg))
        return (b'').join(outmsg)

    def error(self, msg, line=None):
        raise ValueError, b'error: ' + self.gen_error(msg, line)
        return

    def warn(self, msg, line=None):
        sys.stderr.write(b'warning: ' + self.gen_error(msg, line) + b'\n')
        return

    def readline(self):
        if self.linebuf:
            line = self.linebuf[-1]
            del self.linebuf[-1]
            return line
        else:
            buildup_line = b''
            while 1:
                line = self.file.readline()
                if line == b'':
                    line = None
                if self.strip_comments and line:
                    pos = line.find(b'#')
                    if pos == -1:
                        pass
                    elif pos == 0 or line[pos - 1] != b'\\':
                        eol = line[-1] == b'\n' and b'\n' or b''
                        line = line[0:pos] + eol
                        if line.strip() == b'':
                            continue
                    else:
                        line = line.replace(b'\\#', b'#')
                if self.join_lines and buildup_line:
                    if line is None:
                        self.warn(b'continuation line immediately precedes end-of-file')
                        return buildup_line
                    if self.collapse_join:
                        line = line.lstrip()
                    line = buildup_line + line
                    if isinstance(self.current_line, list):
                        self.current_line[1] = self.current_line[1] + 1
                    else:
                        self.current_line = [
                         self.current_line,
                         self.current_line + 1]
                elif line is None:
                    return
                if isinstance(self.current_line, list):
                    self.current_line = self.current_line[1] + 1
                else:
                    self.current_line = self.current_line + 1
                if self.lstrip_ws and self.rstrip_ws:
                    line = line.strip()
                elif self.lstrip_ws:
                    line = line.lstrip()
                elif self.rstrip_ws:
                    line = line.rstrip()
                if (line == b'' or line == b'\n') and self.skip_blanks:
                    continue
                if self.join_lines:
                    if line[-1] == b'\\':
                        buildup_line = line[:-1]
                        continue
                    if line[-2:] == b'\\\n':
                        buildup_line = line[0:-2] + b'\n'
                        continue
                return line

            return

    def readlines(self):
        lines = []
        while 1:
            line = self.readline()
            if line is None:
                return lines
            lines.append(line)

        return

    def unreadline(self, line):
        self.linebuf.append(line)
        return
