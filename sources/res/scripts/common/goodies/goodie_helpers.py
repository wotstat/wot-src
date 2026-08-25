from __future__ import absolute_import, division
from collections import namedtuple
from copy import deepcopy
from future.utils import viewitems
from typing import TYPE_CHECKING, Type
from goodies.GoodieConditions import MaxVehicleLevel
from goodies.GoodieDefinition import GoodieDefinition
from goodies.GoodieResources import Gold, Credits, Experience, CrewExperience, FreeExperience, FrontlineExperience
from goodies.GoodieTargets import BuyPremiumAccount, BuySlot, PostBattle, BuyGoldTankmen, BuyVehicle, EpicMeta, DemountOptionalDevice, EpicPostBattle, DropSkill, XpTransfer, BuyPet
from goodies.goodie_multiple_resources import FreeXpCrewXpMultiResourceList, FreeXpMainXpMultiResourceList
from goodies.Goodies import GoodieException
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from goodies.goodie_constants import GOODIE_TARGET_TYPE, GOODIE_CONDITION_TYPE, GOODIE_RESOURCE_TYPE
if TYPE_CHECKING:
    from typing import Tuple, Dict
    from goodies.Goodies import Goodies
    from goodies.GoodieResources import GoodieResourceType
GoodieData = namedtuple(b'GoodieData', [18, 19, 20, 21, 22, 23, 24, 
 25, 26, 27, 28])
GoodieExpirationData = namedtuple(b'GoodieExpirationData', [b'booster', b'timestamp', b'amount'])
_CONDITIONS = {(GOODIE_CONDITION_TYPE.MAX_VEHICLE_LEVEL): MaxVehicleLevel}
_TARGETS = {(GOODIE_TARGET_TYPE.ON_BUY_PREMIUM): BuyPremiumAccount, 
   (GOODIE_TARGET_TYPE.ON_BUY_SLOT): BuySlot, 
   (GOODIE_TARGET_TYPE.ON_POST_BATTLE): PostBattle, 
   (GOODIE_TARGET_TYPE.ON_BUY_GOLD_TANKMEN): BuyGoldTankmen, 
   (GOODIE_TARGET_TYPE.ON_BUY_VEHICLE): BuyVehicle, 
   (GOODIE_TARGET_TYPE.ON_EPIC_META): EpicMeta, 
   (GOODIE_TARGET_TYPE.ON_DEMOUNT_OPTIONAL_DEVICE): DemountOptionalDevice, 
   (GOODIE_TARGET_TYPE.EPIC_POST_BATTLE): EpicPostBattle, 
   (GOODIE_TARGET_TYPE.ON_DROP_SKILL): DropSkill, 
   (GOODIE_TARGET_TYPE.XP_TRANSFER): XpTransfer, 
   (GOODIE_TARGET_TYPE.ON_BUY_PET): BuyPet}
RESOURCES = {(GOODIE_RESOURCE_TYPE.GOLD): Gold, 
   (GOODIE_RESOURCE_TYPE.CREDITS): Credits, 
   (GOODIE_RESOURCE_TYPE.XP): Experience, 
   (GOODIE_RESOURCE_TYPE.CREW_XP): CrewExperience, 
   (GOODIE_RESOURCE_TYPE.FREE_XP): FreeExperience, 
   (GOODIE_RESOURCE_TYPE.FL_XP): FrontlineExperience, 
   (GOODIE_RESOURCE_TYPE.FREE_XP_CREW_XP): FreeXpCrewXpMultiResourceList, 
   (GOODIE_RESOURCE_TYPE.FREE_XP_MAIN_XP): FreeXpMainXpMultiResourceList}
RESOURCE_TO_GOODIE_LOOKUP = {resource: goodieType for goodieType, resource in viewitems(RESOURCES)}
GOODIE_CONDITION_TO_TEXT = {MaxVehicleLevel: b'max_vehicle_level'}
GOODIE_RESOURCE_TO_TEXT = {Gold: b'gold', 
   Credits: b'credits', 
   Experience: b'experience', 
   CrewExperience: b'crew_experience', 
   FreeExperience: b'free_experience', 
   FrontlineExperience: b'fl_experience', 
   FreeXpCrewXpMultiResourceList: b'free_xp_and_crew_xp'}
GOODIE_TARGET_TO_TEXT = {BuyPremiumAccount: b'premium', 
   BuySlot: b'slot', 
   PostBattle: b'post_battle', 
   BuyGoldTankmen: b'gold_tankmen', 
   BuyVehicle: b'vehicle', 
   EpicMeta: b'epic_meta', 
   DemountOptionalDevice: b'demount_optional_device', 
   EpicPostBattle: b'epic_post_battle', 
   DropSkill: b'drop_skill', 
   XpTransfer: b'xp_transfer', 
   BuyPet: b'pet'}
