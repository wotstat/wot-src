from __future__ import absolute_import
import copy, random, time, typing
from builtins import zip
from future.utils import listitems, iteritems, itervalues
from past.builtins import xrange, basestring
from account_shared import getCustomizationItem
from constants import LOOTBOX_TOKEN_PREFIX
from dog_tags_common.components_config import componentConfigAdapter
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Dict, Optional

def _packTrack(track):
    result = []
    if not track:
        return None
    else:
        curByte = curPos = 0
        for flag in track:
            if flag:
                curByte |= 1 << curPos
            curPos += 1
            if curPos > 7:
                result.append(curByte)
                curByte = curPos = 0

        result.append(curByte)
        result = (b'').join((b'{:02x}').format(x) for x in bytearray(result))
        return result


def _trackIterator(packedTrack):
    for curByte in bytearray.fromhex(packedTrack):
        for i in xrange(8):
            result = bool(curByte & 1 << i)
            yield result

    return


def __mergeValue(total, key, value, isLeaf=False, count=1, *args):
    total[key] = total.get(key, 0) + count * value
    return


def __mergeFactor(total, key, value, isLeaf, count=1, *args):
    if isLeaf:
        total[key] = total.get(key, 0) + count * (max(value, 1) - 1)
    else:
        total[key] = total.get(key, 0) + count * value
    return


def __mergeItems(total, key, value, isLeaf=False, count=1, *args):
    items = total.setdefault(key, {})
    for itemCompDescr, itemCount in iteritems(value):
        items[itemCompDescr] = items.get(itemCompDescr, 0) + count * itemCount

    return


def __mergeList(total, key, value, count):
    items = total.setdefault(key, [])
    items.extend((value if isinstance(value, list) else [value]) * count)
    return


def __mergeVehicles(total, key, value, isLeaf, count, *args):
    __mergeList(total, key, value, count)
    return


def __mergeTankmen(total, key, value, isLeaf, count, *args):
    __mergeList(total, key, value, count)
    return


def __mergeCustomizations(total, key, value, isLeaf, count, vehTypeCompDescr):
    customizations = total.setdefault(key, [])
    for subvalue in value:
        currentValue = __findCustomization(customizations, subvalue)
        if currentValue is not None:
            currentValue[b'value'] += subvalue[b'value'] * count
        else:
            subvalue = copy.deepcopy(subvalue)
            subvalue[b'value'] *= count
            if b'boundToCurrentVehicle' in subvalue:
                subvalue[b'vehTypeCompDescr'] = vehTypeCompDescr
            customizations.append(subvalue)

    return


def __findCustomization(customizations, value):
    for customization in customizations:
        if all(customization.get(param) == value.get(param) for param in (b'custType', b'id', b'vehTypeCompDescr')):
            return customization

    return


def __mergeCrewSkins(total, key, value, isLeaf, count, *args):
    __mergeList(total, key, value, count)
    return


def __mergeTokens(total, key, value, isLeaf=False, count=1, *args):
    totalTokens = total.setdefault(key, {})
    for tokenID, tokenData in iteritems(value):
        total = totalTokens.setdefault(tokenID, {b'count': 0, b'expires': {}, b'limit': 0})
        total[b'count'] += count * tokenData.get(b'count', 1)
        if total[b'count'] == 0:
            totalTokens.pop(tokenID)
            continue
        if not total[b'expires']:
            total[b'expires'] = tokenData[b'expires']
        if b'limit' in tokenData:
            total[b'limit'] = tokenData[b'limit'] if total[b'limit'] == 0 else max(total[b'limit'], tokenData[b'limit'])
        extItems = tokenData.get(b'extItems', None)
        if extItems:
            __mergeList(total, b'extItems', extItems, 1)

    return


def __mergeGoodies(total, key, value, isLeaf=False, count=1, *args):
    totalGoodies = total.setdefault(key, {})
    for goodieID, goodieData in iteritems(value):
        total = totalGoodies.setdefault(goodieID, {b'count': 0, b'expires': {}, b'limit': 0})
        total[b'count'] += count * goodieData.get(b'count', 1)
        if not total[b'expires'] and b'expires' in goodieData:
            total[b'expires'] = goodieData[b'expires']
        if b'limit' in goodieData:
            total[b'limit'] = goodieData[b'limit'] if total[b'limit'] == 0 else max(total[b'limit'], goodieData[b'limit'])

    return


def __mergeEntitlements(total, key, value, isLeaf=False, count=1, *args):
    totalEntitlements = total.setdefault(key, {})
    for entitlementCode, entitlementData in iteritems(value):
        total = totalEntitlements.setdefault(entitlementCode, {b'count': 0})
        total[b'count'] += count * entitlementData.get(b'count', 1)
        if b'expires' not in total and b'expires' in entitlementData:
            total[b'expires'] = entitlementData[b'expires']

    return


