import copy, random, time, typing
from account_shared import getCustomizationItem
from battle_pass_common import NON_VEH_CD
from debug_utils import LOG_WARNING
from dog_tags_common.components_config import componentConfigAdapter
from soft_exception import SoftException
from copy import deepcopy
from WeakMethod import WeakMethodProxy
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
    for itemCompDescr, itemCount in value.iteritems():
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
        if all([customization.get(param) == value.get(param) for param in (b'custType', b'id', b'vehTypeCompDescr')]):
            return customization

    return


def __mergeCrewSkins(total, key, value, isLeaf, count, *args):
    __mergeList(total, key, value, count)
    return


def __mergeTokens(total, key, value, isLeaf=False, count=1, *args):
    totalTokens = total.setdefault(key, {})
    for tokenID, tokenData in value.iteritems():
        total = totalTokens.setdefault(tokenID, {b'count': 0, b'expires': {}, b'limit': 0})
        total[b'count'] += count * tokenData.get(b'count', 1)
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
    for goodieID, goodieData in value.iteritems():
        total = totalGoodies.setdefault(goodieID, {b'count': 0, b'expires': {}, b'limit': 0})
        total[b'count'] += count * goodieData.get(b'count', 1)
        if not total[b'expires'] and b'expires' in goodieData:
            total[b'expires'] = goodieData[b'expires']
        if b'limit' in goodieData:
            total[b'limit'] = goodieData[b'limit'] if total[b'limit'] == 0 else max(total[b'limit'], goodieData[b'limit'])

    return


def __mergeEntitlements(total, key, value, isLeaf=False, count=1, *args):
    totalEntitlements = total.setdefault(key, {})
    for entitlementCode, entitlementData in value.iteritems():
        total = totalEntitlements.setdefault(entitlementCode, {b'count': 0})
        total[b'count'] += count * entitlementData.get(b'count', 1)
        if b'expires' not in total and b'expires' in entitlementData:
            total[b'expires'] = entitlementData[b'expires']

    return


def __mergeEntitlementList(total, key, value, isLeaf=False, count=1, *args):
    entitlementList = total.setdefault(key, {})
    entitlementList.setdefault(b'items', []).extend(value.get(b'items', []) * count)
    return


def __mergeCurrencies(total, key, value, isLeaf=False, count=1, *args):
    totalCurrency = total.setdefault(key, {})
    for currencyCode, currencyData in value.iteritems():
        total = totalCurrency.setdefault(currencyCode, {b'count': 0})
        total[b'count'] += count * currencyData.get(b'count', 1)

    return


def __mergeDossier(total, key, value, isLeaf=False, count=1, *args):
    totalDossiers = total.setdefault(key, {})
    for _dossierType, changes in value.iteritems():
        totalDossier = totalDossiers.setdefault(_dossierType, {})
        duplicatedkeys = not isinstance(changes, dict)
        it = changes if duplicatedkeys else changes.iteritems()
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
    for fragmentCD, fragmentData in value.iteritems():
        totalBlueprints.setdefault(fragmentCD, 0)
        totalBlueprints[fragmentCD] += count * fragmentData

    return


def __mergeEnhancements(total, key, value, isLeaf=False, count=1, *args):
    enhancementsTotal = total.setdefault(key, {})
    for enhancementID, enhancementData in value.iteritems():
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
    for vehLevel, freePremiumCrewCount in value.iteritems():
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


def __mergeParagonsUnlocks(total, key, value, isLeaf, count, *args):
    total.setdefault(key, {})
    total[key].setdefault(b'ids', set()).update(value.get(b'ids', set()))
    return


def __mergePreferredMapSlots(total, key, value, isLeaf, count, *args):
    preferredMapSlots = total.setdefault(key, {})
    for slotID, slotDurationDays in value.iteritems():
        preferredMapSlots.setdefault(slotID, 0)
        preferredMapSlots[slotID] += count * slotDurationDays

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
   b'paragonsUnlocks': __mergeParagonsUnlocks, 
   b'preferredMapSlots': __mergePreferredMapSlots}

