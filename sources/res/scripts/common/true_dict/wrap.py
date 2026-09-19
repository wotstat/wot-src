from __future__ import absolute_import
from typing import Any
from .core import TrueDict
FixedDict = Any

class MemberProxy(object):

    def __init__(self, memberName):
        self.memberName = memberName
        return

    def __get__(self, inst, owner):
        return inst.fixedDict[self.memberName]

    def __set__(self, inst, value):
        inst.fixedDict[self.memberName] = value
        return

    def __delete__(self, inst):
        raise NotImplementedError(self.memberName)
        return


class TrueDictWrapped(TrueDict):
    keysProxy = MemberProxy(b'keys')
    valuesProxy = MemberProxy(b'values')

    def __init__(self, fixedDict):
        self.fixedDict = fixedDict
        super(TrueDictWrapped, self).__init__(self.keysProxy, self.valuesProxy)
        return


class TrueDictConverter(object):

    def createObjFromDict(self, fixedDict):
        return TrueDictWrapped(fixedDict)

    def getDictFromObj(self, obj):
        if isinstance(obj, TrueDictWrapped):
            return obj.fixedDict
        if isinstance(obj, TrueDict):
            return {b'keys': (list(obj.iter_keys())), b'values': (list(obj.iter_values()))}
        if isinstance(obj, dict):
            if set(obj.keys()) == {b'keys', b'values'}:
                return obj
        raise TypeError(b'TrueDictConverter: cannot convert %r to a FIXED_DICT' % (type(obj),))
        return

    def isSameType(self, obj):
        if isinstance(obj, TrueDict):
            return True
        if isinstance(obj, dict):
            return set(obj.keys()) == {b'keys', b'values'}
        return False


instance = TrueDictConverter()
