from string import lower
from typing import TYPE_CHECKING
from constants import LOOTBOX_KEY_PREFIX, LOOTBOX_TOKEN_PREFIX, VERY_BIG_TIME
from items import makeIntCompactDescrByID, parseIntCompactDescr
from items.components.c11n_constants import CustomizationNamesToTypes, CustomizationTypeNames
from optional_bonuses import BONUS_MERGERS
from soft_exception import SoftException
AVAILABLE_STATISTICS_STORAGE = (b'pdata', b'webservice')
if TYPE_CHECKING:
    from typing import Any, Callable, Dict, List, Union

class _LootboxTokenPrefix(object):
    LB_COMP = b'lb_comp:'
    LB_LIMIT_ITEM = b'lb_limit_item:'


class _TokenPostfix(object):
    HIDDEN_FROM_CLIENT = b'_srv'
    NO_LOG = b'_no_log'


def makeLootboxTokenID(boxID):
    return LOOTBOX_TOKEN_PREFIX + str(boxID)


def makeLBKeyTokenID(keyID):
    return LOOTBOX_KEY_PREFIX + str(keyID)


def makeLootboxID(tokenName):
    try:
        if tokenName.startswith(LOOTBOX_TOKEN_PREFIX):
            strID = tokenName[len(LOOTBOX_TOKEN_PREFIX):]
            return int(strID)
    except Exception:
        pass

    raise SoftException((b'Invalid tokenName: {}').format(tokenName))
    return


def makeLBKeyID(tokenName):
    try:
        if tokenName.startswith(LOOTBOX_KEY_PREFIX):
            strID = tokenName[len(LOOTBOX_KEY_PREFIX):]
            return int(strID)
    except Exception:
        pass

    raise SoftException((b'Invalid tokenName: {}').format(tokenName))
    return


def isLootboxToken(tokenName):
    try:
        makeLootboxID(tokenName)
        return True
    except Exception:
        return False

    return


def __pruneVehicles(rewards):
    result = []
    for vehiclesDict in rewards:
        newVehiclesDict = {}
        for vehCD, vehicleData in vehiclesDict.iteritems():
            if b'rentCompensation' in vehicleData:
                continue
            if b'customCompensation' in vehicleData:
                continue
            newVehiclesDict[vehCD] = vehicleData

        if newVehiclesDict:
            result.append(newVehiclesDict)

    return result


def __pruneTokens(rewards):
    result = {}
    for tokenID, data in rewards.iteritems():
        maySendToClient = not any({
         tokenID.endswith(_TokenPostfix.NO_LOG),
         tokenID.endswith(_TokenPostfix.HIDDEN_FROM_CLIENT),
         tokenID.startswith(_LootboxTokenPrefix.LB_COMP),
         tokenID.startswith(_LootboxTokenPrefix.LB_LIMIT_ITEM),
         data.get(b'count', 0) < 0})
        if not maySendToClient:
            continue
        result[tokenID] = data

    return result


def __pruneCustomizations(rewards):
    result = []
    for customization in rewards:
        if customization.get(b'boundToCurrentVehicle', False):
            continue
        if customization.get(b'customCompensation'):
            continue
        result.append(customization)

    return result


_PRUNE_MERGERS = {b'vehicles': __pruneVehicles, 
   b'tokens': __pruneTokens, 
   b'customizations': __pruneCustomizations, 
   b'meta': (lambda v: None)}

def mergeDiffStat(storage, diff):
    for key, value in diff.iteritems():
        if key in _PRUNE_MERGERS:
            value = _PRUNE_MERGERS[key](value)
            if not value:
                continue
        if key in BONUS_MERGERS:
            BONUS_MERGERS[key](storage, key, value, False, 1, None)

    return


REWARD_ITEM_IDS = {b'freeXP': 1, b'credits': 2, 
   b'gold': 3, 
   b'crystal': 4, 
   b'eventCoin': 5, 
   b'bpcoin': 6, 
   b'equipCoin': 7, 
   b'premium_plus': 8, 
   b'slots': 9, 
   b'berths': 10, 
   b'items': 11, 
   b'vehicles': 12, 
   b'tankmen': 13, 
   b'crewSkins': 14, 
   b'tokens': 15, 
   b'goodies': 16, 
   b'customizations': 17, 
   b'dossier': 18, 
   b'blueprints': 19, 
   b'entitlements': 20, 
   b'currencies': 21, 
   b'dogTagComponents': 22, 
   b'preferredMapSlots': 23}
ID_TO_NAME = dict((v, k) for k, v in REWARD_ITEM_IDS.iteritems())
EXTENSIONS_CONVERTER_PROCESSOR = {}
EXTENSIONS_UNPACK_PROCESSOR = {}

