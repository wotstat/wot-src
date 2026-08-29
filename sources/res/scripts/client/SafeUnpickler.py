import sys, cPickle, StringIO

class SafeUnpickler(object):
    PICKLE_SAFE = {b'__builtin__': (set([0, 1, 2, 3, 4])), 
       b'datetime': (set([b'datetime'])), 
       b'_BWp': (set([b'Array', b'FixedDict'])), 
       b'Math': (set([b'Vector2', b'Vector3']))}

    @classmethod
    def find_class(cls, module, name):
        if module not in cls.PICKLE_SAFE:
            raise cPickle.UnpicklingError(b'Attempting to unpickle unsafe module %s' % module)
        __import__(module)
        mod = sys.modules[module]
        classesSet = cls.PICKLE_SAFE[module]
        if name not in classesSet or classesSet is None:
            raise cPickle.UnpicklingError(b'Attempting to unpickle unsafe class %s' % name)
        klass = getattr(mod, name)
        return klass

    @classmethod
    def loads(cls, pickle_string):
        pickle_obj = cPickle.Unpickler(StringIO.StringIO(pickle_string))
        pickle_obj.find_global = cls.find_class
        return pickle_obj.load()