def __mergeEntitlementList(total, key, value, isLeaf=False, count=1, *args):
    entitlementList = total.setdefault(key, {})
    entitlementList.setdefault(b'items', []).extend(value.get(b'items', []) * count)
    return


def __mergePets(total, key, value, isLeaf, count, *args):
    total.setdefault(key, set()).update(value)
    return


def __mergeCurrencies(total, key, value, isLeaf=False, count=1, *args):
    totalCurrency = total.setdefault(key, {})
    for currencyCode, currencyData in iteritems(value):
        total = totalCurrency.setdefault(currencyCode, {b'count': 0})
        total[b'count'] = total.get(b'count', 0) + count * currencyData.get(b'count', 1)

    return


def __mergeDossier(total, key, value, isLeaf=False, count=1, *args):
    totalDossiers = total.setdefault(key, {})
    for _dossierType, changes in iteritems(value):
        totalDossier = totalDossiers.setdefault(_dossierType, {})
        duplicatedkeys = not isinstance(changes, dict)
        it = changes if duplicatedkeys else iteritems(changes)
        for record, data in it:
            block, name = record
            try:
                record = (
                 block, int(name))
            except:
                pass

            total = totalDossier.setdefault(record, {b'value': 0, 
               b'unique': False, 
               b'type': b'add'})
            dataValue = data[b'value']
            if isinstance(dataValue, basestring):
                if dataValue == b'timestamp':
                    total[b'value'] = int(time.time())
            else:
                total[b'value'] += dataValue * count
            total[b'unique'] = data[b'unique']
            total[b'type'] = data[b'type']
            if b'actualValue' in data:
                total[b'actualValue'] = data[b'actualValue']

    return


def __mergeBlueprints(total, key, value, isLeaf=False, count=1, *args):
    totalBlueprints = total.setdefault(key, {})
    for fragmentCD, fragmentData in iteritems(value):
        totalBlueprints.setdefault(fragmentCD, 0)
        totalBlueprints[fragmentCD] += count * fragmentData

    return


def __mergeEnhancements(total, key, value, isLeaf=False, count=1, *args):
    enhancementsTotal = total.setdefault(key, {})
    for enhancementID, enhancementData in iteritems(value):
        enhancementMerged = enhancementsTotal.setdefault(enhancementID, {})
        enhancementMerged.update({b'count': (enhancementMerged.get(b'count', 0) + enhancementData.get(b'count', 0) * count), 
           b'wipe': (enhancementMerged.get(b'wipe', False) or enhancementData.get(b'wipe', False))})

    return


def __mergeDogTag(total, key, value, isLeaf=False, count=1, *args):
    dogTags = total.setdefault(key, [])
    dogTags.extend(value)
    dogTags.sort(key=(lambda v: componentConfigAdapter.getComponentById(v[b'id']).viewType.value))
    return


def __mergeBattlePassPoints(total, key, value, isLeaf=False, count=1, *args):
    NON_VEH_CD = 0
    defaultBattlePassPoints = {b'vehicles': {NON_VEH_CD: 0}}
    seasonID = value.get(b'seasonID')
    chapterID = value.get(b'chapterID')
    if seasonID:
        defaultBattlePassPoints[b'seasonID'] = seasonID
    if chapterID:
        defaultBattlePassPoints[b'chapterID'] = chapterID
    battlePass = total.setdefault(key, defaultBattlePassPoints)
    battlePass[b'vehicles'][NON_VEH_CD] += value.get(b'vehicles', {}).get(NON_VEH_CD, 0) * count
    return


def __mergeFreePremiumCrew(total, key, value, isLeaf=False, count=1, *args):
    freePremiumCrewBonus = total.setdefault(key, {})
    for vehLevel, freePremiumCrewCount in iteritems(value):
        freePremiumCrewBonus.setdefault(vehLevel, 0)
        freePremiumCrewBonus[vehLevel] += freePremiumCrewCount * count

    return


def __mergeMeta(total, key, value, isLeaf=False, count=1, *args):
    total[key] = value
    return


def __mergeNoviceReset(total, key, value, isLeaf=False, count=1, *args):
    total[key] = value
    return


def __mergeDailyQuestReroll(total, key, value, isLeaf, count, *args):
    total.setdefault(key, set()).update(value)
    return


