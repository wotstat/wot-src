import re
from collections import namedtuple
import typing, nations
from constants import RentType
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.game_control.veh_comparison_basket import isValidVehicleForComparing
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items import CREW_SKILL_TO_KPI_NAME_MAP, GUI_ITEM_TYPE, KPI
from gui.shared.gui_items.Vehicle import Vehicle, getShortUserName, getUserName
from gui.shop import SHOP_RENT_SEASON_TYPE_MAP, SHOP_RENT_TYPE_MAP
from helpers import dependency, i18n, time_utils
from helpers.func_utils import replaceImgPrefix
from items.components.supply_slot_categories import SlotCategories
from items import vehicles
from nation_change.nation_change_helpers import getGroupByVehTypeCompactDescr, iterVehTypeCDsInNationGroup
from rent_common import SeasonRentDuration
from shared_utils import first
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Dict, Union, Any, Optional
    from gui.shared.gui_items.Tankman import Tankman
    from web.web_client_api.shop.crew import _ShopTankman, _ShopRecruit
    AnyTankman = Union[Tankman, _ShopTankman, _ShopRecruit]
COLOR_TAG_OPEN = b'{colorTagOpen}'
COLOR_TAG_CLOSE = b'{colorTagClose}'
_WHITESPACE_RE = re.compile(b'\\s+')
_RENT_DURATION_MAP = {(SeasonRentDuration.ENTIRE_SEASON): (SHOP_RENT_TYPE_MAP[RentType.SEASON_RENT]), 
   (SeasonRentDuration.SEASON_CYCLE): (SHOP_RENT_TYPE_MAP[RentType.SEASON_CYCLE_RENT])}

def formatValueToColorTag(value):
    return COLOR_TAG_OPEN + value + COLOR_TAG_CLOSE


def _formatPrice(itemPrice):
    if itemPrice.isActionPrice():
        price = itemPrice.defPrice.toDict()
        price[b'discount'] = itemPrice.price.toDict()
        return price
    else:
        return itemPrice.price.toDict() or None


def _formatFloat(val):
    return round(val, 4)


def _formatKPI(kpiList):

    def _formatKPIValue(kpi, value):
        if kpi.type == KPI.Type.AGGREGATE_MUL:
            minValue, maxValue = value
            return (
             _formatFloat(minValue), _formatFloat(maxValue))
        if kpi.type in (KPI.Type.MUL, KPI.Type.ADD):
            return _formatFloat(value)
        return value

    return [{b'name': (kpi.name), b'type': (kpi.type), b'specValue': (_formatKPIValue(kpi, kpi.specValue) if kpi.specValue else None), b'vehicleTypes': (kpi.vehicleTypes), b'value': (_formatKPIValue(kpi, kpi.value) if kpi.type != KPI.Type.ONE_OF else _formatKPI(kpi.value)), b'descr': (backport.text(kpi.getDescriptionR()) if kpi.getDescriptionR() > 0 else b'')} for kpi in kpiList]


def _formatActionParams(actionInfo):
    return actionInfo.discount.getParams()


def _formatTechName(value):
    parts = value.split(b':')
    if len(parts) > 1:
        return parts[1]
    return value


def _formatImagePaths(item):
    return {b'small': (replaceImgPrefix(item.getShopIcon(size=STORE_CONSTANTS.ICON_SIZE_SMALL))), 
       b'medium': (replaceImgPrefix(item.getShopIcon(size=STORE_CONSTANTS.ICON_SIZE_MEDIUM))), 
       b'large': (replaceImgPrefix(item.getShopIcon(size=STORE_CONSTANTS.ICON_SIZE_LARGE)))}


def _formatVehicleRestore(item):
    if item.isRestorePossible():
        restoreInfo = item.restoreInfo
        restorePrice = item.restorePrice
        currency = restorePrice.getCurrency()
        if item.hasLimitedRestore():
            restoreEndDate = time_utils.timestampToISO(restoreInfo.changedAt + restoreInfo.getRestoreTimeLeft())
        else:
            restoreEndDate = None
        return {b'price': {currency: (restorePrice.getSignValue(currency))}, 
           b'endDate': restoreEndDate}
    else:
        return