def _vehiclesInventoryChecker(account, key):
    invId = account._inventory.getVehicleInvID(key)
    if invId != 0:
        return not account._rent.isVehicleRented(invId) or account._recycleBin.availableRestoreVehicle(key)
    return account._recycleBin.availableRestoreVehicle(key)


ITEM_INVENTORY_CHECKERS = {b'vehicles': _vehiclesInventoryChecker, 
   b'customizations': (lambda account, key: account._customizations20.getItems((key,), 0)[key] > 0), 
   b'tokens': (lambda account, key: account._quests.hasToken(key))}
RENT_ITEM_INVENTORY_CHECKERS = {b'vehicles': (lambda account, key: account._rent.isVehicleRented(account._inventory.getVehicleInvID(key)))}

def __vehiclesExistanceChecker(bonusValue, cache):
    for itemID, itemData in bonusValue.iteritems():
        if cache.isItemExists(b'vehicles', itemID, bool(itemData.get(b'rent', None))):
            return True

    return False


def __tokensExistanceChecker(bonusValue, cache):
    for itemID in bonusValue.iterkeys():
        if cache.isItemExists(b'tokens', itemID):
            return True

    return False


def __customizationsExistanceChecker(bonusValue, cache):
    for customization in bonusValue:
        c11nItem = getCustomizationItem(customization[b'custType'], customization[b'id'])[0]
        if cache.isItemExists(b'customizations', c11nItem.compactDescr):
            return True

    return False


UNIQUE_BONUSES_EXISTANCE_CHECKERS = {b'vehicles': __vehiclesExistanceChecker, 
   b'tokens': __tokensExistanceChecker, 
   b'customizations': __customizationsExistanceChecker}

def __vehiclesCacheUpdater(bonusValue, cache):
    for itemID, itemData in bonusValue.iteritems():
        cache.onItemAccepted(b'vehicles', itemID, bool(itemData.get(b'rent', None)))

    return


def __tokensCacheUpdater(bonusValue, cache):
    for itemID in bonusValue.iterkeys():
        cache.onItemAccepted(b'tokens', itemID)

    return


def __customizationsCacheUpdater(bonusValue, cache):
    for customization in bonusValue:
        c11nItem = getCustomizationItem(customization[b'custType'], customization[b'id'])[0]
        cache.onItemAccepted(b'customizations', c11nItem.compactDescr)

    return


UNIQUE_BONUSES_CACHE_UPDATERS = {b'vehicles': __vehiclesCacheUpdater, 
   b'tokens': __tokensCacheUpdater, 
   b'customizations': __customizationsCacheUpdater}

