class error(Exception):
    pass


_names = [
 b'dbhash', b'gdbm', b'dbm', b'dumbdbm']
_errors = [error]
_defaultmod = None
for _name in _names:
    try:
        _mod = __import__(_name)
    except ImportError:
        continue

    if not _defaultmod:
        _defaultmod = _mod
    _errors.append(_mod.error)

if not _defaultmod:
    raise ImportError, b'no dbm clone found; tried %s' % _names
error = tuple(_errors)

def open(file, flag=b'r', mode=438):
    from whichdb import whichdb
    result = whichdb(file)
    if result is None:
        if b'c' in flag or b'n' in flag:
            mod = _defaultmod
        else:
            raise error, b"need 'c' or 'n' flag to open new db"
    elif result == b'':
        raise error, b'db type could not be determined'
    else:
        mod = __import__(result)
    return mod.open(file, flag, mode)
