from items._xml import raiseWrongXml, readFloat
from typing import Dict, Tuple, Iterable, List, TYPE_CHECKING
if TYPE_CHECKING:
    import ResMgr
STATIC_ATTR_PREFIX = b'miscAttrs/'
DYNAMIC_ATTR_PREFIX = b'dynAttrs/'
AUTOSHOOT_ATTR_PREFIX = b'autoShootAttrs/'
ALLOWED_STATIC_ATTRS = {
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
 32, 
 33, 
 34, 
 35, 
 36, 
 37, 
 38, 
 39, 
 40, 
 41, 
 42, 
 43, 
 44, 
 45, 
 46, 
 47, 
 48, 
 49, 
 50, 
 51, 
 52, 
 53, 
 54, 
 55, 
 56, 
 57, 
 58, 
 59, 
 60, 
 61}
ALLOWED_DYNAMIC_ATTRS = {
 7, 
 62, 
 63, 
 64, 
 65, 
 14, 
 15, 
 66, 
 21, 
 22, 
 67, 
 23, 
 24, 
 68, 
 69, 
 29, 
 70, 
 71, 
 72, 
 73, 
 74, 
 75, 
 76, 
 34, 
 35, 
 77, 
 78, 
 40, 
 46, 
 79, 
 80, 
 81, 
 52, 
 54, 
 55, 
 82, 
 83, 
 84, 
 85, 
 86, 
 87, 
 88, 
 60, 
 61, 
 89, 
 90, 
 91}
AUTOSHOOT_DYNAMIC_ATTRS = {
 b'rate/multiplier',
 b'shotDispersionPerSecFactor',
 b'maxShotDispersionFactor'}
ALLOWED_ATTRS = {STATIC_ATTR_PREFIX: ALLOWED_STATIC_ATTRS, 
   DYNAMIC_ATTR_PREFIX: ALLOWED_DYNAMIC_ATTRS, 
   AUTOSHOOT_ATTR_PREFIX: AUTOSHOOT_DYNAMIC_ATTRS}
ALLOWED_ATTR_PREFIXES = set(ALLOWED_ATTRS.keys())

class MODIFIER_TYPE:
    MUL = b'mul'
    ADD = b'add'


def _parseAttrName(complexName):
    for attrPrefix in ALLOWED_ATTR_PREFIXES:
        if complexName.startswith(attrPrefix):
            return (attrPrefix, intern(complexName[len(attrPrefix):]))

    return (None, None)


def readModifiers(xmlCtx, section):
    xmlCtx = (
     xmlCtx, section.name)
    modifiers = []
    for opType, data in section.items():
        name = data.readString(b'name')
        value = readFloat(xmlCtx, data, b'value')
        modifier = createModifier(xmlCtx, opType, name, value)
        if modifier:
            modifiers.append(modifier)

    return modifiers


def createModifier(ctx, opType, name, value):
    if opType not in (MODIFIER_TYPE.MUL, MODIFIER_TYPE.ADD):
        return raiseWrongXml(ctx, opType, b'Unknown operation type')
    attrType, attrName = _parseAttrName(name)
    if attrType not in ALLOWED_ATTRS:
        return raiseWrongXml(ctx, name, b'Unknown attribute type')
    if attrName not in ALLOWED_ATTRS.get(attrType):
        return raiseWrongXml(ctx, name, b'Unknown attribute name')
    return (opType, attrType, attrName, value)


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class SingleCollectorHelper(object):
    _EMPTY_CHECKER = {(MODIFIER_TYPE.ADD): (lambda value: isclose(value, 0.0)), 
       (MODIFIER_TYPE.MUL): (lambda value: isclose(value, 1.0))}
    _APPLIERS = {(MODIFIER_TYPE.ADD): (lambda currentValue, addValue: currentValue + addValue), 
       (MODIFIER_TYPE.MUL): (lambda currentValue, addValue: currentValue * addValue)}

    @staticmethod
    def isEmpty(opType, value):
        return SingleCollectorHelper._EMPTY_CHECKER[opType](value)

    @staticmethod
    def collect(total, modifiersList, attrPrefix):
        isEmpty = SingleCollectorHelper.isEmpty
        appliers = SingleCollectorHelper._APPLIERS
        for modifiers in modifiersList:
            for opType, attrType, attrName, value in modifiers:
                if attrType != attrPrefix:
                    continue
                if isEmpty(opType, value):
                    continue
                total[attrName] = appliers[opType](total[attrName], value)

        return


class AggregatedCollectorHelper(object):
    _EMPTY_CHECKER = {(MODIFIER_TYPE.ADD): (lambda value: isclose(value, 0.0)), 
       (MODIFIER_TYPE.MUL): (lambda value: isclose(value, 0.0))}
    _MERGERS = {(MODIFIER_TYPE.ADD): (lambda currentValue, addValue: currentValue + addValue), 
       (MODIFIER_TYPE.MUL): (lambda currentValue, addValue: currentValue + (addValue - 1))}
    _APPLIERS = {(MODIFIER_TYPE.ADD): (lambda currentValue, addValue: currentValue + addValue), 
       (MODIFIER_TYPE.MUL): (lambda currentValue, addValue: currentValue * (addValue + 1))}

    @staticmethod
    def isEmpty(opType, value):
        return AggregatedCollectorHelper._EMPTY_CHECKER[opType](value)

    @staticmethod
    def collect(total, modifiersList, attrPrefix):
        uniqueAttrs = dict()
        mergers = AggregatedCollectorHelper._MERGERS
        for modifiers in modifiersList:
            for opType, attrType, attrName, value in modifiers:
                if attrType != attrPrefix:
                    continue
                key = (
                 attrName, opType)
                uniqueAttrs[key] = mergers[opType](uniqueAttrs.get(key, 0.0), value)

        isEmpty = AggregatedCollectorHelper.isEmpty
        appliers = AggregatedCollectorHelper._APPLIERS
        for (attrName, opType), value in uniqueAttrs.iteritems():
            if isEmpty(opType, value):
                continue
            total[attrName] = appliers[opType](total[attrName], value)

        return


def onCollectAttributes(total, modifiersList, attrPrefix, asAggregated):
    if asAggregated:
        AggregatedCollectorHelper.collect(total, modifiersList, attrPrefix)
    else:
        SingleCollectorHelper.collect(total, modifiersList, attrPrefix)
    return