BONUS_MERGERS = {b'credits': __mergeValue, 
   b'gold': __mergeValue, 
   b'xp': __mergeValue, 
   b'crystal': __mergeValue, 
   b'eventCoin': __mergeValue, 
   b'bpcoin': __mergeValue, 
   b'equipCoin': __mergeValue, 
   b'freeXP': __mergeValue, 
   b'tankmenXP': __mergeValue, 
   b'vehicleXP': __mergeValue, 
   b'creditsFactor': __mergeFactor, 
   b'xpFactor': __mergeFactor, 
   b'freeXPFactor': __mergeFactor, 
   b'tankmenXPFactor': __mergeFactor, 
   b'vehicleXPFactor': __mergeFactor, 
   b'items': __mergeItems, 
   b'vehicles': __mergeVehicles, 
   b'slots': __mergeValue, 
   b'berths': __mergeValue, 
   b'premium': __mergeValue, 
   b'premium_plus': __mergeValue, 
   b'premium_vip': __mergeValue, 
   b'tokens': __mergeTokens, 
   b'goodies': __mergeGoodies, 
   b'dossier': __mergeDossier, 
   b'tankmen': __mergeTankmen, 
   b'customizations': __mergeCustomizations, 
   b'crewSkins': __mergeCrewSkins, 
   b'blueprintsAny': __mergeItems, 
   b'blueprints': __mergeBlueprints, 
   b'enhancements': __mergeEnhancements, 
   b'entitlements': __mergeEntitlements, 
   b'entitlementList': __mergeEntitlementList, 
   b'currencies': __mergeCurrencies, 
   b'rankedDailyBattles': __mergeValue, 
   b'rankedBonusBattles': __mergeValue, 
   b'dogTagComponents': __mergeDogTag, 
   b'battlePassPoints': __mergeBattlePassPoints, 
   b'freePremiumCrew': __mergeFreePremiumCrew, 
   b'meta': __mergeMeta, 
   b'dailyQuestReroll': __mergeDailyQuestReroll, 
   b'noviceReset': __mergeNoviceReset, 
   b'pets': __mergePets}
ITEM_INVENTORY_CHECKERS = {b'vehicles': (lambda account, key: account._inventory.getVehicleInvID(key) != 0 and not account._rent.isVehicleRented(account._inventory.getVehicleInvID(key))), 
   b'customizations': (lambda account, key: account._customizations20.getItems((key,), 0)[key] > 0), 
   b'tokens': (lambda account, key: account._quests.hasToken(key))}
RENT_ITEM_INVENTORY_CHECKERS = {b'vehicles': (lambda account, key: account._rent.isVehicleRented(account._inventory.getVehicleInvID(key)))}
SKIP_INVENTORY_CHANGE_CHECKERS = {b'tokens': (lambda key: key.startswith(LOOTBOX_TOKEN_PREFIX))}

class BonusItemsCache(object):

    def __init__(self, account, cache=None):
        self.__account = account
        self.__cache = cache or {}
        return

    def getRawData(self):
        return self.__cache

    def onItemAccepted(self, itemName, itemKey, isRent=False):
        cache = self.__cache.setdefault(itemName, {})
        state = cache.setdefault(itemKey, {}).get(isRent, None)
        if state is not None:
            wasInInventory, _ = state
        else:
            wasInInventory = (RENT_ITEM_INVENTORY_CHECKERS if isRent else ITEM_INVENTORY_CHECKERS)[itemName](self.__account, itemKey)
        cache[itemKey][isRent] = (wasInInventory, True)
        return

    def isItemExists(self, itemName, itemKey, isRent=False):
        cache = self.__cache.setdefault(itemName, {})
        state = cache.setdefault(itemKey, {}).get(isRent, None)
        if state is not None:
            wasInInventory, wasAccepted = state
        else:
            wasInInventory = (RENT_ITEM_INVENTORY_CHECKERS if isRent else ITEM_INVENTORY_CHECKERS)[itemName](self.__account, itemKey)
            wasAccepted = False
            cache[itemKey][isRent] = (wasInInventory, wasAccepted)
        if isRent and itemName in ITEM_INVENTORY_CHECKERS and cache[itemKey].get(False, None) is None:
            cache[itemKey][False] = (
             ITEM_INVENTORY_CHECKERS[itemName](self.__account, itemKey), False)
        return wasInInventory or wasAccepted or isRent and any(state for state in cache[itemKey].get(False, ()))

    def getFinalizedCache(self):
        result = {}
        for bonus, checks in iteritems(self.__cache):
            bonusResult = result.setdefault(bonus, {})
            for key, keyData in iteritems(checks):
                keyResult = bonusResult.setdefault(key, {})
                for flag, (wasInInventory, wasAccepted) in iteritems(keyData):
                    keyResult[flag] = (
                     wasInInventory or wasAccepted, False)

        return result

    @staticmethod
    def isInventoryChanged(account, itemsCache):
        for bonus, checks in iteritems(itemsCache):
            checker = ITEM_INVENTORY_CHECKERS[bonus]
            skipChecker = SKIP_INVENTORY_CHANGE_CHECKERS.get(bonus)
            for key, keyData in iteritems(checks):
                if skipChecker and skipChecker(key):
                    continue
                if False in keyData and checker(account, key) != keyData[False][0]:
                    return True

        return False