def _formatVehicleOwnership(item):
    if item.isInInventory and item.activeInNationGroup:
        result = {}
        if not item.isRented:
            result[b'type'] = b'permanent'
        elif item.rentalIsOver:
            result[b'type'] = b'rentalsOver'
        else:
            result[b'type'] = b'rented'
            info = item.rentInfo
            event = info.getActiveSeasonRent()

            def _formatInfinite(val):
                if val < float(b'inf'):
                    return val
                return -1

            if event:
                rentType = b'event'
            elif item.isTelecomRent:
                rentType = b'telecom'
            else:
                rentType = None
            result[b'info'] = {b'event': ({b'type': (SHOP_RENT_SEASON_TYPE_MAP.get(event.seasonType, b'unknown')), b'id': (event.seasonID), b'duration': (_RENT_DURATION_MAP.get(event.duration, b'undefined')), b'expire': (event.expiryTime)} if event else None), 
               b'rentType': rentType, 
               b'time': (_formatInfinite(info.getTimeLeft())), 
               b'battles': (_formatInfinite(info.battlesLeft)), 
               b'wins': (_formatInfinite(info.winsLeft))}
        return result
    return


def _formatVehicleNationChange(vehicle):
    if vehicle.hasNationGroup:
        result = {}
        result[b'isAvailable'] = vehicle.isNationChangeAvailable
        result[b'otherNationsVehCDs'] = list(iterVehTypeCDsInNationGroup(vehicle.intCD))
        nationGroupVehicles = getGroupByVehTypeCompactDescr(vehicle.intCD)
        nationID, _ = vehicles.g_list.getIDsByName(nationGroupVehicles[0])
        result[b'mainNation'] = nations.NAMES[nationID]
        return result
    else:
        return


def _formatVehicleComparingAvailability(item):
    return not isValidVehicleForComparing(item)


def _formatUserName(item):
    if isinstance(item, Vehicle):
        return getUserName(item.descriptor.type, textPrefix=True)
    return item.userName


def _formatShortUserName(item):
    if isinstance(item, Vehicle):
        return getShortUserName(item.descriptor.type, textPrefix=True)
    return item.shortUserName


def _formatOptDeviceCategories(item):
    if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
        return list(item.descriptor.categories)
    return []


def _formatOptDeviceEffects(item):
    if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
        itemR = R.strings.artefacts.dyn(item.descriptor.groupName)
        effectR = itemR.dyn(b'effect') if itemR else None
        effectsList = [backport.text(effect()) for effect in effectR.values()] if effectR else []
        return effectsList
    else:
        return []


def _formatTags(item):
    if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
        tags = set(item.tags)
        tags.difference_update(SlotCategories.ALL)
        tags.add(item.descriptor.tierlessName)
        tags.update(item.descriptor.categories)
        return list(tags)
    return list(item.tags)


Field = namedtuple(b'Field', (b'name', b'getter'))
idField = Field(b'id', (lambda i: i.intCD))
nameField = Field(b'name', _formatUserName)
nationField = Field(b'nation', (lambda i: i.nationName))
nationNameField = Field(b'nationName', (lambda i: i.nationUserName))
typeField = Field(b'type', (lambda i: i.type))
typeNameField = Field(b'typeName', (lambda i: i.typeUserName))
descriptionField = Field(b'description', (lambda i: i.fullDescription))
shortDescriptionSpecialField = Field(b'shortDescriptionSpecial', (lambda i: i.shortDescriptionSpecial))
longDescriptionSpecialField = Field(b'longDescriptionSpecial', (lambda i: i.longDescriptionSpecial))
inventoryCountField = Field(b'inventoryCount', (lambda i: i.inventoryCount))
buyPriceField = Field(b'buyPrice', (lambda i: _formatPrice(i.buyPrices.itemPrice)))
sellPriceField = Field(b'sellPrice', (lambda i: _formatPrice(i.sellPrices.itemPrice)))
tagsField = Field(b'tags', _formatTags)
kpiField = Field(b'kpi', (lambda i: _formatKPI(i.getKpi())))
techNameField = Field(b'techName', (lambda i: _formatTechName(i.name)))
imagesField = Field(b'images', _formatImagePaths)
optDeviceCategoriesField = Field(b'categories', _formatOptDeviceCategories)
optDeviceEffectField = Field(b'effects', _formatOptDeviceEffects)
optDeviceGroupName = Field(b'groupName', (lambda i: backport.text(R.strings.artefacts.dyn(i.descriptor.tierlessName).name())))
_vehicleComponentsFieldSet = (
 idField,
 nameField,
 techNameField,
 buyPriceField,
 sellPriceField,
 descriptionField,
 inventoryCountField,
 shortDescriptionSpecialField,
 longDescriptionSpecialField,
 imagesField)