def getProbableBonuses(bonusType, value):
    if bonusType == b'allof':
        bonusData = value[0]
        probability, bonuses = bonusData[0], bonusData[3]
        return (probability, [bonuses] if bonuses is not None else [])
    if bonusType == b'oneof':
        return (
         None, [bonus for _, _, _, bonus in value[1]])
    return (
     None, [])


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
            wasInInventory, wasAccepted, acceptedCount = state
        else:
            wasInInventory = (RENT_ITEM_INVENTORY_CHECKERS if isRent else ITEM_INVENTORY_CHECKERS)[itemName](self.__account, itemKey)
            acceptedCount = 0
        cache[itemKey][isRent] = (wasInInventory, True, acceptedCount + 1)
        return

    def isItemExists(self, itemName, itemKey, isRent=False):
        cache = self.__cache.setdefault(itemName, {})
        state = cache.setdefault(itemKey, {}).get(isRent, None)
        if state is not None:
            wasInInventory, wasAccepted, _ = state
        else:
            wasInInventory = (RENT_ITEM_INVENTORY_CHECKERS if isRent else ITEM_INVENTORY_CHECKERS)[itemName](self.__account, itemKey)
            wasAccepted = False
            acceptedCount = 0
            cache[itemKey][isRent] = (wasInInventory, wasAccepted, acceptedCount)
        if isRent and itemName in ITEM_INVENTORY_CHECKERS and cache[itemKey].get(False, None) is None:
            cache[itemKey][False] = (
             ITEM_INVENTORY_CHECKERS[itemName](self.__account, itemKey), False, 0)
        return wasInInventory or wasAccepted or isRent and any(state for state in cache[itemKey].get(False, ()))

    def getAcceptedCount(self, itemName, itemKey, isRent=False):
        cache = self.__cache.setdefault(itemName, {})
        state = cache.setdefault(itemKey, {}).get(isRent, None)
        if state is not None:
            _, _, acceptedCount = state
        else:
            wasInInventory = (RENT_ITEM_INVENTORY_CHECKERS if isRent else ITEM_INVENTORY_CHECKERS)[itemName](self.__account, itemKey)
            wasAccepted = False
            acceptedCount = 0
            cache[itemKey][isRent] = (wasInInventory, wasAccepted, acceptedCount)
        return acceptedCount

    def getFinalizedCache(self):
        result = {}
        for bonus, checks in self.__cache.iteritems():
            bonusResult = result.setdefault(bonus, {})
            for key, keyData in checks.iteritems():
                keyResult = bonusResult.setdefault(key, {})
                for flag, (wasInInventory, wasAccepted, acceptedCount) in keyData.iteritems():
                    keyResult[flag] = (
                     wasInInventory or wasAccepted, False, acceptedCount)

        return result

    @staticmethod
    def isInventoryChanged(account, itemsCache):
        for bonus, checks in itemsCache.iteritems():
            checker = ITEM_INVENTORY_CHECKERS[bonus]
            for key, keyData in checks.iteritems():
                if False in keyData and checker(account, key) != keyData[False][0]:
                    return True

        return False


DEEP_CHECKERS = {b'groups': (lambda nodeAcceptor, bonusNode, checkInventory, depthLevel: all(nodeAcceptor.depthCheck(subBonusNode, checkInventory, depthLevel) for subBonusNode in bonusNode)), 
   b'allof': (lambda nodeAcceptor, bonusNode, checkInventory, depthLevel: all(nodeAcceptor.isAcceptable(subBonusNode[-1], False, depthLevel - 1) for subBonusNode in bonusNode)), 
   b'oneof': (lambda nodeAcceptor, bonusNode, checkInventory, depthLevel: any(nodeAcceptor.isAcceptable(subBonusNode[-1], checkInventory, depthLevel - 1) for subBonusNode in bonusNode[-1]))}