DEEP_CHECKERS = {b'groups': (lambda nodeAcceptor, bonusNode, checkInventory, depthLevel: all(nodeAcceptor.depthCheck(subBonusNode, checkInventory, depthLevel) for subBonusNode in bonusNode)), 
   b'allof': (lambda nodeAcceptor, bonusNode, checkInventory, depthLevel: all(nodeAcceptor.isAcceptable(subBonusNode[-1], False, depthLevel - 1) for subBonusNode in bonusNode)), 
   b'oneof': (lambda nodeAcceptor, bonusNode, checkInventory, depthLevel: any(nodeAcceptor.isAcceptable(subBonusNode[-1], checkInventory, depthLevel - 1) for subBonusNode in bonusNode[-1]))}

class BonusNodeAcceptor(object):

    def __init__(self, account, bonusConfig=None, counters=None, bonusCache=None, probabilityStage=0, logTracker=None, shouldResetUsedLimits=True, dropInGroupHistory=None, trackedByNameSections=None):
        self.__account = account
        self.__limitsConfig = bonusConfig.get(b'limits', None) if bonusConfig else None
        self.__maxStage = bonusConfig.get(b'probabilityStageCount', 1) - 1 if bonusConfig else 0
        self.__useBonusProbability = bonusConfig.get(b'useBonusProbability', False) if bonusConfig else False
        self.__locals = None
        self.__cooldowns = None
        self.__uses = None
        self.__shouldVisitNodes = None
        self.__bonusCache = bonusCache or BonusItemsCache(account)
        probabilityStage = min(probabilityStage, self.__maxStage)
        self.__probabilitiesStage = [
         probabilityStage, probabilityStage]
        self.__bonusProbabilityUses = None
        self.__shouldUseBonusProbability = False
        self.__isMaxStageReached = self.__maxStage <= probabilityStage
        self.__logTracker = logTracker
        self.__usedLimits = set()
        self.__shouldResetUsedLimits = shouldResetUsedLimits
        self.__initCounters(counters or {})
        self.__dropInGroupsBonuses = dropInGroupHistory or {}
        self.__dropInGroupsBonusesLimit = bonusConfig.get(b'dropInGroupItemsCount', 0) if bonusConfig else 0
        self.__trackedByNameSections = trackedByNameSections if trackedByNameSections is not None else {}
        return

    def __initCounters(self, counters):
        if self.__limitsConfig:
            self.__uses = uses = {}
            self.__cooldowns = cooldowns = {}
            self.__locals = {}
            self.__bonusProbabilityUses = bonusProbabilityUses = {}
            for limitID, config in iteritems(self.__limitsConfig):
                if b'guaranteedFrequency' in config or b'maxFrequency' in config or b'useBonusProbabilityAfter' in config:
                    cooldowns[limitID], uses[limitID], bonusProbabilityUses[limitID] = counters.get(limitID, (0, 0, 0))

        return

    def getCounters(self):
        if not self.__limitsConfig:
            return
        else:
            result = {}
            cooldowns = self.__cooldowns
            uses = self.__uses
            bonusProbabilityUses = self.__bonusProbabilityUses
            for limitID, config in iteritems(self.__limitsConfig):
                if b'guaranteedFrequency' in config or b'maxFrequency' in config or b'useBonusProbabilityAfter' in config:
                    result[limitID] = (
                     cooldowns[limitID], uses[limitID], bonusProbabilityUses[limitID])

            return result or None

    def getBonusCache(self):
        return self.__bonusCache

    def getTrackedByNameSections(self):
        return self.__trackedByNameSections

    def isAcceptable(self, bonusNode, checkInventory=True, depthLevel=None):
        if self.isLimitReached(bonusNode):
            return False
        bonusNodeProperties = bonusNode.get(b'properties', {})
        dropInGroup = bonusNodeProperties.get(b'dropInGroup', False)
        if self.isBonusesInSameGroupAlreadyPicked(bonusNode):
            return False
        if self.isSectionTrackedByNameLimitReached(bonusNodeProperties):
            return False
        trackedByNameLimit = bonusNodeProperties.get(b'trackedByNameLimit')
        if checkInventory and not (dropInGroup or trackedByNameLimit) and self.isBonusExists(bonusNode):
            return False
        return self.depthCheck(bonusNode, checkInventory, depthLevel)

    def getNodesForVisit(self, ids):
        if ids and self.__shouldVisitNodes:
            return self.__shouldVisitNodes.intersection(ids)
        else:
            return

    def isLimitReached(self, bonusNode):
        if not self.__limitsConfig:
            return False
        else:
            limitID = bonusNode.get(b'properties', {}).get(b'limitID', None)
            if not limitID:
                return False
            if self.__locals.get(limitID, 1) <= 0:
                return True
            if self.__cooldowns.get(limitID, 0) > 0:
                return True
            return False

    def updateBonusCache(self, bonusNode):
        cache = self.__bonusCache
        if b'vehicles' in bonusNode:
            for itemID, itemData in iteritems(bonusNode[b'vehicles']):
                cache.onItemAccepted(b'vehicles', itemID, bool(itemData.get(b'rent', None)))

        if b'tokens' in bonusNode:
            for itemID in bonusNode[b'tokens']:
                cache.onItemAccepted(b'tokens', itemID)

        if b'customizations' in bonusNode:
            for customization in bonusNode[b'customizations']:
                c11nItem = getCustomizationItem(customization[b'custType'], customization[b'id'])[0]
                cache.onItemAccepted(b'customizations', c11nItem.compactDescr)

        return

    def isBonusExists(self, bonusNode):
        cache = self.__bonusCache
        if b'vehicles' in bonusNode:
            for itemID, itemData in iteritems(bonusNode[b'vehicles']):
                if cache.isItemExists(b'vehicles', itemID, bool(itemData.get(b'rent', None))):
                    return True

        if b'tokens' in bonusNode:
            for itemID, itemData in iteritems(bonusNode[b'tokens']):
                if cache.isItemExists(b'tokens', itemID):
                    return True

        if b'customizations' in bonusNode:
            for customization in bonusNode[b'customizations']:
                c11nItem = getCustomizationItem(customization[b'custType'], customization[b'id'])[0]
                if cache.isItemExists(b'customizations', c11nItem.compactDescr):
                    return True

        return False

    def isBonusesInSameGroupAlreadyPicked(self, bonusNode):
        if not bonusNode.get(b'properties', {}).get(b'dropInGroup', False):
            return False
        if b'vehicles' in bonusNode:
            cache = self.__dropInGroupsBonuses.setdefault(b'vehicles', set())
            for itemID in bonusNode[b'vehicles']:
                if itemID in cache:
                    return True

        if b'tokens' in bonusNode:
            cache = self.__dropInGroupsBonuses.setdefault(b'tokens', set())
            for itemID in bonusNode[b'tokens']:
                if itemID in cache:
                    return True

        if b'customizations' in bonusNode:
            cache = self.__dropInGroupsBonuses.setdefault(b'customizations', set())
            for customization in bonusNode[b'customizations']:
                c11nItem = getCustomizationItem(customization[b'custType'], customization[b'id'])[0]
                if c11nItem.compactDescr in cache:
                    return True

        return False

    def updateBonusesInSameGroup(self, bonusNode):
        if not bonusNode.get(b'properties', {}).get(b'dropInGroup', False):
            return
        if b'vehicles' in bonusNode:
            cache = self.__dropInGroupsBonuses.setdefault(b'vehicles', set())
            for itemID in bonusNode[b'vehicles']:
                cache.add(itemID)

        if b'tokens' in bonusNode:
            cache = self.__dropInGroupsBonuses.setdefault(b'tokens', set())
            for itemID in bonusNode[b'tokens']:
                cache.add(itemID)

        if b'customizations' in bonusNode:
            cache = self.__dropInGroupsBonuses.setdefault(b'customizations', set())
            for customization in bonusNode[b'customizations']:
                c11nItem = getCustomizationItem(customization[b'custType'], customization[b'id'])[0]
                cache.add(c11nItem.compactDescr)

        return

    def isSectionTrackedByNameLimitReached(self, bonusNodeProperties):
        if not self.__trackedByNameSections:
            return False
        else:
            trackedByNameLimit = bonusNodeProperties.get(b'trackedByNameLimit')
            if trackedByNameLimit is None:
                return False
            previousLimitValue = self.__trackedByNameSections.get(bonusNodeProperties.get(b'name'), 0)
            if previousLimitValue < trackedByNameLimit:
                return False
            return True

    def updateTrackedByNameSections(self, bonusNodeProperties):
        if bonusNodeProperties.get(b'trackedByNameLimit') is None:
            return
        else:
            bonusNodeName = bonusNodeProperties.get(b'name', b'')
            self.__trackedByNameSections[bonusNodeName] = self.__trackedByNameSections.get(bonusNodeName, 0) + 1
            return

    def depthCheck(self, bonusNode, checkInventory, depthLevel=None):
        currentDepthLevel = bonusNode.get(b'properties', {}).get(b'depthLevel', 0) if depthLevel is None else depthLevel
        if currentDepthLevel <= 0:
            return True
        else:
            return all(DEEP_CHECKERS[bonusNodeName](self, bonusNodeValue, checkInventory, currentDepthLevel) for bonusNodeName, bonusNodeValue in iteritems(bonusNode) if bonusNodeName in DEEP_CHECKERS)

    def getProbabilityStages(self):
        return self.__probabilitiesStage

    def getCurrentProbabilityStage(self):
        return self.__probabilitiesStage[0]

    def __increaseProbabilityStage(self):
        if self.__probabilitiesStage[1] < self.__maxStage:
            self.__probabilitiesStage[1] += 1
        return

    def __updateProbabilityStages(self):
        self.__probabilitiesStage[0] = self.__probabilitiesStage[1]
        return

    def __resetFlags(self):
        if not self.__isMaxStageReached or self.__shouldUseBonusProbability:
            self.__isMaxStageReached = self.__probabilitiesStage[1] >= self.__maxStage
            self.__shouldUseBonusProbability = False
        return

    def getDropInGroupInfo(self):
        for k, v in listitems(self.__dropInGroupsBonuses):
            if len(v) == 0:
                self.__dropInGroupsBonuses.pop(k)

        return self.__dropInGroupsBonuses

    def __updateDropInGroupLimits(self):
        if self.__dropInGroupsBonusesLimit <= sum(len(v) for v in itervalues(self.__dropInGroupsBonuses)):
            for v in itervalues(self.__dropInGroupsBonuses):
                v.clear()

        return

    def getUseBonusProbability(self):
        return self.__shouldUseBonusProbability

    def getStagesInfo(self):
        return tuple(self.getProbabilityStages() + [self.__maxStage + 1])

    def getUsedLimits(self):
        return self.__usedLimits

    def getLoggingInfo(self):
        if self.__logTracker is None:
            return
        else:
            beginStage, endStage, stagesCount = self.getStagesInfo()
            usedLimits = self.getUsedLimits()
            return self.__logTracker.generateInfo(beginStage, endStage, stagesCount, usedLimits)

    def accept(self, bonusNode):
        bonusNodeProperties = bonusNode.get(b'properties') or {}
        if bonusNodeProperties.get(b'probabilityStageDependence', False):
            self.__increaseProbabilityStage()
        limitID = bonusNodeProperties.get(b'limitID', None)
        if limitID:
            limitConfig = self.__limitsConfig[limitID]
            if not limitConfig.get(b'countDuplicates', True) and self.isBonusExists(bonusNode):
                return
            if limitID in self.__locals:
                self.__locals[limitID] -= 1
            if limitID in self.__cooldowns:
                self.__cooldowns[limitID] = limitConfig.get(b'maxFrequency', 0)
            if limitID in self.__uses:
                self.__uses[limitID] = 0
            if limitID in self.__bonusProbabilityUses and not self.__isMaxStageReached:
                self.__bonusProbabilityUses[limitID] = 0
        self.updateBonusCache(bonusNode)
        self.updateBonusesInSameGroup(bonusNode)
        self.updateTrackedByNameSections(bonusNodeProperties)
        return

    def reuse(self):
        self.__updateProbabilityStages()
        self.__resetFlags()
        self.__updateDropInGroupLimits()
        if not self.__limitsConfig:
            return
        else:
            self.__locals = locals = {}
            cooldowns = self.__cooldowns
            uses = self.__uses
            self.__shouldVisitNodes = set([])
            bonusProbabilityUses = self.__bonusProbabilityUses
            if self.__shouldResetUsedLimits:
                self.__usedLimits = set()
            for limitID, limitConfig in iteritems(self.__limitsConfig):
                bonusLimit = limitConfig.get(b'bonusLimit', None)
                if bonusLimit is not None:
                    locals[limitID] = bonusLimit
                cooldown = limitConfig.get(b'maxFrequency', None)
                if cooldown is not None:
                    cooldowns[limitID] -= 1
                guaranteedFrequency = limitConfig.get(b'guaranteedFrequency', None)
                if guaranteedFrequency is not None:
                    uses[limitID] += 1
                    if uses[limitID] >= guaranteedFrequency:
                        self.__shouldVisitNodes.add(limitID)
                        self.__usedLimits.add(limitID)
                bonusProbabilityAfter = limitConfig.get(b'useBonusProbabilityAfter', None)
                if bonusProbabilityAfter is not None and not self.__isMaxStageReached and self.__useBonusProbability:
                    bonusProbabilityUses[limitID] += 1
                    if bonusProbabilityUses[limitID] > bonusProbabilityAfter:
                        self.__shouldUseBonusProbability = True
                        self.__usedLimits.add(limitID)

            return