_vehicleArtifactsFieldSet = _vehicleComponentsFieldSet + (tagsField, kpiField)
_vehicleOptDeviceFieldSet = _vehicleArtifactsFieldSet + (
 optDeviceCategoriesField,
 optDeviceEffectField,
 optDeviceGroupName)

class Formatter(object):
    __slots__ = (b'__fields',)

    def __init__(self, fields):
        self.__fields = fields
        return

    def format(self, item, allowedFields=None):
        if allowedFields is None:
            return {field.name: field.getter(item) for field in self.__fields}
        else:
            return {field.name: field.getter(item) for field in self.__fields if field.name in allowedFields}


def makeActionFormatter():
    fields = [
     Field(b'id', (lambda actionInfo: actionInfo.getID())),
     Field(b'startDate', (lambda actionInfo: time_utils.timestampToISO(actionInfo.getExactStartTime()))),
     Field(b'endDate', (lambda actionInfo: time_utils.timestampToISO(actionInfo.getExactFinishTime()))),
     Field(b'name', (lambda actionInfo: actionInfo.getTitle())),
     Field(b'description', (lambda actionInfo: actionInfo.event.getDescription())),
     Field(b'triggerChainID', (lambda actionInfo: actionInfo.getTriggerChainID())),
     Field(b'type', (lambda actionInfo: actionInfo.discount.getName())),
     Field(b'params', _formatActionParams)]
    return Formatter(fields)


def makeVehicleFormatter(includeInventoryFields=False):
    isPremiumField = Field(b'isPremium', (lambda i: i.isPremium))
    levelField = Field(b'level', (lambda i: i.level))
    isUnlockedField = Field(b'isUnlocked', (lambda i: i.isUnlocked))
    shortName = Field(b'shortName', _formatShortUserName)
    restore = Field(b'restore', _formatVehicleRestore)
    isTradeInAvailableField = Field(b'isTradeInAvailable', (lambda i: i.isTradeInAvailable))
    isTradeOffAvailableField = Field(b'isTradeOffAvailable', (lambda i: i.isTradeOffAvailable))
    tradeOffPriceField = Field(b'tradeOffPrice', (lambda i: i.tradeOffPrice.toDict() or None))
    inHangarField = Field(b'inHangar', (lambda i: i.isInInventory))
    ownershipField = Field(b'ownership', _formatVehicleOwnership)
    nationChangeField = Field(b'nationChange', _formatVehicleNationChange)
    clanLockField = Field(b'clanLock', (lambda i: i.clanLock))
    isCollectibleField = Field(b'isCollectible', (lambda i: i.isCollectible))
    isNotComparingAvailableField = Field(b'isNotComparingAvailable', _formatVehicleComparingAvailability)
    isOnlyForBattleRoyaleBattles = Field(b'isOnlyForBattleRoyaleBattles', (lambda i: i.isOnlyForBattleRoyaleBattles))
    fields = [
     idField, 
     nameField, 
     shortName, 
     techNameField, 
     nationField, 
     nationNameField, 
     typeField, 
     typeNameField, 
     levelField, 
     descriptionField, 
     shortDescriptionSpecialField, 
     longDescriptionSpecialField, 
     isPremiumField, 
     buyPriceField, 
     sellPriceField, 
     isUnlockedField, 
     imagesField, 
     isTradeInAvailableField, 
     isTradeOffAvailableField, 
     tradeOffPriceField, 
     restore, 
     inHangarField, 
     ownershipField, 
     nationChangeField, 
     clanLockField, 
     isCollectibleField, 
     isNotComparingAvailableField, 
     isOnlyForBattleRoyaleBattles]
    if includeInventoryFields:
        shellFormatter = makeShellFormatter(includeCount=True)
        shellsField = Field(b'shells', (lambda i: [shellFormatter.format(s) for s in i.shells.installed.getItems()]))
        moduleFormatter = makeModuleFormatter()
        modulesField = Field(b'modules', (lambda i: [moduleFormatter.format(m) for m in i.modules if m is not None]))
        deviceFormatter = makeDeviceFormatter()
        devicesField = Field(b'devices', (lambda i: [deviceFormatter.format(d) if d is not None else None for d in i.optDevices.installed]))
        equipmentFormatter = makeEquipmentFormatter()
        equipmentField = Field(b'equipment', (lambda i: [equipmentFormatter.format(e) if e is not None else None for e in i.consumables.installed.getItems()]))
        crewFormatter = makeCrewFormatter()
        crewField = Field(b'crew', (lambda i: [crewFormatter.format(c) if c else None for _, c in i.crew]))

        def formatReadiness(vehicle):
            isReady = vehicle.isReadyToFight
            data = {b'isReady': isReady}
            if not isReady:
                reason, stateLevel = vehicle.getState()
                data[b'reason'] = reason
                data[b'stateLevel'] = stateLevel
            return data

        readinessField = Field(b'readiness', formatReadiness)
        isFavoriteField = Field(b'isFavorite', (lambda i: i.isFavorite))
        fields.extend([
         shellsField, 
         modulesField, 
         devicesField, 
         equipmentField, 
         crewField, 
         readinessField, 
         isFavoriteField])
    return Formatter(fields)


