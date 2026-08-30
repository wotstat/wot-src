import __builtin__, imp, marshal, os, sys, traceback
MAGIC = imp.get_magic()
__all__ = [
 b'compile', b'main', b'PyCompileError']

class PyCompileError(Exception):

    def __init__(self, exc_type, exc_value, file, msg=b''):
        exc_type_name = exc_type.__name__
        if exc_type is SyntaxError:
            tbtext = (b'').join(traceback.format_exception_only(exc_type, exc_value))
            errmsg = tbtext.replace(b'File "<string>"', b'File "%s"' % file)
        else:
            errmsg = b'Sorry: %s: %s' % (exc_type_name, exc_value)
        Exception.__init__(self, msg or errmsg, exc_type_name, exc_value, file)
        self.exc_type_name = exc_type_name
        self.exc_value = exc_value
        self.file = file
        self.msg = msg or errmsg
        return

    def __str__(self):
        return self.msg


def wr_long(f, x):
    f.write(chr(x & 255))
    f.write(chr(x >> 8 & 255))
    f.write(chr(x >> 16 & 255))
    f.write(chr(x >> 24 & 255))
    return


def compile(file, cfile=None, dfile=None, doraise=False):
    with open(file, b'U') as f:
        try:
            timestamp = long(os.fstat(f.fileno()).st_mtime)
        except AttributeError:
            timestamp = long(os.stat(file).st_mtime)

        codestring = f.read()
    try:
        codeobject = __builtin__.compile(codestring, dfile or file, b'exec')
    except Exception as err:
        py_exc = PyCompileError(err.__class__, err, dfile or file)
        if doraise:
            raise py_exc
        else:
            sys.stderr.write(py_exc.msg + b'\n')
            return

    if cfile is None:
        cfile = file + (__debug__ and b'c' or b'o')
    with open(cfile, b'wb') as fc:
        fc.write(b'\x00\x00\x00\x00')
        wr_long(fc, timestamp)
        marshal.dump(codeobject, fc)
        fc.flush()
        fc.seek(0, 0)
        fc.write(MAGIC)
    return


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    rv = 0
    if args == [b'-']:
        while True:
            filename = sys.stdin.readline()
            if not filename:
                break
            filename = filename.rstrip(b'\n')
            try:
                compile(filename, doraise=True)
            except PyCompileError as error:
                rv = 1
                sys.stderr.write(b'%s\n' % error.msg)
            except IOError as error:
                rv = 1
                sys.stderr.write(b'%s\n' % error)

    else:
        for filename in args:
            try:
                compile(filename, doraise=True)
            except PyCompileError as error:
                rv = 1
                sys.stderr.write(b'%s\n' % error.msg)

    return rv


if __name__ == b'__main__':
    sys.exit(main())
