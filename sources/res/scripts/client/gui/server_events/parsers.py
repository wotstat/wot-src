import typing, weakref
from gui.server_events import formatters, conditions
from gui.server_events.conditions import Cumulativable, CumulativeResult, _ConditionsGroup
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
from shared_utils import first
if typing.TYPE_CHECKING:
    from typing import Optional, Tuple, Union
    from gui.shared.gui_items.Vehicle import Vehicle

class ConditionsParser(object):
    LOGICAL_OPS = {b'and': (conditions.AndGroup), 
       b'or': (conditions.OrGroup)}
    NEGATIVE_OP = b'not'

    def __init__(self, section, rootName=b''):
        self._section = section
        self._rootNode = None
        self.__rootName = rootName
        return

    def getConditions(self):
        if self._rootNode is None:
            self._rootNode = self._parse()
        return self._rootNode

    def getSection(self):
        return self._section

    def clearCache(self):
        self._rootNode = None
        return

    def forEachNodeInTree(self, handler):
        self.__forEachNode(self.getConditions(), handler)
        return

    def _handleCondition(self, name, data, uniqueName, group):
        return

    def _parse(self):
        if len(self._section) <= 0:
            return conditions.AndGroup()
        startParsingPoint = self._section
        unionOps = set(self.LOGICAL_OPS.keys()).intersection(dict(self._section).keys())
        if unionOps:
            rootGroup = self.LOGICAL_OPS[unionOps.pop()]()
            startParsingPoint = self._section[0][1]
        else:
            rootGroup = conditions.AndGroup()
        self._parseNode(self.__rootName, startParsingPoint, rootGroup)
        return rootGroup

    def _parseNode(self, uniquePath, section, group, isNegative=False):
        for idx, (nodeName, nodeData) in enumerate(section):
            newNode = None
            uniqueName = formatters.makeUniquePath(uniquePath, nodeName)
            if nodeName in self.LOGICAL_OPS:
                newNode = self.LOGICAL_OPS[nodeName](isNegative)
                self._parseNode(uniqueName, nodeData, newNode)
            elif nodeName == self.NEGATIVE_OP:
                self._parseNode(uniqueName, nodeData, group, True)
            elif group.find(nodeName) is not None:
                uniqueName = b'%s%d' % (uniqueName, idx)
            newNode = self._handleCondition(nodeName, nodeData, uniqueName, group)
            if newNode is not None and isNegative:
                newNode.negate()
            if newNode is not None:
                group.add(newNode)

        return

    def __forEachNode(self, group, handler):
        if group.isEmpty() is None:
            return
        else:
            for node in group.items:
                if isinstance(node, conditions._ConditionsGroup):
                    self.__forEachNode(node, handler)
                else:
                    handler(node)

            return


class AccountRequirements(ConditionsParser):

    def __init__(self, section):
        super(AccountRequirements, self).__init__(section, rootName=b'account')
        self._hasIgrCondition = False
        return

    def clearItemsCache(self):
        self.forEachNodeInTree((lambda node: node.clearItemsCache()))
        return

    def _handleCondition(self, name, data, uniqueName, group):
        if name == b'token':
            return conditions.Token(uniqueName, data)
        if name == b'premium':
            return conditions.PremiumAccount(uniqueName, data)
        if name == b'premiumPlus':
            return conditions.PremiumPlusAccount(uniqueName, data)
        if name == b'wotPlus':
            return conditions.WotPlus(uniqueName, data)
        if name == b'inClan':
            return conditions.InClan(uniqueName, data)
        if name == b'igrType':
            self._hasIgrCondition = True
            return conditions.IGR(uniqueName, data)
        if name == b'GR':
            return conditions.GlobalRating(uniqueName, data)
        if name == b'dossier':
            return conditions.AccountDossierValue(uniqueName, data)
        if name == b'vehiclesUnlocked':
            return conditions.VehiclesUnlocked(uniqueName, data)
        if name == b'vehiclesOwned':
            return conditions.VehiclesOwned(uniqueName, data)
        if name == b'activeProgression':
            return conditions.VersusAIProgression(uniqueName, data)
        if name == b'quest':
            return conditions.QuestCondition(uniqueName, data)
        return

    def isAvailable(self):
        conds = self.getConditions()
        if not conds.isEmpty():
            return conds.isAvailable()
        return True

    def hasIGRCondition(self):
        self.getConditions()
        return self._hasIgrCondition

    def getTokens(self):
        results = []

        def handler(node):
            if node.getName() == b'token':
                results.append(node)
            return

        self.forEachNodeInTree(handler)
        return results