class BonusNodeAcceptor(object):

    def __init__(self, account, bonusConfig=None, counters=None, bonusCache=None, probabilityStage=0, rotationLevel=0, logTracker=None, shouldResetUsedLimits=True, ignoredLimits=None):
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
        self.__maxRotationLevel = bonusConfig.get(b'rotationLevelCount', 1) - 1 if bonusConfig else 0
        rotationLevel = min(rotationLevel, self.__maxRotationLevel)
        self.__rotationsLevel = [
         rotationLevel, rotationLevel]
        self.currentLimitsID = set()
        self.__ignoredLimits = ignoredLimits or set()
        self.__initCounters(counters or {})
        self._bonusTrack = []
        return

    def __initCounters(self, counters):
        if self.__limitsConfig:
            self.__uses = uses = {}
            self.__cooldowns = cooldowns = {}
            self.__locals = {}
            self.__bonusProbabilityUses = bonusProbabilityUses = {}
            for limitID, config in self.__limitsConfig.iteritems():
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
            for limitID, config in self.__limitsConfig.iteritems():
                if b'guaranteedFrequency' in config or b'maxFrequency' in config or b'useBonusProbabilityAfter' in config:
                    result[limitID] = (
                     cooldowns[limitID], uses[limitID], bonusProbabilityUses[limitID])

            return result or None

    def setCounters(self, counters):
        for limitID, counterTuple in counters.iteritems():
            self.__cooldowns[limitID], self.__uses[limitID], self.__bonusProbabilityUses[limitID] = counterTuple

        return

    def getBonusCache(self):
        return self.__bonusCache

    def isAcceptable(self, bonusNode, checkInventory=True, depthLevel=None):
        if self.isLimitReached(bonusNode):
            return False
        if checkInventory and self.isBonusExists(bonusNode):
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
            if limitID in self.__ignoredLimits:
                return False
            if self.__locals.get(limitID, 1) <= 0:
                return True
            if self.__cooldowns.get(limitID, 0) > 0:
                return True
            return False

    def updateBonusCache(self, bonusNode):
        cache = self.__bonusCache
        for itemType, updater in UNIQUE_BONUSES_CACHE_UPDATERS.iteritems():
            if itemType in bonusNode:
                updater(bonusNode[itemType], cache)

        return

    def updateIgnoredLimits(self, ignoredLimits):
        self.__ignoredLimits = ignoredLimits
        return

    def isBonusExists(self, bonusNode):
        cache = self.__bonusCache
        for itemType, checker in UNIQUE_BONUSES_EXISTANCE_CHECKERS.iteritems():
            if itemType in bonusNode:
                if checker(bonusNode[itemType], cache):
                    return True

        return False

    def depthCheck(self, bonusNode, checkInventory, depthLevel=None):
        currentDepthLevel = bonusNode.get(b'properties', {}).get(b'depthLevel', 0) if depthLevel is None else depthLevel
        if currentDepthLevel <= 0:
            return True
        else:
            return all(DEEP_CHECKERS[bonusNodeName](self, bonusNodeValue, checkInventory, currentDepthLevel) for bonusNodeName, bonusNodeValue in bonusNode.iteritems() if bonusNodeName in DEEP_CHECKERS)

    def getProbabilityStages(self):
        return self.__probabilitiesStage

    def setModifiedProbabilityStage(self, probabilitiesStage):
        self.__probabilitiesStage[1] = probabilitiesStage
        return

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
            rotationLevel = self.getCurrentRotationLevel()
            return self.__logTracker.generateInfo(beginStage, endStage, stagesCount, usedLimits, rotationLevel)

    def accept(self, bonusNode):
        if bonusNode.get(b'properties', {}).get(b'probabilityStageDependence', False):
            self.__increaseProbabilityStage()
        limitID = bonusNode.get(b'properties', {}).get(b'limitID', None)
        if limitID and limitID not in self.__ignoredLimits:
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
        return

    def reuse(self):
        self.__updateProbabilityStages()
        self.__resetFlags()
        self.__updateRotationLevel()
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
            for limitID, limitConfig in self.__limitsConfig.iteritems():
                if limitID in self.__ignoredLimits:
                    continue
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

    def isOverStage(self, bonusNode):
        if self.isBonusExists(bonusNode):
            return False
        return self.rotationCheck(bonusNode)

    def isMaxRotationLevel(self):
        return self.__rotationsLevel[1] == self.__maxRotationLevel

    def rotationCheck(self, bonusNode):
        rotationCheck = self.rotationCheck
        isOverStage = self.isOverStage
        getDict = bonusNode.get
        val = getDict(b'groups')
        if val is not None:
            for sub in val:
                if rotationCheck(sub):
                    break
            else:
                return False

        val = getDict(b'allof')
        if val is not None:
            for _, _, _, sub in val:
                if isOverStage(sub):
                    break
            else:
                return False

        val = getDict(b'oneof')
        if val is not None:
            for _, _, _, sub in val[1]:
                if isOverStage(sub):
                    break
            else:
                return False

        return True

    def increaseRotationLevel(self):
        if self.__rotationsLevel[1] < self.__maxRotationLevel:
            self.__rotationsLevel[1] += 1
            return
        LOG_WARNING(b'The rotation level cannot be increased above the maximum, accountID: %d' % self.__account.id)
        return

    def getCurrentRotationLevel(self):
        return self.__rotationsLevel[0]

    def getRotationLevels(self):
        return self.__rotationsLevel

    def setModifiedRotationLevel(self, rotationLevel):
        if rotationLevel <= self.__maxRotationLevel:
            self.__rotationsLevel[1] = rotationLevel
            return
        LOG_WARNING(b'The rotation level cannot be set above the maximum, accountID: %d' % self.__account.id)
        return

    def isRotation(self):
        return bool(self.__maxRotationLevel)

    def __updateRotationLevel(self):
        self.__rotationsLevel[0] = self.__rotationsLevel[1]
        return

    def reInitCounters(self, bonusConfig):
        self.__limitsConfig = bonusConfig.get(b'limits', None) if bonusConfig else None
        if self.__limitsConfig:
            cooldowns = {}
            uses = {}
            bonusProbabilityUses = {}
            for limitID, config in self.__limitsConfig.iteritems():
                if b'guaranteedFrequency' in config or b'maxFrequency' in config or b'useBonusProbabilityAfter' in config:
                    cooldowns[limitID], uses[limitID], bonusProbabilityUses[limitID] = self.__cooldowns.get(limitID, 0), self.__uses.get(limitID, 0), self.__bonusProbabilityUses.get(limitID, 0)

            self.__cooldowns = cooldowns
            self.__uses = uses
            self.__bonusProbabilityUses = bonusProbabilityUses
        else:
            self.__cooldowns = None
            self.__uses = None
            self.__bonusProbabilityUses = None
        return

    def trackChoice(self, choice):
        self._bonusTrack.append(choice)
        return

    def getBonusTrack(self):
        return _packTrack(self._bonusTrack)


