import os, stat
from genericpath import *
from genericpath import _unicode
from ntpath import expanduser, expandvars, isabs, islink, splitdrive, splitext, split, walk
__all__ = [
 5, 6, 7, 8, 9, 10, 
 11, 12, 13, 14, 15, 
 16, 17, 18, 19, 20, 
 21, 22, 
 23, 24, 25, 26, 27, 28, 
 29, 30, 31, 32, 33, 34, 35, 
 36, 
 37, 38, 39]
curdir = b'.'
pardir = b'..'
extsep = b'.'
sep = b'/'
altsep = b'\\'
pathsep = b';'
defpath = b'.;C:\\bin'
devnull = b'nul'

def normcase(s):
    return s.replace(b'\\', b'/').lower()


def join(a, *p):
    path = a
    for b in p:
        if isabs(b):
            path = b
        elif path == b'' or path[-1:] in b'/\\:':
            path = path + b
        else:
            path = path + b'/' + b

    return path


def splitunc(p):
    if p[1:2] == b':':
        return (b'', p)
    firstTwo = p[0:2]
    if firstTwo == b'//' or firstTwo == b'\\\\':
        normp = normcase(p)
        index = normp.find(b'/', 2)
        if index == -1:
            return (
             b'', p)
        index = normp.find(b'/', index + 1)
        if index == -1:
            index = len(p)
        return (p[:index], p[index:])
    return (
     b'', p)


def basename(p):
    return split(p)[1]


def dirname(p):
    return split(p)[0]


lexists = exists

def ismount(path):
    unc, rest = splitunc(path)
    if unc:
        return rest in (b'', b'/', b'\\')
    p = splitdrive(path)[1]
    return len(p) == 1 and p[0] in b'/\\'


def normpath(path):
    path = path.replace(b'\\', b'/')
    prefix, path = splitdrive(path)
    while path[:1] == b'/':
        prefix = prefix + b'/'
        path = path[1:]

    comps = path.split(b'/')
    i = 0
    while i < len(comps):
        if comps[i] == b'.':
            del comps[i]
        elif comps[i] == b'..' and i > 0 and comps[i - 1] not in (b'', b'..'):
            del comps[i - 1:i + 1]
            i = i - 1
        elif comps[i] == b'' and i > 0 and comps[i - 1] != b'':
            del comps[i]
        else:
            i = i + 1

    if not prefix and not comps:
        comps.append(b'.')
    return prefix + (b'/').join(comps)


def abspath(path):
    if not isabs(path):
        if isinstance(path, _unicode):
            cwd = os.getcwdu()
        else:
            cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


realpath = abspath
supports_unicode_filenames = False
