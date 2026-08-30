import os, struct, sys
try:
    import dbm
    _dbmerror = dbm.error
except ImportError:
    dbm = None
    _dbmerror = IOError

def whichdb(filename):
    try:
        f = open(filename + os.extsep + b'pag', b'rb')
        f.close()
        if not (dbm.library == b'GNU gdbm' and sys.platform == b'os2emx'):
            f = open(filename + os.extsep + b'dir', b'rb')
            f.close()
        return b'dbm'
    except IOError:
        try:
            f = open(filename + os.extsep + b'db', b'rb')
            f.close()
            if dbm is not None:
                d = dbm.open(filename)
                d.close()
                return b'dbm'
        except (IOError, _dbmerror):
            pass

    try:
        os.stat(filename + os.extsep + b'dat')
        size = os.stat(filename + os.extsep + b'dir').st_size
        if size == 0:
            return b'dumbdbm'
        f = open(filename + os.extsep + b'dir', b'rb')
        try:
            if f.read(1) in (b"'", b'"'):
                return b'dumbdbm'
        finally:
            f.close()

    except (OSError, IOError):
        pass

    try:
        f = open(filename, b'rb')
    except IOError:
        return

    s16 = f.read(16)
    f.close()
    s = s16[0:4]
    if len(s) != 4:
        return b''
    else:
        try:
            magic, = struct.unpack(b'=l', s)
        except struct.error:
            return b''

        if magic in (324508366, 324508365, 324508367):
            return b'gdbm'
        if magic in (398689, 1628767744):
            return b'bsddb185'
        try:
            magic, = struct.unpack(b'=l', s16[-4:])
        except struct.error:
            return b''

        if magic in (398689, 1628767744):
            return b'dbhash'
        return b''


if __name__ == b'__main__':
    for filename in sys.argv[1:]:
        print whichdb(filename) or b'UNKNOWN', filename
