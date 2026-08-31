from __future__ import absolute_import
from past.builtins import intern
from future.utils import iteritems
from typing import Dict, Tuple, Iterable, List, TYPE_CHECKING
from items import _xml
if TYPE_CHECKING:
    import ResMgr
STATIC_ATTR_PREFIX = b'miscAttrs/'
DYNAMIC_ATTR_PREFIX = b'dynAttrs/'
DESCR_MODIFY_ATTR_PREFIX = b'descrAttrs/'
AUTOSHOOT_ATTR_PREFIX = b'autoShootAttrs/'
ALLOWED_STATIC_ATTRS = {
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
 61, 
 62, 
 63, 
 64, 
 65, 
 66, 
 67}
ALLOWED_DYNAMIC_ATTRS = {
 11, 
 18, 
 19, 
 68, 
 69, 
 25, 
 26, 
 70, 
 27, 
 28, 
 71, 
 72, 
 33, 
 73, 
 74, 
 75, 
 76, 
 77, 
 78, 
 79, 
 39, 
 80, 
 44, 
 81, 
 82, 
 83, 
 56, 
 58, 
 59, 
 84, 
 85, 
 86, 
 87, 
 88, 
 89, 
 90, 
 50, 
 38, 
 91, 
 92, 
 93, 
 94, 
 95}
AUTOSHOOT_DYNAMIC_ATTRS = {
 b'shotIntervalMultFactor',
 b'shotDispersionPerShotFactor',
 b'maxShotDispersionFactor'}

class DescrModifyAttrsCheker(object):

    def __contains__(self, item):
        from items.descr_modify_attrs import checkAttrName
        return checkAttrName(item)


ALLOWED_ATTRS = {STATIC_ATTR_PREFIX: ALLOWED_STATIC_ATTRS, 
   DYNAMIC_ATTR_PREFIX: ALLOWED_DYNAMIC_ATTRS, 
   AUTOSHOOT_ATTR_PREFIX: AUTOSHOOT_DYNAMIC_ATTRS, 
   DESCR_MODIFY_ATTR_PREFIX: (DescrModifyAttrsCheker())}
ALLOWED_ATTR_PREFIXES = set(ALLOWED_ATTRS.keys())

class MODIFIER_TYPE:
    MUL = b'mul'
    ADD = b'add'
    SET = b'set'


class MODIFIER_FILTER_TYPE:
    COMMON = b'common'
    DEFAULT = b'default'
    SIEGE = b'siege'


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
        if opType not in (MODIFIER_TYPE.MUL, MODIFIER_TYPE.ADD, MODIFIER_TYPE.SET):
            _xml.raiseWrongXml(xmlCtx, opType, b'Unknown operation type')
        name = data.readString(b'name')
        filterName = data.readString(b'filter') or MODIFIER_FILTER_TYPE.COMMON
        attrType, attrName = _parseAttrName(name)
        names = ALLOWED_ATTRS.get(attrType)
        if opType == MODIFIER_TYPE.SET and attrType != DESCR_MODIFY_ATTR_PREFIX:
            _xml.raiseWrongXml(xmlCtx, opType, (b'Set not supported just for {}').format(attrType))
        if names is None:
            _xml.raiseWrongXml(xmlCtx, name, b'Unknown attribute type')
        if attrName not in names:
            _xml.raiseWrongXml(xmlCtx, name, b'Unknown attribute name')
        value = data.readFloat(b'value')
        modifiers.append((opType, attrType, attrName, value, filterName))

    return modifiers


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
    def collect(total, modifiersList, attrPrefix, filter=None):
        isEmpty = SingleCollectorHelper.isEmpty
        appliers = SingleCollectorHelper._APPLIERS
        for modifiers in modifiersList:
            for opType, attrType, attrName, value, modifierFilter in modifiers:
                if filter and modifierFilter not in filter:
                    continue
                if attrType != attrPrefix:
                    continue
                if isEmpty(opType, value):
                    continue
                total[attrName] = appliers[opType](total.get(attrName, 0), value)

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
    def collect(total, modifiersList, attrPrefix, filter=None):
        uniqueAttrs = {}
        mergers = AggregatedCollectorHelper._MERGERS
        for modifiers in modifiersList:
            for opType, attrType, attrName, value, modifierFilter in modifiers:
                if filter and modifierFilter not in filter:
                    continue
                if attrType != attrPrefix:
                    continue
                key = (
                 attrName, opType)
                uniqueAttrs[key] = mergers[opType](uniqueAttrs.get(key, 0.0), value)

        isEmpty = AggregatedCollectorHelper.isEmpty
        appliers = AggregatedCollectorHelper._APPLIERS
        for (attrName, opType), value in iteritems(uniqueAttrs):
            if isEmpty(opType, value):
                continue
            total[attrName] = appliers[opType](total.get(attrName, 0), value)

        return


def onCollectAttributes(total, modifiersList, attrPrefix, asAggregated, filter=None):
    if asAggregated:
        AggregatedCollectorHelper.collect(total, modifiersList, attrPrefix, filter)
    else:
        SingleCollectorHelper.collect(total, modifiersList, attrPrefix, filter)
    return
