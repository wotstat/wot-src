import sys, ctypes, weakref
from multiprocessing import heap, RLock
from multiprocessing.forking import assert_spawning, ForkingPickler
__all__ = [
 4, 5, 6, 7, 8, 9]
typecode_to_type = {b'c': (ctypes.c_char), 
   b'b': (ctypes.c_byte), 
   b'B': (ctypes.c_ubyte), b'h': (ctypes.c_short), 
   b'H': (ctypes.c_ushort), b'i': (ctypes.c_int), 
   b'I': (ctypes.c_uint), b'l': (ctypes.c_long), 
   b'L': (ctypes.c_ulong), b'f': (ctypes.c_float), 
   b'd': (ctypes.c_double)}
try:
    typecode_to_type[b'u'] = ctypes.c_wchar
except AttributeError:
    pass

def _new_value(type_):
    size = ctypes.sizeof(type_)
    wrapper = heap.BufferWrapper(size)
    return rebuild_ctype(type_, wrapper, None)


def RawValue(typecode_or_type, *args):
    type_ = typecode_to_type.get(typecode_or_type, typecode_or_type)
    obj = _new_value(type_)
    ctypes.memset(ctypes.addressof(obj), 0, ctypes.sizeof(obj))
    obj.__init__(*args)
    return obj


def RawArray(typecode_or_type, size_or_initializer):
    type_ = typecode_to_type.get(typecode_or_type, typecode_or_type)
    if isinstance(size_or_initializer, (int, long)):
        type_ = type_ * size_or_initializer
        obj = _new_value(type_)
        ctypes.memset(ctypes.addressof(obj), 0, ctypes.sizeof(obj))
        return obj
    else:
        type_ = type_ * len(size_or_initializer)
        result = _new_value(type_)
        result.__init__(*size_or_initializer)
        return result

    return


def Value(typecode_or_type, *args, **kwds):
    lock = kwds.pop(b'lock', None)
    if kwds:
        raise ValueError(b'unrecognized keyword argument(s): %s' % kwds.keys())
    obj = RawValue(typecode_or_type, *args)
    if lock is False:
        return obj
    else:
        if lock in (True, None):
            lock = RLock()
        if not hasattr(lock, b'acquire'):
            raise AttributeError(b"'%r' has no method 'acquire'" % lock)
        return synchronized(obj, lock)


def Array(typecode_or_type, size_or_initializer, **kwds):
    lock = kwds.pop(b'lock', None)
    if kwds:
        raise ValueError(b'unrecognized keyword argument(s): %s' % kwds.keys())
    obj = RawArray(typecode_or_type, size_or_initializer)
    if lock is False:
        return obj
    else:
        if lock in (True, None):
            lock = RLock()
        if not hasattr(lock, b'acquire'):
            raise AttributeError(b"'%r' has no method 'acquire'" % lock)
        return synchronized(obj, lock)


def copy(obj):
    new_obj = _new_value(type(obj))
    ctypes.pointer(new_obj)[0] = obj
    return new_obj


def synchronized(obj, lock=None):
    if isinstance(obj, ctypes._SimpleCData):
        return Synchronized(obj, lock)
    else:
        if isinstance(obj, ctypes.Array):
            if obj._type_ is ctypes.c_char:
                return SynchronizedString(obj, lock)
            return SynchronizedArray(obj, lock)
        cls = type(obj)
        try:
            scls = class_cache[cls]
        except KeyError:
            names = [field[0] for field in cls._fields_]
            d = dict((name, make_property(name)) for name in names)
            classname = b'Synchronized' + cls.__name__
            scls = class_cache[cls] = type(classname, (SynchronizedBase,), d)

        return scls(obj, lock)

    return


def reduce_ctype(obj):
    assert_spawning(obj)
    if isinstance(obj, ctypes.Array):
        return (rebuild_ctype, (obj._type_, obj._wrapper, obj._length_))
    else:
        return (
         rebuild_ctype, (type(obj), obj._wrapper, None))
        return


def rebuild_ctype(type_, wrapper, length):
    if length is not None:
        type_ = type_ * length
    ForkingPickler.register(type_, reduce_ctype)
    obj = type_.from_address(wrapper.get_address())
    obj._wrapper = wrapper
    return obj


def make_property(name):
    try:
        return prop_cache[name]
    except KeyError:
        d = {}
        exec template % ((name,) * 7) in d
        prop_cache[name] = d[name]
        return d[name]

    return


template = b'\ndef get%s(self):\n    self.acquire()\n    try:\n        return self._obj.%s\n    finally:\n        self.release()\ndef set%s(self, value):\n    self.acquire()\n    try:\n        self._obj.%s = value\n    finally:\n        self.release()\n%s = property(get%s, set%s)\n'
prop_cache = {}
class_cache = weakref.WeakKeyDictionary()

class SynchronizedBase(object):

    def __init__(self, obj, lock=None):
        self._obj = obj
        self._lock = lock or RLock()
        self.acquire = self._lock.acquire
        self.release = self._lock.release
        return

    def __reduce__(self):
        assert_spawning(self)
        return (synchronized, (self._obj, self._lock))

    def get_obj(self):
        return self._obj

    def get_lock(self):
        return self._lock

    def __repr__(self):
        return b'<%s wrapper for %s>' % (type(self).__name__, self._obj)


class Synchronized(SynchronizedBase):
    value = make_property(b'value')


class SynchronizedArray(SynchronizedBase):

    def __len__(self):
        return len(self._obj)

    def __getitem__(self, i):
        self.acquire()
        try:
            return self._obj[i]
        finally:
            self.release()

        return

    def __setitem__(self, i, value):
        self.acquire()
        try:
            self._obj[i] = value
        finally:
            self.release()

        return

    def __getslice__(self, start, stop):
        self.acquire()
        try:
            return self._obj[start:stop]
        finally:
            self.release()

        return

    def __setslice__(self, start, stop, values):
        self.acquire()
        try:
            self._obj[start:stop] = values
        finally:
            self.release()

        return


class SynchronizedString(SynchronizedArray):
    value = make_property(b'value')
    raw = make_property(b'raw')