class NodeVisitor(object):
    SKIP_KEYS = frozenset((b'config', b'properties', b'needsExpansion'))

    def __init__(self, mergers, args):
        self._mergers = mergers
        self._mergersArgs = args
        self._handlers = {}
        self.registerHandler(b'oneof', self.onOneOf)
        self.registerHandler(b'allof', self.onAllOf)
        self.registerHandler(b'groups', self.onGroup)
        self.registerHandler(b'rotation', self.onRotations)
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

    def onRotations(self, storage, values):
        raise NotImplementedError()
        return

    def onMergeValue(self, storage, name, value, isLeaf):
        self._mergers[name](storage, name, value, isLeaf, *self._mergersArgs)
        return

    def _beforeWalk(self, storage, bonusSection):
        return bonusSection

    def _afterWalk(self, storage, bonusSection):
        return

    def registerHandler(self, key, func):
        self._handlers[key] = WeakMethodProxy(func)
        return

    def _walkSubsection(self, storage, bonusSection):
        result = {}
        SKIP_KEYS = self.SKIP_KEYS
        onMergeValue = self.onMergeValue
        for bonusName, bonusValue in bonusSection.iteritems():
            handler = self._handlers.get(bonusName)
            if handler is not None:
                handler(result, bonusValue)
            elif bonusName in SKIP_KEYS:
                continue
            else:
                onMergeValue(result, bonusName, bonusValue, True)

        for name, value in result.iteritems():
            onMergeValue(storage, name, value, False)

        return

    def walkBonuses(self, bonusSection, storage=None):
        result = storage if storage is not None else {}
        bonusSection = self._beforeWalk(result, bonusSection)
        self._walkSubsection(result, bonusSection)
        self._afterWalk(result, bonusSection)
        return result


class TrackVisitor(NodeVisitor):

    def __init__(self, track, *args):
        super(TrackVisitor, self).__init__(BONUS_MERGERS, args)
        self.__track = _trackIterator(track)
        return

    def onOneOf(self, storage, values):
        for probability, bonusProbability, limitIDs, bonusValue in values[1]:
            if next(self.__track):
                self._walkSubsection(storage, bonusValue)
                return

        return

    def onRotations(self, storage, values):
        values = values[b'groups']
        for bonusValue in values:
            if next(self.__track):
                self._walkSubsection(storage, bonusValue)
                break

        return

    def onAllOf(self, storage, values):
        for probability, bonusProbability, refGlobalID, bonusValue in values:
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
        self.__nodeAcceptor = nodeAcceptor
        self.__preVisitor = PreVisitor(nodeAcceptor)
        return

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
                        self.__nodeAcceptor.trackChoice(False)

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
            self.__nodeAcceptor.trackChoice(False)

        self.__nodeAcceptor.trackChoice(True)
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
                self.__nodeAcceptor.trackChoice(True)
                self.__nodeAcceptor.accept(bonusValue)
                self._walkSubsection(storage, bonusValue)
            else:
                self.__nodeAcceptor.trackChoice(False)

        return

    def onGroup(self, storage, values):
        for bonusValue in values:
            self._walkSubsection(storage, bonusValue)

        return

    def onRotations(self, storage, values):
        return

    def _beforeWalk(self, storage, bonusSection):
        bonusSection = self._preVisitorWalkBonuses(bonusSection)
        acceptor = self.__nodeAcceptor
        acceptor.reuse()
        return bonusSection

    def _preVisitorWalkBonuses(self, bonusSection):
        if self.__nodeAcceptor.isRotation():
            return self.__preVisitor.walkBonuses(bonusSection)
        return bonusSection


