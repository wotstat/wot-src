from __future__ import absolute_import
import gui
from gui.Scaleform.daapi.view.lobby.techtree.settings import SelectedNation
from gui.Scaleform.daapi.view.lobby.techtree.settings import VehicleClassInfo
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.Scaleform.daapi.view.lobby.techtree.event_helpers import TechTreeFormatters
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS
from helpers import i18n
__all__ = (b'ResearchItemsObjDumper', b'NationObjDumper')

class _BaseDumper(object):
    __slots__ = (b'_cache', b'_vClassInfo')

    def __init__(self, cache=None):
        super(_BaseDumper, self).__init__()
        self._cache = cache
        self._vClassInfo = VehicleClassInfo()
        return

    def clear(self, full=False):
        raise NotImplementedError
        return

    def dump(self, data):
        return {}


class ResearchBaseDumper(_BaseDumper):

    def __init__(self, cache=None):
        super(ResearchBaseDumper, self).__init__(cache or self._getDefaultCacheObj())
        return

    def clear(self, full=False):
        nodes = self._cache[b'nodes']
        while nodes:
            nodes.pop().clear()

        if full:
            self._vClassInfo.clear()
        return

    def invalidateCachedItemData(self, sectionName, idx, node, rootItem):
        newItem = self._getItemData(node, rootItem)
        self._cache[sectionName][idx] = newItem
        return newItem

    def dump(self, data):
        self.clear()
        rootItem = data.getRootItem()
        cachedNodes = self._cache[b'nodes']
        for node in data.getNodes():
            renderer = node.getDisplayInfo().get(b'renderer')
            if renderer and renderer != b'vehicle':
                cachedNodes.append(self._getItemData(node, rootItem))

        return self._cache

    def _getDefaultCacheObj(self):
        return {b'nodes': []}

    def _getItemData(self, node, rootItem):
        nodeCD = node.getNodeCD()
        if node.isVehicle():
            vClass = self._vClassInfo.getInfoByTags(node.getTags())
        else:
            vClass = {b'name': (node.getTypeName())}
        data = {b'id': nodeCD, 
           b'nameString': (node.getShortUserName()), 
           b'primaryClass': vClass, 
           b'level': (node.getLevel()), 
           b'iconPath': (node.getIcon()), 
           b'smallIconPath': (node.getSmallIcon()), 
           b'state': (node.getState()), 
           b'displayInfo': (node.getDisplayInfo()), 
           b'extraInfo': (node.getExtraInfo(rootItem))}
        return data


class ResearchItemsObjDumper(ResearchBaseDumper):

    def clear(self, full=False):
        nodes = self._cache[b'top']
        while nodes:
            nodes.pop().clear()

        return

    def dump(self, data):
        self.clear()
        self._fillCacheSection(b'nodes', data, data.getNodes())
        self._fillCacheSection(b'top', data, data.getTopLevel())
        return self._cache

    def _fillCacheSection(self, sectionName, data, items):
        rootItem = data.getRootItem()
        self._cache[sectionName] = [self._getItemData(node, rootItem) for node in items]
        return

    def _getDefaultCacheObj(self):
        defCache = super(ResearchItemsObjDumper, self)._getDefaultCacheObj()
        defCache[b'top'] = []
        return defCache

    def _getExtraInfo(self, data):
        item = data.getRootItem()
        result = {}
        if item.isPremium:
            if item.isSpecial:
                tag = b'special'
            else:
                tag = b'premium'
            typeString = i18n.makeString((b'#tooltips:tankCaruselTooltip/vehicleType/elite/{0:>s}').format(item.type))
            result = {b'type': (item.type), 
               b'title': (gui.makeHtmlString(b'html_templates:lobby/research', b'premium_title', ctx={b'name': (item.userName), 
                          b'type': typeString, 
                          b'level': (i18n.makeString((b'#tooltips:level/{0:d}').format(item.level)))})), 
               b'benefitsHead': (i18n.makeString((b'#menu:research/{0:>s}/benefits/head').format(tag))), 
               b'benefitsList': (gui.makeHtmlString(b'html_templates:lobby/research', (b'{0:>s}_benefits').format(tag), ctx={b'description': (item.fullDescription)})), 
               b'isPremiumIgr': (item.isPremiumIGR)}
        return result

    def _getItemData(self, node, rootItem):
        data = super(ResearchItemsObjDumper, self)._getItemData(node, rootItem)
        data.update({b'state': (node.getState()), 
           b'earnedXP': (node.getEarnedXP()), 
           b'unlockProps': (node.getUnlockTuple()), 
           b'buyPrice': (node.getBuyPrices())})
        return data


