from warnings import warnpy3k
warnpy3k(b'the dircache module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import os
__all__ = [
 b'listdir', b'opendir', b'annotate', b'reset']
cache = {}

def reset():
    global cache
    cache = {}
    return


def listdir(path):
    try:
        cached_mtime, list = cache[path]
        del cache[path]
    except KeyError:
        cached_mtime, list = -1, []

    mtime = os.stat(path).st_mtime
    if mtime != cached_mtime:
        list = os.listdir(path)
        list.sort()
    cache[path] = (
     mtime, list)
    return list


opendir = listdir

def annotate(head, list):
    for i in range(len(list)):
        if os.path.isdir(os.path.join(head, list[i])):
            list[i] = list[i] + b'/'

    return
