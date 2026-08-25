from __future__ import absolute_import
from future.utils import listvalues, viewitems
import ResMgr, constants
from constants import IS_CLIENT, IS_WEB, TTC_TOOLTIP_SECTIONS
from items import _xml
from items.attributes_helpers import readModifiers
from items.artefacts_helpers import VehicleFilter, readKpi
from typing import Dict, Optional, Tuple, List, Union, Set
from post_progression_common import ACTION_TYPES, FEATURES_NAMES, PAIR_TYPES, parseActionCompDescr, ID_THRESHOLD, POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES, POST_PROGRESSION_BUY_MODIFICATIONS_PRICES, POST_PROGRESSION_UNLOCK_AND_BUY_MODIFICATIONS_PRICES, ALLOWED_CURRENCIES_FOR_TREE_STEP, ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP, ALLOWED_ACTIONS_CATEGORIES, unpackActiveModifications
from soft_exception import SoftException
_XML_NAMESPACE = b'xmlns:xmlref'

def getFeatures(actionCDs, vppCache):
    result = set()
    for actionCD in actionCDs:
        actionType, itemId, _ = parseActionCompDescr(actionCD)
        if actionType == ACTION_TYPES.FEATURE:
            featureName = vppCache.features[itemId].name
            result.add(featureName)

    return result


def getActiveModifications(actionCDs, vppCache, postProgressionTree=0):
    result = unpackActiveModifications(actionCDs, vppCache, postProgressionTree)
    for actionCD in actionCDs:
        actionType, itemID, subID = parseActionCompDescr(actionCD)
        if actionType == ACTION_TYPES.MODIFICATION:
            result.append(itemID)
        elif actionType == ACTION_TYPES.PAIR_MODIFICATION:
            if subID == PAIR_TYPES.FIRST:
                result.append(vppCache.pairs[itemID].first[0])
            elif subID == PAIR_TYPES.SECOND:
                result.append(vppCache.pairs[itemID].second[0])

    return result


class SimpleItem(object):
    __slots__ = (b'id',)

    def __init__(self):
        self.id = None
        return

    def readFromXML(self, xmlCtx, section, *args):
        xmlCtx = (xmlCtx, section.name)
        self.id = _xml.readInt(xmlCtx, section, b'id', 1)
        return


class ActionItem(SimpleItem):
    __slots__ = (b'name', b'actionType', b'locName', b'imgName', b'tooltipSection', b'categories')

    def __init__(self):
        super(ActionItem, self).__init__()
        self.name = None
        self.imgName = None
        self.locName = None
        self.actionType = None
        return

    def readFromXML(self, xmlCtx, section, *args):
        super(ActionItem, self).readFromXML(xmlCtx, section, *args)
        if self.id >= ID_THRESHOLD:
            _xml.raiseWrongXml(xmlCtx, b'id', (b'id: {} must be less than {}').format(self.id, ID_THRESHOLD))
        self.name = section.name
        if IS_CLIENT or IS_WEB:
            self.imgName = _xml.readStringWithDefaultValue(xmlCtx, section, b'imgName', self.name)
            self.locName = _xml.readStringWithDefaultValue(xmlCtx, section, b'locName', self.name)
            self.tooltipSection = _xml.readStringWithDefaultValue(xmlCtx, section, b'tooltipSection', TTC_TOOLTIP_SECTIONS.EQUIPMENT)
        if IS_CLIENT or constants.IS_LOAD_GLOSSARY:
            self.categories = self._readCategories(xmlCtx, section)
        return

    @staticmethod
    def _readCategories(xmlCtx, section):
        categories = set()
        if section.has_key(b'categories'):
            categories.update(_xml.readTupleOfStrings(xmlCtx, section, b'categories'))
            for category in categories:
                if category not in ALLOWED_ACTIONS_CATEGORIES:
                    raise SoftException((b"Unknown category '{}'").format(category))

        return categories


