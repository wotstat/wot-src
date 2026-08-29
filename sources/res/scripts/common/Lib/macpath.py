import os, warnings
from stat import *
import genericpath
from genericpath import *
from genericpath import _unicode
__all__ = [
 4, 5, 6, 7, 8, 9, 
 10, 11, 12, 13, 14, 
 15, 16, 17, 18, 19, 
 20, 21, 
 22, 23, 24, 25, 26, 
 27, 28, 29, 30, 31, 32, 33, 
 34, 
 35, 36]
curdir = b':'
pardir = b'::'
extsep = b'.'
sep = b':'
pathsep = b'\n'
defpath = b':'
altsep = None
devnull = b'Dev:Null'

def normcase(path):
    return path.lower()


def isabs(s):
    return b':' in s and s[0] != b':'


def join(s, *p):
    path = s
    for t in p:
        if not path or isabs(t):
            path = t
            continue
        if t[:1] == b':':
            t = t[1:]
        if b':' not in path:
            path = b':' + path
        if path[-1:] != b':':
            path = path + b':'
        path = path + t

    return path


def split(s):
    if b':' not in s:
        return (b'', s)
    colon = 0
    for i in range(len(s)):
        if s[i] == b':':
            colon = i + 1

    path, file = s[:colon - 1], s[colon:]
    if path and b':' not in path:
        path = path + b':'
    return (
     path, file)


def splitext(p):
    return genericpath._splitext(p, sep, altsep, extsep)


splitext.__doc__ = genericpath._splitext.__doc__

def splitdrive(p):
    return (
     b'', p)


def dirname(s):
    return split(s)[0]


def basename(s):
    return split(s)[1]


def ismount(s):
    if not isabs(s):
        return False
    components = split(s)
    return len(components) == 2 and components[1] == b''


def islink(s):
    try:
        import Carbon.File
        return Carbon.File.ResolveAliasFile(s, 0)[2]
    except:
        return False

    return


def lexists(path):
    try:
        st = os.lstat(path)
    except os.error:
        return False

    return True


def expandvars(path):
    return path


def expanduser(path):
    return path


class norm_error(Exception):
    pass


def normpath(s):
    if b':' not in s:
        return b':' + s
    comps = s.split(b':')
    i = 1
    while i < len(comps) - 1:
        if comps[i] == b'' and comps[i - 1] != b'':
            if i > 1:
                del comps[i - 1:i + 1]
                i = i - 1
            else:
                raise norm_error, b'Cannot use :: immediately after volume name'
        else:
            i = i + 1

    s = (b':').join(comps)
    if s[-1] == b':' and len(comps) > 2 and s != b':' * len(s):
        s = s[:-1]
    return s


def walk(top, func, arg):
    warnings.warnpy3k(b'In 3.x, os.path.walk is removed in favor of os.walk.', stacklevel=2)
    try:
        names = os.listdir(top)
    except os.error:
        return

    func(arg, top, names)
    for name in names:
        name = join(top, name)
        if isdir(name) and not islink(name):
            walk(name, func, arg)

    return


def abspath(path):
    if not isabs(path):
        if isinstance(path, _unicode):
            cwd = os.getcwdu()
        else:
            cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


def realpath(path):
    path = abspath(path)
    try:
        import Carbon.File
    except ImportError:
        return path

    if not path:
        return path
    components = path.split(b':')
    path = components[0] + b':'
    for c in components[1:]:
        path = join(path, c)
        try:
            path = Carbon.File.FSResolveAliasFile(path, 1)[0].as_pathname()
        except Carbon.File.Error:
            pass

    return path


supports_unicode_filenames = True
