from __future__ import absolute_import
import logging
from enum import Enum
from typing import TYPE_CHECKING
from gui.server_events.bonuses import IntelligenceBlueprintBonus, NationalBlueprintBonus
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters.blueprints_requester import getVehicleCDForIntelligence, getVehicleCDForNational
from shared_utils import first
_logger = logging.getLogger(__name__)
if TYPE_CHECKING:
    from typing import Any, Dict, Optional, Union
    from gui.server_events.bonuses import CustomizationsBonus, GoodiesBonus, ItemsBonus, LootBoxTokensBonus, SimpleBonus, TmanTemplateTokensBonus, TokensBonus, VehicleBlueprintBonus, VehiclesBonus

class BonusesLayoutAttrs(object):
    BONUSES = b'bonuses'
    DEFAULT = b'default'
    PRIORITY = b'priority'
    VISIBILITY = b'isVisible'
    OVERRIDE = b'override'
    RARITY = b'rarity'
    ID = b'id'
    MAIN = (
     PRIORITY, VISIBILITY)


class _HelperTypes(str, Enum):
    RENT = b'rent'
    LOCKED_STYLE = b'lockedStyle'
    STYLE_3D = b'style3D'
    TROPHY_DEVICE = b'trophyDevice'
    MODERNIZED_DEVICE = b'modernizedDevice'
    IMPROVED_DEVICE = b'improvedDevice'
    OPTIONAL_DEVICE = b'optionalDevice'
    CREW_BATTLE_BOOSTER = b'crewBattleBooster'
    DEVICE_BATTLE_BOOSTER = b'deviceBattleBooster'
    CONSUMABLE = b'consumable'
    STIMULATOR = b'stimulator'
    DEMOUNT_KIT = b'demountKit'
    RECERTIFICATION_FORM = b'recertificationForm'
    MENTORING_LICENSE = b'mentoringLicense'
    TANKWOMAN = b'tankwoman'


class BonusesLayoutHelper(object):

    @classmethod
    def getParameter(cls, bonus, source, parameter, subTypeGetter=None, valueGetter=None):
        default = source.get(parameter)
        subType = cls.__getSubType(bonus, subTypeGetter)
        source = source.get(subType, source)
        default = source.get(parameter, default)
        value = cls.__getValue(bonus, source, valueGetter)
        source = source.get(value, source)
        default = source.get(parameter, default)
        return source.get(parameter, default)

    @classmethod
    def __getSubType(cls, bonus, subTypeGetter):
        getter = subTypeGetter() if subTypeGetter is not None else getDefaultSubTypeGetter()
        return cls.__selectGetter(bonus, getter, BaseSubTypeGetter).getSubType(bonus)

    @classmethod
    def __getValue(cls, bonus, source, valueGetter):
        getter = valueGetter() if valueGetter is not None else getDefaultValueGetter()
        return cls.__selectGetter(bonus, getter, BaseValueGetter).getValue(bonus, source)

    @staticmethod
    def __selectGetter(bonus, getters, default):
        return getters.get(bonus.getName(), default)


class BaseSubTypeGetter(object):

    @staticmethod
    def getSubType(bonus):
        _logger.debug(b'No subType getter for bonus: %s', bonus.getName())
        return


