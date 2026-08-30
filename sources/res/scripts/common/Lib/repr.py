__all__ = [
 b'Repr', b'repr']
import __builtin__
from itertools import islice

class Repr:

    def __init__(self):
        self.maxlevel = 6
        self.maxtuple = 6
        self.maxlist = 6
        self.maxarray = 5
        self.maxdict = 4
        self.maxset = 6
        self.maxfrozenset = 6
        self.maxdeque = 6
        self.maxstring = 30
        self.maxlong = 40
        self.maxother = 20
        return

    def repr(self, x):
        return self.repr1(x, self.maxlevel)

    def repr1(self, x, level):
        typename = type(x).__name__
        if b' ' in typename:
            parts = typename.split()
            typename = (b'_').join(parts)
        if hasattr(self, b'repr_' + typename):
            return getattr(self, b'repr_' + typename)(x, level)
        else:
            s = __builtin__.repr(x)
            if len(s) > self.maxother:
                i = max(0, (self.maxother - 3) // 2)
                j = max(0, self.maxother - 3 - i)
                s = s[:i] + b'...' + s[len(s) - j:]
            return s

        return

    def _repr_iterable(self, x, level, left, right, maxiter, trail=b''):
        n = len(x)
        if level <= 0 and n:
            s = b'...'
        else:
            newlevel = level - 1
            repr1 = self.repr1
            pieces = [repr1(elem, newlevel) for elem in islice(x, maxiter)]
            if n > maxiter:
                pieces.append(b'...')
            s = (b', ').join(pieces)
            if n == 1 and trail:
                right = trail + right
        return b'%s%s%s' % (left, s, right)

    def repr_tuple(self, x, level):
        return self._repr_iterable(x, level, b'(', b')', self.maxtuple, b',')

    def repr_list(self, x, level):
        return self._repr_iterable(x, level, b'[', b']', self.maxlist)

    def repr_array(self, x, level):
        header = b"array('%s', [" % x.typecode
        return self._repr_iterable(x, level, header, b'])', self.maxarray)

    def repr_set(self, x, level):
        x = _possibly_sorted(x)
        return self._repr_iterable(x, level, b'set([', b'])', self.maxset)

    def repr_frozenset(self, x, level):
        x = _possibly_sorted(x)
        return self._repr_iterable(x, level, b'frozenset([', b'])', self.maxfrozenset)

    def repr_deque(self, x, level):
        return self._repr_iterable(x, level, b'deque([', b'])', self.maxdeque)

    def repr_dict(self, x, level):
        n = len(x)
        if n == 0:
            return b'{}'
        if level <= 0:
            return b'{...}'
        newlevel = level - 1
        repr1 = self.repr1
        pieces = []
        for key in islice(_possibly_sorted(x), self.maxdict):
            keyrepr = repr1(key, newlevel)
            valrepr = repr1(x[key], newlevel)
            pieces.append(b'%s: %s' % (keyrepr, valrepr))

        if n > self.maxdict:
            pieces.append(b'...')
        s = (b', ').join(pieces)
        return b'{%s}' % (s,)

    def repr_str(self, x, level):
        s = __builtin__.repr(x[:self.maxstring])
        if len(s) > self.maxstring:
            i = max(0, (self.maxstring - 3) // 2)
            j = max(0, self.maxstring - 3 - i)
            s = __builtin__.repr(x[:i] + x[len(x) - j:])
            s = s[:i] + b'...' + s[len(s) - j:]
        return s

    def repr_long(self, x, level):
        s = __builtin__.repr(x)
        if len(s) > self.maxlong:
            i = max(0, (self.maxlong - 3) // 2)
            j = max(0, self.maxlong - 3 - i)
            s = s[:i] + b'...' + s[len(s) - j:]
        return s

    def repr_instance(self, x, level):
        try:
            s = __builtin__.repr(x)
        except Exception:
            return b'<%s instance at %x>' % (x.__class__.__name__, id(x))

        if len(s) > self.maxstring:
            i = max(0, (self.maxstring - 3) // 2)
            j = max(0, self.maxstring - 3 - i)
            s = s[:i] + b'...' + s[len(s) - j:]
        return s


def _possibly_sorted(x):
    try:
        return sorted(x)
    except Exception:
        return list(x)

    return


aRepr = Repr()
repr = aRepr.repr
