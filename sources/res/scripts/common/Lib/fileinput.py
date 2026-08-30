import sys, os
__all__ = [
 2, 3, 4, 5, 6, 7, 
 8, 9, 10]
_state = None
DEFAULT_BUFSIZE = 8192

def input(files=None, inplace=0, backup=b'', bufsize=0, mode=b'r', openhook=None):
    global _state
    if _state and _state._file:
        raise RuntimeError, b'input() already active'
    _state = FileInput(files, inplace, backup, bufsize, mode, openhook)
    return _state


def close():
    global _state
    state = _state
    _state = None
    if state:
        state.close()
    return


def nextfile():
    if not _state:
        raise RuntimeError, b'no active input()'
    return _state.nextfile()


def filename():
    if not _state:
        raise RuntimeError, b'no active input()'
    return _state.filename()


def lineno():
    if not _state:
        raise RuntimeError, b'no active input()'
    return _state.lineno()


def filelineno():
    if not _state:
        raise RuntimeError, b'no active input()'
    return _state.filelineno()


def fileno():
    if not _state:
        raise RuntimeError, b'no active input()'
    return _state.fileno()


def isfirstline():
    if not _state:
        raise RuntimeError, b'no active input()'
    return _state.isfirstline()


def isstdin():
    if not _state:
        raise RuntimeError, b'no active input()'
    return _state.isstdin()


class FileInput:

    def __init__(self, files=None, inplace=0, backup=b'', bufsize=0, mode=b'r', openhook=None):
        if isinstance(files, basestring):
            files = (
             files,)
        elif files is None:
            files = sys.argv[1:]
        if not files:
            files = (b'-',)
        else:
            files = tuple(files)
        self._files = files
        self._inplace = inplace
        self._backup = backup
        self._savestdout = None
        self._output = None
        self._filename = None
        self._startlineno = 0
        self._filelineno = 0
        self._file = None
        self._isstdin = False
        self._backupfilename = None
        if mode not in (b'r', b'rU', b'U', b'rb'):
            raise ValueError(b"FileInput opening mode must be one of 'r', 'rU', 'U' and 'rb'")
        self._mode = mode
        if inplace and openhook:
            raise ValueError(b'FileInput cannot use an opening hook in inplace mode')
        elif openhook and not hasattr(openhook, b'__call__'):
            raise ValueError(b'FileInput openhook must be callable')
        self._openhook = openhook
        return

    def __del__(self):
        self.close()
        return

    def close(self):
        try:
            self.nextfile()
        finally:
            self._files = ()

        return

    def __iter__(self):
        return self

    def next(self):
        while 1:
            line = self._readline()
            if line:
                self._filelineno += 1
                return line
            if not self._file:
                raise StopIteration
            self.nextfile()

        return

    def __getitem__(self, i):
        if i != self.lineno():
            raise RuntimeError, b'accessing lines out of order'
        try:
            return self.next()
        except StopIteration:
            raise IndexError, b'end of input reached'

        return

    def nextfile(self):
        savestdout = self._savestdout
        self._savestdout = 0
        if savestdout:
            sys.stdout = savestdout
        output = self._output
        self._output = 0
        try:
            if output:
                output.close()
        finally:
            file = self._file
            self._file = None
            try:
                del self._readline
            except AttributeError:
                pass

            try:
                if file and not self._isstdin:
                    file.close()
            finally:
                backupfilename = self._backupfilename
                self._backupfilename = 0
                if backupfilename and not self._backup:
                    try:
                        os.unlink(backupfilename)
                    except OSError:
                        pass

                self._isstdin = False

        return

    def readline(self):
        while 1:
            line = self._readline()
            if line:
                self._filelineno += 1
                return line
            if not self._file:
                return line
            self.nextfile()

        return

    def _readline(self):
        if not self._files:
            return b''
        else:
            self._filename = self._files[0]
            self._files = self._files[1:]
            self._startlineno = self.lineno()
            self._filelineno = 0
            self._file = None
            self._isstdin = False
            self._backupfilename = 0
            if self._filename == b'-':
                self._filename = b'<stdin>'
                self._file = sys.stdin
                self._isstdin = True
            elif self._inplace:
                self._backupfilename = self._filename + (self._backup or os.extsep + b'bak')
                try:
                    os.unlink(self._backupfilename)
                except os.error:
                    pass

                os.rename(self._filename, self._backupfilename)
                self._file = open(self._backupfilename, self._mode)
                try:
                    perm = os.fstat(self._file.fileno()).st_mode
                except OSError:
                    self._output = open(self._filename, b'w')
                else:
                    fd = os.open(self._filename, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, perm)
                    self._output = os.fdopen(fd, b'w')
                    try:
                        if hasattr(os, b'chmod'):
                            os.chmod(self._filename, perm)
                    except OSError:
                        pass

                self._savestdout = sys.stdout
                sys.stdout = self._output
            elif self._openhook:
                self._file = self._openhook(self._filename, self._mode)
            else:
                self._file = open(self._filename, self._mode)
            self._readline = self._file.readline
            return self._readline()

    def filename(self):
        return self._filename

    def lineno(self):
        return self._startlineno + self._filelineno

    def filelineno(self):
        return self._filelineno

    def fileno(self):
        if self._file:
            try:
                return self._file.fileno()
            except ValueError:
                return -1

        else:
            return -1
        return

    def isfirstline(self):
        return self._filelineno == 1

    def isstdin(self):
        return self._isstdin


def hook_compressed(filename, mode):
    ext = os.path.splitext(filename)[1]
    if ext == b'.gz':
        import gzip
        return gzip.open(filename, mode)
    else:
        if ext == b'.bz2':
            import bz2
            return bz2.BZ2File(filename, mode)
        return open(filename, mode)

    return


def hook_encoded(encoding):
    import io

    def openhook(filename, mode):
        mode = mode.replace(b'U', b'').replace(b'b', b'') or b'r'
        return io.open(filename, mode, encoding=encoding, newline=b'')

    return openhook


def _test():
    import getopt
    inplace = 0
    backup = 0
    opts, args = getopt.getopt(sys.argv[1:], b'ib:')
    for o, a in opts:
        if o == b'-i':
            inplace = 1
        if o == b'-b':
            backup = a

    for line in input(args, inplace=inplace, backup=backup):
        if line[-1:] == b'\n':
            line = line[:-1]
        if line[-1:] == b'\r':
            line = line[:-1]
        print b'%d: %s[%d]%s %s' % (lineno(), filename(), filelineno(),
         isfirstline() and b'*' or b'', line)

    print b'%d: %s[%d]' % (lineno(), filename(), filelineno())
    return


if __name__ == b'__main__':
    _test()
