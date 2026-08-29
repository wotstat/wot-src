from abc import ABCMeta, abstractproperty
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import List, Tuple

class Modifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, value):
        self.value = value
        return

    nameValueReplay = abstractproperty((lambda *_: None))
    operand = abstractproperty((lambda *_: None))
    resultName = abstractproperty((lambda *_: None))
    resultFactor = abstractproperty((lambda *_: None))


class Credits(Modifier):
    nameValueReplay = property((lambda self: b'creditsReplay'))
    operand = property((lambda self: b'subtotalCredits'))
    resultName = property((lambda self: b'directivesCredits'))
    resultFactor = property((lambda self: b'directivesCreditsFactor100'))


class Xp(Modifier):
    nameValueReplay = property((lambda self: b'xpReplay'))
    operand = property((lambda self: b'subtotalXP'))
    resultName = property((lambda self: b'directivesXP'))
    resultFactor = property((lambda self: b'directivesXPFactor100'))


class CrewXp(Modifier):
    nameValueReplay = property((lambda self: b'tmenXPReplay'))
    operand = property((lambda self: b'subtotalTMenXP'))
    resultName = property((lambda self: b'directivesTMenXP'))
    resultFactor = property((lambda self: b'directivesTMenXPFactor100'))


class FreeXp(Modifier):
    nameValueReplay = property((lambda self: b'freeXPReplay'))
    operand = property((lambda self: b'subtotalFreeXP'))
    resultName = property((lambda self: b'directivesFreeXP'))
    resultFactor = property((lambda self: b'directivesFreeXPFactor100'))


def getSubclasses(cls):
    return {subclass.__name__: subclass for subclass in cls.__subclasses__()}


class Operation(object):

    def __init__(self, operationType, modifiers):
        self.operationType = operationType
        self.modifierList = []
        modifiersClass = getSubclasses(Modifier)
        for m, v in modifiers:
            cls = modifiersClass.get(m)
            if cls:
                modifier = cls(v)
                self.modifierList.append(modifier)

        return