class StripVisitor(NodeVisitor):
    NON_STRIPPED_PROPERTIES = (b'mainRotationBranch',)

    class ValuesMerger:

        def __getitem__(self, item):
            return self.copyMerger

        @staticmethod
        def copyMerger(storage, name, value, isLeaf):
            storage[name] = value
            return

    def __init__(self, needProbabilitiesInfo=False, requiredLimitIds=None):
        super(StripVisitor, self).__init__(self.ValuesMerger(), tuple())
        self.__needProbabilitiesInfo = needProbabilitiesInfo
        self.__requiredLimitIds = requiredLimitIds
        self.registerHandler(b'properties', self.onProperties)
        return

    def onRotations(self, storage, values):
        strippedValue = {}
        self._walkSubsection(strippedValue, values)
        storage[b'rotation'] = strippedValue
        return

    def onProperties(self, storage, values):
        strippedProperties = {prop: values[prop] for prop in self.NON_STRIPPED_PROPERTIES if prop in values}
        if strippedProperties:
            storage[b'properties'] = strippedProperties
        return

    def onOneOf(self, storage, values):
        strippedValues = []
        _, values = values
        needProbabilitiesInfo = self.__needProbabilitiesInfo
        requiredLimitIds = self.__requiredLimitIds
        for probability, bonusProbability, refGlobalID, bonusValue in values:
            if bonusValue.get(b'properties', {}).get(b'surprise', False):
                continue
            strippedValue = {}
            self._walkSubsection(strippedValue, bonusValue)
            strippedValues.append((
             probability if needProbabilitiesInfo else [-1],
             -1,
             refGlobalID.intersection(requiredLimitIds) if refGlobalID and requiredLimitIds else None,
             strippedValue))

        storage[b'oneof'] = (
         None, strippedValues)
        return

    def onAllOf(self, storage, values):
        strippedValues = []
        needProbabilitiesInfo = self.__needProbabilitiesInfo
        requiredLimitIds = self.__requiredLimitIds
        for probability, bonusProbability, refGlobalID, bonusValue in values:
            if bonusValue.get(b'properties', {}).get(b'surprise', False):
                continue
            strippedValue = {}
            self._walkSubsection(strippedValue, bonusValue)
            strippedValues.append((
             probability if needProbabilitiesInfo else [-1],
             -1,
             refGlobalID.intersection(requiredLimitIds) if refGlobalID and requiredLimitIds else None,
             strippedValue))

        storage[b'allof'] = strippedValues
        return

    def onGroup(self, storage, values):
        strippedValues = []
        for bonusValue in values:
            strippedValue = {}
            self._walkSubsection(strippedValue, bonusValue)
            strippedValues.append(strippedValue)

        storage[b'groups'] = strippedValues
        return


