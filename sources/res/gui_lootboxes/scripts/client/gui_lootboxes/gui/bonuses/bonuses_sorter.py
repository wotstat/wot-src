import itertools, typing
from constants import LOOTBOX_TOKEN_PREFIX, PREMIUM_ENTITLEMENTS, LOOTBOX_KEY_PREFIX
from gui.server_events.bonuses import VehiclesBonus, splitBonuses
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.money import Currency
from gui_lootboxes.gui.bonuses.bonuses_helpers import TOKEN_COMPENSATION_PREFIX, parseCompenstaionToken
from gui_lootboxes.gui.bonuses.bonuses_order_config import BonusesSortTags
from helpers import dependency
from shared_utils import first
from skeletons.gui.game_control import IGuiLootBoxesController
VEHICLE_MAX_LEVEL = 10
__VEHICLES_REVERSED_COUNTER = itertools.count(0, -1)
__CURRENCY_ORDER = (Currency.GOLD, Currency.CREDITS, Currency.FREE_XP, Currency.CRYSTAL, Currency.EQUIP_COIN)

def _getCustomizationTag(bonus):
    item = bonus.getC11nItem(first(bonus.getCustomizations()))
    if item.itemTypeID == GUI_ITEM_TYPE.STYLE and item.is3D:
        return BonusesSortTags.UNIQUE_CUSTOMIZATION
    if item.itemTypeID == GUI_ITEM_TYPE.STYLE:
        return BonusesSortTags.STYLE
    return BonusesSortTags.CUSTOMIZATION


def _getGoodiesTag(bonus):
    booster = first(bonus.getBoosters().keys())
    if booster is not None:
        return BonusesSortTags.PERSONAL_BOOSTER
    else:
        rf = first(bonus.getRecertificationForms().keys())
        if rf is not None:
            return BonusesSortTags.CURRENCY
        dk = first(bonus.getDemountKits().keys())
        if dk is not None:
            return BonusesSortTags.CURRENCY
        return BonusesSortTags.UNSORTABLE


def _getItemTag(bonus):
    item = first(bonus.getItems().keys())
    itemTypeID = item.itemTypeID
    if itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE and (item.isDeluxe or item.isTrophy or item.isModernized):
        return BonusesSortTags.RARITY_OPT_DEV
    if itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
        return BonusesSortTags.OPT_DEV
    if itemTypeID == GUI_ITEM_TYPE.EQUIPMENT:
        return BonusesSortTags.EQUIPMENT
    return BonusesSortTags.BATTLE_BOOSTER


def _getTankmenTag(bonus):
    tankman = first(bonus.getTankmenDescriptors())
    if tankman.isUnique:
        return BonusesSortTags.UNIQUE_TANKMEN
    return BonusesSortTags.TANKMEN


def _getTankmenTokenTag(bonus):
    info = getRecruitInfo(first(bonus.getTokens().iterkeys()))
    if info and info.isUnique():
        return BonusesSortTags.UNIQUE_TANKMEN
    return BonusesSortTags.TANKMEN


def _getTokensTag(bonus):
    tokenId = first(bonus.getTokens().iterkeys())
    if tokenId.startswith(TOKEN_COMPENSATION_PREFIX):
        _, _, item, _ = parseCompenstaionToken(tokenId)
        if item == b'cllc':
            return BonusesSortTags.CLLC_ITEM_COMP
    if tokenId.startswith(LOOTBOX_TOKEN_PREFIX):
        return BonusesSortTags.CUSTOM_LOOTBOX
    if tokenId.startswith(LOOTBOX_KEY_PREFIX):
        return BonusesSortTags.CUSTOM_LOOTBOXKEY
    return BonusesSortTags.UNSORTABLE


