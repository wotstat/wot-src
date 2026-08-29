import sys

def _resolve_name(name, package, level):
    if not hasattr(package, b'rindex'):
        raise ValueError(b"'package' not set to a string")
    dot = len(package)
    for x in xrange(level, 1, -1):
        try:
            dot = package.rindex(b'.', 0, dot)
        except ValueError:
            raise ValueError(b'attempted relative import beyond top-level package')

    return b'%s.%s' % (package[:dot], name)


def import_module(name, package=None):
    if name.startswith(b'.'):
        if not package:
            raise TypeError(b"relative imports require the 'package' argument")
        level = 0
        for character in name:
            if character != b'.':
                break
            level += 1

        name = _resolve_name(name[level:], package, level)
    __import__(name)
    return sys.modules[name]
