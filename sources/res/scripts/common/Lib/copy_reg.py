from types import ClassType as _ClassType
__all__ = [
 2, 3, 
 4, 5, 6]
dispatch_table = {}

def pickle(ob_type, pickle_function, constructor_ob=None):
    if type(ob_type) is _ClassType:
        raise TypeError(b'copy_reg is not intended for use with classes')
    if not hasattr(pickle_function, b'__call__'):
        raise TypeError(b'reduction functions must be callable')
    dispatch_table[ob_type] = pickle_function
    if constructor_ob is not None:
        constructor(constructor_ob)
    return


def constructor(object):
    if not hasattr(object, b'__call__'):
        raise TypeError(b'constructors must be callable')
    return


try:
    complex
except NameError:
    pass
else:

    def pickle_complex(c):
        return (complex, (c.real, c.imag))


    pickle(complex, pickle_complex, complex)

def _reconstructor(cls, base, state):
    if base is object:
        obj = object.__new__(cls)
    else:
        obj = base.__new__(cls, state)
        if base.__init__ != object.__init__:
            base.__init__(obj, state)
    return obj


_HEAPTYPE = 512

def _reduce_ex(self, proto):
    for base in self.__class__.__mro__:
        if hasattr(base, b'__flags__') and not base.__flags__ & _HEAPTYPE:
            break
    else:
        base = object

    if base is object:
        state = None
    elif base is self.__class__:
        raise TypeError, b"can't pickle %s objects" % base.__name__
    state = base(self)
    args = (self.__class__, base, state)
    try:
        getstate = self.__getstate__
    except AttributeError:
        if getattr(self, b'__slots__', None):
            raise TypeError(b'a class that defines __slots__ without defining __getstate__ cannot be pickled')
        try:
            dict = self.__dict__
        except AttributeError:
            dict = None

    else:
        dict = getstate()

    if dict:
        return (_reconstructor, args, dict)
    else:
        return (
         _reconstructor, args)
        return


def __newobj__(cls, *args):
    return cls.__new__(cls, *args)


def _slotnames(cls):
    names = cls.__dict__.get(b'__slotnames__')
    if names is not None:
        return names
    else:
        names = []
        if not hasattr(cls, b'__slots__'):
            pass
        else:
            for c in cls.__mro__:
                if b'__slots__' in c.__dict__:
                    slots = c.__dict__[b'__slots__']
                    if isinstance(slots, basestring):
                        slots = (
                         slots,)
                    for name in slots:
                        if name in (b'__dict__', b'__weakref__'):
                            continue
                        elif name.startswith(b'__') and not name.endswith(b'__'):
                            stripped = c.__name__.lstrip(b'_')
                            if stripped:
                                names.append(b'_%s%s' % (stripped, name))
                            else:
                                names.append(name)
                        else:
                            names.append(name)

            try:
                cls.__slotnames__ = names
            except:
                pass

        return names


_extension_registry = {}
_inverted_registry = {}
_extension_cache = {}

def add_extension(module, name, code):
    code = int(code)
    if not 1 <= code <= 2147483647:
        raise ValueError, b'code out of range'
    key = (
     module, name)
    if _extension_registry.get(key) == code and _inverted_registry.get(code) == key:
        return
    if key in _extension_registry:
        raise ValueError(b'key %s is already registered with code %s' % (
         key, _extension_registry[key]))
    if code in _inverted_registry:
        raise ValueError(b'code %s is already in use for key %s' % (
         code, _inverted_registry[code]))
    _extension_registry[key] = code
    _inverted_registry[code] = key
    return


def remove_extension(module, name, code):
    key = (
     module, name)
    if _extension_registry.get(key) != code or _inverted_registry.get(code) != key:
        raise ValueError(b'key %s is not registered with code %s' % (
         key, code))
    del _extension_registry[key]
    del _inverted_registry[code]
    if code in _extension_cache:
        del _extension_cache[code]
    return


def clear_extension_cache():
    _extension_cache.clear()
    return
