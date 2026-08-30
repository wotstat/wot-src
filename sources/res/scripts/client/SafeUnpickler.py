from __future__ import absolute_import
import sys, copy
from io import BytesIO
from future.moves import pickle

class SafeUnpickler(object):
    PICKLE_SAFE = {b'__builtin__': {
                      0, 1, 2, 3, 
                      4}, 
       b'datetime': {
                   b'datetime'}, 
       b'_BWp': {
               b'Array', b'FixedDict'}, 
       b'Math': {
               b'Vector2', b'Vector3'}}

    def __init__(self):
        import items.components.shared_components as sc
        sc.MechanicsParams.createMechanicsParamsOrigin = copy.deepcopy
        return

    @classmethod
    def find_class(cls, module, name):
        if module not in cls.PICKLE_SAFE:
            raise pickle.UnpicklingError(b'Attempting to unpickle unsafe module %s' % module)
        __import__(module)
        mod = sys.modules[module]
        classesSet = cls.PICKLE_SAFE[module]
        if name not in classesSet:
            raise pickle.UnpicklingError(b'Attempting to unpickle unsafe class %s' % name)
        klass = getattr(mod, name)
        return klass

    @classmethod
    def loads(cls, pickle_string):
        pickle_obj = pickle.Unpickler(BytesIO(pickle_string))
        pickle_obj.find_global = cls.find_class
        return pickle_obj.load()