class TokenQuestAccountRequirements(AccountRequirements):

    def _handleCondition(self, name, data, uniqueName, group):
        if name == b'token':
            return conditions.TokenQuestToken(uniqueName, data)
        return super(TokenQuestAccountRequirements, self)._handleCondition(name, data, uniqueName, group)


class VehicleRequirements(ConditionsParser):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, section):
        super(VehicleRequirements, self).__init__(section, rootName=b'vehicle')
        self._suitableVehicles = None
        return

    def clearItemsCache(self):
        self._suitableVehicles = None
        self.forEachNodeInTree((lambda node: node.clearItemsCache()))
        return

    def isAvailable(self, vehicle):
        return self.getConditions().isAvailable(vehicle)

    def isAnyVehicleAcceptable(self):
        results = set()

        def handler(node):
            if node.getName() == b'vehicleDescr':
                results.add(node.isAnyVehicleAcceptable())
            elif node.getName() in (b'premiumVehicle', b'hasReceivedMultipliedXP'):
                results.add(False)
            return

        self.forEachNodeInTree(handler)
        return False not in results

    def getAvailableVehiclesCD(self):
        vehicleDescr = self.getConditions().find(b'vehicleDescr')
        vehicleTypes = first(vehicleDescr.parseFilters())
        if vehicleTypes:
            return map(int, vehicleTypes)
        else:
            return

    def getSuitableVehicles(self):
        if self._suitableVehicles is None:
            invVehs = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY)
            isAvailable = self.isAvailable
            self._suitableVehicles = tuple([vehicleItem.intCD for vehicleItem in invVehs.itervalues() if isAvailable(vehicleItem)])
        return self._suitableVehicles

    def _handleCondition(self, name, data, uniqueName, group):
        if name == b'premium':
            return conditions.PremiumVehicle(uniqueName, data)
        if name == b'hasReceivedMultipliedXP':
            return conditions.XPMultipliedVehicle(uniqueName, data)
        if name == b'vehicleDescr':
            return conditions.VehicleDescr(uniqueName, data)
        if name == b'installedModules':
            return conditions.InstalledModulesOnVehicle(uniqueName, data)
        if name == b'correspondedCamouflage':
            return conditions.CorrespondedCamouflage(uniqueName, data)
        if name == b'customization':
            return conditions.Customization(uniqueName, data)
        return


class PreBattleConditions(ConditionsParser):

    def __init__(self, section):
        super(PreBattleConditions, self).__init__(section, rootName=b'preBattle')
        return

    def _handleCondition(self, name, data, uniqueName, group):
        if name == b'unit':
            tmpGroup = self.LOGICAL_OPS[b'and']()
            self._parseNode(uniqueName, data, tmpGroup)
            for element in tmpGroup.items:
                group.add(element)

        elif name == b'bonusTypes':
            return conditions.BattleBonusType(uniqueName, data)
        if name == b'isSquad':
            return conditions.BattleSquad(uniqueName, data)
        if name == b'clanMembership':
            return conditions.BattleClanMembership(uniqueName, data, self)
        if name == b'mapCamouflageKind':
            return conditions.BattleCamouflage(uniqueName, data)
        if name == b'geometryNames':
            return conditions.BattleMap(uniqueName, data)
        return


