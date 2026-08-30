import warnings
warnings.warn(b'The posixfile module is deprecated; fcntl.lockf() provides better locking', DeprecationWarning, 2)

class _posixfile_:
    states = [
     b'open', b'closed']

    def __repr__(self):
        file = self._file_
        return b"<%s posixfile '%s', mode '%s' at %s>" % (
         self.states[file.closed], file.name, file.mode,
         hex(id(self))[2:])

    def open(self, name, mode=b'r', bufsize=-1):
        import __builtin__
        return self.fileopen(__builtin__.open(name, mode, bufsize))

    def fileopen(self, file):
        import types
        if repr(type(file)) != b"<type 'file'>":
            raise TypeError, b'posixfile.fileopen() arg must be file object'
        self._file_ = file
        for maybemethod in dir(file):
            if not maybemethod.startswith(b'_'):
                attr = getattr(file, maybemethod)
                if isinstance(attr, types.BuiltinMethodType):
                    setattr(self, maybemethod, attr)

        return self

    def file(self):
        return self._file_

    def dup(self):
        import posix
        if not hasattr(posix, b'fdopen'):
            raise AttributeError, b'dup() method unavailable'
        return posix.fdopen(posix.dup(self._file_.fileno()), self._file_.mode)

    def dup2(self, fd):
        import posix
        if not hasattr(posix, b'fdopen'):
            raise AttributeError, b'dup() method unavailable'
        posix.dup2(self._file_.fileno(), fd)
        return posix.fdopen(fd, self._file_.mode)

    def flags(self, *which):
        import fcntl, os
        if which:
            if len(which) > 1:
                raise TypeError, b'Too many arguments'
            which = which[0]
        else:
            which = b'?'
        l_flags = 0
        if b'n' in which:
            l_flags = l_flags | os.O_NDELAY
        if b'a' in which:
            l_flags = l_flags | os.O_APPEND
        if b's' in which:
            l_flags = l_flags | os.O_SYNC
        file = self._file_
        if b'=' not in which:
            cur_fl = fcntl.fcntl(file.fileno(), fcntl.F_GETFL, 0)
            if b'!' in which:
                l_flags = cur_fl & ~l_flags
            else:
                l_flags = cur_fl | l_flags
        l_flags = fcntl.fcntl(file.fileno(), fcntl.F_SETFL, l_flags)
        if b'c' in which:
            arg = b'!' not in which
            l_flags = fcntl.fcntl(file.fileno(), fcntl.F_SETFD, arg)
        if b'?' in which:
            which = b''
            l_flags = fcntl.fcntl(file.fileno(), fcntl.F_GETFL, 0)
            if os.O_APPEND & l_flags:
                which = which + b'a'
            if fcntl.fcntl(file.fileno(), fcntl.F_GETFD, 0) & 1:
                which = which + b'c'
            if os.O_NDELAY & l_flags:
                which = which + b'n'
            if os.O_SYNC & l_flags:
                which = which + b's'
            return which
        return

    def lock(self, how, *args):
        import struct, fcntl
        if b'w' in how:
            l_type = fcntl.F_WRLCK
        elif b'r' in how:
            l_type = fcntl.F_RDLCK
        elif b'u' in how:
            l_type = fcntl.F_UNLCK
        else:
            raise TypeError, b'no type of lock specified'
        if b'|' in how:
            cmd = fcntl.F_SETLKW
        elif b'?' in how:
            cmd = fcntl.F_GETLK
        else:
            cmd = fcntl.F_SETLK
        l_whence = 0
        l_start = 0
        l_len = 0
        if len(args) == 1:
            l_len = args[0]
        elif len(args) == 2:
            l_len, l_start = args
        elif len(args) == 3:
            l_len, l_start, l_whence = args
        elif len(args) > 3:
            raise TypeError, b'too many arguments'
        import sys, os
        if sys.platform in (b'netbsd1', b'openbsd2', b'freebsd2', b'freebsd3', b'freebsd4', b'freebsd5', b'freebsd6', b'freebsd7', b'freebsd8', b'bsdos2', b'bsdos3', b'bsdos4'):
            flock = struct.pack(b'lxxxxlxxxxlhh', l_start, l_len, os.getpid(), l_type, l_whence)
        elif sys.platform in (b'aix3', b'aix4'):
            flock = struct.pack(b'hhlllii', l_type, l_whence, l_start, l_len, 0, 0, 0)
        else:
            flock = struct.pack(b'hhllhh', l_type, l_whence, l_start, l_len, 0, 0)
        flock = fcntl.fcntl(self._file_.fileno(), cmd, flock)
        if b'?' in how:
            if sys.platform in (b'netbsd1', b'openbsd2', b'freebsd2', b'freebsd3', b'freebsd4', b'freebsd5', b'bsdos2', b'bsdos3', b'bsdos4'):
                l_start, l_len, l_pid, l_type, l_whence = struct.unpack(b'lxxxxlxxxxlhh', flock)
            elif sys.platform in (b'aix3', b'aix4'):
                l_type, l_whence, l_start, l_len, l_sysid, l_pid, l_vfs = struct.unpack(b'hhlllii', flock)
            elif sys.platform == b'linux2':
                l_type, l_whence, l_start, l_len, l_pid, l_sysid = struct.unpack(b'hhllhh', flock)
            else:
                l_type, l_whence, l_start, l_len, l_sysid, l_pid = struct.unpack(b'hhllhh', flock)
            if l_type != fcntl.F_UNLCK:
                if l_type == fcntl.F_RDLCK:
                    return (b'r', l_len, l_start, l_whence, l_pid)
                else:
                    return (
                     b'w', l_len, l_start, l_whence, l_pid)

        return


def open(name, mode=b'r', bufsize=-1):
    return _posixfile_().open(name, mode, bufsize)


def fileopen(file):
    return _posixfile_().fileopen(file)


SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2