def makeShopTankmanFormatter():
    return Formatter((
     Field(b'groupName', (lambda i: i.groupName)),
     Field(b'location', (lambda i: i.location.value)),
     Field(b'role', _formatTankmanRole),
     Field(b'rank', _formatTankmanRank),
     Field(b'vehicle', _formatVehicleInfo),
     Field(b'name', _formatTankmanNames),
     Field(b'isPremium', (lambda i: i.isPremium)),
     Field(b'gender', (lambda i: i.gender.value)),
     Field(b'nation', _formatTankmanNationInfo),
     Field(b'icons', _formatTankmanIcons)))


def _formatTankmanRole(crewItem):
    return {b'id': (crewItem.roleID), 
       b'name': (crewItem.roleName), 
       b'userName': (crewItem.roleUserName)}


def _formatTankmanRank(crewItem):
    return {b'id': (crewItem.rankID), 
       b'userName': (crewItem.rankUserName)}


def _formatVehicleInfo(crewItem):
    return {vType: {b'id': (descr.type.compactDescr), b'type': (first(t for t in vehicles.VEHICLE_CLASS_TAGS if t in descr.type.tags)), b'name': (descr.type.userString), b'nation': (nations.MAP[descr.type.id[0]])} for vType, descr in (
     (
      b'current', crewItem.vehicleDescr),
     (
      b'native', crewItem.vehicleNativeDescr)) if descr is not None}


def _formatTankmanNames(crewItem):
    return {b'first': (crewItem.firstUserName), 
       b'last': (crewItem.lastUserName), 
       b'full': (crewItem.fullUserName)}


def _formatTankmanNationInfo(crewItem):
    return {b'id': (crewItem.nationID), 
       b'name': (crewItem.nationName), 
       b'userName': (crewItem.nationUserName)}


def _formatTankmanIcons(crewItem):
    return {b'person': (crewItem.icon), 
       b'role': (crewItem.role), 
       b'rank': (crewItem.iconRank)}


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def makeDeviceFormatter(compatVehGetter=None, fittedVehGetter=None, itemsCache=None):
    fields = list(_vehicleOptDeviceFieldSet)
    fields.append(Field(b'removePrice', (lambda i: _formatPrice(i.getRemovalPrice(itemsCache.items)))))
    if compatVehGetter:
        fields.append(Field(b'compatVehicles', (lambda i: compatVehGetter(i.intCD))))
    if fittedVehGetter:
        fields.append(Field(b'fittedVehicles', (lambda i: fittedVehGetter(i.intCD))))
    return Formatter(fields)


def makeEquipmentFormatter(fittedVehGetter=None):
    fields = list(_vehicleArtifactsFieldSet)
    fields.remove(descriptionField)
    fields.extend([
     Field(b'cooldown', (lambda i: i.descriptor.cooldownSeconds)),
     Field(b'nations', (lambda i: [nations.NAMES[i] for i in sorted(i.descriptor.compatibleNations())])),
     Field(b'description', (lambda i: i.descriptor.description))])
    if fittedVehGetter:
        fields.append(Field(b'fittedVehicles', (lambda i: fittedVehGetter(i.intCD))))
    return Formatter(fields)


