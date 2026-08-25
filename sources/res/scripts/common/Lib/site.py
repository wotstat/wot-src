import sys, os, __builtin__, traceback
PREFIXES = [
 sys.prefix, sys.exec_prefix]
ENABLE_USER_SITE = None
USER_SITE = None
USER_BASE = None

def makepath(*paths):
    dir = os.path.join(*paths)
    try:
        dir = os.path.abspath(dir)
    except OSError:
        pass

    return (dir, os.path.normcase(dir))


def abs__file__():
    for m in sys.modules.values():
        if hasattr(m, b'__loader__'):
            continue
        try:
            m.__file__ = os.path.abspath(m.__file__)
        except (AttributeError, OSError):
            pass

    return


def removeduppaths():
    L = []
    known_paths = set()
    for dir in sys.path:
        dir, dircase = makepath(dir)
        if dircase not in known_paths:
            L.append(dir)
            known_paths.add(dircase)

    sys.path[:] = L
    return known_paths


def _init_pathinfo():
    d = set()
    for dir in sys.path:
        try:
            if os.path.isdir(dir):
                dir, dircase = makepath(dir)
                d.add(dircase)
        except TypeError:
            continue

    return d


def addpackage(sitedir, name, known_paths):
    if known_paths is None:
        _init_pathinfo()
        reset = 1
    else:
        reset = 0
    fullname = os.path.join(sitedir, name)
    try:
        f = open(fullname, b'rU')
    except IOError:
        return

    with f:
        for n, line in enumerate(f):
            if line.startswith(b'#'):
                continue
            try:
                if line.startswith((b'import ', b'import\t')):
                    exec line
                    continue
                line = line.rstrip()
                dir, dircase = makepath(sitedir, line)
                if dircase not in known_paths and os.path.exists(dir):
                    sys.path.append(dir)
                    known_paths.add(dircase)
            except Exception as err:
                print >> sys.stderr, (b'Error processing line {:d} of {}:\n').format(n + 1, fullname)
                for record in traceback.format_exception(*sys.exc_info()):
                    for line in record.splitlines():
                        print >> sys.stderr, b'  ' + line

                print >> sys.stderr, b'\nRemainder of file ignored'
                break

    if reset:
        known_paths = None
    return known_paths


def addsitedir(sitedir, known_paths=None):
    if known_paths is None:
        known_paths = _init_pathinfo()
        reset = 1
    else:
        reset = 0
    sitedir, sitedircase = makepath(sitedir)
    if sitedircase not in known_paths:
        sys.path.append(sitedir)
    try:
        names = os.listdir(sitedir)
    except os.error:
        return

    dotpth = os.extsep + b'pth'
    names = [name for name in names if name.endswith(dotpth)]
    for name in sorted(names):
        addpackage(sitedir, name, known_paths)

    if reset:
        known_paths = None
    return known_paths


def check_enableusersite():
    if sys.flags.no_user_site:
        return False
    else:
        if hasattr(os, b'getuid') and hasattr(os, b'geteuid'):
            if os.geteuid() != os.getuid():
                return None
        if hasattr(os, b'getgid') and hasattr(os, b'getegid'):
            if os.getegid() != os.getgid():
                return None
        return True


def getuserbase():
    global USER_BASE
    if USER_BASE is not None:
        return USER_BASE
    else:
        from sysconfig import get_config_var
        USER_BASE = get_config_var(b'userbase')
        return USER_BASE


def getusersitepackages():
    global USER_SITE
    user_base = getuserbase()
    if USER_SITE is not None:
        return USER_SITE
    else:
        from sysconfig import get_path
        import os
        if sys.platform == b'darwin':
            from sysconfig import get_config_var
            if get_config_var(b'PYTHONFRAMEWORK'):
                USER_SITE = get_path(b'purelib', b'osx_framework_user')
                return USER_SITE
        USER_SITE = get_path(b'purelib', b'%s_user' % os.name)
        return USER_SITE