class Modification(ActionItem):
    __slots__ = (b'kpi', b'modifiers')

    def __init__(self):
        super(Modification, self).__init__()
        self.actionType = ACTION_TYPES.MODIFICATION
        self.modifiers = None
        self.categories = set()
        self.kpi = []
        return

    def readFromXML(self, xmlCtx, section, *args):
        super(Modification, self).readFromXML(xmlCtx, section, *args)
        xmlCtx = (xmlCtx, section.name)
        self.modifiers = readModifiers(xmlCtx, section[b'modifiers'])
        if IS_CLIENT and section.has_key(b'kpi'):
            self.kpi = readKpi(xmlCtx, section[b'kpi'])
        return


class PairModification(ActionItem):
    __slots__ = (b'first', b'second')

    def __init__(self):
        super(PairModification, self).__init__()
        self.actionType = ACTION_TYPES.PAIR_MODIFICATION
        self.first = None
        self.second = None
        return

    def readFromXML(self, xmlCtx, section, *args):
        super(PairModification, self).readFromXML(xmlCtx, section, *args)
        xmlCtx = (xmlCtx, section.name)
        modifications = args[0]
        self.first = self._readModificationID(xmlCtx, section[b'first'], modifications)
        self.second = self._readModificationID(xmlCtx, section[b'second'], modifications)
        return

    @staticmethod
    def _readModificationID(xmlCtx, section, modificationIDs):
        xmlCtx = (xmlCtx, section.name)
        name = _xml.readString(xmlCtx, section, b'name')
        priceTag = _xml.readString(xmlCtx, section, b'price')
        modificationID = modificationIDs.get(name)
        if modificationID is None:
            _xml.raiseWrongXml(xmlCtx, name, b'Unknown modification')
        return (
         modificationID, priceTag)


class ProgressionFeature(ActionItem):
    __slots__ = ()

    def __init__(self):
        super(ProgressionFeature, self).__init__()
        self.actionType = ACTION_TYPES.FEATURE
        return

    def readFromXML(self, xmlCtx, section, *args):
        super(ProgressionFeature, self).readFromXML(xmlCtx, section, *args)
        if self.name not in FEATURES_NAMES:
            _xml.raiseWrongXml(xmlCtx, section.name, b'Unknown feature name')
        return


class TreeStep(SimpleItem):
    __slots__ = (b'priceTag', b'action', b'unlocks', b'requiredUnlocks', b'vehicleFilter', b'level', b'position', b'directions', b'type', b'unlockStrategy')

    def __init__(self):
        super(TreeStep, self).__init__()
        self.priceTag = None
        self.action = None
        self.unlocks = None
        self.requiredUnlocks = tuple()
        self.vehicleFilter = None
        self.level = None
        self.position = None
        self.directions = None
        self.type = None
        self.unlockStrategy = all
        return

    def readFromXML(self, xmlCtx, section, *args):
        super(TreeStep, self).readFromXML(xmlCtx, section, *args)
        xmlCtx = (xmlCtx, section.name)
        self.priceTag = _xml.readString(xmlCtx, section, b'price')
        self.action = self._readAction(xmlCtx, section[b'action'], args[0])
        self.unlocks = _xml.readTupleOfInts(xmlCtx, section, b'unlocks') if section.has_key(b'unlocks') else tuple()
        self.level = _xml.readInt(xmlCtx, section, b'level')
        if section.has_key(b'vehicleFilter'):
            self.vehicleFilter = VehicleFilter.readVehicleFilter((xmlCtx, b'vehicleFilter'), section[b'vehicleFilter'])
        else:
            self.vehicleFilter = None
        if section.has_key(b'unlockStrategyAny'):
            self.unlockStrategy = any
        if IS_CLIENT or IS_WEB or constants.IS_LOAD_GLOSSARY:
            if section.has_key(b'position'):
                self.position = _xml.readTupleOfInts(xmlCtx, section, b'position')
            if section.has_key(b'directions'):
                self.directions = _xml.readTupleOfStrings(xmlCtx, section, b'directions')
            if section.has_key(b'type'):
                self.type = _xml.readString(xmlCtx, section, b'type')
        return

    def addRequiredUnlock(self, stepID):
        self.requiredUnlocks = self.requiredUnlocks + (stepID,)
        return

    @staticmethod
    def _readAction(xmlCtx, section, actionResolvers):
        if section is None:
            _xml.raiseWrongXml(xmlCtx, None, b'Action not found')
        xmlCtx = (
         xmlCtx, section.name)
        actionType = _xml.readString(xmlCtx, section, b'type')
        actionValue = _xml.readString(xmlCtx, section, b'value')
        resolver = actionResolvers.get(actionType)
        if resolver is None:
            _xml.raiseWrongXml(xmlCtx, actionType, b'Unknown action specified')
        typeID, valueID = resolver(actionValue)
        if valueID is None:
            _xml.raiseWrongXml(xmlCtx, actionValue, b'Unknown value for specified action type')
        return (
         typeID, valueID)