def __convertVehicles(_, rewards):
    result = []
    for vehiclesDict in rewards:
        for vehCD in vehiclesDict.iterkeys():
            convertVehicleDict = {b'item_type_id': (REWARD_ITEM_IDS[b'vehicles']), 
               b'item_type_cd': vehCD, 
               b'amount': 1}
            result.append(convertVehicleDict)

    return result


def __convertTokens(_, rewards):
    result = []
    for tokenName, tokenData in rewards.iteritems():
        convertTokenDict = {b'value_type_id': (REWARD_ITEM_IDS[b'tokens']), 
           b'amount': (tokenData[b'count']), 
           b'ext_info': tokenName}
        result.append(convertTokenDict)

    return result


def __convertGoodies(_, rewards):
    result = []
    for goodieID, goodieData in rewards.iteritems():
        convertGoodieDict = {b'item_type_id': (REWARD_ITEM_IDS[b'goodies']), 
           b'amount': (goodieData[b'count']), 
           b'item_type_cd': goodieID}
        result.append(convertGoodieDict)

    return result


def __convertDossier(_, rewards):
    result = []
    for dossierType, changes in rewards.iteritems():
        for _ in changes.iteritems():
            convertDossierDict = {b'item_type_id': (REWARD_ITEM_IDS[b'dossier'])}
            result.append(convertDossierDict)

    return result


def __convertItems(_, rewards):
    result = []
    for itemCompDescr, itemCount in rewards.iteritems():
        convertItemDict = {b'item_type_id': (REWARD_ITEM_IDS[b'items']), 
           b'amount': itemCount, 
           b'item_type_cd': itemCompDescr}
        result.append(convertItemDict)

    return result


def __convertCustomizations(_, rewards):
    result = []
    for customizationData in rewards:
        custType = CustomizationNamesToTypes[customizationData[b'custType'].upper()]
        cid = customizationData[b'id']
        convertCustomizationDict = {b'item_type_id': (REWARD_ITEM_IDS[b'customizations']), 
           b'amount': (customizationData[b'value']), 
           b'item_type_cd': (makeIntCompactDescrByID(b'customizationItem', custType, cid))}
        result.append(convertCustomizationDict)

    return result


def __convertBlueprints(_, rewards):
    result = []
    for fragmentID, count in rewards.iteritems():
        convertBlueprintDict = {b'item_type_id': (REWARD_ITEM_IDS[b'blueprints']), 
           b'amount': count, 
           b'item_type_cd': fragmentID}
        result.append(convertBlueprintDict)

    return result


def __convertEntitlements(_, rewards):
    result = []
    for entitlementCode, entitlementData in rewards.iteritems():
        convertEntitlementDict = {b'value_type_id': (REWARD_ITEM_IDS[b'entitlements']), 
           b'amount': (entitlementData[b'count']), 
           b'ext_info': entitlementCode}
        result.append(convertEntitlementDict)

    return result


def __convertCrewSkins(_, rewards):
    result = []
    for crewSkinData in rewards:
        convertCrewSkinDict = {b'item_type_id': (REWARD_ITEM_IDS[b'crewSkins']), 
           b'amount': (crewSkinData[b'count']), 
           b'item_type_cd': (crewSkinData[b'id'])}
        result.append(convertCrewSkinDict)

    return result


def __convertEntitlementList(_, rewards):
    result = []
    for entitlementData in rewards:
        convertEntitlementDict = {b'value_type_id': (REWARD_ITEM_IDS[b'entitlements']), 
           b'amount': (entitlementData[b'count']), 
           b'ext_info': (entitlementData[b'id'])}
        result.append(convertEntitlementDict)

    return result


def __convertCurrencies(_, rewards):
    result = []
    for currencyCode, currencyData in rewards.iteritems():
        convertCurrencyDict = {b'value_type_id': (REWARD_ITEM_IDS[b'currencies']), 
           b'amount': (currencyData[b'count']), 
           b'ext_info': currencyCode}
        result.append(convertCurrencyDict)

    return result


def __convertPreferredMapSlots(_, rewards):
    result = []
    for slotID, slotDurationDays in rewards.iteritems():
        result.append({b'value_type_id': (REWARD_ITEM_IDS[b'preferredMapSlots']), 
           b'amount': slotDurationDays, 
           b'ext_info': slotID})

    return result


def __unpackPreferredMapSlots(item):
    slotID = item[b'ext_info']
    if not isinstance(slotID, int):
        slotID = int(slotID)
    return {b'preferredMapSlots': {slotID: (item[b'amount'])}}


def __defaultConverter(bonusName, rewards):
    result = []
    if isinstance(rewards, int):
        convertDict = {b'value_type_id': (REWARD_ITEM_IDS[bonusName]), b'amount': rewards}
        result.append(convertDict)
    return result