GOODIE_TEXT_TO_CONDITION = {b'max_vehicle_level': (GOODIE_CONDITION_TYPE.MAX_VEHICLE_LEVEL)}
GOODIE_TEXT_TO_RESOURCE = {b'credits': (GOODIE_RESOURCE_TYPE.CREDITS), 
   b'experience': (GOODIE_RESOURCE_TYPE.XP), 
   b'crew_experience': (GOODIE_RESOURCE_TYPE.CREW_XP), 
   b'free_experience': (GOODIE_RESOURCE_TYPE.FREE_XP), 
   b'gold': (GOODIE_RESOURCE_TYPE.GOLD), 
   b'fl_experience': (GOODIE_RESOURCE_TYPE.FL_XP), 
   b'free_xp_and_crew_xp': (GOODIE_RESOURCE_TYPE.FREE_XP_CREW_XP), 
   b'free_xp_and_main_xp': (GOODIE_RESOURCE_TYPE.FREE_XP_MAIN_XP)}
GOODIE_TEXT_TO_TARGET = {b'premium': (GOODIE_TARGET_TYPE.ON_BUY_PREMIUM), 
   b'slot': (GOODIE_TARGET_TYPE.ON_BUY_SLOT), 
   b'post_battle': (GOODIE_TARGET_TYPE.ON_POST_BATTLE), 
   b'gold_tankmen': (GOODIE_TARGET_TYPE.ON_BUY_GOLD_TANKMEN), 
   b'vehicle': (GOODIE_TARGET_TYPE.ON_BUY_VEHICLE), 
   b'epic_meta': (GOODIE_TARGET_TYPE.ON_EPIC_META), 
   b'demount_optional_device': (GOODIE_TARGET_TYPE.ON_DEMOUNT_OPTIONAL_DEVICE), 
   b'epic_post_battle': (GOODIE_TARGET_TYPE.EPIC_POST_BATTLE), 
   b'drop_skill': (GOODIE_TARGET_TYPE.ON_DROP_SKILL), 
   b'xp_transfer': (GOODIE_TARGET_TYPE.XP_TRANSFER), 
   b'pet': (GOODIE_TARGET_TYPE.ON_BUY_PET)}
CURRENCY_TO_RESOURCE_TYPE = {b'gold': (GOODIE_RESOURCE_TYPE.GOLD), 
   b'credits': (GOODIE_RESOURCE_TYPE.CREDITS)}
CURRENCY_TO_RESOURCE = {k: RESOURCES[v] for k, v in viewitems(CURRENCY_TO_RESOURCE_TYPE)}

def loadDefinitions(d):
    goodies = {b'goodies': {}, b'prices': (deepcopy(d[b'prices'])), b'notInShop': (deepcopy(d[b'notInShop']))}
    for uid, definition in viewitems(d[b'goodies']):
        v_variety, v_target, v_enabled, v_lifetime, v_useby, v_limit, v_autostart, v_condition, v_resource, v_expireAfter, v_roundToEndOfGameDay = definition
        if v_condition is not None:
            condition = _CONDITIONS.get(v_condition[0])(v_condition[1])
        else:
            condition = None
        target = _TARGETS[v_target[0]](v_target[1], v_target[2])
        resource = RESOURCES[v_resource[0]]
        value = resource.provideCompatibleValueDescr(actualVal=v_resource[1], isPercent=v_resource[2])
        goodies[b'goodies'][uid] = GoodieDefinition(uid=uid, variety=v_variety, target=target, enabled=v_enabled, lifetime=v_lifetime, useby=v_useby, counter=v_limit, autostart=v_autostart, resource=resource, value=value, condition=condition, expireAfter=v_expireAfter, roundToEndOfGameDay=v_roundToEndOfGameDay)

    return goodies


def getPriceWithDiscount(price, resourceData):
    _, value, isPercentage = resourceData
    if isPercentage:
        result = int(price - price * (value / float(100)))
        if result < 0:
            return 0
        return result
    else:
        return max(price - value, 0)
    return


def getPremiumCost(premiumCosts, goodie):
    if goodie.target[0] == GOODIE_TARGET_TYPE.ON_BUY_PREMIUM:
        price = premiumCosts.get(goodie.getTargetValue(), None)
        if price is None:
            return
        return getPriceWithDiscount(price, goodie.resource)
    else:
        return


def loadPdata(pdataGoodies, goodies, logID):
    for uid, (status, finishTime, count, expirations) in viewitems(pdataGoodies):
        try:
            goodies.load(uid, status, finishTime, count, expirations)
        except GoodieException as detail:
            LOG_CURRENT_EXCEPTION()
            LOG_ERROR(b'Cannot load a goodie', detail, logID)

    return


def calcDefaultPrice(default, actual):
    result = {}
    defaultPrices = default[b'prices']
    actualPrices = actual[b'prices']
    for goodieID, defaultPrice in viewitems(defaultPrices):
        actualPrice = actualPrices.get(goodieID, None)
        if actualPrice is None:
            continue
        changedCredits = changedGold = 0
        if defaultPrice[0] > actualPrice[0]:
            changedCredits = defaultPrice[0] - actualPrice[0]
        if defaultPrice[1] > actualPrice[1]:
            changedGold = defaultPrice[1] - actualPrice[1]
        if changedCredits or changedGold:
            result[goodieID] = (
             changedCredits, changedGold)

    return result


def wipe(goodies, pdata, leaveGold):
    if leaveGold:
        for goodieID in list(pdata[b'goodies']):
            price = goodies[b'prices'].get(goodieID, None)
            if price is not None and price[0] != 0:
                del pdata[b'goodies'][goodieID]

    else:
        pdata[b'goodies'].clear()
    if b'pr2_conversion' in pdata:
        del pdata[b'pr2_conversion']
    return
