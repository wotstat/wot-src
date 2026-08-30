import sys, os
__all__ = [
 b'getline', b'clearcache', b'checkcache']

def getline(filename, lineno, module_globals=None):
    lines = getlines(filename, module_globals)
    if 1 <= lineno <= len(lines):
        return lines[lineno - 1]
    else:
        return b''

    return


cache = {}

def clearcache():
    global cache
    cache = {}
    return


def getlines(filename, module_globals=None):
    if filename in cache:
        return cache[filename][2]
    try:
        return updatecache(filename, module_globals)
    except MemoryError:
        clearcache()
        return []

    return


def checkcache(filename=None):
    if filename is None:
        filenames = cache.keys()
    elif filename in cache:
        filenames = [
         filename]
    else:
        return
    for filename in filenames:
        size, mtime, lines, fullname = cache[filename]
        if mtime is None:
            continue
        try:
            stat = os.stat(fullname)
        except os.error:
            del cache[filename]
            continue

        if size != stat.st_size or mtime != stat.st_mtime:
            del cache[filename]

    return


def updatecache(filename, module_globals=None):
    if filename in cache:
        del cache[filename]
    if not filename or filename.startswith(b'<') and filename.endswith(b'>'):
        return []
    fullname = filename
    try:
        stat = os.stat(fullname)
    except OSError:
        basename = filename
        if module_globals and b'__loader__' in module_globals:
            name = module_globals.get(b'__name__')
            loader = module_globals[b'__loader__']
            get_source = getattr(loader, b'get_source', None)
            if name and get_source:
                try:
                    data = get_source(name)
                except (ImportError, IOError):
                    pass
                else:
                    if data is None:
                        return []
                    else:
                        cache[filename] = (len(data), None, [line + b'\n' for line in data.splitlines()], fullname)
                        return cache[filename][2]

        if os.path.isabs(filename):
            return []
        for dirname in sys.path:
            try:
                fullname = os.path.join(dirname, basename)
            except (TypeError, AttributeError):
                continue

            try:
                stat = os.stat(fullname)
                break
            except os.error:
                pass

        else:
            return []

    try:
        with open(fullname, b'rU') as fp:
            lines = fp.readlines()
    except IOError:
        return []

    if lines and not lines[-1].endswith(b'\n'):
        lines[-1] += b'\n'
    size, mtime = stat.st_size, stat.st_mtime
    cache[filename] = (size, mtime, lines, fullname)
    return lines