class NationObjDumper(_BaseDumper):
    DEBUG_ITEMS = (18689, 5393, 6417, 7217)

    def __init__(self, cache=None):
        if cache is None:
            cache = {b'nodes': [], b'displaySettings': {}, b'gridSettings': {}, b'premiumSettings': {}, b'scrollIndex': (-1)}
        super(NationObjDumper, self).__init__(cache)
        return

    def clear(self, full=False):
        nodes = self._cache[b'nodes']
        while nodes:
            nodes.pop().clear()

        if full:
            self._vClassInfo.clear()
            self._cache[b'displaySettings'].clear()
            self._cache[b'gridSettings'].clear()
            self._cache[b'premiumSettings'].clear()
        return

    def dump(self, data):
        self.clear()
        self._cache[b'nodes'] = [self._getVehicleData(node) for node in data.getNodes()]
        self._cache[b'scrollIndex'] = data._scrollIndex
        self._cache[b'displaySettings'].update(g_techTreeDP.getDisplaySettings(SelectedNation.getIndex()))
        self._cache[b'gridSettings'].update(g_techTreeDP.getGridSettings(SelectedNation.getIndex()))
        self._cache[b'premiumSettings'].update(g_techTreeDP.getPremiumGridSettings(SelectedNation.getIndex()))
        return self._cache

    def _getVehicleData(self, node):
        tags = node.getTags()
        blueprints = node.getBpfProps()
        return {b'id': (node.getNodeCD()), 
           b'state': (node.getState()), 
           b'type': (node.getTypeName()), 
           b'nameString': (node.getShortUserName()), 
           b'primaryClass': (self._vClassInfo.getInfoByTags(tags)), 
           b'level': (node.getLevel()), 
           b'smallIconPath': (node.getSmallIcon()), 
           b'earnedXP': (node.getEarnedXP()), 
           b'displayInfo': (node.getDisplayInfo()), 
           b'unlockProps': (node.getUnlockTuple()), 
           b'isRemovable': (node.isRented()), 
           b'vehCompareTreeNodeData': (node.getCompareData()), 
           b'blueprintLabel': (node.getBlueprintLabel()), 
           b'blueprintProgress': (node.getBlueprintProgress()), 
           b'blueprintCanConvert': (blueprints.canConvert if blueprints is not None else False), 
           b'buyPrice': (node.getBuyPrices()), 
           b'isNationChangeAvailable': (node.hasItemNationGroup()), 
           b'isTopActionNode': (g_techTreeDP.isActionEndNode(node)), 
           b'actionMessage': (self.__getTooltipString(node)), 
           b'isPromoted': (node.getLevel() > 10)}

    def __getTooltipString(self, node):
        isActionNode = node.getState() & NODE_STATE_FLAGS.HAS_TECH_TREE_EVENT > 0
        if not isActionNode:
            return b''
        if g_techTreeDP.isActionStartNode(node):
            eventsListener = g_techTreeDP.techTreeEventsListener
            actionID = eventsListener.getActiveAction(vehicleCD=node.getNodeCD(), nationID=node.getNationID())
            return TechTreeFormatters.getActionInfoStr(eventsListener.getUserName(actionID), eventsListener.getFinishTime(actionID))
        return b''
