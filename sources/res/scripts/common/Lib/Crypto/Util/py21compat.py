__revision__ = b'$Id$'
__all__ = []
import sys, __builtin__
try:
    (
     True, False)
except NameError:
    True, False = (1, 0)
    __all__ += [b'True', b'False']

try:
    object
except NameError:

    class object:
        pass


    __all__ += [b'object']

try:
    isinstance(5, (int, long))
except TypeError:
    __all__ += [b'isinstance']
    _builtin_type_map = {tuple: (type(())), 
       list: (type([])), 
       str: (type(b'')), 
       unicode: (type(u'')), 
       int: (type(0)), 
       long: (type(0L))}

    def isinstance(obj, t):
        if not __builtin__.isinstance(t, type(())):
            return __builtin__.isinstance(obj, _builtin_type_map.get(t, t))
        else:
            for typ in t:
                if __builtin__.isinstance(obj, _builtin_type_map.get(typ, typ)):
                    return True

            return False

        return


try:

    class A:

        def a():
            return

        a = staticmethod(a)


except NameError:

    class staticmethod:

        def __init__(self, anycallable):
            self.__call__ = anycallable
            return


    __all__ += [b'staticmethod']
