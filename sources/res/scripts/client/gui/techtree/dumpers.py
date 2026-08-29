import gui
from account_helpers.AccountSettings import AccountSettings, EarlyAccess
from gui.techtree.techtree_dp import g_techTreeDP
from gui.techtree.settings import VehicleClassInfo, NODE_STATE
from helpers import i18n
__all__ = (b'ResearchItemsObjDumper', b'StubDumper')

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
        bpProgress = 0
        if node.isVehicle():
            vClass = self._vClassInfo.getInfoByTags(node.getTags())
            bpProgress = node.getBlueprintProgress()
        else:
            vClass = {b'name': (node.getTypeName())}
        data = {b'id': nodeCD, 
           b'nameString': (node.getShortUserName()), 
           b'primaryClass': vClass, 
           b'level': (node.getLevel()), 
           b'iconPath': (node.getIcon()), 
           b'smallIconPath': (node.getSmallIcon()), 
           b'state': (node.getState()), 
           b'extendedState': (node.getExtendedState()), 
           b'displayInfo': (node.getDisplayInfo()), 
           b'extraInfo': (node.getExtraInfo(rootItem)), 
           b'blueprintProgress': bpProgress}
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
        self._cache[sectionName] = map((lambda node: self._getItemData(node, rootItem)), items)
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
        paragonsPoints = node.getParagonsPoints()
        data.update({b'state': (node.getState()), 
           b'earnedXP': (node.getEarnedXP()), 
           b'unlockProps': (node.getUnlockTuple()), 
           b'buyPrice': (node.getBuyPrices()), 
           b'paragonsPoints': ((b'+{}').format(paragonsPoints) if paragonsPoints else b''), 
           b'paragonsType': (node.getParagonsType())})
        if NODE_STATE.isEarlyAccess(node.getState()):
            data.update(_getEarlyAccessVehicleData(node))
        return data


class StubDumper(_BaseDumper):

    def clear(self, full=False):
        return


def _getEarlyAccessVehicleData(node):
    isVehicleBlocked = node.getNodeCD() in g_techTreeDP.earlyAccessController.getBlockedVehicles()
    isBuyState = not g_techTreeDP.earlyAccessController.isAnyQuestAvailable()
    return {b'isFirstTimeEarlyAccessShow': (not AccountSettings.getEarlyAccess(EarlyAccess.TREE_SEEN)), 
       b'isEarlyAccessLocked': isVehicleBlocked, 
       b'isEarlyAccessPaused': (g_techTreeDP.earlyAccessController.isPaused()), 
       b'earlyAccessCurrentTokens': (g_techTreeDP.earlyAccessController.getTokensBalance()), 
       b'earlyAccessTotalTokens': (g_techTreeDP.earlyAccessController.getVehiclePrice(node.getNodeCD())), 
       b'isEarlyAccessCanBuy': (not isVehicleBlocked and isBuyState)}
