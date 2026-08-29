try:
    from errno import EINVAL
except ImportError:
    EINVAL = 22

__all__ = [b'StringIO']

def _complain_ifclosed(closed):
    if closed:
        raise ValueError, b'I/O operation on closed file'
    return


class StringIO:

    def __init__(self, buf=b''):
        if not isinstance(buf, basestring):
            buf = str(buf)
        self.buf = buf
        self.len = len(buf)
        self.buflist = []
        self.pos = 0
        self.closed = False
        self.softspace = 0
        return

    def __iter__(self):
        return self

    def next(self):
        _complain_ifclosed(self.closed)
        r = self.readline()
        if not r:
            raise StopIteration
        return r

    def close(self):
        if not self.closed:
            self.closed = True
            del self.buf
            del self.pos
        return

    def isatty(self):
        _complain_ifclosed(self.closed)
        return False

    def seek(self, pos, mode=0):
        _complain_ifclosed(self.closed)
        if self.buflist:
            self.buf += (b'').join(self.buflist)
            self.buflist = []
        if mode == 1:
            pos += self.pos
        elif mode == 2:
            pos += self.len
        self.pos = max(0, pos)
        return

    def tell(self):
        _complain_ifclosed(self.closed)
        return self.pos

    def read(self, n=-1):
        _complain_ifclosed(self.closed)
        if self.buflist:
            self.buf += (b'').join(self.buflist)
            self.buflist = []
        if n is None or n < 0:
            newpos = self.len
        else:
            newpos = min(self.pos + n, self.len)
        r = self.buf[self.pos:newpos]
        self.pos = newpos
        return r

    def readline(self, length=None):
        _complain_ifclosed(self.closed)
        if self.buflist:
            self.buf += (b'').join(self.buflist)
            self.buflist = []
        i = self.buf.find(b'\n', self.pos)
        if i < 0:
            newpos = self.len
        else:
            newpos = i + 1
        if length is not None and length >= 0:
            if self.pos + length < newpos:
                newpos = self.pos + length
        r = self.buf[self.pos:newpos]
        self.pos = newpos
        return r

    def readlines(self, sizehint=0):
        total = 0
        lines = []
        line = self.readline()
        while line:
            lines.append(line)
            total += len(line)
            if 0 < sizehint <= total:
                break
            line = self.readline()

        return lines

    def truncate(self, size=None):
        _complain_ifclosed(self.closed)
        if size is None:
            size = self.pos
        elif size < 0:
            raise IOError(EINVAL, b'Negative size not allowed')
        elif size < self.pos:
            self.pos = size
        self.buf = self.getvalue()[:size]
        self.len = size
        return

    def write(self, s):
        _complain_ifclosed(self.closed)
        if not s:
            return
        if not isinstance(s, basestring):
            s = str(s)
        spos = self.pos
        slen = self.len
        if spos == slen:
            self.buflist.append(s)
            self.len = self.pos = spos + len(s)
            return
        if spos > slen:
            self.buflist.append(b'\x00' * (spos - slen))
            slen = spos
        newpos = spos + len(s)
        if spos < slen:
            if self.buflist:
                self.buf += (b'').join(self.buflist)
            self.buflist = [
             self.buf[:spos], s, self.buf[newpos:]]
            self.buf = b''
            if newpos > slen:
                slen = newpos
        else:
            self.buflist.append(s)
            slen = newpos
        self.len = slen
        self.pos = newpos
        return

    def writelines(self, iterable):
        write = self.write
        for line in iterable:
            write(line)

        return

    def flush(self):
        _complain_ifclosed(self.closed)
        return

    def getvalue(self):
        _complain_ifclosed(self.closed)
        if self.buflist:
            self.buf += (b'').join(self.buflist)
            self.buflist = []
        return self.buf


def test():
    import sys
    if sys.argv[1:]:
        file = sys.argv[1]
    else:
        file = b'/etc/passwd'
    lines = open(file, b'r').readlines()
    text = open(file, b'r').read()
    f = StringIO()
    for line in lines[:-2]:
        f.write(line)

    f.writelines(lines[-2:])
    if f.getvalue() != text:
        raise RuntimeError, b'write failed'
    length = f.tell()
    print b'File length =', length
    f.seek(len(lines[0]))
    f.write(lines[1])
    f.seek(0)
    print b'First line =', repr(f.readline())
    print b'Position =', f.tell()
    line = f.readline()
    print b'Second line =', repr(line)
    f.seek(-len(line), 1)
    line2 = f.read(len(line))
    if line != line2:
        raise RuntimeError, b'bad result after seek back'
    f.seek(len(line2), 1)
    list = f.readlines()
    line = list[-1]
    f.seek(f.tell() - len(line))
    line2 = f.read()
    if line != line2:
        raise RuntimeError, b'bad result after seek back from EOF'
    print b'Read', len(list), b'more lines'
    print b'File length =', f.tell()
    if f.tell() != length:
        raise RuntimeError, b'bad length'
    f.truncate(length / 2)
    f.seek(0, 2)
    print b'Truncated length =', f.tell()
    if f.tell() != length / 2:
        raise RuntimeError, b'truncate did not adjust length'
    f.close()
    return


if __name__ == b'__main__':
    test()