def addusersitepackages(known_paths):
    global ENABLE_USER_SITE
    user_site = getusersitepackages()
    if ENABLE_USER_SITE and os.path.isdir(user_site):
        addsitedir(user_site, known_paths)
    return known_paths


def getsitepackages():
    sitepackages = []
    seen = set()
    for prefix in PREFIXES:
        if not prefix or prefix in seen:
            continue
        seen.add(prefix)
        if sys.platform in (b'os2emx', b'riscos'):
            sitepackages.append(os.path.join(prefix, b'Lib', b'site-packages'))
        elif os.sep == b'/':
            sitepackages.append(os.path.join(prefix, b'lib', b'python' + sys.version[:3], b'site-packages'))
            sitepackages.append(os.path.join(prefix, b'lib', b'site-python'))
        else:
            sitepackages.append(prefix)
            sitepackages.append(os.path.join(prefix, b'lib', b'site-packages'))

    return sitepackages


def addsitepackages(known_paths):
    for sitedir in getsitepackages():
        if os.path.isdir(sitedir):
            addsitedir(sitedir, known_paths)

    return known_paths


def setBEGINLIBPATH():
    dllpath = os.path.join(sys.prefix, b'Lib', b'lib-dynload')
    libpath = os.environ[b'BEGINLIBPATH'].split(b';')
    if libpath[-1]:
        libpath.append(dllpath)
    else:
        libpath[-1] = dllpath
    os.environ[b'BEGINLIBPATH'] = (b';').join(libpath)
    return


def setquit():
    if os.sep == b':':
        eof = b'Cmd-Q'
    elif os.sep == b'\\':
        eof = b'Ctrl-Z plus Return'
    else:
        eof = b'Ctrl-D (i.e. EOF)'

    class Quitter(object):

        def __init__(self, name):
            self.name = name
            return

        def __repr__(self):
            return b'Use %s() or %s to exit' % (self.name, eof)

        def __call__(self, code=None):
            try:
                sys.stdin.close()
            except:
                pass

            raise SystemExit(code)
            return

    __builtin__.quit = Quitter(b'quit')
    __builtin__.exit = Quitter(b'exit')
    return


class _Printer(object):
    MAXLINES = 23

    def __init__(self, name, data, files=(), dirs=()):
        self.__name = name
        self.__data = data
        self.__files = files
        self.__dirs = dirs
        self.__lines = None
        return

    def __setup(self):
        if self.__lines:
            return
        else:
            data = None
            for dir in self.__dirs:
                for filename in self.__files:
                    filename = os.path.join(dir, filename)
                    try:
                        fp = file(filename, b'rU')
                        data = fp.read()
                        fp.close()
                        break
                    except IOError:
                        pass

                if data:
                    break

            if not data:
                data = self.__data
            self.__lines = data.split(b'\n')
            self.__linecnt = len(self.__lines)
            return

    def __repr__(self):
        self.__setup()
        if len(self.__lines) <= self.MAXLINES:
            return (b'\n').join(self.__lines)
        else:
            return b'Type %s() to see the full %s text' % ((self.__name,) * 2)

        return

    def __call__(self):
        self.__setup()
        prompt = b'Hit Return for more, or q (and Return) to quit: '
        lineno = 0
        while 1:
            try:
                for i in range(lineno, lineno + self.MAXLINES):
                    print self.__lines[i]

            except IndexError:
                break
            else:
                lineno += self.MAXLINES
                key = None
                while key is None:
                    key = raw_input(prompt)
                    if key not in (b'', b'q'):
                        key = None

                if key == b'q':
                    break

        return


def setcopyright():
    __builtin__.copyright = _Printer(b'copyright', sys.copyright)
    if sys.platform[:4] == b'java':
        __builtin__.credits = _Printer(b'credits', b'Jython is maintained by the Jython developers (www.jython.org).')
    else:
        __builtin__.credits = _Printer(b'credits', b'    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands\n    for supporting Python development.  See www.python.org for more information.')
    here = os.path.dirname(os.__file__)
    __builtin__.license = _Printer(b'license', b'See https://www.python.org/psf/license/', [
     b'LICENSE.txt', b'LICENSE'], [
     os.path.join(here, os.pardir), here, os.curdir])
    return


