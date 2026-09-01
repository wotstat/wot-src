from __future__ import absolute_import
import sys, weakref, typing
from debug_utils import LOG_CURRENT_EXCEPTION
from frameworks.wulf import WindowFlags
from gui.Scaleform.daapi.view.lobby.techtree.settings import UNKNOWN_VEHICLE_LEVEL, UnlockProps
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.app_loader import sf_lobby
from gui.impl.pub import WindowImpl
from gui.shared.formatters import icons
from helpers import dependency
from helpers.i18n import makeString
from items import vehicles
from shared_utils import CONST_CONTAINER
from skeletons.gui.shared import IItemsCache
from gui.impl import backport
from gui.impl.gen import R
from soft_exception import SoftException

class TOOLTIP_TYPE(CONST_CONTAINER):
    VEHICLE = b'vehicle'
    TANKMAN = b'tankman'
    NOT_RECRUITED_TANKMAN = b'notRecruitedTankman'
    SPECIAL_TANKMAN = b'specialTankman'
    SKILL = b'skill'
    CREW_SKIN = b'crew_skin'
    CREW_BOOK = b'crew_book'
    CREW_BUNDLE = b'crewBundle'
    ACHIEVEMENT = b'achievement'
    ACHIEVEMENT_ATTR = b'achievementAttr'
    MODULE = b'module'
    SHELL = b'shell'
    EQUIPMENT = b'equipment'
    EFFICIENCY = b'efficiency'
    FORTIFICATIONS = b'fortification'
    IGR = b'igr'
    CYBER_SPORT = b'cyberSport'
    MAP = b'map'
    CONTROL = b'control'
    PRIVATE_QUESTS = b'privateQuests'
    CONTACT = b'contact'
    QUESTS = b'quests'
    EPIC_QUESTS = b'epicQuests'
    HANGAR_TUTORIAL = b'hangarTutorial'
    CLAN_PROFILE = b'clanProfile'
    TECH_CUSTOMIZATION = b'techCustomization'
    BOOSTER = b'booster'
    VEHICLE_FILTER = b'vehicleFilter'
    VEH_CMP_CUSTOMIZATION = b'vehCmpCustomization'
    RESERVE = b'reserve'
    RANKED_STEP = b'rankedStep'
    RANKED_RANK = b'rankedRank'
    RANKED_CALENDAR_DAY = b'rankedCalendarDayInfo'
    RANKED_CALENDAR_DAY_EXTENDED = b'rankedCalendarDayInfoExtended'
    RANKED_SELECTOR_INFO = b'rankedSelectorInfo'
    RANKED_DIVISION_INFO = b'rankedDivisionInfo'
    RANKED_YEAR_REWARD = b'rankedYearReward'
    RANKED_QUESTS_PREVIEW = b'rankedQuestsPreview'
    FAKE = b'fake'
    VEHICLE_ELITE_BONUS = b'vehicleEliteBonus'
    VEHICLE_HISTORICAL_REFERENCE = b'vehicleHistoricalReference'
    MARATHON = b'marathon'
    EPIC_SKILL_INFO = b'epicSkillInfo'
    BLUEPRINTS = b'blueprintsInfo'
    FRONTLINE = b'frontlineInfo'
    BATTLE_ROYALE_SELECTOR_INFO = b'battleRoyaleSelectorInfo'
    BATTLE_ROYALE_SELECTOR_CALENDAR_INFO = b'battleRoyaleSelectorCalendarInfo'
    BATTLE_ROYALE_WIDGET_INFO = b'battleRoyaleWidgetInfo'
    SESSION_STATS = b'sessionStats'
    TRADE_IN_INFO = b'tradeInInfo'
    TRADE_IN_INFO_NOT_AVAILABLE = b'tradeInInfoNotAvailable'
    TRADE_IN_STATE_NOT_AVAILABLE = b'tradeInStateNotAvailable'
    DEMOUNT_KIT = b'demountKit'
    VEHICLE_COLLECTOR = b'vehicleCollector'
    BATTLE_PASS_GIFT_TOKEN = b'battlePassGiftToken'
    BATTLE_PASS_POINTS = b'battlePassPoints'
    EPIC_BATTLE_GIFT_TOKEN = b'epicBattleGiftToken'
    MAPBOX_SELECTOR_INFO = b'mapboxSelectorInfo'
    MAPBOX_CALENDAR_DAY = b'mapboxCalendarDay'
    REFERRAL_PROGRAMM = b'referralProgram'
    EPIC_RANK_UNLOCK = b'epicRankUnlock'
    RANKED_SELECTABLE_REWARD = b'rankedSelectableReward'