class NodeVisitor(object):

    def __init__(self, mergers, args):
        self._mergers = mergers
        self._mergersArgs = args
        return

    def onOneOf(self, storage, values):
        raise NotImplementedError()
        return

    def onAllOf(self, storage, values):
        raise NotImplementedError()
        return

    def onGroup(self, storage, values):
        raise NotImplementedError()
        return

    def onMergeValue(self, storage, name, value, isLeaf):
        self._mergers[name](storage, name, value, isLeaf, *self._mergersArgs)
        return

    def beforeWalk(self, storage, bonusSection):
        return

    def _walkSubsection(self, storage, bonusSection):
        result = {}
        for bonusName, bonusValue in iteritems(bonusSection):
            if bonusName == b'oneof':
                self.onOneOf(result, bonusValue)
            elif bonusName == b'allof':
                self.onAllOf(result, bonusValue)
            elif bonusName == b'groups':
                self.onGroup(result, bonusValue)
            elif bonusName in (b'config', b'properties', b'needsExpansion'):
                continue
            else:
                self.onMergeValue(result, bonusName, bonusValue, True)

        for name, value in iteritems(result):
            self.onMergeValue(storage, name, value, False)

        return

    def walkBonuses(self, bonusSection, storage=None):
        result = storage if storage is not None else {}
        self.beforeWalk(result, bonusSection)
        self._walkSubsection(result, bonusSection)
        return result