class VehiclesSubTypeGetter(BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        subType = b''
        vehicles = bonus.getVehicles()
        vehicle, vehInfo = first(vehicles)
        if vehicle.isOutfitLocked:
            subType = _HelperTypes.LOCKED_STYLE
        if bonus.isRentVehicle(vehInfo):
            subType = _HelperTypes.RENT
        return subType


class CustomizationSubTypeGetter(BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        customizations = bonus.getCustomizations()
        itemData = first(customizations)
        c11nItem = bonus.getC11nItem(itemData)
        itemType = c11nItem.itemTypeName
        if itemType == b'style':
            if c11nItem.isLockedOnVehicle:
                return _HelperTypes.LOCKED_STYLE
            if c11nItem.is3D:
                return _HelperTypes.STYLE_3D
        return itemType


class GoodiesSubTypeGetter(BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        subType = b''
        if bonus.getDemountKits():
            return _HelperTypes.DEMOUNT_KIT
        if bonus.getRecertificationForms():
            return _HelperTypes.RECERTIFICATION_FORM
        if bonus.getMentoringLicenses():
            return _HelperTypes.MENTORING_LICENSE
        return subType


class ItemsSubTypeGetter(BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        subType = b''
        items = bonus.getItems()
        item = first(items)
        if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
            if item.isTrophy:
                subType = _HelperTypes.TROPHY_DEVICE
            elif item.isModernized:
                subType = _HelperTypes.MODERNIZED_DEVICE
            elif item.isDeluxe:
                subType = _HelperTypes.IMPROVED_DEVICE
            else:
                subType = _HelperTypes.OPTIONAL_DEVICE
        elif item.itemTypeID == GUI_ITEM_TYPE.EQUIPMENT:
            subType = _HelperTypes.CONSUMABLE
            if item.isStimulator:
                subType = _HelperTypes.STIMULATOR
        elif item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER:
            if item.isCrewBooster():
                subType = _HelperTypes.CREW_BATTLE_BOOSTER
            else:
                subType = _HelperTypes.DEVICE_BATTLE_BOOSTER
        return subType


class TankmanSubTypeGetter(BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        keys = bonus.getValue()
        tID = first(keys)
        recruitInfo = getRecruitInfo(tID)
        if recruitInfo.isFemale():
            return _HelperTypes.TANKWOMAN
        return b''


class CurrenciesSubTypeGetter(BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        return bonus.getCode()


class BaseValueGetter(object):

    @classmethod
    def getValue(cls, bonus, _):
        _logger.debug(b'No value getter for bonus: %s', bonus.getName())
        return


class IntCDValueGetter(BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        keys = bonus.getValue()
        value = str(first(keys))
        return value


class BlueprintValueGetter(BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, source):
        intCD = first(bonus.getValue())
        if isinstance(bonus, (IntelligenceBlueprintBonus, NationalBlueprintBonus)):
            for key in source.keys():
                if key not in BonusesLayoutAttrs.MAIN:
                    if intCD == cls.__transformKey(key, bonus):
                        return key

        return str(intCD)

    @staticmethod
    def __transformKey(key, bonus):
        intCD = int(key)
        if isinstance(bonus, IntelligenceBlueprintBonus):
            intCD = getVehicleCDForIntelligence(intCD)
        elif isinstance(bonus, NationalBlueprintBonus):
            intCD = getVehicleCDForNational(intCD)
        return intCD


class CustomizationValueGetter(BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        customizations = bonus.getCustomizations()
        itemData = first(customizations)
        if itemData.get(b'custType', b'') == b'attachment':
            c11nItem = bonus.getC11nItem(itemData)
            return c11nItem.rarity
        return str(itemData.get(b'id', b''))


class VehiclesValueGetter(BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        value = bonus.getValue()
        if isinstance(value, list):
            value = first(value)
        return str(first(value.keys()))


class TankmanValueGetter(BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        keys = bonus.getValue()
        tID = first(keys)
        recruitInfo = getRecruitInfo(tID)
        return recruitInfo.getGroupName()


class TokenValueGetter(BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        return first(bonus.getTokens(), b'')


class LootBoxValueGetter(BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        box = bonus.getBox()
        return (b'{}_{}').format(box.getType(), box.getCategory())


def getDefaultValueGetter():
    return {b'default': BaseValueGetter, 
       b'blueprints': BlueprintValueGetter, 
       b'items': IntCDValueGetter, 
       b'goodies': IntCDValueGetter, 
       b'crewBooks': IntCDValueGetter, 
       b'customizations': CustomizationValueGetter, 
       b'vehicles': VehiclesValueGetter, 
       b'tmanToken': TankmanValueGetter, 
       b'tokens': TokenValueGetter, 
       b'lootBox': LootBoxValueGetter}


def getDefaultSubTypeGetter():
    return {b'default': BaseSubTypeGetter, 
       b'customizations': CustomizationSubTypeGetter, 
       b'currencies': CurrenciesSubTypeGetter, 
       b'goodies': GoodiesSubTypeGetter, 
       b'items': ItemsSubTypeGetter, 
       b'vehicles': VehiclesSubTypeGetter, 
       b'tmanToken': TankmanSubTypeGetter}
