from _functools import partial, reduce
WRAPPER_ASSIGNMENTS = (b'__module__', b'__name__', b'__doc__')
WRAPPER_UPDATES = (b'__dict__',)

def update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
    for attr in assigned:
        setattr(wrapper, attr, getattr(wrapped, attr))

    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

    return wrapper


def wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)


def total_ordering(cls):
    convert = {b'__lt__': [
                 (
                  b'__gt__', (lambda self, other: not (self < other or self == other))),
                 (
                  b'__le__', (lambda self, other: self < other or self == other)),
                 (
                  b'__ne__', (lambda self, other: not self == other)),
                 (
                  b'__ge__', (lambda self, other: not self < other))], 
       b'__le__': [
                 (
                  b'__ge__', (lambda self, other: not self <= other or self == other)),
                 (
                  b'__lt__', (lambda self, other: self <= other and not self == other)),
                 (
                  b'__ne__', (lambda self, other: not self == other)),
                 (
                  b'__gt__', (lambda self, other: not self <= other))], 
       b'__gt__': [
                 (
                  b'__lt__', (lambda self, other: not (self > other or self == other))),
                 (
                  b'__ge__', (lambda self, other: self > other or self == other)),
                 (
                  b'__ne__', (lambda self, other: not self == other)),
                 (
                  b'__le__', (lambda self, other: not self > other))], 
       b'__ge__': [
                 (
                  b'__le__', (lambda self, other: not self >= other or self == other)),
                 (
                  b'__gt__', (lambda self, other: self >= other and not self == other)),
                 (
                  b'__ne__', (lambda self, other: not self == other)),
                 (
                  b'__lt__', (lambda self, other: not self >= other))]}
    defined_methods = set(dir(cls))
    roots = defined_methods & set(convert)
    if not roots:
        raise ValueError(b'must define at least one ordering operation: < > <= >=')
    root = max(roots)
    for opname, opfunc in convert[root]:
        if opname not in defined_methods:
            opfunc.__name__ = opname
            opfunc.__doc__ = getattr(int, opname).__doc__
            setattr(cls, opname, opfunc)

    return cls


def cmp_to_key(mycmp):

    class K(object):
        __slots__ = [
         b'obj']

        def __init__(self, obj, *args):
            self.obj = obj
            return

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

        def __hash__(self):
            raise TypeError(b'hash not implemented')
            return

    return K