class TrackVisitor(NodeVisitor):

    def __init__(self, track, *args):
        super(TrackVisitor, self).__init__(BONUS_MERGERS, args)
        self.__track = _trackIterator(track)
        return

    def onOneOf(self, storage, values):
        for _, _, _, bonusValue in values[1]:
            if next(self.__track):
                self._walkSubsection(storage, bonusValue)
                return

        return

    def onAllOf(self, storage, values):
        for _, _, _, bonusValue in values:
            if next(self.__track):
                self._walkSubsection(storage, bonusValue)

        return

    def onGroup(self, storage, values):
        for bonusValue in values:
            self._walkSubsection(storage, bonusValue)

        return


class ProbabilityVisitor(NodeVisitor):

    def __init__(self, nodeAcceptor, *args):
        super(ProbabilityVisitor, self).__init__(BONUS_MERGERS, args)
        self.__bonusTrack = []
        self.__nodeAcceptor = nodeAcceptor
        return

    def getBonusTrack(self):
        return _packTrack(self.__bonusTrack)

    def onOneOf(self, storage, values):
        rand = random.random()
        limitIDs, bonusNodes = values
        acceptor = self.__nodeAcceptor
        shouldVisitNodes = acceptor.getNodesForVisit(limitIDs)
        probablitiesStage = acceptor.getCurrentProbabilityStage()
        useBonusProbability = acceptor.getUseBonusProbability()
        if shouldVisitNodes:
            check = lambda _, nodeLimitIDs: nodeLimitIDs and nodeLimitIDs.intersection(shouldVisitNodes)
        else:
            check = lambda probability, _: probability > rand
        for i, (probabilities, bonusProbability, nodeLimitIDs, bonusValue) in enumerate(bonusNodes):
            probability = probabilities[probablitiesStage]
            if check(bonusProbability if useBonusProbability else probability, nodeLimitIDs):
                selectedIdx = i
                selectedValue = bonusValue
                break
        else:
            raise SoftException(b'Unreachable code, oneof probability bug %s' % bonusNodes)

        isAcceptable = acceptor.isAcceptable
        if not isAcceptable(selectedValue):
            availableBonusNodes = []
            sumOfAvailableProbabilities = 0
            sumOfPreviousProbabilities = 0
            previousOwnProbability = 0.0
            canUsePrevInsteadOfZeroProbability = False
            for index, (probabilities, bonusProbability, _, bonusValue) in enumerate(bonusNodes):
                ownProbability = bonusProbability if useBonusProbability else probabilities[probablitiesStage]
                if ownProbability != 0.0:
                    ownProbability, sumOfPreviousProbabilities = ownProbability - sumOfPreviousProbabilities, ownProbability
                if ownProbability != 0.0:
                    canUsePrevInsteadOfZeroProbability = True
                    previousOwnProbability = ownProbability
                    probability = ownProbability
                else:
                    if canUsePrevInsteadOfZeroProbability and previousOwnProbability != 0.0:
                        probability = previousOwnProbability
                    else:
                        continue
                if index != selectedIdx and bonusValue.get(b'properties', {}).get(b'compensation', False) and isAcceptable(bonusValue):
                    sumOfAvailableProbabilities += probability
                    availableBonusNodes.append((index, probability, bonusValue))
                    canUsePrevInsteadOfZeroProbability = False

            if not availableBonusNodes:
                shouldCompensated = selectedValue.get(b'properties', {}).get(b'shouldCompensated', False)
                if not isAcceptable(selectedValue, False) or shouldCompensated:
                    for i in xrange(len(bonusNodes)):
                        self.__trackChoice(False)

                    return
            elif len(availableBonusNodes) == 1:
                selectedIdx, _, selectedValue = availableBonusNodes[0]
            randomValue = random.random() * sumOfAvailableProbabilities
            sumOfPreviousProbabilities = 0
            for bonusNode in availableBonusNodes:
                sumOfPreviousProbabilities += bonusNode[1]
                if randomValue < sumOfPreviousProbabilities:
                    selectedIdx, _, selectedValue = bonusNode
                    break
            else:
                raise SoftException((b'Unreachable code, oneof probability bug, random value: {}, available bonus nodes: {}').format(randomValue, availableBonusNodes))

        for i in xrange(selectedIdx):
            self.__trackChoice(False)

        self.__trackChoice(True)
        acceptor.accept(selectedValue)
        self._walkSubsection(storage, selectedValue)
        return

    def onAllOf(self, storage, values):
        acceptor = self.__nodeAcceptor
        probabilityStage = acceptor.getCurrentProbabilityStage()
        useBonusProbability = acceptor.getUseBonusProbability()
        for probabilities, bonusProbability, nodeLimitIDs, bonusValue in values:
            probability = bonusProbability if useBonusProbability else probabilities[probabilityStage]
            shouldVisitNodes = acceptor.getNodesForVisit(nodeLimitIDs)
            if shouldVisitNodes or probability > random.random() and acceptor.isAcceptable(bonusValue, False):
                self.__trackChoice(True)
                self.__nodeAcceptor.accept(bonusValue)
                self._walkSubsection(storage, bonusValue)
            else:
                self.__trackChoice(False)

        return

    def onGroup(self, storage, values):
        for bonusValue in values:
            self._walkSubsection(storage, bonusValue)

        return

    def beforeWalk(self, storage, bonusSection):
        acceptor = self.__nodeAcceptor
        acceptor.reuse()
        return

    def __trackChoice(self, choice):
        self.__bonusTrack.append(choice)
        return