def getDefaultConverterProcessor():
    default = {b'freeXP': __defaultConverter, 
       b'credits': __defaultConverter, 
       b'gold': __defaultConverter, 
       b'crystal': __defaultConverter, 
       b'eventCoin': __defaultConverter, 
       b'bpcoin': __defaultConverter, 
       b'equipCoin': __defaultConverter, 
       b'premium_plus': __defaultConverter, 
       b'slots': __defaultConverter, 
       b'berths': __defaultConverter, 
       b'vehicles': __convertVehicles, 
       b'items': __convertItems, 
       b'tokens': __convertTokens, 
       b'goodies': __convertGoodies, 
       b'dossier': (lambda n, v: []), b'tankmen': (lambda n, v: []), b'customizations': __convertCustomizations, 
       b'crewSkins': __convertCrewSkins, 
       b'blueprints': __convertBlueprints, 
       b'entitlements': __convertEntitlements, 
       b'entitlementList': __convertEntitlementList, 
       b'currencies': __convertCurrencies, 
       b'dogTagComponents': (lambda n, v: []), b'preferredMapSlots': __convertPreferredMapSlots}
    default.update(EXTENSIONS_CONVERTER_PROCESSOR)
    return default


def __defaultUnpacker(item):
    return {(ID_TO_NAME[item[b'value_type_id']]): (item[b'amount'])}


def __unpackVehicles(item):
    return {b'vehicles': [{(item[b'item_type_cd']): {}}]}


def __unpackItems(item):
    return {b'items': {(item[b'item_type_cd']): (item[b'amount'])}}


def __unpackTokens(item):
    return {b'tokens': {(item[b'ext_info']): {b'count': (item[b'amount']), b'expires': {b'at': VERY_BIG_TIME}}}}


def __unpackGoodies(item):
    return {b'goodies': {(item[b'item_type_cd']): {b'count': (item[b'amount'])}}}


def __unpackCustomizations(item):
    _, ctype, cid = parseIntCompactDescr(item[b'item_type_cd'])
    return {b'customizations': [
                         {b'custType': (lower(CustomizationTypeNames[ctype])), 
                            b'id': cid, 
                            b'value': (item[b'amount']), 
                            b'isPermanent': True}]}


def __unpackCrewSkins(item):
    return {b'crewSkins': [{b'count': (item[b'amount']), b'id': (item[b'item_type_cd'])}]}


def __unpackBlueprints(item):
    return {b'blueprints': {(item[b'item_type_cd']): (item[b'amount'])}}


def __unpackCurrencies(item):
    return {b'currencies': {(item[b'ext_info']): {b'count': (item[b'amount'])}}}


def __unpackEntitlements(item):
    return {b'entitlements': {(item[b'ext_info']): {b'count': (item[b'amount'])}}}


def getDefaultUnpackProcessor():
    default = {b'freeXP': __defaultUnpacker, 
       b'credits': __defaultUnpacker, 
       b'gold': __defaultUnpacker, 
       b'crystal': __defaultUnpacker, 
       b'eventCoin': __defaultUnpacker, 
       b'bpcoin': __defaultUnpacker, 
       b'equipCoin': __defaultUnpacker, 
       b'premium_plus': __defaultUnpacker, 
       b'slots': __defaultUnpacker, 
       b'berths': __defaultUnpacker, 
       b'vehicles': __unpackVehicles, 
       b'items': __unpackItems, 
       b'tokens': __unpackTokens, 
       b'goodies': __unpackGoodies, 
       b'dossier': (lambda i: {}), b'tankmen': (lambda i: {}), b'customizations': __unpackCustomizations, 
       b'crewSkins': __unpackCrewSkins, 
       b'blueprints': __unpackBlueprints, 
       b'entitlements': __unpackEntitlements, 
       b'entitlementList': (lambda i: {}), b'currencies': __unpackCurrencies, 
       b'dogTagComponents': (lambda i: {}), b'preferredMapSlots': __unpackPreferredMapSlots}
    default.update(EXTENSIONS_UNPACK_PROCESSOR)
    return default


def packLootboxResultToKafka(appliedResult):
    kafkaLog = []
    converterProcess = getDefaultConverterProcessor()
    for bonusName, bonus in appliedResult.iteritems():
        if bonusName in _PRUNE_MERGERS:
            bonus = _PRUNE_MERGERS[bonusName](bonus)
            if not bonus:
                continue
        if bonusName in converterProcess:
            result = converterProcess[bonusName](bonusName, bonus)
            kafkaLog.extend(result)

    return kafkaLog


def unpackLootboxStatistic(statistic):
    result = {}
    unpackProcessor = getDefaultUnpackProcessor()
    for item in statistic:
        rewardItemID = item.get(b'value_type_id') or item.get(b'item_type_id')
        bonusName = ID_TO_NAME[rewardItemID]
        if bonusName in unpackProcessor:
            unpackRes = unpackProcessor[bonusName](item)
            mergeDiffStat(result, unpackRes)

    return result