BONUS_TAG_HANDLER_MAP = {(Currency.CREDITS): (lambda b: BonusesSortTags.CURRENCY), 
   (Currency.GOLD): (lambda b: BonusesSortTags.RARITY_CURRENCY), 
   (Currency.CRYSTAL): (lambda b: BonusesSortTags.RARITY_CURRENCY), 
   (Currency.EVENT_COIN): (lambda b: BonusesSortTags.CURRENCY), 
   (Currency.BPCOIN): (lambda b: BonusesSortTags.CURRENCY), 
   (Currency.EQUIP_COIN): (lambda b: BonusesSortTags.RARITY_CURRENCY), 
   b'slots': (lambda b: BonusesSortTags.SLOT), 
   b'berths': (lambda b: BonusesSortTags.BERTH), 
   (PREMIUM_ENTITLEMENTS.BASIC): (lambda b: BonusesSortTags.PREMIUM), 
   (PREMIUM_ENTITLEMENTS.PLUS): (lambda b: BonusesSortTags.PREMIUM), 
   (VehiclesBonus.VEHICLES_BONUS): (lambda b: BonusesSortTags.VEHICLE), 
   b'tankmen': _getTankmenTag, 
   b'customizations': _getCustomizationTag, 
   b'lbStyleProgress': (lambda b: BonusesSortTags.LB_STYLE_PROGRESS), 
   b'goodies': _getGoodiesTag, 
   b'items': _getItemTag, 
   b'blueprints': (lambda b: BonusesSortTags.BLUEPRINT), 
   b'blueprintsAny': (lambda b: BonusesSortTags.BLUEPRINT), 
   b'crewSkins': (lambda b: BonusesSortTags.CUSTOMIZATION), 
   b'collectionItem': (lambda b: BonusesSortTags.NARRATIVE_CLLC_ITEM), 
   b'randomCrewbook': (lambda b: BonusesSortTags.CREW_BOOK), 
   b'crewBooks': (lambda b: BonusesSortTags.CREW_BOOK), 
   b'dogTagComponents': (lambda b: BonusesSortTags.CUSTOMIZATION), 
   b'preferredMapSlots': (lambda b: BonusesSortTags.CUSTOMIZATION), 
   b'dossier': (lambda b: BonusesSortTags.CUSTOMIZATION), 
   b'tmanToken': _getTankmenTokenTag, 
   b'battleToken': _getTokensTag, 
   b'freeXP': (lambda b: BonusesSortTags.CURRENCY), 
   b'entitlements': (lambda b: BonusesSortTags.CURRENCY), 
   b'lootBoxToken': (lambda b: BonusesSortTags.CUSTOM_LOOTBOX), 
   b'currencies': (lambda b: BonusesSortTags.CUSTOM_CURRENCY)}

def getVehBonusSortKey(bonus):
    vehicle, vehInfo = first(bonus.getVehicles())
    compensatedNumber = vehInfo.get(b'compensatedNumber', 0)
    compensation = vehInfo.get(b'customCompensation')
    hasCompensation = compensatedNumber and compensation is not None
    return (hasCompensation, -vehicle.level, vehicle)


@dependency.replace_none_kwargs(guiLootBoxController=IGuiLootBoxesController)
def getTokensSortKey(bonus, guiLootBoxController=None):
    tokenId = first(bonus.getTokens().iterkeys())
    if tokenId.startswith(LOOTBOX_KEY_PREFIX) and guiLootBoxController is not None:
        lbKey = guiLootBoxController.getKeyByTokenID(tokenId)
        if lbKey is not None:
            return -lbKey.openProbability
    if tokenId.startswith(LOOTBOX_TOKEN_PREFIX) and guiLootBoxController is not None:
        lb = guiLootBoxController.getGuiLootBoxByTokenID(tokenId)
        if lb is not None:
            return -lb.getWeight()
    return bonus.getName()


BONUSES_KEY_FUNC = {b'items': (lambda b: first(b.getItems())), 
   b'crewBooks': (lambda b: first(b.getItems())), 
   b'vehicles': getVehBonusSortKey, 
   b'battleToken': getTokensSortKey, 
   b'lbStyleProgress': (lambda b: b.getProgressLevel())}

def _defaultBonusKeyFunc(bonus):
    return bonus.getName()


def getBonusSortTag(bonus):
    return BONUS_TAG_HANDLER_MAP.get(bonus.getName(), (lambda b: BonusesSortTags.UNSORTABLE))(bonus)


def getBonusesSortKeyFunc(order):
    return (lambda b: (
     order.index(getBonusSortTag(b)), BONUSES_KEY_FUNC.get(b.getName(), _defaultBonusKeyFunc)(b)))


def sortBonuses(bonuses, order, sortFunc=getBonusesSortKeyFunc):
    return sorted(splitBonuses(bonuses), key=sortFunc(order))


def getStatisticSortKeyFunc(order):
    mapping = {b'items': (lambda b: first(b.getItems())), 
       b'crewBooks': (lambda b: first(b.getItems())), 
       b'battleToken': getTokensSortKey, 
       b'vehicles': (lambda b: next(__VEHICLES_REVERSED_COUNTER)), 
       (Currency.CREDITS): (lambda b: __CURRENCY_ORDER.index(b.getName())), 
       (Currency.GOLD): (lambda b: __CURRENCY_ORDER.index(b.getName())), 
       (Currency.CRYSTAL): (lambda b: __CURRENCY_ORDER.index(b.getName())), 
       (Currency.FREE_XP): (lambda b: __CURRENCY_ORDER.index(b.getName())), 
       (Currency.EQUIP_COIN): (lambda b: __CURRENCY_ORDER.index(b.getName())), 
       b'lbStyleProgress': (lambda b: b.getProgressLevel())}
    return (lambda b: (
     order.index(getBonusSortTag(b)), mapping.get(b.getName(), _defaultBonusKeyFunc)(b)))