class TOOLTIP_COMPONENT(CONST_CONTAINER):
    TECH_MAIN = b'technical_maintenance'
    HANGAR = b'hangar'
    SHOP = b'shop'
    INVENTORY = b'inventory'
    PERSONAL_CASE = b'personal_case'
    CAROUSEL = b'carousel'
    RESEARCH = b'research'
    PROFILE = b'profile'
    PROFILE_VEHICLE = b'profileVehicle'
    FINAL_STATISTIC = b'FinalStatistic'
    CYBER_SPORT_UNIT = b'CyberSportUnit'
    FORTIFICATIONS = b'fortification'
    CLAN_PROFILE = b'clanProfile'
    SETTINGS = b'settings'
    CUSTOMIZATION = b'customization'
    CONTACT = b'contact'
    HANGAR_TUTORIAL = b'hangarTutorial'
    TECH_CUSTOMIZATION = b'techCustomization'
    BOOSTER = b'booster'
    BADGE = b'badge'
    RANK = b'ranked'
    RESERVE = b'reserve'
    BLUEPRINT = b'blueprints'
    SESSION_STATS = b'sessionStats'
    CREW = b'crew'
    CREW_BOOK = b'crewBook'
    TRADE_IN = b'tradeIn'
    DEMOUNT_KIT = b'demountKit'
    MODULE_INFO = b'moduleInfo'
    BATTLE_PASS = b'battlePass'
    EPIC_BATTLE = b'epicBattle'
    RECERTIFICATION_FORM = b'recertificationForm'
    MENTOR_LICENSE = b'mentorLicense'
    FULL_STATS = b'fullStats'


class ACTION_TOOLTIPS_TYPE(CONST_CONTAINER):
    ECONOMICS = b'economics'
    ITEM = b'item'
    BOOSTER = b'booster'
    CAMOUFLAGE = b'camouflage'
    EMBLEMS = b'emblems'
    AMMO = b'ammo'
    RENT = b'rent'


class ACTION_TOOLTIPS_STATE(CONST_CONTAINER):
    DISCOUNT = b'discount'
    PENALTY = b'penalty'


class ToolTipBaseData(object):

    def __init__(self, context, toolTipType):
        super(ToolTipBaseData, self).__init__()
        self._context = context
        self._toolTipType = toolTipType
        self.calledBy = None
        return

    @sf_lobby
    def app(self):
        return

    @property
    def context(self):
        return self._context

    def isDynamic(self):
        return False

    def getDisplayableData(self, *args, **kwargs):
        return

    def buildToolTip(self, *args, **kwargs):
        return {b'type': (self.getType()), 
           b'component': (self.context.getComponent()), 
           b'data': (self.getDisplayableData(*args, **kwargs))}

    def getType(self):
        return self._toolTipType


class ToolTipData(ToolTipBaseData):

    def __init__(self, context, toolTipType):
        super(ToolTipData, self).__init__(context, toolTipType)
        self.item = None
        self.fields = tuple()
        return

    def getDisplayableData(self, *args, **kwargs):
        self.item = self.context.buildItem(*args, **kwargs)
        result = {}
        for field in self.fields:
            key, value = field.buildData()
            if field.isAvailable and key not in self.context.fieldsToExclude:
                result[key] = value

        return result


class WulfTooltipData(ToolTipData):

    def getDisplayableData(self, *args, **kwargs):
        parent = kwargs.get(b'parent')
        return WindowImpl(wndFlags=WindowFlags.SERVICE_WINDOW, content=self.getTooltipContent(*args, **kwargs), parent=parent, areaID=R.areas.specific())

    def buildToolTip(self, *args, **kwargs):
        return

    def getTooltipContent(self, *args, **kwargs):
        raise SoftException((b'getTooltipContent should be overriden in {}').format(self))
        return


class ToolTipDataField(object):

    def __init__(self, tooltip, name):
        self._tooltip = weakref.proxy(tooltip)
        self._name = name
        self._isAvailable = True
        return

    def buildData(self):
        return (self._name, self._getValue())

    @property
    def isAvailable(self):
        return self._isAvailable

    def _getValue(self):
        return


class ToolTipAttrField(ToolTipDataField):

    def __init__(self, context, name, attr=None):
        super(ToolTipAttrField, self).__init__(context, name)
        self._attr = attr
        return

    def _getItem(self):
        return self._tooltip.item

    def _getValue(self):
        attr = self._attr or self._name
        item = self._getItem()
        if hasattr(item, attr):
            return getattr(item, attr)
        return super(ToolTipAttrField, self)._getValue()


class ToolTipMethodField(ToolTipDataField):

    def __init__(self, context, name, method=None, args=None):
        super(ToolTipMethodField, self).__init__(context, name)
        self._method = method
        self._args = args or tuple()
        return

    def _getItem(self):
        return self._tooltip.item

    def _getValue(self):
        attr = self._method or self._name
        item = self._getItem()
        if hasattr(item, attr):
            return getattr(item, attr)(*self._args)
        return super(ToolTipMethodField, self)._getValue()