def makeBattleBoosterFormatter(fittedVehGetter=None):
    fields = list(_vehicleArtifactsFieldSet)
    fields.remove(descriptionField)

    def formatAffectedSkill(i):
        if i.isCrewBooster():
            return CREW_SKILL_TO_KPI_NAME_MAP.get(i.getAffectedSkillName(), b'')
        return b''

    def formatBoosterType(i):
        if i.isCrewBooster():
            return b'skill'
        return b'device'

    def formatBoosterTypeName(i):
        if i.isCrewBooster():
            key = ITEM_TYPES.TANKMAN_SKILLS_TYPE_SKILL_SHORT
        else:
            key = ITEM_TYPES.OPTIONALDEVICE_NAME
        return i18n.makeString(key)

    def formatBoosterDescription(i):
        if i.isCrewBooster():
            return i.getCrewBoosterDescription(False)
        else:
            return i.getOptDeviceBoosterDescription(vehicle=None, valueFormatter=formatValueToColorTag)

    fields.extend([
     Field(b'affectedSkill', formatAffectedSkill),
     Field(b'affectedSkillName', (lambda i: i.getAffectedSkillUserName())),
     Field(b'boosterType', formatBoosterType),
     Field(b'boosterTypeName', formatBoosterTypeName),
     Field(b'description', formatBoosterDescription)])
    if fittedVehGetter:
        fields.append(Field(b'fittedVehicles', (lambda i: fittedVehGetter(i.intCD))))
    return Formatter(fields)


def makeBoosterFormatter():
    fields = [
     Field(b'id', (lambda booster: booster.boosterID)),
     Field(b'inventoryCount', (lambda booster: booster.count)),
     Field(b'kpi', (lambda booster: _formatKPI(booster.kpi))),
     Field(b'description', (lambda booster: booster.getBonusDescription(valueFormatter=formatValueToColorTag))),
     shortDescriptionSpecialField,
     longDescriptionSpecialField,
     Field(b'duration', (lambda booster: booster.effectTime)),
     Field(b'type', (lambda booster: booster.boosterGuiType)),
     nameField,
     buyPriceField,
     imagesField]
    return Formatter(fields)


def makeModuleFormatter():
    fields = [
     idField,
     Field(b'name', (lambda i: i.longUserName)),
     Field(b'type', (lambda i: i.descriptor.itemTypeName)),
     techNameField,
     nationField,
     buyPriceField,
     sellPriceField,
     inventoryCountField,
     imagesField]
    return Formatter(fields)


def makeShellFormatter(includeCount=False):
    fields = [
     idField, 
     nameField, 
     inventoryCountField, 
     sellPriceField, 
     buyPriceField, 
     typeField, 
     nationField, 
     techNameField, 
     imagesField]
    if includeCount:
        fields.append(Field(b'count', (lambda i: i.count)))
    return Formatter(fields)


def makeCrewFormatter():
    fields = [
     Field(b'fullName', (lambda i: i.fullUserName)),
     Field(b'role', (lambda i: i.role)),
     Field(b'roleLevel', (lambda i: i.realRoleLevel.lvl))]
    return Formatter(fields)


def makePremiumPackFormatter():
    fields = [
     nameField,
     shortDescriptionSpecialField,
     longDescriptionSpecialField,
     Field(b'buyPrice', (lambda pack: _formatPrice(pack.buyPrice))),
     Field(b'duration', (lambda pack: pack.duration)),
     Field(b'id', (lambda pack: pack.id))]
    return Formatter(fields)


def makeCustomizationFormatter():
    fields = [
     Field(b'id', (lambda i: i.id)),
     Field(b'type', (lambda i: i.itemTypeName)),
     Field(b'priceGroup', (lambda i: i.priceGroup)),
     Field(b'installedCount', (lambda i: i.installedCount())),
     buyPriceField,
     sellPriceField]
    return Formatter(fields)


def makeInventoryEnhancementsFormatter():
    fields = [
     Field(b'id', (lambda i: i.id)),
     Field(b'count', (lambda i: i.count))]
    return Formatter(fields)


def makeInstalledEnhancementsFormatter():
    fields = [
     Field(b'vehicle_int_cd', (lambda i: i.vehIntCD)),
     Field(b'enhancements', (lambda i: i.enhancements))]
    return Formatter(fields)


def makeCrewBooksFormatter():
    fields = [
     idField,
     Field(b'images', (lambda item: {b'small': (replaceImgPrefix(item.getShopIcon(size=b'small'))), 
        b'medium': (replaceImgPrefix(item.getShopIcon(size=b'big'))), 
        b'large': (replaceImgPrefix(item.getShopIcon(size=b'large')))})),
     Field(b'type', (lambda book: book.getBookType())),
     Field(b'nation', (lambda book: book.getNation()))]
    return Formatter(fields)