class ProgressionTree(SimpleItem):
    __slots__ = (b'steps', b'rootStep', b'ppBattleIndex')

    def __init__(self):
        super(ProgressionTree, self).__init__()
        self.steps = None
        self.rootStep = None
        self.ppBattleIndex = None
        return

    def readFromXML(self, xmlCtx, section, *args):
        super(ProgressionTree, self).readFromXML(xmlCtx, section, *args)
        xmlCtx = (xmlCtx, section.name)
        if not section.has_key(b'steps'):
            _xml.raiseWrongXml(xmlCtx, None, b'Steps not found')
        features, modifications, pairModifications = args
        _ACTION_RESOLVERS = {b'modification': (lambda x: (
                           ACTION_TYPES.MODIFICATION, modifications.get(x))), 
           b'pair_modification': (lambda x: (
                                ACTION_TYPES.PAIR_MODIFICATION, pairModifications.get(x))), 
           b'feature': (lambda x: (
                      ACTION_TYPES.FEATURE, features.get(x)))}
        steps = {}
        for name, data in section[b'steps'].items():
            if name != b'step':
                _xml.raiseWrongXml(xmlCtx, name, b'Unexpected subsection')
            step = TreeStep()
            step.readFromXML(xmlCtx, data, _ACTION_RESOLVERS)
            steps[step.id] = step

        for stepID, step in viewitems(steps):
            for unlockID in step.unlocks:
                steps[unlockID].addRequiredUnlock(stepID)

        self.steps = steps
        self.rootStep = _xml.readInt(xmlCtx, section, b'rootStep')
        if self.rootStep not in self.steps or steps[self.rootStep].requiredUnlocks:
            _xml.raiseWrongXml(xmlCtx, None, (b'Invalid root step id {}').format(self.rootStep))
        self._validateLevels(xmlCtx)
        self.ppBattleIndex = listvalues(steps)
        self.ppBattleIndex.sort(key=(lambda step: step.id))
        return

    def _validateLevels(self, xmlCtx):
        steps = self.steps
        for stepID, step in viewitems(steps):
            for unlockID in step.unlocks:
                unlockerLevel = step.level
                unlocksLevel = steps[unlockID].level
                if unlocksLevel < unlockerLevel:
                    _xml.raiseWrongXml(xmlCtx, None, b'Invalid step level for stepID=%s, unlocksID=%s, unlockerLevel=%s, unlocksLevel=%s' % (
                     stepID, unlockID, unlockerLevel, unlocksLevel))

        return