class PreVisitor(NodeVisitor):

    class ValuesMerger:

        def __getitem__(self, item):
            return self.copyMerger

        @staticmethod
        def copyMerger(storage, name, value, isLeaf):
            storage[name] = value
            return

    def __init__(self, nodeAcceptor):
        super(PreVisitor, self).__init__(self.ValuesMerger(), tuple())
        self.__nodeAcceptor = nodeAcceptor
        self.registerHandler(b'config', self.onConfig)
        self.registerHandler(b'properties', self.onProperties)
        self.__handlersSet = set(self._handlers)
        return

    def _afterWalk(self, storage, bonusSection):
        self._stripConfig(storage)
        return

    def _stripConfig(self, result):
        if self.__nodeAcceptor.currentLimitsID:
            limit = result[b'config'][b'limits']
            result[b'config'][b'limits'] = {key: limit[key] for key in self.__nodeAcceptor.currentLimitsID}
        self.__nodeAcceptor.reInitCounters(result[b'config'])
        return

    def onProperties(self, storage, values):
        limitID = values.get(b'limitID')
        if limitID:
            self.__nodeAcceptor.currentLimitsID.update({limitID})
        storage[b'properties'] = values
        return

    def onRotations(self, storage, values):
        values = values[b'groups']
        acceptor = self.__nodeAcceptor
        rotationLevel = self.__nodeAcceptor.getCurrentRotationLevel()
        if rotationLevel > 0:
            for _ in xrange(rotationLevel):
                acceptor.trackChoice(False)

        rotationBonus = {}
        for idx in xrange(rotationLevel, len(values)):
            try:
                rotationBonus.clear()
                acceptor.currentLimitsID.clear()
                self._walkSubsection(rotationBonus, values[idx])
                acceptor.trackChoice(True)
                break
            except NeedIncreaseRotationLevel:
                acceptor.trackChoice(False)
                acceptor.increaseRotationLevel()

        else:
            raise SoftException(b'Unreachable code, rotation level bug %s' % values)

        if not rotationBonus:
            raise SoftException((b'Current rotation is empty, rotationLevels: {}, rotation: {}').format(acceptor.getRotationLevels(), values))
        storage.update(rotationBonus)
        return

    def onOneOf(self, storage, values):
        limitIDs, values = values
        oneofValues = []
        for probabilities, bonusProbability, nodeLimitIDs, bonusValue in values:
            if bonusValue.get(b'properties', {}).get(b'mainRotationBranch', False) and not self.__nodeAcceptor.isMaxRotationLevel():
                if not self.__nodeAcceptor.isOverStage(bonusValue):
                    raise NeedIncreaseRotationLevel()
            oneofStorage = {}
            if not self.__handlersSet.isdisjoint(bonusValue):
                self._walkSubsection(oneofStorage, bonusValue)
            oneofValues.append((
             probabilities,
             bonusProbability,
             nodeLimitIDs,
             oneofStorage or bonusValue))

        storage[b'oneof'] = (
         limitIDs, oneofValues)
        return

    def onAllOf(self, storage, values):
        allOfValues = []
        for probabilities, bonusProbability, nodeLimitIDs, bonusValue in values:
            if bonusValue.get(b'properties', {}).get(b'mainRotationBranch', False) and not self.__nodeAcceptor.isMaxRotationLevel():
                if not self.__nodeAcceptor.isOverStage(bonusValue):
                    raise NeedIncreaseRotationLevel()
            allOfstorage = {}
            if not self.__handlersSet.isdisjoint(bonusValue):
                self._walkSubsection(allOfstorage, bonusValue)
            allOfValues.append((
             probabilities,
             bonusProbability,
             nodeLimitIDs,
             allOfstorage or bonusValue))

        storage[b'allof'] = allOfValues
        return

    def onGroup(self, storage, values):
        groupValues = []
        for bonusValue in values:
            if bonusValue.get(b'properties', {}).get(b'mainRotationBranch', False) and not self.__nodeAcceptor.isMaxRotationLevel():
                if not self.__nodeAcceptor.isOverStage(bonusValue):
                    raise NeedIncreaseRotationLevel()
            groupStorage = {}
            self._walkSubsection(groupStorage, bonusValue)
            groupValues.append(groupStorage)

        storage[b'groups'] = groupValues
        return

    def onConfig(self, storage, values):
        storage[b'config'] = deepcopy(values)
        return


class NeedIncreaseRotationLevel(SoftException):
    pass