class PostBattleConditions(ConditionsParser):

    def __init__(self, section, preBattleCond):
        self.__preBattleCond = weakref.proxy(preBattleCond)
        super(PostBattleConditions, self).__init__(section, rootName=b'postBattle')
        return

    def _handleCondition(self, name, data, uniqueName, group):
        if name == b'win':
            return conditions.Win(uniqueName, data)
        if name == b'isAlive':
            return conditions.Survive(uniqueName, data)
        if name == b'achievements':
            return conditions.Achievements(uniqueName, data)
        if name == b'vehicleKills':
            return conditions.VehicleKills(uniqueName, data)
        if name == b'vehicleDamage':
            return conditions.VehicleDamage(uniqueName, data)
        if name == b'vehicleStun':
            return conditions.VehicleStun(uniqueName, data)
        if name == b'clanKills':
            return conditions.ClanKills(uniqueName, data)
        if name == b'results':
            return conditions.BattleResults(uniqueName, data)
        if name == b'crits':
            return conditions.CritsGroup(uniqueName, data)
        if name == b'unit':
            return conditions.UnitResults(uniqueName, data, self.__preBattleCond)
        if name == b'multiStunEvent':
            return conditions.MultiStunEvent(uniqueName, data)
        if name == b'isFirstBlood':
            return conditions.FirstBlood(uniqueName, data)
        return


class BonusConditions(ConditionsParser):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, section, progress, preBattleCond):
        self.__preBattleCond = weakref.proxy(preBattleCond)
        super(BonusConditions, self).__init__(section, rootName=b'bonusBattle')
        dictSec = dict(section)
        self._isDaily = conditions._getNodeValue(dictSec, b'daily', False)
        self._isWeekly = conditions._getNodeValue(dictSec, b'weekly', False)
        self._bonusLimit = conditions._getNodeValue(dictSec, b'bonusLimit')
        self._groupBy = None
        if b'groupBy' in dictSec:
            self._groupBy = conditions._getNodeValue(dict(dictSec[b'groupBy']), b'groupName')
        self._inRow = conditions._getNodeValue(dictSec, b'inrow', False)
        self._progress = progress
        return

    def isDaily(self):
        return self._isDaily

    def isWeekly(self):
        return self._isWeekly

    def getBonusLimit(self):
        return self._bonusLimit

    def getGroupByValue(self):
        return self._groupBy

    def isInRow(self):
        return self._inRow

    def getProgress(self):
        return self._progress

    def _handleCondition(self, name, data, uniqueName, group):
        if name == b'battles':
            return conditions.BattlesCount(uniqueName, data, self, preBattleCond=self.__preBattleCond)
        if name == b'vehicleKills':
            return conditions.VehicleKillsCumulative(uniqueName, data, self)
        if name == b'vehicleDamage':
            return conditions.VehicleDamageCumulative(uniqueName, data, self)
        if name == b'vehicleStun':
            return conditions.VehicleStunCumulative(uniqueName, data, self)
        if name == b'cumulativeExt' or name == b'cumulative' or name == b'unit':
            unitFlag = bool(name == b'unit')
            result = []
            if unitFlag:
                if b'cumulative' in dict(data):
                    conditionKey = b'cumulative'
                else:
                    conditionKey = b'cumulativeExt'
                currentCollection = enumerate(dict(data)[conditionKey])
            else:
                currentCollection = enumerate(data)
            for idx, element in currentCollection:
                _, elements = element
                description = tuple()
                for elementName, value in elements:
                    if elementName == b'description':
                        description = (
                         (
                          elementName, value),)
                    elif elementName == b'key':
                        key = value[0][1]
                    elif elementName in (b'equal', b'greater', b'greaterOrEqual'):
                        elementValue = value[0][1]
                    else:
                        raise SoftException(b'Incorrect tag in cumulative or cummulativeExt (%s)' % elementName)

                element = (
                 b'value', (key, elementValue))
                if unitFlag:
                    result.append(conditions.CumulativeResult(b'%s%d' % (uniqueName, idx), (element,) + description, self, isUnit=True, preBattleCond=self.__preBattleCond))
                else:
                    result.append(conditions.CumulativeResult(b'%s%d' % (uniqueName, idx), (element,) + description, self))

            return result
        if name == b'cumulativeSum':
            return conditions.CumulativeSum(uniqueName, data, self)
        return

    def isGroupProgressCompleted(self, groupByKey):
        progress = {}
        if self._progress is not None:
            progress = self._progress.get(groupByKey, {})
        if self._bonusLimit is not None:
            return progress.get(b'bonusCount', 0) >= self._bonusLimit
        else:
            return False