class ToolTipAttrCheckField(ToolTipAttrField):

    def __init__(self, context, name, value, attr=None):
        super(ToolTipAttrCheckField, self).__init__(context, name, attr)
        self._value = value
        return

    def _getValue(self):
        return super(ToolTipAttrCheckField, self)._getValue() == self._value


class ToolTipMethodCheckField(ToolTipMethodField):

    def __init__(self, context, name, value, method=None, args=None):
        super(ToolTipMethodCheckField, self).__init__(context, name, method, args)
        self._value = value
        return

    def _getValue(self):
        return super(ToolTipMethodCheckField, self)._getValue() == self._value


class ToolTipParameterField(ToolTipDataField):

    def _getParameterValue(self, *args):
        return


def getComplexStatus(statusKey, **kwargs):
    try:
        if not statusKey:
            return (None, None)
        else:
            headerKey = statusKey + b'/header'
            textKey = statusKey + b'/text'
            header = makeString(headerKey, **kwargs)
            text = makeString(textKey, **kwargs)
            if headerKey == TOOLTIPS.VEHICLESTATUS_INPREMIUMIGRONLY_HEADER:
                icon = icons.premiumIgrSmall()
                header = makeString(headerKey, icon=icon)
            if header == headerKey.split(b':', 1)[1]:
                header = None
            if text == textKey.split(b':', 1)[1]:
                text = None
            return (header, text)

    except Exception:
        LOG_CURRENT_EXCEPTION()
        return (None, None)

    return


def getComplexStatusWULF(statusKey, **kwargs):
    header, text = (None, None)
    if statusKey:
        headerKey = statusKey.dyn(b'header')
        textKey = statusKey.dyn(b'text')
        if headerKey.exists():
            header = backport.text(headerKey(), **kwargs)
        if textKey.exists():
            text = backport.text(textKey(), **kwargs)
        if headerKey is R.strings.tooltips.vehicleStatus.inPremiumIgrOnly.header:
            header = backport.text(headerKey(), icon=icons.premiumIgrSmall())
    return (
     header, text)


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getUnlockPrice(compactDescr, parentCD=None, vehicleLevel=UNKNOWN_VEHICLE_LEVEL, blueprintCount=0, itemsCache=None):
    itemTypeId, _, _ = vehicles.parseIntCompactDescr(compactDescr)
    freeXP = itemsCache.items.stats.actualFreeXP
    unlocks = itemsCache.items.stats.unlocks
    xpVehs = itemsCache.items.stats.vehiclesXPs
    g_techTreeDP.load()
    pricesDict = g_techTreeDP.getUnlockPrices(compactDescr)

    def getUnlockProps(isAvailable, vehCompDescr, unlockProps=None):
        if unlockProps is not None:
            unlockPrice = unlockProps.xpCost
        elif vehCompDescr in pricesDict:
            unlockPrice = pricesDict[vehCompDescr]
        else:
            vehicle = itemsCache.items.getItemByCD(parentCD)
            _, unlockPrice, _ = vehicle.getUnlockDescrByIntCD(compactDescr)
        oldPrice = unlockProps.xpFullCost if unlockProps is not None else unlockPrice
        discount = unlockProps.discount if unlockProps is not None else 0
        pVehXp = xpVehs.get(vehCompDescr, 0)
        need = unlockPrice - pVehXp
        needWithFreeXP = need - freeXP
        return (isAvailable, unlockPrice, min(need, needWithFreeXP), oldPrice, discount)

    if itemTypeId == vehicles._VEHICLE:
        isAvailable, unlockProps = g_techTreeDP.isNext2Unlock(compactDescr, unlocks, xpVehs, freeXP, vehicleLevel)
        if parentCD is not None and parentCD == unlockProps.parentID:
            return getUnlockProps(isAvailable, parentCD, unlockProps)
        xpCost = pricesDict.get(parentCD, 0)
        if xpCost == 0 and parentCD is None:
            xpCost = unlockProps.xpFullCost
        discount, newCost = g_techTreeDP.getBlueprintDiscountData(compactDescr, vehicleLevel, xpCost, blueprintCount)
        unlockProps = UnlockProps(parentCD, -1, newCost, None, discount, xpCost)
        return getUnlockProps(isAvailable, unlockProps.parentID, unlockProps)
    else:
        isAvailable = compactDescr in unlocks
        if parentCD is not None:
            return getUnlockProps(isAvailable, parentCD)
        vehsCompDescrs = [compDescr for compDescr in pricesDict if compDescr in unlocks]
        if not vehsCompDescrs:
            vehsCompDescrs = pricesDict.keys()
        minUnlockPrice = sys.maxsize
        minUnlockPriceVehCD = None
        for vcd in vehsCompDescrs:
            if pricesDict[vcd] <= minUnlockPrice:
                minUnlockPrice = pricesDict[vcd]
                minUnlockPriceVehCD = vcd

        if minUnlockPriceVehCD is None:
            return (isAvailable, 0, 0, 0, 0)
        return getUnlockProps(isAvailable, minUnlockPriceVehCD)
