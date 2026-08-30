__version__ = b'4.0.3'
__all__ = [
 1, 
 2, 
 3, 
 4, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22, 
 23, 
 24, 
 25, 
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32]

def message_from_string(s, *args, **kws):
    from email.parser import Parser
    return Parser(*args, **kws).parsestr(s)


def message_from_file(fp, *args, **kws):
    from email.parser import Parser
    return Parser(*args, **kws).parse(fp)


import sys

class LazyImporter(object):

    def __init__(self, module_name):
        self.__name__ = b'email.' + module_name
        return

    def __getattr__(self, name):
        __import__(self.__name__)
        mod = sys.modules[self.__name__]
        self.__dict__.update(mod.__dict__)
        return getattr(mod, name)


_LOWERNAMES = [
 2, 
 3, 
 4, 
 39, 
 5, 
 6, 
 7, 
 8, 
 16, 
 18, 
 1, 
 17]
_MIMENAMES = [
 40, 
 41, 
 42, 
 8, 
 43, 
 44, 
 45]
for _name in _LOWERNAMES:
    importer = LazyImporter(_name.lower())
    sys.modules[b'email.' + _name] = importer
    setattr(sys.modules[b'email'], _name, importer)

import email.mime
for _name in _MIMENAMES:
    importer = LazyImporter(b'mime.' + _name.lower())
    sys.modules[b'email.MIME' + _name] = importer
    setattr(sys.modules[b'email'], b'MIME' + _name, importer)
    setattr(sys.modules[b'email.mime'], _name, importer)