class StripVisitor(NodeVisitor):

    class ValuesMerger:

        def __getitem__(self, item):
            return self.copyMerger

        @staticmethod
        def copyMerger(storage, name, value, isLeaf):
            storage[name] = value
            return

    def __init__(self, needProbabilitiesInfo=False):
        self.__needProbabilitiesInfo = needProbabilitiesInfo
        super(StripVisitor, self).__init__(self.ValuesMerger(), tuple())
        return

    def __getShownProbability(self, probability, prevProbability=None):
        if self.__needProbabilitiesInfo:
            if prevProbability and probability != [0.0] * len(probability):
                return [currProb - prevProb for currProb, prevProb in zip(probability, prevProbability)]
            return probability
        return [
         -1]
        return

    def onOneOf(self, storage, values):
        strippedValues = []
        _, values = values
        for index, (probability, _, _, bonusValue) in enumerate(values):
            stippedValue = {}
            self._walkSubsection(stippedValue, bonusValue)
            prevProbability = values[index - 1][0] if index > 0 else None
            bonusValueName = bonusValue.get(b'properties', {}).get(b'name', None)
            if bonusValueName:
                stippedValue[b'properties'] = {b'name': bonusValueName}
            strippedValues.append((self.__getShownProbability(probability, prevProbability), -1, None, stippedValue))

        storage[b'oneof'] = (None, strippedValues)
        return

    def onAllOf(self, storage, values):
        strippedValues = []
        for probability, _, _, bonusValue in values:
            stippedValue = {}
            self._walkSubsection(stippedValue, bonusValue)
            bonusValueName = bonusValue.get(b'properties', {}).get(b'name', None)
            if bonusValueName:
                stippedValue[b'properties'] = {b'name': bonusValueName}
            strippedValues.append((self.__getShownProbability(probability), -1, None, stippedValue))

        storage[b'allof'] = strippedValues
        return

    def onGroup(self, storage, values):
        strippedValues = []
        for bonusValue in values:
            stippedValue = {}
            self._walkSubsection(stippedValue, bonusValue)
            strippedValues.append(stippedValue)

        storage[b'groups'] = strippedValues
        return
