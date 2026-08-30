import sys, os
try:
    import ctypes
    ctypes.windll.kernel32.GetFinalPathNameByHandleW
except (ImportError, AttributeError):

    def convert_path(s):
        return s


else:

    def convert_path(s):
        udir = s.decode(b'mbcs')
        hdir = ctypes.windll.kernel32.CreateFileW(udir, 128, 1, None, 3, 33554432, None)
        if hdir == -1:
            return s
        else:
            buf = ctypes.create_unicode_buffer(u'', 32768)
            res = ctypes.windll.kernel32.GetFinalPathNameByHandleW(hdir, buf, len(buf), 0)
            ctypes.windll.kernel32.CloseHandle(hdir)
            if res == 0:
                return s
            s = buf[:res].encode(b'mbcs')
            if s.startswith(b'\\\\?\\'):
                s = s[4:]
            if s.startswith(b'UNC'):
                s = b'\\' + s[3:]
            return s


prefix = os.path.join(sys.prefix, b'tcl')
if not os.path.exists(prefix):
    tcltk = b'tcltk'
    if sys.maxsize > 2147483647L:
        tcltk = b'tcltk64'
    prefix = os.path.join(sys.prefix, b'externals', tcltk, b'lib')
    prefix = os.path.abspath(prefix)
if os.path.exists(prefix):
    prefix = convert_path(prefix)
    if b'TCL_LIBRARY' not in os.environ:
        for name in os.listdir(prefix):
            if name.startswith(b'tcl'):
                tcldir = os.path.join(prefix, name)
                if os.path.isdir(tcldir):
                    os.environ[b'TCL_LIBRARY'] = tcldir

    import _tkinter
    ver = str(_tkinter.TCL_VERSION)
    if b'TK_LIBRARY' not in os.environ:
        v = os.path.join(prefix, b'tk' + ver)
        if os.path.exists(os.path.join(v, b'tclIndex')):
            os.environ[b'TK_LIBRARY'] = v
    if b'TIX_LIBRARY' not in os.environ:
        for name in os.listdir(prefix):
            if name.startswith(b'tix'):
                tixdir = os.path.join(prefix, name)
                if os.path.isdir(tixdir):
                    os.environ[b'TIX_LIBRARY'] = tixdir
