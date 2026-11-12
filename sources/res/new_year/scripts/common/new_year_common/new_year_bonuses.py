from constants import ALL_EVENT_TYPES_FOR_BONUSES
from constants_utils import AbstractExtensionBonuses
from functools import partial
from new_year_common.items import collectibles
from new_year_common.items.components.ny_constants import CurrentNYConstants, TOY_TYPE_IDS_BY_NAME, YEARS_INFO, YEARS, PREV_NY_TOYS_COLLECTIONS, TOY_PARAMETER
from optional_bonuses import __mergeItems as mergeItems, __mergeValue as mergeValue
from soft_exception import SoftException

class NewYearBonuses(AbstractExtensionBonuses):

    def _getSupportedQuests(self):
        return {ALL_EVENT_TYPES_FOR_BONUSES: {
                                       CurrentNYConstants.FILLERS,
                                       CurrentNYConstants.TOY_BONUS,
                                       CurrentNYConstants.ANY_OF,
                                       CurrentNYConstants.ATMOSPHERE_POINTS,
                                       CurrentNYConstants.ALL_OF}}

    def _getReaders(self):
        result = {(CurrentNYConstants.ANY_OF): (NewYearBonuses.__readBonusNYAnyOf), 
           (CurrentNYConstants.FILLERS): (NewYearBonuses.__readBonusNYFillers), 
           (CurrentNYConstants.ATMOSPHERE_POINTS): (NewYearBonuses.__readBonusNYAtmospherePoints), 
           (CurrentNYConstants.ALL_OF): (NewYearBonuses.__readBonusNYAllOf)}
        result.update({YEARS_INFO.getToyBonusTagForYear(year): partial(NewYearBonuses.__readBonusNYToy, year) for year in YEARS.ALL})
        return result

    def _getMergers(self):
        result = {(CurrentNYConstants.TOYS): mergeItems, 
           (CurrentNYConstants.ANY_OF): (NewYearBonuses.__mergeNYAnyOf), 
           (CurrentNYConstants.FILLERS): mergeValue, 
           (CurrentNYConstants.ATMOSPHERE_POINTS): mergeValue, 
           (CurrentNYConstants.ALL_OF): mergeItems}
        result.update({collection: mergeItems for collection in PREV_NY_TOYS_COLLECTIONS})
        return result

    def _getItemInventoryCheckers(self):
        return {(CurrentNYConstants.TOYS): (lambda account, key: account.AccountNewYearComponent.isToyPresentInCollection(key, YEARS_INFO.CURRENT_YEAR_STR))}

    def _getUniqueBonusCheckers(self):
        return {(CurrentNYConstants.TOYS): (NewYearBonuses.__nyToysExistanceChecker)}

    def _getUniqueBonusCacheUpdater(self):
        return {(CurrentNYConstants.TOYS): (NewYearBonuses.__nyToysCacheUpdater)}

    def _getConverterProcessor(self):
        return {(CurrentNYConstants.TOYS): (
                                     CurrentNYConstants.TOY_REWARD_ITEM_ID, self.__convertToys, self.__unpackToys)}

    @staticmethod
    def __convertToys(_, rewards):
        result = []
        for itemCompDescr, itemCount in rewards.iteritems():
            convertItemDict = {b'item_type_id': (CurrentNYConstants.TOY_REWARD_ITEM_ID), b'item_type_cd': itemCompDescr, 
               b'amount': itemCount}
            result.append(convertItemDict)

        return result

    @staticmethod
    def __unpackToys(item):
        return {(CurrentNYConstants.TOYS): {(item[b'item_type_cd']): (item[b'amount'])}}

    @staticmethod
    def __readBonusNYToy(year, bonus, name, section, eventType, checkLimit):
        if section.has_key(b'id'):
            tid = section[b'id'].asInt
            cache = collectibles.g_cache[YEARS.getYearStrFromYearNum(year)].toys
            if tid not in cache:
                raise SoftException((b'Unknown NY{} toyID: {}').format(year, tid))
            count = section[b'count'].asInt if section.has_key(b'count') else 0
            toysCollectionKey = YEARS_INFO.getCollectionKeyForYear(year)
            nyToys = bonus.setdefault(toysCollectionKey, {})
            nyToys[tid] = count
        return

    @staticmethod
    def __nyToysExistanceChecker(bonusValue, cache):
        for itemID in bonusValue.iterkeys():
            if cache.isItemExists(CurrentNYConstants.TOYS, itemID):
                return True

        return False

    @staticmethod
    def __nyToysCacheUpdater(bonusValue, cache):
        for itemID in bonusValue.iterkeys():
            cache.onItemAccepted(CurrentNYConstants.TOYS, itemID)

        return

    @staticmethod
    def __readBonusNYAnyOf(bonus, name, section, eventType, checkLimit):
        if section.has_key(b'setting'):
            settingID = YEARS_INFO.CURRENT_SETTING_IDS_BY_NAME[section.readString(b'setting')]
            if settingID not in TOY_PARAMETER.CURRENT_USUAL_RANGE:
                raise SoftException((b'Unavailable toy setting - {}').format(settingID))
        else:
            settingID = -1
        if section.has_key(b'type'):
            typeID = TOY_TYPE_IDS_BY_NAME[section.readString(b'type')]
            if typeID not in TOY_PARAMETER.TOY_USUAL_TYPES_RANGE:
                raise SoftException((b'Unavailable toy type - {}').format(typeID))
        else:
            typeID = -1
        if section.has_key(b'rank'):
            rank = section[b'rank'].asInt
        else:
            rank = -1
        bonus.setdefault(CurrentNYConstants.ANY_OF, []).append((typeID, settingID, rank))
        return

    @staticmethod
    def __mergeNYAnyOf(total, key, value, isLeaf=False, count=1, *args):
        result = total.setdefault(key, [])
        result.extend(value if isinstance(value, list) else [value])
        return

    @staticmethod
    def __readBonusNYAllOf(bonus, name, section, eventType, checkLimit):
        if section.has_key(b'setting'):
            settingID = YEARS_INFO.CURRENT_SETTING_IDS_BY_NAME[section.readString(b'setting')]
        else:
            settingID = -1
        if section.has_key(b'type'):
            typeID = TOY_TYPE_IDS_BY_NAME[section.readString(b'type')]
        else:
            typeID = -1
        if section.has_key(b'rank'):
            rank = section[b'rank'].asInt
        else:
            rank = -1
        if section.has_key(b'count'):
            count = section[b'count'].asInt
        else:
            count = 1
        bonus.setdefault(CurrentNYConstants.ALL_OF, {}).setdefault((typeID, settingID, rank), 0)
        bonus[CurrentNYConstants.ALL_OF][(typeID, settingID, rank)] += count
        return

    @staticmethod
    def __readBonusNYFillers(bonus, name, section, eventType, checkLimit):
        count = section.asInt
        bonus[CurrentNYConstants.FILLERS] = bonus.get(CurrentNYConstants.FILLERS, 0) + count
        return

    @staticmethod
    def __readBonusNYAtmospherePoints(bonus, name, section, eventType, checkLimit):
        count = section.asInt
        bonus[CurrentNYConstants.ATMOSPHERE_POINTS] = bonus.get(CurrentNYConstants.ATMOSPHERE_POINTS, 0) + count
        return