class _Helper(object):

    def __repr__(self):
        return b'Type help() for interactive help, or help(object) for help about object.'

    def __call__(self, *args, **kwds):
        import pydoc
        return pydoc.help(*args, **kwds)


def sethelper():
    __builtin__.help = _Helper()
    return


def aliasmbcs():
    if sys.platform == b'win32':
        import locale, codecs
        enc = locale.getdefaultlocale()[1]
        if enc.startswith(b'cp'):
            try:
                codecs.lookup(enc)
            except LookupError:
                import encodings
                encodings._cache[enc] = encodings._unknown
                encodings.aliases.aliases[enc] = b'mbcs'

    return


def setencoding():
    encoding = b'ascii'
    if encoding != b'ascii':
        sys.setdefaultencoding(encoding)
    return


def execsitecustomize():
    try:
        import sitecustomize
    except ImportError:
        pass
    except Exception:
        if sys.flags.verbose:
            sys.excepthook(*sys.exc_info())
        else:
            print >> sys.stderr, b"'import sitecustomize' failed; use -v for traceback"

    return


def execusercustomize():
    try:
        import usercustomize
    except ImportError:
        pass
    except Exception:
        if sys.flags.verbose:
            sys.excepthook(*sys.exc_info())
        else:
            print >> sys.stderr, b"'import usercustomize' failed; use -v for traceback"

    return


def main():
    global ENABLE_USER_SITE
    abs__file__()
    known_paths = removeduppaths()
    if ENABLE_USER_SITE is None:
        ENABLE_USER_SITE = check_enableusersite()
    known_paths = addusersitepackages(known_paths)
    known_paths = addsitepackages(known_paths)
    if sys.platform == b'os2emx':
        setBEGINLIBPATH()
    setquit()
    setcopyright()
    sethelper()
    aliasmbcs()
    setencoding()
    execsitecustomize()
    if ENABLE_USER_SITE:
        execusercustomize()
    if hasattr(sys, b'setdefaultencoding'):
        del sys.setdefaultencoding
    return


main()

def _script():
    help = b"    %s [--user-base] [--user-site]\n\n    Without arguments print some useful information\n    With arguments print the value of USER_BASE and/or USER_SITE separated\n    by '%s'.\n\n    Exit codes with --user-base or --user-site:\n      0 - user site directory is enabled\n      1 - user site directory is disabled by user\n      2 - uses site directory is disabled by super user\n          or for security reasons\n     >2 - unknown error\n    "
    args = sys.argv[1:]
    if not args:
        print b'sys.path = ['
        for dir in sys.path:
            print b'    %r,' % (dir,)

        print b']'
        print b'USER_BASE: %r (%s)' % (USER_BASE,
         b'exists' if os.path.isdir(USER_BASE) else b"doesn't exist")
        print b'USER_SITE: %r (%s)' % (USER_SITE,
         b'exists' if os.path.isdir(USER_SITE) else b"doesn't exist")
        print b'ENABLE_USER_SITE: %r' % ENABLE_USER_SITE
        sys.exit(0)
    buffer = []
    if b'--user-base' in args:
        buffer.append(USER_BASE)
    if b'--user-site' in args:
        buffer.append(USER_SITE)
    if buffer:
        print os.pathsep.join(buffer)
        if ENABLE_USER_SITE:
            sys.exit(0)
        elif ENABLE_USER_SITE is False:
            sys.exit(1)
        elif ENABLE_USER_SITE is None:
            sys.exit(2)
        else:
            sys.exit(3)
    else:
        import textwrap
        print textwrap.dedent(help % (sys.argv[0], os.pathsep))
        sys.exit(10)
    return


if __name__ == b'__main__':
    _script()