class PostProgressionCache(object):
    __slots__ = (b'_features', b'_featureIDs', b'_modifications', b'_modificationIDs', b'_pairs', b'_pairIDs', b'_trees', b'_treeIDs', b'_prices', b'actionToStorage')

    def __init__(self, featuresXML, modificationsXML, pairsXML, treesXML, pricesXML):
        self._features, self._featureIDs = self._readItems(featuresXML, ProgressionFeature)
        self._modifications, self._modificationIDs = self._readItems(modificationsXML, Modification)
        self._pairs, self._pairIDs = self._readItems(pairsXML, PairModification, self._modificationIDs)
        self._trees, self._treeIDs = self._readItems(treesXML, ProgressionTree, self.featureIDs, self.modificationIDs, self.pairIDs)
        self._prices = self._readPrices(pricesXML)
        self.actionToStorage = {(ACTION_TYPES.FEATURE): (self._features), 
           (ACTION_TYPES.MODIFICATION): (self._modifications), 
           (ACTION_TYPES.PAIR_MODIFICATION): (self._pairs)}
        return

    @property
    def features(self):
        return self._features

    @property
    def featureIDs(self):
        return self._featureIDs

    @property
    def modifications(self):
        return self._modifications

    @property
    def modificationIDs(self):
        return self._modificationIDs

    @property
    def pairs(self):
        return self._pairs

    @property
    def pairIDs(self):
        return self._pairIDs

    @property
    def trees(self):
        return self._trees

    @property
    def treeIDs(self):
        return self._treeIDs

    @property
    def prices(self):
        return self._prices

    def getAction(self, actionType, actionID):
        return self.actionToStorage[actionType][actionID]

    def getChildActions(self, parent):
        return [(self.modifications[modificationID], priceTag) for modificationID, priceTag in (
         parent.first, parent.second)]

    def getModificationByName(self, name):
        if name in self._modificationIDs:
            return self._modifications[self._modificationIDs[name]]
        else:
            return

    def _readItems(self, xmlPath, classObj, *args):
        xmlCtx = (
         None, xmlPath)
        section = ResMgr.openSection(xmlPath)
        if section is None:
            _xml.raiseWrongXml(None, xmlPath, b'Unable to open or read')
        ids = {}
        names = {}
        for name, data in section.items():
            if name == _XML_NAMESPACE:
                continue
            item = classObj()
            item.readFromXML(xmlCtx, data, *args)
            if item.id in ids:
                _xml.raiseWrongXml(xmlCtx, name, b'Duplicate item id')
            if name in names:
                _xml.raiseWrongXml(xmlCtx, name, b'Duplicate item name')
            names[name] = item.id
            ids[item.id] = item

        ResMgr.purge(xmlPath)
        return (ids, names)

    @staticmethod
    def _readPrices(xmlPath):
        xmlCtx = (None, xmlPath)
        section = ResMgr.openSection(xmlPath)
        if section is None:
            _xml.raiseWrongXml(None, xmlPath, b'Unable to open or read')
        prices = {}
        for name, data in section.items():
            if name not in POST_PROGRESSION_UNLOCK_AND_BUY_MODIFICATIONS_PRICES:
                _xml.raiseWrongXml(xmlCtx, name, b'Incorrect price tag <%s>' % name)
            ctx = (
             xmlCtx, name)
            prices[name] = {}
            for sname, _ in data.items():
                _, level = str(sname).split(b'_', 1)
                prices[name][int(level)] = _xml.readPostProgressionPrice(ctx, data, sname)

            if name in POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES:
                for _, value in viewitems(prices[name]):
                    if not ALLOWED_CURRENCIES_FOR_TREE_STEP.issuperset(value.keys()):
                        raise SoftException((b'Wrong currency for section: {}, path: {}').format(name, xmlPath))

            if name in POST_PROGRESSION_BUY_MODIFICATIONS_PRICES:
                for _, value in viewitems(prices[name]):
                    if not ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP.issuperset(value.keys()):
                        raise SoftException((b'Wrong currency for section: {}, path: {}').format(name, xmlPath))

        return prices
