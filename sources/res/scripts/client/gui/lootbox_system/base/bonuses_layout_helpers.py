import logging
from enum import Enum
from typing import TYPE_CHECKING
from gui.lootbox_system.base.common import BonusesLayoutAttrs
from gui.server_events.bonuses import IntelligenceBlueprintBonus, NationalBlueprintBonus
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.utils.requesters.blueprints_requester import getVehicleCDForIntelligence, getVehicleCDForNational
from messenger.formatters.service_channel_helpers import getCustomizationItem
from shared_utils import first
_logger = logging.getLogger(__name__)
if TYPE_CHECKING:
    from typing import Any, Dict, Optional, Union
    from gui.server_events.bonuses import CustomizationsBonus, GoodiesBonus, ItemsBonus, LootBoxTokensBonus, SimpleBonus, TmanTemplateTokensBonus, TokensBonus, VehicleBlueprintBonus, VehiclesBonus

class BonusesHelper(object):

    @classmethod
    def getParameter(cls, bonus, source, parameter):
        default = source.get(parameter)
        subType = cls.__getSubType(bonus)
        if subType in source:
            source = source[subType]
            default = source.get(parameter, default)
        value = cls.__getValue(bonus, source)
        if value in source:
            source = source[value]
            default = source.get(parameter, default)
        if parameter in source:
            return source[parameter]
        return default

    @classmethod
    def __getSubType(cls, bonus):
        return cls.__selectGetter(bonus, _SUBTYPE_GETTERS, _BaseSubTypeGetter).getSubType(bonus)

    @classmethod
    def __getValue(cls, bonus, source):
        return cls.__selectGetter(bonus, _VALUE_GETTERS, _BaseValueGetter).getValue(bonus, source)

    @staticmethod
    def __selectGetter(bonus, getters, default):
        return getters.get(bonus.getName(), default)


class _HelperTypes(str, Enum):
    RENT = b'rent'
    LOCKED_3D_STYLE = b'locked3DStyle'
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


class _BaseSubTypeGetter(object):

    @staticmethod
    def getSubType(bonus):
        _logger.debug(b'No subType getter for bonus: %s', bonus.getName())
        return


class _VehiclesSubTypeGetter(_BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        subType = b''
        vehicles = bonus.getVehicles()
        _, vehInfo = first(vehicles)
        styleID = vehInfo.get(b'customization', {}).get(b'styleId')
        if styleID is not None:
            c11nItem = getCustomizationItem(styleID, b'style')
            if c11nItem is not None and c11nItem.isLockedOnVehicle:
                subType = _HelperTypes.LOCKED_STYLE
                if c11nItem.is3D:
                    subType = _HelperTypes.LOCKED_3D_STYLE
        if bonus.isRentVehicle(vehInfo):
            subType = _HelperTypes.RENT
        return subType


class _CustomizationSubTypeGetter(_BaseSubTypeGetter):

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


class _GoodiesSubTypeGetter(_BaseSubTypeGetter):

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


class _ItemsSubTypeGetter(_BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        subType = b''
        items = bonus.getItems().keys()
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


class _TankmanSubTypeGetter(_BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        keys = bonus.getValue().keys()
        tID = first(keys)
        recruitInfo = getRecruitInfo(tID)
        if recruitInfo.isFemale():
            return _HelperTypes.TANKWOMAN
        return b''


class _CurrenciesSubTypeGetter(_BaseSubTypeGetter):

    @staticmethod
    def getSubType(bonus):
        return bonus.getCode()


_SUBTYPE_GETTERS = {b'default': _BaseSubTypeGetter, 
   b'customizations': _CustomizationSubTypeGetter, 
   b'currencies': _CurrenciesSubTypeGetter, 
   b'goodies': _GoodiesSubTypeGetter, 
   b'items': _ItemsSubTypeGetter, 
   b'vehicles': _VehiclesSubTypeGetter, 
   b'tmanToken': _TankmanSubTypeGetter}

class _BaseValueGetter(object):

    @classmethod
    def getValue(cls, bonus, _):
        _logger.debug(b'No value getter for bonus: %s', bonus.getName())
        return


class _IntCDValueGetter(_BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        keys = bonus.getValue().keys()
        value = str(first(keys))
        return value


class _BlueprintValueGetter(_BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, source):
        intCD = bonus.getValue()[0]
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


class _CustomizationValueGetter(_BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        customizations = bonus.getCustomizations()
        itemData = first(customizations)
        return str(itemData.get(b'id', b''))


class _VehiclesValueGetter(_BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        value = bonus.getValue()
        if isinstance(value, list):
            value = first(value)
        return str(first(value.keys()))


class _TankmanValueGetter(_BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        keys = bonus.getValue().keys()
        tID = first(keys)
        recruitInfo = getRecruitInfo(tID)
        return recruitInfo.getGroupName()


class _TokenValueGetter(_BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        return first(bonus.getTokens().iterkeys(), b'')


class _LootBoxValueGetter(_BaseValueGetter):

    @classmethod
    def getValue(cls, bonus, _):
        box = bonus.getBox()
        return (b'{}_{}').format(box.getType(), box.getCategory())


_VALUE_GETTERS = {b'default': _BaseValueGetter, 
   b'blueprints': _BlueprintValueGetter, 
   b'items': _IntCDValueGetter, 
   b'goodies': _IntCDValueGetter, 
   b'crewBooks': _IntCDValueGetter, 
   b'customizations': _CustomizationValueGetter, 
   b'vehicles': _VehiclesValueGetter, 
   b'tmanToken': _TankmanValueGetter, 
   b'tokens': _TokenValueGetter, 
   b'lootBox': _LootBoxValueGetter}
