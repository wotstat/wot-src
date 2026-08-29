import logging
from collections import namedtuple
from math import ceil
from typing import TYPE_CHECKING
from constants import LOOTBOX_TOKEN_PREFIX, PREMIUM_ENTITLEMENTS, RESOURCE_TOKEN_PREFIX, LOOTBOX_KEY_PREFIX
from early_access_common import isEarlyAccessToken
from epic_constants import EPIC_ARMORY_YARD_TOKEN_NAME
from gui.Scaleform.genConsts.SLOT_HIGHLIGHT_TYPES import SLOT_HIGHLIGHT_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.settings import ICONS_SIZES
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen_utils import INVALID_RES_ID
from gui.impl.lobby.loot_box.loot_box_helper import getKeyByTokenID
from gui.ranked_battles.constants import YEAR_POINTS_TOKEN
from gui.server_events.formatters import parseComplexToken, TOKEN_SIZES
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.formatters import text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE, getItemIconName
from gui.shared.gui_items.Tankman import getRoleUserName
from gui.shared.gui_items.badge import Badge
from gui.shared.gui_items.crew_skin import localizedFullName, Rarity
from gui.shared.gui_items.customization import CustomizationTooltipContext
from gui.shared.money import Currency
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import time_utils, i18n, dependency
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX
from personal_missions import PM_BRANCH
from shared_utils import CONST_CONTAINER, findFirst, first
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.offers import IOffersDataProvider
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
if TYPE_CHECKING:
    from typing import Callable, List, Optional, Any, Union, Dict
    from account_helpers.offers.events_data import OfferEventData
    from gui.goodies.goodie_items import Booster
    from gui.server_events.bonuses import SimpleBonus, CrystalBonus, GoodiesBonus, PlusPremiumDaysBonus, EpicSelectTokensBonus, X5BattleTokensBonus, X3CrewTokensBonus
    from gui.server_events.cond_formatters.formatters import ConditionFormatter
    from gui.shared.gui_items.crew_book import CrewBook
_logger = logging.getLogger(__name__)

def getOfferTokenByGift(tokenID):
    return tokenID.replace(b'_gift', b'')


EPIC_AWARD_SIZE = b's360x270'

class AWARDS_SIZES(CONST_CONTAINER):
    SMALL = b'small'
    BIG = b'big'


class COMPLETION_TOKENS_SIZES(CONST_CONTAINER):
    SMALL = b'small'
    BIG = b'big'
    HUGE = b'huge'


class LABEL_ALIGN(CONST_CONTAINER):
    RIGHT = b'right'
    CENTER = b'center'


PACK_RENT_VEHICLES_BONUS = b'packRentVehicleBonus'
BATTLE_BONUS_X5_TOKEN = b'battle_bonus_x5'
CREW_BONUS_X3_TOKEN = b'crew_bonus_x3'
GOLD_MISSION = b'goldmission'
BR_PROGRESSION_TOKEN = b'img:battle_royale:progression'
AWARD_IMAGES = {(AWARDS_SIZES.SMALL): {(Currency.CREDITS): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_CREDITS), 
                          (Currency.GOLD): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_GOLD), 
                          (Currency.CRYSTAL): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_CRYSTAL), 
                          (Currency.EVENT_COIN): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_EVENTCOIN), 
                          (Currency.BPCOIN): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_BPCOIN), 
                          (Currency.EQUIP_COIN): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_EQUIPCOIN), 
                          b'creditsFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_CREDITS), 
                          b'freeXP': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_FREEEXP), 
                          b'freeXPFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_FREEEXP), 
                          b'tankmenXP': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_TANKMENXP), 
                          b'tankmenXPFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_TANKMENXP), 
                          b'xp': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_EXP), 
                          b'xpFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_EXP), 
                          b'dailyXPFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_SMALL_FREEEXP)}, 
   (AWARDS_SIZES.BIG): {(Currency.CREDITS): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_CREDITS), 
                        (Currency.GOLD): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_GOLD), 
                        (Currency.CRYSTAL): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_CRYSTAL), 
                        (Currency.EVENT_COIN): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_EVENTCOIN), 
                        (Currency.BPCOIN): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_BPCOIN), 
                        (Currency.EQUIP_COIN): (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_EQUIPCOIN), 
                        b'creditsFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_CREDITS), 
                        b'freeXP': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_FREEXP), 
                        b'freeXPFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_FREEXP), 
                        b'tankmenXP': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_TANKMENXP), 
                        b'tankmenXPFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_TANKMENXP), 
                        b'xp': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_EXP), 
                        b'xpFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_EXP), 
                        b'dailyXPFactor': (RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_BIG_FREEXP)}}
EARLY_ACCESS_TOKEN_IMAGES = {(AWARDS_SIZES.SMALL): (backport.image(R.images.gui.maps.icons.early_access.tokens.c_32x32())), 
   (AWARDS_SIZES.BIG): (backport.image(R.images.gui.maps.icons.early_access.tokens.c_80x80()))}
EARLY_ACCESS_TOKEN_IMAGES_PADDINGS = {(AWARDS_SIZES.SMALL): 8, 
   (AWARDS_SIZES.BIG): 0}
EARLY_ACCESS_TOKEN_IMAGES_GAP = {(AWARDS_SIZES.SMALL): 8, 
   (AWARDS_SIZES.BIG): 0}

def getRecertificationFormImages():
    result = {(AWARDS_SIZES.SMALL): (backport.image(R.images.gui.maps.icons.recertification.common_48x48())), 
       (AWARDS_SIZES.BIG): (backport.image(R.images.gui.maps.icons.recertification.common_80x80()))}
    return result


def _getMultiplierFormatter(formatter):

    def wrapper(text):
        return formatter((b'x{}').format(text))

    return wrapper


TEXT_FORMATTERS = {(Currency.CREDITS): (text_styles.credits), 
   (Currency.GOLD): (text_styles.gold), 
   (Currency.CRYSTAL): (text_styles.crystal), 
   (Currency.EVENT_COIN): (text_styles.eventCoin), 
   (Currency.BPCOIN): (text_styles.bpcoin), 
   (Currency.EQUIP_COIN): (text_styles.equipCoin), 
   b'creditsFactor': (_getMultiplierFormatter(text_styles.credits)), 
   b'freeXP': (text_styles.expText), 
   b'freeXPFactor': (_getMultiplierFormatter(text_styles.expText)), 
   b'tankmenXP': (text_styles.expText), 
   b'tankmenXPFactor': (_getMultiplierFormatter(text_styles.expText)), 
   b'xp': (text_styles.expText), 
   b'xpFactor': (_getMultiplierFormatter(text_styles.expText)), 
   b'dailyXPFactor': (_getMultiplierFormatter(text_styles.expText)), 
   b'vehicles': (text_styles.gold), 
   b'tmanToken': (text_styles.stats)}
TEXT_ALIGNS = {b'creditsFactor': (LABEL_ALIGN.RIGHT), 
   b'freeXPFactor': (LABEL_ALIGN.RIGHT), 
   b'tankmenXPFactor': (LABEL_ALIGN.RIGHT), 
   b'dailyXPFactor': (LABEL_ALIGN.RIGHT), 
   b'xpFactor': (LABEL_ALIGN.RIGHT)}

def getCompensationFormattersMap():
    return {b'vehicles': (VehiclesCompensationFormatter()), 
       b'crewSkins': (CrewSkinsCompensationFormatter())}


def getDefaultFormattersMap():
    simpleBonusFormatter = SimpleBonusFormatter()
    tokenBonusFormatter = TokenBonusFormatter()
    countableIntegralBonusFormatter = CountableIntegralBonusFormatter()
    return {b'strBonus': simpleBonusFormatter, 
       (Currency.GOLD): simpleBonusFormatter, 
       (Currency.CREDITS): simpleBonusFormatter, 
       (Currency.CRYSTAL): simpleBonusFormatter, 
       (Currency.EVENT_COIN): simpleBonusFormatter, 
       (Currency.BPCOIN): simpleBonusFormatter, 
       (Currency.EQUIP_COIN): simpleBonusFormatter, 
       b'freeXP': simpleBonusFormatter, 
       b'xp': simpleBonusFormatter, 
       b'tankmenXP': simpleBonusFormatter, 
       b'xpFactor': simpleBonusFormatter, 
       b'creditsFactor': simpleBonusFormatter, 
       b'freeXPFactor': simpleBonusFormatter, 
       b'tankmenXPFactor': simpleBonusFormatter, 
       b'dailyXPFactor': simpleBonusFormatter, 
       b'groups': (EmptyFormatter()), 
       b'collectionItem': (EmptyFormatter()), 
       (PREMIUM_ENTITLEMENTS.BASIC): (PremiumDaysBonusFormatter()), 
       (PREMIUM_ENTITLEMENTS.PLUS): (PremiumDaysBonusFormatter()), 
       b'vehicles': (VehiclesBonusFormatter()), 
       b'meta': simpleBonusFormatter, 
       b'tokens': tokenBonusFormatter, 
       b'tankwomanBonus': (TankwomanBonusFormatter()), 
       b'battleToken': tokenBonusFormatter, 
       b'lootBoxToken': tokenBonusFormatter, 
       b'tankmen': (TankmenBonusFormatter()), 
       b'customizations': (CustomizationsBonusFormatter()), 
       b'goodies': (GoodiesBonusFormatter()), 
       b'items': (ItemsBonusFormatter()), 
       b'dossier': (DossierBonusFormatter()), 
       b'progressionXPToken': tokenBonusFormatter, 
       b'blueprints': (BlueprintBonusFormatter()), 
       b'blueprintsAny': (BlueprintBonusFormatter()), 
       b'finalBlueprints': (BlueprintBonusFormatter()), 
       b'crewSkins': (CrewSkinsBonusFormatter()), 
       b'crewBooks': (CrewBooksBonusFormatter()), 
       b'slots': countableIntegralBonusFormatter, 
       b'berths': countableIntegralBonusFormatter, 
       b'entitlements': (EntitlementFormatter()), 
       b'rankedDailyBattles': countableIntegralBonusFormatter, 
       b'rankedBonusBattles': countableIntegralBonusFormatter, 
       b'tmanToken': (TmanTemplateBonusFormatter()), 
       b'battlePassPoints': (BattlePassBonusFormatter()), 
       b'currencies': (CurrenciesBonusFormatter()), 
       b'preferredMapSlots': (PreferredMapSlotBonusFormatter())}


def getEpicFormattersMap():
    return {(Currency.CRYSTAL): (CrystalEpicBonusFormatter()), 
       b'goodies': (GoodiesEpicBonusFormatter()), 
       b'crewBooks': (CrewBooksEpicBonusFormatter()), 
       (PREMIUM_ENTITLEMENTS.PLUS): (PremiumDaysEpicBonusFormatter()), 
       b'items': (ItemsEpicBonusFormatter()), 
       b'blueprints': (BlueprintGroupEpicBonusFormatter()), 
       b'battlePassPoints': (BattlePassEpicBonusFormatter())}


def getEventBoardsFormattersMap():
    mapping = getDefaultFormattersMap()
    mapping.update({b'dossier': (EventBoardsDossierBonusFormatter()), 
       b'badgesGroup': (BadgesGroupBonusFormatter())})
    return mapping


def getEpicBattleFormattersMap():
    mapping = getDefaultFormattersMap()
    mapping.update({b'abilityPts': (EpicAbilityPtsFormatter()), 
       b'items': (EpicItemsBonusFormatter()), 
       b'dossier': (EpicDossierBonusFormatter()), 
       b'vehicles': (RankedVehiclesBonusFormatter()), 
       b'epicSelectToken': (InstructionEpicBattleBonusFormatter()), 
       b'goodies': (GoodiesEpicBattleBonusFormatter()), 
       b'entitlements': (EntitlementWulfTooltipFormatter()), 
       b'battleToken': (EpicBattleTokenBonusFormatter())})
    return mapping


def getEpicSetFormattersMap():
    mapping = getDefaultFormattersMap()
    mapping.update({b'abilityPts': (EpicAbilityPtsFormatter()), 
       b'items': (EpicItemsBonusFormatter()), 
       b'dossier': (EpicDossierBonusFormatter()), 
       b'vehicles': (RankedVehiclesBonusFormatter())})
    return mapping


def getPackRentVehiclesFormattersMap():
    mapping = getDefaultFormattersMap()
    mapping.update({b'vehicles': (RentVehiclesBonusFormatter())})
    return mapping


def getLootboxesFormatterMap():
    mapping = getDefaultFormattersMap()
    mapping.update({b'vehicles': (RentVehiclesBonusFormatter())})
    return mapping


def getPostBattleFormatterMap():
    mapping = getLootboxesFormatterMap()
    mapping.update({b'blueprints': (BlueprintGroupBonusFormatter()), 
       b'finalBlueprints': (BlueprintGroupBonusFormatter())})
    return mapping


def getMissionsDefaultFormatterMap():
    mapping = getDefaultFormattersMap()
    mapping.update({b'blueprints': (BlueprintGroupBonusFormatter()), 
       b'finalBlueprints': (BlueprintGroupBonusFormatter()), 
       b'entitlements': (EntitlementWulfTooltipFormatter())})
    return mapping


def getRankedFormatterMap(context=None):
    tokenBonusFormatter = RankedPointFormatter()
    mapping = getDefaultFormattersMap()
    mapping.update({b'tokens': tokenBonusFormatter, 
       b'selectableBonus': (RankedSelectableAwardFormatter()), 
       b'battleToken': tokenBonusFormatter, 
       b'vehicles': (RankedVehiclesBonusFormatter()), 
       b'items': (RankedItemsBonusFormatter()), 
       b'customizations': (RankedCustomizationsBonusFormatter())})
    return mapping


def getBattlePassFormatterMap():
    mapping = getDefaultFormattersMap()
    mapping.update({b'blueprints': (BlueprintGroupBonusFormatter()), 
       b'finalBlueprints': (BlueprintGroupBonusFormatter()), 
       b'items': (EpicItemsBonusFormatter()), 
       (PREMIUM_ENTITLEMENTS.BASIC): (BattlePassPremiumDaysBonusFormatter()), 
       (PREMIUM_ENTITLEMENTS.PLUS): (BattlePassPremiumDaysBonusFormatter())})
    return mapping


def getRoyaleFormatterMap():
    simpleBonusFormatter = SimpleBonusFormatter()
    return {(Currency.GOLD): simpleBonusFormatter, 
       (Currency.CREDITS): simpleBonusFormatter, 
       (Currency.CRYSTAL): simpleBonusFormatter, 
       (PREMIUM_ENTITLEMENTS.BASIC): (PremiumDaysBonusFormatter()), 
       (PREMIUM_ENTITLEMENTS.PLUS): (PremiumDaysBonusFormatter()), 
       b'customizations': (CustomizationsBonusFormatter()), 
       b'dossier': (DossierBonusFormatter())}


def getMarathonRewardScrenFormatterMap():
    mapping = getDefaultFormattersMap()
    mapping[PREMIUM_ENTITLEMENTS.BASIC] = PremiumDaysMarathonFormatter()
    mapping[PREMIUM_ENTITLEMENTS.PLUS] = PremiumDaysMarathonFormatter()
    mapping[b'tankmen'] = TankmenMarathonRewardBonusFormatter()
    return mapping


def getDefaultAwardFormatter():
    return AwardsPacker(getDefaultFormattersMap())


def getMissionsDefaultAwardFormatter():
    return AwardsPacker(getMissionsDefaultFormatterMap())


def getEpicAwardFormatter():
    return AwardsPacker(getEpicFormattersMap())


def getEpicBattleViewAwardPacker():
    return AwardsPacker(getEpicBattleFormattersMap())


def getEpicViewAwardPacker():
    return AwardsPacker(getEpicSetFormattersMap())


def getEventBoardsAwardPacker():
    return AwardsPacker(getEventBoardsFormattersMap())


def getPackRentVehiclesAwardPacker():
    return AwardsPacker(getPackRentVehiclesFormattersMap())


def getLootboxesAwardsPacker():
    return AwardsPacker(getLootboxesFormatterMap())


def getPostBattleAwardsPacker():
    return AwardsPacker(getPostBattleFormatterMap())


def getRankedAwardsPacker(context=None):
    return AwardsPacker(getRankedFormatterMap(context))


def getRoyaleAwardsPacker():
    return AwardsPacker(getRoyaleFormatterMap())


def getPersonalMissionAwardPacker():
    mapping = getDefaultFormattersMap()
    mapping.update({b'completionTokens': (CompletionTokensBonusFormatter()), 
       b'freeTokens': (FreeTokensBonusFormatter())})
    return AwardsPacker(mapping)


def getOperationPacker():
    mapping = getDefaultFormattersMap()
    mapping.update({b'customizations': (OperationCustomizationsBonusFormatter()), 
       b'battleToken': (CustomizationUnlockFormatter())})
    return AwardsPacker(mapping)


def getAnniversaryPacker():
    formattersMap = getDefaultFormattersMap()
    formattersMap[b'dossier'] = LoyalServiceBonusFormatter()
    return AwardsPacker(formattersMap)


def getBattlePassAwardsPacker():
    return AwardsPacker(getBattlePassFormatterMap())


def getMarathonRewardScreenPacker():
    return AwardsPacker(getMarathonRewardScrenFormatterMap())


def formatCountLabel(count, defaultStr=b''):
    if count > 1:
        return (b'x{}').format(count)
    return defaultStr


def formatTimeLabel(hours):
    time = hours
    if hours >= time_utils.HOURS_IN_DAY:
        time = ceil(hours / time_utils.HOURS_IN_DAY)
        timeMetric = i18n.makeString(b'#menu:header/account/premium/days')
    else:
        timeMetric = i18n.makeString(b'#menu:header/account/premium/hours')
    return str(int(time)) + b' ' + timeMetric


_PreformattedBonus = namedtuple(b'_PreformattedBonus', b'bonusName label userName images tooltip labelFormatter areTokensPawned specialArgs specialAlias isSpecial isCompensation align highlightType overlayType highlightIcon overlayIcon compensationReason postProcessTags isWulfTooltip padding gap ')

class PostProcessTags(CONST_CONTAINER):
    IS_SUFFIX_BADGE = b'isSuffixBadge'
    IS_PREFIX_BADGE = b'isPrefixBadge'

    @classmethod
    def getBadgeTag(cls, badge):
        if badge.isSuffixLayout():
            return cls.IS_SUFFIX_BADGE
        return cls.IS_PREFIX_BADGE


class PreformattedBonus(_PreformattedBonus):

    def getImage(self, size):
        return self.images.get(size, b'')

    def getFormattedLabel(self, formatter=None):
        formatter = formatter or self.labelFormatter
        if formatter and self.label:
            return formatter(self.label)
        return self.label

    def getHighlightType(self, size):
        types = self.highlightType
        return types and types.get(size, SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT) or SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT

    def getOverlayType(self, size):
        types = self.overlayType
        return types and types.get(size, SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT) or SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT

    def getHighlightIcon(self, size):
        icons = self.highlightIcon
        return icons and icons.get(size, SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT) or SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT

    def getOverlayIcon(self, size):
        icons = self.overlayIcon
        return icons and icons.get(size, SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT) or SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT

    def getGap(self, size):
        gap = self.gap
        return gap and gap.get(size, 0) or 0

    def getPadding(self, size):
        padding = self.padding
        return padding and padding.get(size, 0) or 0


PreformattedBonus.__new__.__defaults__ = (
 None, None, None, None, None, None, False, None, None, False, False,
 LABEL_ALIGN.CENTER, None, None, None, None, None, tuple(), False, 0, 0)

class QuestsBonusComposer(object):

    def __init__(self, awardsFormatter=None):
        self.__bonusFormatter = awardsFormatter or getDefaultAwardFormatter()
        return

    def getPreformattedBonuses(self, bonuses):
        return self.__bonusFormatter.format(bonuses)

    def getFormattedBonuses(self, bonuses, size=AWARDS_SIZES.SMALL):
        preformattedBonuses = self.getPreformattedBonuses(bonuses)
        return self._packBonuses(preformattedBonuses, size)

    def _packBonuses(self, preformattedBonuses, size):
        result = []
        for b in preformattedBonuses:
            result.append(self._packBonus(b, size))

        return result

    def _packBonus(self, bonus, size=AWARDS_SIZES.SMALL):
        return {b'label': (bonus.getFormattedLabel()), 
           b'imgSource': (bonus.getImage(size)), 
           b'tooltip': (bonus.tooltip), 
           b'isSpecial': (bonus.isSpecial), 
           b'specialAlias': (bonus.specialAlias), 
           b'specialArgs': (bonus.specialArgs), 
           b'align': (bonus.align), 
           b'userName': (bonus.userName)}


class AwardsPacker(object):

    def __init__(self, formatters=None):
        self.__formatters = formatters or {}
        return

    def format(self, bonuses):
        preformattedBonuses = []
        for b in bonuses:
            if b.isShowInGUI():
                formatter = self._getBonusFormatter(b)
                if formatter:
                    preformattedBonuses.extend(formatter.format(b))
                else:
                    _logger.warn(b'No formatter found for %s', b.getName())

        return preformattedBonuses

    def getFormattersMap(self):
        return self.__formatters

    def _getBonusFormatter(self, bonus):
        return self.__formatters.get(bonus.getName())


class AwardFormatter(object):

    def format(self, bonus):
        return self._format(bonus)

    def _format(self, bonus):
        return


class EmptyFormatter(AwardFormatter):

    def _format(self, bonus):
        return []


class SimpleBonusFormatter(AwardFormatter):

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=bonus.getName(), label=self._getLabel(bonus), userName=self._getUserName(bonus), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), tooltip=bonus.getTooltip(), align=self._getLabelAlign(bonus), isCompensation=self._isCompensation(bonus), highlightType=self._getHighlightType(bonus), overlayType=self._getOverlayType(bonus), highlightIcon=self._getHighlightIcon(bonus), overlayIcon=self._getOverlayIcon(bonus), compensationReason=self._getCompensationReason(bonus))]

    @classmethod
    def _getUserName(cls, bonus):
        return i18n.makeString(QUESTS.getBonusName(bonus.getName()))

    @classmethod
    def _getLabel(cls, bonus):
        return bonus.formatValue()

    @classmethod
    def _getLabelFormatter(cls, bonus):
        return TEXT_FORMATTERS.get(bonus.getName(), text_styles.stats)

    @classmethod
    def _getLabelAlign(cls, bonus):
        return TEXT_ALIGNS.get(bonus.getName(), LABEL_ALIGN.CENTER)

    @classmethod
    def _getImages(cls, bonus):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = AWARD_IMAGES.get(size, {}).get(bonus.getName())

        return result

    @classmethod
    def _isCompensation(cls, bonus):
        return bonus.isCompensation()

    @classmethod
    def _getHighlightType(cls, item):
        return {}

    @classmethod
    def _getOverlayType(cls, item):
        return {}

    @classmethod
    def _getHighlightIcon(cls, item):
        return {}

    @classmethod
    def _getOverlayIcon(cls, item):
        return {}

    @classmethod
    def _getCompensationReason(cls, bonus):
        compensationReasonBonus = bonus.getCompensationReason()
        if compensationReasonBonus is not None:
            bonusName = compensationReasonBonus.getName()
            bonusFormatter = getCompensationFormattersMap().get(bonusName)
            if bonusFormatter is not None:
                formattedReason = bonusFormatter.format(compensationReasonBonus)
                if formattedReason:
                    return formattedReason[0]
                return
        return


class CrystalEpicBonusFormatter(SimpleBonusFormatter):

    @classmethod
    def _getLabelFormatter(cls, bonus):
        return text_styles.textEpic

    @classmethod
    def _getImages(cls, bonus):
        size = EPIC_AWARD_SIZE
        return {size: (RES_ICONS.getBonusIcon(size, bonus.getName()))}


class CountableIntegralBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=bonus.getName(), label=formatCountLabel(bonus.getValue()), userName=self._getUserName(bonus), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), tooltip=bonus.getTooltip(), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus))]

    @classmethod
    def _getLabelFormatter(cls, bonus):
        return text_styles.stats

    @classmethod
    def _getImages(cls, bonus):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = RES_ICONS.getBonusIcon(size, bonus.getName())

        return result


class CompletionTokensBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        uniqueName = self._getUniqueName(bonus)
        return [
         PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(uniqueName), label=formatCountLabel(bonus.getCount()), images=self._getImages(uniqueName), tooltip=self._getTooltip(uniqueName), labelFormatter=self._getLabelFormatter(bonus), align=LABEL_ALIGN.RIGHT)]

    @classmethod
    def _getUserName(cls, nameID):
        return i18n.makeString(QUESTS.getBonusName(nameID))

    @classmethod
    def _getImages(cls, imageID):
        result = {}
        for size in COMPLETION_TOKENS_SIZES.ALL():
            result[size] = RES_ICONS.getBonusIcon(size, imageID)

        return result

    @classmethod
    def _getTooltip(cls, tooltipID):
        header = i18n.makeString(TOOLTIPS.getAwardHeader(tooltipID))
        body = i18n.makeString(TOOLTIPS.getAwardBody(tooltipID))
        if header or body:
            return makeTooltip(header or None, body or None)
        return b''

    @classmethod
    def _getUniqueName(cls, bonus):
        context = bonus.getContext()
        operationID = context[b'operationID']
        chainID = context[b'chainID']
        return b'%s_%s_%s' % (bonus.getName(), operationID, chainID)


class FreeTokensBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        areTokensPawned = bonus.areTokensPawned()
        ctx = bonus.getContext()
        if areTokensPawned:
            specialAlias = TOOLTIPS_CONSTANTS.FREE_SHEET_USED
            specialArgs = [ctx.get(b'campaignID')]
        else:
            specialAlias = TOOLTIPS_CONSTANTS.FREE_SHEET
            specialArgs = [ctx.get(b'campaignID')]
        return [
         PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(bonus), label=formatCountLabel(bonus.getCount()), images=self._getImages(bonus.getImageFileName()), labelFormatter=self._getLabelFormatter(bonus), align=LABEL_ALIGN.RIGHT, isCompensation=bonus.isCompensation(), isSpecial=True, specialAlias=specialAlias, specialArgs=specialArgs, areTokensPawned=areTokensPawned)]

    @classmethod
    def _getImages(cls, imageID):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = RES_ICONS.getBonusIcon(size, imageID)

        return result


class PremiumDaysBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(bonus), images=self._getImages(bonus), tooltip=bonus.getTooltip(), isCompensation=self._isCompensation(bonus))]

    @classmethod
    def _getImages(cls, bonus):
        result = {}
        for size in AWARDS_SIZES.ALL():
            imgPath = RES_ICONS.getPremiumDaysAwardIcon(size, bonus.getName(), bonus.getValue())
            if imgPath is None:
                imgPath = RES_ICONS.getPremiumDaysAwardIcon(size, bonus.getName(), b'universal')
            result[size] = imgPath

        return result


class PremiumDaysMarathonFormatter(PremiumDaysBonusFormatter):

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=b'items', label=formatCountLabel(bonus.getValue()), userName=self._getUserName(bonus), images=self._getImages(bonus), tooltip=bonus.getTooltip(), isCompensation=self._isCompensation(bonus))]

    @classmethod
    def _getImages(cls, bonus):
        result = {}
        for size in AWARDS_SIZES.ALL():
            imgPath = RES_ICONS.getPremiumDaysAwardIcon(size, bonus.getName(), b'universal')
            result[size] = imgPath

        return result


class PremiumDaysEpicBonusFormatter(PremiumDaysBonusFormatter):

    @classmethod
    def _getImages(cls, bonus):
        size = EPIC_AWARD_SIZE
        return {size: (RES_ICONS.getPremiumDaysAwardIcon(size, bonus.getName(), bonus.getValue()))}


class BattlePassPremiumDaysBonusFormatter(SimpleBonusFormatter):
    __PREMIUM_DAYS_ICONS = (1, 2, 3, 7, 14, 30, 90, 180, 360)

    def _format(self, bonus):
        count = bonus.getValue()
        hasOwnIcon = count in self.__PREMIUM_DAYS_ICONS
        return [
         PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(bonus), label=formatCountLabel(1 if hasOwnIcon else bonus.getValue()), labelFormatter=self._getLabelFormatter(bonus), align=LABEL_ALIGN.RIGHT, images=self._getImages(bonus, hasIcon=hasOwnIcon), tooltip=bonus.getTooltip(), isCompensation=self._isCompensation(bonus))]

    @classmethod
    def _getImages(cls, bonus, hasIcon=False):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = RES_ICONS.getPremiumDaysAwardIcon(size, bonus.getName(), bonus.getValue() if hasIcon else 1)

        return result


class SeniorityPremiumDaysBonusFormatter(PremiumDaysBonusFormatter):
    __PREMIUM_DAYS_ICONS = (1, 2, 3, 7, 14, 30, 90, 180, 360)

    def _format(self, bonus):
        return [
         PreformattedBonus(label=self._getLabel(bonus), bonusName=bonus.getName(), userName=self._getUserName(bonus), images=self._getImages(bonus), tooltip=bonus.getTooltip(), isCompensation=self._isCompensation(bonus))]

    @classmethod
    def _getLabel(cls, bonus):
        if bonus.getValue() not in cls.__PREMIUM_DAYS_ICONS:
            return formatTimeLabel(bonus.getValue() * time_utils.HOURS_IN_DAY)
        return


class TokenBonusFormatter(SimpleBonusFormatter):
    eventsCache = dependency.descriptor(IEventsCache)
    itemsCache = dependency.descriptor(IItemsCache)

    @staticmethod
    def getBonusFactorTooltip(name):
        return makeTooltip(header=backport.text(R.strings.tooltips.quests.bonuses.token.dyn(name).header()), body=backport.text(R.strings.tooltips.quests.bonuses.token.dyn(name).body()))

    def _format(self, bonus):
        result = []
        for tokenID, token in bonus.getTokens().iteritems():
            formatted = self._getFormattedBonus(tokenID, token, bonus)
            if formatted is not None:
                result.append(formatted)

        return result

    def _getFormattedBonus(self, tokenID, token, bonus):
        formatted = None
        complexToken = parseComplexToken(tokenID)
        if tokenID.startswith(BR_PROGRESSION_TOKEN):
            return self._formatBRComplexToken(complexToken, token, bonus)
        else:
            if complexToken.isDisplayable:
                formatted = self._formatComplexToken(complexToken, token, bonus)
            elif tokenID.startswith(LOOTBOX_TOKEN_PREFIX):
                formatted = self._formatLootBoxToken(tokenID, token, bonus)
            elif tokenID.startswith(LOOTBOX_KEY_PREFIX):
                formatted = self._formatLootBoxKey(tokenID, token, bonus)
            elif tokenID.startswith(BATTLE_BONUS_X5_TOKEN):
                formatted = self._formatBonusToken(BATTLE_BONUS_X5_TOKEN, token, bonus)
            elif tokenID.startswith(CREW_BONUS_X3_TOKEN):
                formatted = self._formatBonusToken(CREW_BONUS_X3_TOKEN, token, bonus)
            elif tokenID.startswith(RESOURCE_TOKEN_PREFIX):
                formatted = self._formatResource(token, bonus)
            elif isEarlyAccessToken(tokenID):
                formatted = self._formatEarlyAccessToken(token, bonus)
            return formatted

    def _formatBRComplexToken(self, complexToken, token, bonus):
        formatted = self._formatComplexToken(complexToken, token, bonus)
        return formatted._replace(tooltip=self.__getBRProgressionTooltip())

    def _formatBonusLabel(self, count):
        return formatCountLabel(count)

    def _getUserName(self, styleID):
        webCache = self.eventsCache.prefetcher
        return i18n.makeString(webCache.getTokenInfo(styleID))

    def _getTokenImages(self, styleID):
        result = {}
        webCache = self.eventsCache.prefetcher
        for awardSizeKey, awardSizeValue in AWARDS_SIZES.getIterator():
            for tokenSizeKey, tokenSizeValue in TOKEN_SIZES.getIterator():
                if awardSizeKey == tokenSizeKey:
                    result[awardSizeValue] = webCache.getTokenImage(styleID, tokenSizeValue)

        return result

    def _formatComplexToken(self, complexToken, token, bonus):
        userName = self._getUserName(complexToken.styleID)
        tokenBase = R.strings.tooltips.quests.bonuses.token
        eventTokenBase = tokenBase.dyn(complexToken.styleID)
        bodyResID = eventTokenBase.body() if eventTokenBase() != INVALID_RES_ID else tokenBase.body()
        description = self.eventsCache.prefetcher.getTokenDetailedInfo(complexToken.styleID)
        if description is None:
            description = backport.text(bodyResID)
        tooltip = makeTooltip(userName, description if description else None)
        return PreformattedBonus(bonusName=bonus.getName(), images=self._getTokenImages(complexToken.styleID), label=self._formatBonusLabel(token.count), userName=self._getUserName(complexToken.styleID), labelFormatter=self._getLabelFormatter(bonus), tooltip=tooltip, align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus))

    def _formatResource(self, token, bonus):
        images = {}
        tooltip = b''
        header = b''
        if hasattr(R.strings.tooltips.quests.bonuses.token.resource, bonus.resourceName):
            header = backport.text(getattr(R.strings.tooltips.quests.bonuses.token.resource, bonus.resourceName).header())
            tooltip = makeTooltip(header, backport.text(getattr(R.strings.tooltips.quests.bonuses.token.resource, bonus.resourceName).body()))
        for size in AWARDS_SIZES.ALL():
            images[size] = RES_ICONS.getResource(size, bonus.resourceName)

        return PreformattedBonus(bonusName=bonus.resourceName, images=images, label=self._formatBonusLabel(token.count), userName=header, labelFormatter=self._getLabelFormatter(bonus), tooltip=tooltip, align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus))

    def _formatLootBoxToken(self, tokenID, token, bonus):
        lootBox = self.itemsCache.items.tokens.getLootBoxByTokenID(tokenID)
        if lootBox is None or token.count <= 0:
            return
        images = {}
        for size in AWARDS_SIZES.ALL():
            images[size] = RES_ICONS.getLootBoxBonusIcon(size, lootBox.getIconName())

        return PreformattedBonus(label=self._formatBonusLabel(token.count), userName=lootBox.getUserName(), labelFormatter=self._getLabelFormatter(bonus), images=images, tooltip=makeTooltip(header=lootBox.getUserName(), body=lootBox.getDescriptionText()), align=self._getLabelAlign(bonus), isCompensation=self._isCompensation(bonus))

    def _formatLootBoxKey(self, tokenID, token, bonus):
        key = getKeyByTokenID(tokenID)
        if key is None or token.count <= 0:
            return
        images = {}
        iconName = key.iconName
        for size in AWARDS_SIZES.ALL():
            resId = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(iconName)
            if resId.isValid():
                images[size] = backport.image(resId())
            else:
                _logger.warning(b'Resouce is invalid gui/maps/icons/quests/bonuses/%s/%s', size, iconName)

        return PreformattedBonus(label=self._formatBonusLabel(token.count), userName=backport.text(R.strings.lootboxes.userName.dyn(key.userName)()), labelFormatter=self._getLabelFormatter(bonus), images=images, tooltip=TOOLTIPS_CONSTANTS.LOOT_BOX_KEY_TOOLTIP, specialArgs=[
         key.keyID], isWulfTooltip=True, align=self._getLabelAlign(bonus), isCompensation=self._isCompensation(bonus))

    def _formatEarlyAccessToken(self, token, bonus):
        if token.count <= 0:
            return None
        else:
            images = {}
            padding = {}
            gap = {}
            for size in AWARDS_SIZES.ALL():
                images[size] = EARLY_ACCESS_TOKEN_IMAGES[size]
                padding[size] = EARLY_ACCESS_TOKEN_IMAGES_PADDINGS[size]
                gap[size] = EARLY_ACCESS_TOKEN_IMAGES_GAP[size]

            return PreformattedBonus(label=self._formatBonusLabel(token.count), userName=backport.text(R.strings.early_access.currencyToken()), labelFormatter=self._getLabelFormatter(bonus), images=images, align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), tooltip=TOOLTIPS_CONSTANTS.EARLY_ACCESS_CURRENCY, isWulfTooltip=True, padding=padding, gap=gap)

    def _formatBonusToken(self, name, token, bonus):
        if token.count <= 0:
            return None
        else:
            return PreformattedBonus(bonusName=bonus.getName(), label=self._formatBonusLabel(token.count), userName=bonus.getUserName(), labelFormatter=self._getLabelFormatter(bonus), images=self.__getBonusFactorImages(name), tooltip=self.getBonusFactorTooltip(name), align=self._getLabelAlign(bonus), isCompensation=self._isCompensation(bonus))

    @staticmethod
    def __getBonusFactorImages(name):
        images = {}
        for size in AWARDS_SIZES.ALL():
            bonusTaskRes = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(name)
            images[size] = backport.image(bonusTaskRes()) if bonusTaskRes.isValid() else None

        return images

    @staticmethod
    def __getBRProgressionTooltip():
        tokenBase = R.strings.battle_royale_progression.quests.bonuses.progressionToken
        return makeTooltip(backport.text(tokenBase.header()), backport.text(tokenBase.body()))


class RankedPointFormatter(TokenBonusFormatter):

    def _format(self, bonus):
        result = []
        for tokenID, token in bonus.getTokens().iteritems():
            formatted = None
            if tokenID.startswith(YEAR_POINTS_TOKEN):
                formatted = self.__formatRankedPointToken(tokenID, token, bonus)
            if formatted is not None:
                result.append(formatted)

        return result

    @classmethod
    def _getUserName(cls, bonus):
        return backport.text(R.strings.tooltips.rankedBattleView.scorePoint.short.header())

    def __formatRankedPointToken(self, tokenID, token, bonus):
        return PreformattedBonus(label=self._formatBonusLabel(token.count), userName=self._getUserName(bonus), labelFormatter=self._getLabelFormatter(bonus), images=self.__getImages(tokenID), tooltip=makeTooltip(header=backport.text(R.strings.tooltips.rankedBattleView.scorePoint.header()), body=backport.text(R.strings.tooltips.rankedBattleView.scorePoint.body())), align=self._getLabelAlign(bonus), isCompensation=self._isCompensation(bonus))

    def __getImages(self, tokenID):
        return {size: backport.image(self.__getImagePath(tokenID, size)()) for size in AWARDS_SIZES.ALL() if self.__getImagePath(tokenID, size)}

    @staticmethod
    def __getImagePath(tokenID, size):
        if tokenID.startswith(YEAR_POINTS_TOKEN):
            return R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(b'rankedPoint')
        else:
            return

    @classmethod
    def _getLabelAlign(cls, bonus):
        return LABEL_ALIGN.RIGHT


class RankedSelectableAwardFormatter(TokenBonusFormatter):
    __offersDP = dependency.descriptor(IOffersDataProvider)

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=bonus.getName(), label=self._formatBonusLabel(self.__getCountForLabel(bonus)), userName=backport.text(R.strings.ranked_battles.yearRewards.tooltip.equipmentChoice.title()), labelFormatter=self._getLabelFormatter(bonus), images=self.__getImages(bonus), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), specialAlias=TOOLTIPS_CONSTANTS.BATTLE_PASS_GIFT_TOKEN, specialArgs=[
          first(bonus.getValue().keys()), True], isSpecial=True)]

    def __getCountForLabel(self, bonus):
        for giftTokenID in bonus.getTokens().iterkeys():
            tokenID = getOfferTokenByGift(giftTokenID)
            if self.__offersDP.getOfferByToken(tokenID) is not None:
                return self.__offersDP.getAmountOfGiftsGenerated(tokenID, 1)

        return 0

    @staticmethod
    def __getImages(bonus):
        imagesRoot = R.images.gui.maps.icons.quests.bonuses
        return {size: backport.image(imagesRoot.dyn(size).dyn(bonus.getType())()) for size in AWARDS_SIZES.ALL()}


class EpicAbilityPtsFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        return [
         PreformattedBonus(label=self._formatBonusLabel(bonus.getValue()), userName=backport.text(R.strings.epic_battle.epicBattleItem.supplyPoints.header()), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), tooltip=makeTooltip(header=backport.text(R.strings.epic_battle.epicBattleItem.supplyPoints.header()), body=backport.text(R.strings.epic_battle.epicBattleItem.supplyPoints.description())), align=LABEL_ALIGN.CENTER, isCompensation=self._isCompensation(bonus))]

    def _formatBonusLabel(self, count):
        return count

    @classmethod
    def _getImages(cls, bonus):
        images = {}
        for size in AWARDS_SIZES.ALL():
            res = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(b'epicAbilityPoint')
            if res:
                images[size] = backport.image(res())

        return images

    @classmethod
    def _getLabelAlign(cls, bonus):
        return LABEL_ALIGN.RIGHT


class TmanTemplateBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        for tokenID, token in bonus.getTokens().iteritems():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                formatted = self.__formatTmanTemplateToken(tokenID, token, bonus)
                if formatted is None:
                    _logger.error(b'Received wrong tman_template token from server: %s', tokenID)
                else:
                    result.append(formatted)

        return result

    def __formatTmanTemplateToken(self, tokenID, _, bonus):
        recruitInfo = getRecruitInfo(tokenID)
        if recruitInfo is None:
            return
        else:
            images = {}
            if recruitInfo.isFemale():
                bonusImageName = b'tankwoman'
            else:
                bonusImageName = b'tankman'
            for size in AWARDS_SIZES.ALL():
                images[size] = RES_ICONS.getBonusIcon(size, bonusImageName)

            nameStr = recruitInfo.getFullUserNameByNation(nationID=None)
            return PreformattedBonus(bonusName=bonus.getName(), userName=nameStr, label=b'', images=images, labelFormatter=self._getLabelFormatter(bonus), align=self._getLabelAlign(bonus), specialAlias=TOOLTIPS_CONSTANTS.TANKMAN_NOT_RECRUITED, specialArgs=[
             tokenID], isSpecial=True)


class CustomizationUnlockFormatter(TokenBonusFormatter):
    c11n = dependency.descriptor(ICustomizationService)
    __TOKEN_POSTFIX = b':camouflage'
    __ICON_NAME = b'camouflage'

    def _format(self, bonus):
        tokens = bonus.getTokens()
        unlockTokenID = findFirst((lambda ID: ID.endswith(self.__TOKEN_POSTFIX)), tokens.keys())
        if unlockTokenID is not None:
            camouflages = self.c11n.getCamouflages(criteria=REQ_CRITERIA.CUSTOMIZATION.UNLOCKED_BY(unlockTokenID))
            branch = bonus.getContext().get(b'branch')
            if branch == PM_BRANCH.REGULAR:
                tooltip = makeTooltip(TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_HEADER, TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_BODY)
            elif branch == PM_BRANCH.PERSONAL_MISSION_2:
                tooltip = makeTooltip(TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_ALLIANCE_HEADER, TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_ALLIANCE_BODY)
            else:
                tooltip = None
            images = {size: RES_ICONS.getBonusIcon(size, self.__ICON_NAME) for size in AWARDS_SIZES.ALL()}
            result = [
             PreformattedBonus(bonusName=bonus.getName(), label=formatCountLabel(len(camouflages)), align=LABEL_ALIGN.RIGHT, images=images, isSpecial=False, tooltip=tooltip)]
        else:
            result = []
        return result


class VehiclesBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        result.extend(self._formatVehicle(bonus, bonus.getVehicles()))
        return result

    def _formatVehicle(self, bonus, vehicles):
        result = []
        for vehicle, vehInfo in vehicles:
            compensation = bonus.compensation(vehicle, bonus)
            if compensation:
                formatter = SimpleBonusFormatter()
                for bonusComp in compensation:
                    formattedComp = formatter.format(bonusComp)
                    result.extend(formattedComp)

            else:
                result.append(self._appendFormattedVehicle(bonus, vehicle, vehInfo))

        return result

    def _getUserName(self, vehicle):
        return vehicle.userName

    @classmethod
    def _getLabel(cls, vehicle):
        if cls.__hasUniqueIcon(vehicle):
            return vehicle.userName
        return b''

    @classmethod
    def _getVehicleLabel(cls, bonus, vehicle, vehInfo):
        return cls._getLabel(vehicle)

    @classmethod
    def _getImages(cls, vehicle, isRent=False):
        result = {}
        for size in AWARDS_SIZES.ALL():
            image = (b'../maps/icons/quests/bonuses/{}/{}').format(size, getItemIconName(vehicle.name))
            if image in RES_ICONS.MAPS_ICONS_QUESTS_BONUSES_ALL_ENUM:
                result[size] = image
            else:
                if isRent:
                    image = RES_ICONS.getRentVehicleAwardIcon(size)
                else:
                    image = RES_ICONS.getVehicleAwardIcon(size)
                result[size] = image

        return result

    @classmethod
    def __hasUniqueIcon(cls, vehicle):
        for size in AWARDS_SIZES.ALL():
            if cls._getImages(vehicle).get(size) != RES_ICONS.getVehicleAwardIcon(size):
                return True

        return False

    def _appendFormattedVehicle(self, bonus, vehicle, vehInfo):
        tmanRoleLevel = bonus.getTmanRoleLevel(vehInfo)
        rentDays = bonus.getRentDays(vehInfo)
        rentBattles = bonus.getRentBattles(vehInfo)
        rentWins = bonus.getRentWins(vehInfo)
        rentSeason = bonus.getRentSeason(vehInfo)
        rentCycle = bonus.getRentCycle(vehInfo)
        if rentDays:
            rentExpiryTime = time_utils.getCurrentTimestamp()
            rentExpiryTime += rentDays * time_utils.ONE_DAY
        else:
            rentExpiryTime = 0
        isRent = rentDays or rentBattles or rentWins or rentSeason or rentCycle
        return PreformattedBonus(bonusName=bonus.getName(), label=self._getVehicleLabel(bonus, vehicle, vehInfo), labelFormatter=self._getLabelFormatter(bonus), userName=self._getUserName(vehicle), images=self._getImages(vehicle, isRent), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.AWARD_VEHICLE, specialArgs=[
         vehicle.intCD, tmanRoleLevel, rentExpiryTime, rentBattles, rentWins, rentSeason, rentCycle], isCompensation=self._isCompensation(bonus))


class RankedVehiclesBonusFormatter(VehiclesBonusFormatter):

    @classmethod
    def _getLabel(cls, vehicle):
        return vehicle.shortUserName

    @classmethod
    def _getVehicleLabel(cls, bonus, vehicle, vehInfo):
        return cls._getLabel(vehicle)

    @classmethod
    def _getLabelFormatter(cls, bonus):
        return text_styles.stats


class VehiclesCompensationFormatter(VehiclesBonusFormatter):

    def _formatVehicle(self, bonus, vehicles):
        result = []
        for vehicle, vehInfo in vehicles:
            compensation = bonus.checkIsCompensatedVehicle(vehicle)
            if compensation:
                result.append(self._appendFormattedVehicle(bonus, vehicle, vehInfo))

        return result

    @classmethod
    def _getLabel(cls, vehicle):
        if cls.__hasUniqueIcon(vehicle):
            return vehicle.shortUserName
        return b''

    @classmethod
    def __hasUniqueIcon(cls, vehicle):
        return True


class RentVehiclesBonusFormatter(VehiclesBonusFormatter):

    def _format(self, bonus):
        result = []
        rentVehicles = []
        restVehicles = []
        for vehicle, vehInfo in bonus.getVehicles():
            if bonus.isRentVehicle(vehInfo):
                rentVehicles.append((vehicle, vehInfo))
            elif bonus.isNonZeroCompensation(vehInfo):
                restVehicles.append((vehicle, vehInfo))

        result.extend(self._formatRent(bonus, rentVehicles))
        result.extend(self._formatVehicle(bonus, restVehicles))
        return result

    def _formatRent(self, bonus, vehicles):
        result = []
        if not vehicles:
            return result
        if len(vehicles) == 1:
            result.extend(self._formatVehicle(bonus, vehicles))
        else:
            result.append(PreformattedBonus(bonusName=PACK_RENT_VEHICLES_BONUS, label=formatCountLabel(len(vehicles)), labelFormatter=text_styles.stats, images=self._getRentImages(), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.PACK_RENT_VEHICLES, specialArgs=self._getRentArgs(bonus, vehicles)))
        return result

    @classmethod
    def _getRentImages(cls):
        result = {}
        for size in AWARDS_SIZES.ALL():
            image = RES_ICONS.getRentVehicleAwardIcon(size)
            result[size] = image

        return result

    @classmethod
    def _getRentArgs(cls, bonus, vehicles):
        rentArgs = []
        for vehicle, vehInfo in vehicles:
            rentDays = bonus.getRentDays(vehInfo)
            rentBattles = bonus.getRentBattles(vehInfo)
            rentWins = bonus.getRentWins(vehInfo)
            shortData = {b'vehicleName': (vehicle.userName), 
               b'isPremium': (vehicle.isPremium), 
               b'vehicleType': (vehicle.type), 
               b'rentDays': rentDays, 
               b'rentBattles': rentBattles, 
               b'rentWins': rentWins}
            rentArgs.append(shortData)

        return rentArgs


class DossierBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        for achievement in bonus.getAchievements():
            result.append(PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(achievement), images=self._getImages(achievement), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.BATTLE_STATS_ACHIEVS, specialArgs=[
             achievement.getBlock(), achievement.getName(), achievement.getValue()], isCompensation=self._isCompensation(bonus)))

        for badge in bonus.getBadges():
            result.append(PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(badge), images=self._getBadgeImages(badge), isSpecial=True, specialAlias=self._getBadgeTooltipAlias(), specialArgs=[
             badge.badgeID], isCompensation=self._isCompensation(bonus), postProcessTags=(
             PostProcessTags.getBadgeTag(badge),)))

        return result

    @classmethod
    def _getUserName(cls, achievement):
        return achievement.getUserName()

    @classmethod
    def _getImages(cls, bonus):
        return {(AWARDS_SIZES.SMALL): (bonus.getSmallIcon()), 
           (AWARDS_SIZES.BIG): (bonus.getBigIcon())}

    @classmethod
    def _getBadgeImages(cls, bonus):
        return {(AWARDS_SIZES.SMALL): (bonus.getAwardBadgeIcon(ICONS_SIZES.X48)), 
           (AWARDS_SIZES.BIG): (bonus.getAwardBadgeIcon(ICONS_SIZES.X80))}

    @classmethod
    def _getBadgeTooltipAlias(cls):
        return TOOLTIPS_CONSTANTS.BADGE


class LoyalServiceBonusFormatter(DossierBonusFormatter):

    def _format(self, bonus):
        result = super(LoyalServiceBonusFormatter, self)._format(bonus)
        result.sort(key=(lambda preFormattedBonus: int(not (PostProcessTags.IS_PREFIX_BADGE in preFormattedBonus.postProcessTags or PostProcessTags.IS_SUFFIX_BADGE in preFormattedBonus.postProcessTags))))
        return result

    @classmethod
    def _getBadgeTooltipAlias(cls):
        return TOOLTIPS_CONSTANTS.BADGE_LOYAL_SERVICE


class EventBoardsDossierBonusFormatter(DossierBonusFormatter):

    @classmethod
    def _getBadgeTooltipAlias(cls):
        return TOOLTIPS_CONSTANTS.EVENT_BOARDS_BADGE


class BadgesGroupBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        badges = bonus.getBadges()
        groupID = bonus.getValue()
        result.append(PreformattedBonus(images={(AWARDS_SIZES.SMALL): (RES_ICONS.getEventBoardBadgesGroup(groupID))}, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.EVENT_BOARDS_BADGES_GROUP, specialArgs=self.__badgesTooltipData(badges), isCompensation=self._isCompensation(bonus)))
        return result

    @classmethod
    def __badgesTooltipData(cls, badges):
        result = []
        for badge in badges:
            result.append({b'name': (badge.getUserName()), 
               b'imgSource': (badge.getSmallIcon()), 
               b'desc': (badge.getUserDescription())})

        return result


class TankmenBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        for group in bonus.getTankmenGroups().itervalues():
            if group[b'skills']:
                key = b'with_skills'
            else:
                key = b'no_skills'
            label = b'#quests:bonuses/item/tankmen/%s' % key
            result.append(PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(key), images=self._getImages(bonus), tooltip=makeTooltip(TOOLTIPS.getAwardHeader(bonus.getName()), i18n.makeString(label, **group)), isCompensation=self._isCompensation(bonus)))

        return result

    @classmethod
    def _getUserName(cls, key):
        return i18n.makeString(b'#quests:bonusName/tankmen/%s' % key)

    @classmethod
    def _getImages(cls, bonus):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = RES_ICONS.getBonusIcon(size, bonus.getName())

        return result


class TankmenMarathonRewardBonusFormatter(TankmenBonusFormatter):

    def _format(self, bonus):
        result = []
        for group in bonus.getTankmenGroups().itervalues():
            if group[b'skills']:
                key = b'with_skills'
            else:
                key = b'no_skills'
            label = b'#quests:bonuses/item/tankmen/%s' % key
            result.append(PreformattedBonus(bonusName=bonus.getName(), userName=self._getUserName(key), images=self._getImages(bonus), specialAlias=TOOLTIPS_CONSTANTS.TANKMAN, tooltip=makeTooltip(backport.text(R.strings.marathon.rewardTooltip.tankmen.header()), i18n.makeString(label, **group)), isCompensation=self._isCompensation(bonus)))

        return result


class TankwomanBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        for tmanInfo in bonus.getTankmenData():
            if tmanInfo.isFemale:
                bonusID = b'tankwoman'
                username = i18n.makeString(QUESTS.BONUSES_ITEM_TANKWOMAN)
                result.append(PreformattedBonus(bonusName=bonus.getName(), userName=username, images=self._getImages(bonusID), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_TANKWOMAN, specialArgs=[]))
            else:
                bonusID = b'tankman'
                username = i18n.makeString(QUESTS.BONUSES_TANKMEN_DESCRIPTION, value=getRoleUserName(tmanInfo.role))
                result.append(PreformattedBonus(bonusName=bonus.getName(), userName=username, images=self._getImages(bonusID), tooltip=makeTooltip(i18n.makeString(QUESTS.BONUSES_TANKMEN_DESCRIPTION, value=getRoleUserName(tmanInfo.role)))))

        return result

    @classmethod
    def _getImages(cls, imageID):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = RES_ICONS.getBonusIcon(size, imageID)

        return result


class CustomizationsBonusFormatter(SimpleBonusFormatter):
    c11n = dependency.descriptor(ICustomizationService)

    def _format(self, bonus):
        customizations = zip(bonus.getCustomizations(), bonus.getList())
        result = [self._createCustomizationBonus(bonus, item, data) for item, data in customizations]
        return result

    def _formatBonusLabel(self, count):
        return formatCountLabel(count)

    def _createCustomizationBonus(self, bonus, item, data):
        c11nItem = bonus.getC11nItem(item)
        return PreformattedBonus(bonusName=bonus.getName(), images=self._getImages(c11nItem), userName=self._getUserName(c11nItem), label=self._formatBonusLabel(item.get(b'value')), labelFormatter=self._getLabelFormatter(bonus), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_AWARD, specialArgs=CustomizationTooltipContext(itemCD=data.get(b'intCD')), isCompensation=self._isCompensation(bonus), align=LABEL_ALIGN.RIGHT)

    @classmethod
    def _getImages(cls, c11nItem):
        result = {}
        for size in AWARDS_SIZES.ALL():
            iconName = c11nItem.itemTypeName
            if iconName == b'style' and c11nItem.modelsSet:
                iconName = b'style_3d'
            result[size] = RES_ICONS.getBonusIcon(size, iconName)

        return result

    @classmethod
    def _getUserName(cls, c11nItem):
        return i18n.makeString(QUESTS.getBonusName(c11nItem.itemTypeName))


class RankedCustomizationsBonusFormatter(CustomizationsBonusFormatter):

    @classmethod
    def _getImages(cls, c11nItem):
        result = {}
        for size in AWARDS_SIZES.ALL():
            resource = R.images.gui.maps.icons.rankedBattles.bonusIcons.dyn((b'style_{}').format(c11nItem.id))
            iconName = c11nItem.itemTypeName
            if not resource.isValid():
                if iconName == b'style' and c11nItem.modelsSet:
                    iconName = b'style_3d'
                resource = R.images.gui.maps.icons.quests.bonuses.dyn(size).dyn(iconName)
            if resource.isValid():
                result[size] = backport.image(resource())

        return result


class OperationCustomizationsBonusFormatter(CustomizationsBonusFormatter):

    def _format(self, bonus):
        customizations = {}
        for item in bonus.getCustomizations():
            cType = item.get(b'custType')
            if cType in customizations:
                item, count = customizations[cType]
                customizations[cType] = (item, count + 1)
            else:
                customizations[cType] = (
                 item, 1)

        branch = bonus.getContext().get(b'branch')
        if branch == PM_BRANCH.REGULAR:
            tooltip = makeTooltip(TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_HEADER, TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_BODY)
        elif branch == PM_BRANCH.PERSONAL_MISSION_2:
            tooltip = makeTooltip(TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_ALLIANCE_HEADER, TOOLTIPS.PERSONALMISSIONS_AWARDS_CAMOUFLAGE_ALLIANCE_BODY)
        else:
            tooltip = None
        result = []
        for item, count in customizations.itervalues():
            c11nItem = bonus.getC11nItem(item)
            result.append(PreformattedBonus(bonusName=bonus.getName(), images=self._getImages(c11nItem), userName=self._getUserName(c11nItem), label=formatCountLabel(count), labelFormatter=self._getLabelFormatter(bonus), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), isSpecial=False, tooltip=tooltip))

        return result


class InstructionEpicBattleBonusFormatter(SimpleBonusFormatter):
    _offersProvider = dependency.descriptor(IOffersDataProvider)

    def _getLabel(self, bonus):
        gifts = self._getGiftsCount(bonus)
        if gifts > 0:
            return formatCountLabel(gifts)
        return b''

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=bonus.getName(), label=self._getLabel(bonus), userName=self._getUserName(bonus), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), compensationReason=self._getCompensationReason(bonus), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.EPIC_BATTLE_INSTRUCTION_TOOLTIP, specialArgs=[
          self._getTokenName(bonus)])]

    @classmethod
    def _getImages(cls, bonus):
        bonusType = cls._getType(bonus)
        result = {(AWARDS_SIZES.SMALL): (backport.image(R.images.gui.maps.icons.quests.bonuses.small.dyn(bonusType)())), 
           (AWARDS_SIZES.BIG): (backport.image(R.images.gui.maps.icons.quests.bonuses.big.dyn(bonusType)()))}
        return result

    @classmethod
    def _getUserName(cls, bonus):
        bonusType = cls._getType(bonus)
        return backport.text(R.strings.tooltips.epicBattlesOffer.title.dyn(bonusType)())

    def _getGiftsCount(self, bonus):
        bonusOffers = []
        for k in bonus.getValue().iterkeys():
            tokenName = k.replace(b'_gift', b'')
            bonusOffers.append(self._offersProvider.getOfferByToken(tokenName))

        giftsCount = 0
        for bonusOffer in bonusOffers:
            if bonusOffer and hasattr(bonusOffer, b'getFirstGift'):
                gift = bonusOffer.getFirstGift()
                giftsCount += gift.giftCount if gift is not None else 0

        return giftsCount

    @classmethod
    def _getTokenName(cls, bonus):
        return bonus.getValue().keys()[0]

    @classmethod
    def _getType(cls, bonus):
        bonusType = cls._getTokenName(bonus).split(b':')[2]
        return bonusType


class GoodiesEpicBattleBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        goodID = list(bonus.getValue())[0]
        return [
         PreformattedBonus(bonusName=bonus.getName(), label=self._getLabel(bonus), userName=self._getUserName(bonus), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), compensationReason=self._getCompensationReason(bonus), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.EPIC_BATTLE_RECERTIFICATION_FORM_TOOLTIP, specialArgs=[
          goodID])]

    def _getLabel(self, bonus):
        return formatCountLabel(list(bonus.getValue().values())[0][b'count'])

    @classmethod
    def _getImages(cls, _):
        return getRecertificationFormImages()


class EpicBattleTokenBonusFormatter(TokenBonusFormatter):

    def _getFormattedBonus(self, tokenID, token, bonus):
        if tokenID.startswith(EPIC_ARMORY_YARD_TOKEN_NAME):
            count = self.itemsCache.items.tokens.getTokenCount(tokenID)
            if token.limit and count < token.limit:
                formatted = self._formatArmoryYardToken(bonus, token)
                return formatted
        return super(EpicBattleTokenBonusFormatter, self)._getFormattedBonus(tokenID, token, bonus)

    def _formatArmoryYardToken(self, bonus, token):
        return PreformattedBonus(label=self.__getArmoryYardLabel(token), userName=backport.text(R.strings.fl_tooltips.armoryYard.currency.progression_token.title()), labelFormatter=self._getLabelFormatter(bonus), images=self.__getArmoryYardImages(), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), compensationReason=self._getCompensationReason(bonus), tooltip=self.__getArmoryYardTooltip())

    @staticmethod
    def __getArmoryYardLabel(token):
        if token.count > 1:
            return (b'x{}').format(token.count)
        return b''

    @staticmethod
    def __getArmoryYardImages():
        return {(AWARDS_SIZES.SMALL): (backport.image(R.images.frontline.gui.maps.icons.bonuses.armory_yard_s48())), 
           (AWARDS_SIZES.BIG): (backport.image(R.images.frontline.gui.maps.icons.bonuses.armory_yard_s80()))}

    @staticmethod
    def __getArmoryYardTooltip():
        armoryYardCurrency = R.strings.fl_tooltips.armoryYard.currency
        featureName = backport.text(armoryYardCurrency.featureName())
        armoryYardTooltip = makeTooltip(header=backport.text(armoryYardCurrency.progression_token.title()), body=backport.text(armoryYardCurrency.progression_token.description(), featureName=featureName))
        return armoryYardTooltip


class GoodiesBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        for booster, count in bonus.getBoosters().iteritems():
            if booster is not None:
                result.append(PreformattedBonus(bonusName=bonus.getName(), images=self._getImages(booster), isSpecial=True, label=formatCountLabel(count), labelFormatter=self._getLabelFormatter(bonus), userName=self._getUserName(booster), specialAlias=TOOLTIPS_CONSTANTS.SHOP_BOOSTER, specialArgs=[
                 booster.boosterID], align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus)))

        for demountKit, count in bonus.getDemountKits().iteritems():
            if demountKit is not None:
                result.append(PreformattedBonus(bonusName=bonus.getName(), images=self._getDemountKitImages(demountKit), isSpecial=True, label=formatCountLabel(count), labelFormatter=self._getLabelFormatter(bonus), userName=demountKit.userName, specialAlias=TOOLTIPS_CONSTANTS.AWARD_DEMOUNT_KIT, specialArgs=[
                 demountKit.intCD], align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus)))

        for form, count in bonus.getRecertificationForms().iteritems():
            if form is not None:
                result.append(PreformattedBonus(bonusName=bonus.getName(), label=formatCountLabel(count), userName=form.userName, labelFormatter=self._getLabelFormatter(bonus), images=self._getImagesRecertificationForm(form), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.EPIC_BATTLE_RECERTIFICATION_FORM_TOOLTIP, specialArgs=[
                 form.goodieID]))

        return result

    @classmethod
    def _getImagesRecertificationForm(cls, _):
        return getRecertificationFormImages()

    @classmethod
    def _getImages(cls, booster):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = RES_ICONS.getBonusIcon(size, booster.getFullNameForResource())

        return result

    @classmethod
    def _getDemountKitImages(cls, demountKit):
        return {(AWARDS_SIZES.SMALL): (demountKit.getIcon(ICONS_SIZES.X48)), 
           (AWARDS_SIZES.BIG): (demountKit.getIcon(ICONS_SIZES.X80))}

    @classmethod
    def _getUserName(cls, booster):
        return booster.userName


class GoodiesEpicBonusFormatter(GoodiesBonusFormatter):

    @classmethod
    def _getLabelFormatter(cls, bonus):
        return text_styles.textEpic

    @classmethod
    def _getIcon(cls, guiTypeName):
        size = EPIC_AWARD_SIZE
        return {size: (RES_ICONS.getBonusIcon(size, guiTypeName))}

    @classmethod
    def _getImages(cls, booster):
        return cls._getIcon(booster.getFullNameForResource())

    @classmethod
    def _getDemountKitImages(cls, demountKit):
        return cls._getIcon(demountKit.demountKitGuiType)


class ItemsBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        for item, count in sorted(bonus.getItems().items(), key=(lambda i: i[0])):
            if item is not None and count:
                result.append(PreformattedBonus(bonusName=bonus.getName(), images=self._getImages(item), isSpecial=True, label=self._formatBonusLabel(count), labelFormatter=self._getLabelFormatter(bonus), userName=self._getUserName(item), specialAlias=self.getTooltip(item), specialArgs=[
                 item.intCD], align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonus), highlightType=self._getHighlightType(item), overlayType=self._getOverlayType(item), highlightIcon=self._getHighlightIcon(item), overlayIcon=self._getOverlayIcon(item)))

        return result

    def _formatBonusLabel(self, count):
        return formatCountLabel(count)

    @classmethod
    def _getUserName(cls, item):
        return item.userName

    @classmethod
    def _getImages(cls, item):
        result = {}
        for size in AWARDS_SIZES.ALL():
            result[size] = RES_ICONS.getBonusIcon(size, item.getGUIEmblemID())

        return result

    @classmethod
    def getTooltip(cls, item):
        if item.itemTypeID == GUI_ITEM_TYPE.EQUIPMENT and b'avatar' in item.tags:
            return TOOLTIPS_CONSTANTS.BATTLE_CONSUMABLE
        if item.itemTypeID == GUI_ITEM_TYPE.SHELL:
            return TOOLTIPS_CONSTANTS.AWARD_SHELL
        if item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER:
            return TOOLTIPS_CONSTANTS.AWARD_BATTLE_BOOSTER
        return TOOLTIPS_CONSTANTS.AWARD_MODULE

    @classmethod
    def _getHighlightType(cls, item):
        return {(AWARDS_SIZES.BIG): (item.getBigHighlightType()), 
           (AWARDS_SIZES.SMALL): (item.getHighlightType())}

    @classmethod
    def _getOverlayType(cls, item):
        return {(AWARDS_SIZES.BIG): (item.getBigOverlayType()), 
           (AWARDS_SIZES.SMALL): (item.getOverlayType())}

    @classmethod
    def _getHighlightIcon(cls, item):
        result = {}
        for size in AWARDS_SIZES.ALL():
            if item.itemTypeName == SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER_NAME:
                result[size] = RES_ICONS.getBonusHighlight(size, SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER)
            else:
                result[size] = SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT

        return result

    @classmethod
    def _getOverlayIcon(cls, item):
        result = {}
        itemTypeName = item.itemTypeName
        for size in AWARDS_SIZES.ALL():
            if itemTypeName == SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER_NAME:
                if item.isCrewBooster():
                    result[size] = RES_ICONS.getBonusOverlay(size, SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER_CREW_REPLACE)
                else:
                    result[size] = RES_ICONS.getBonusOverlay(size, SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER)
            elif item.getOverlayType():
                result[size] = RES_ICONS.getBonusOverlay(size, item.getOverlayType())

        return result


class ItemsEpicBonusFormatter(ItemsBonusFormatter):

    @classmethod
    def _getImages(cls, item):
        size = EPIC_AWARD_SIZE
        return {size: (RES_ICONS.getBonusIcon(size, item.getGUIEmblemID()))}


class EpicItemsBonusFormatter(ItemsBonusFormatter):

    @classmethod
    def _getImages(cls, item):
        result = {}
        for size in AWARDS_SIZES.ALL():
            if item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER and item.isCrewBooster():
                result[size] = RES_ICONS.getBonusIcon(size, item.name)
            else:
                result[size] = RES_ICONS.getBonusIcon(size, item.getGUIEmblemID())

        result[b'tooltip'] = item.getBonusIcon(AWARDS_SIZES.BIG)
        return result

    @classmethod
    def _getOverlayType(cls, item):
        result = super(EpicItemsBonusFormatter, cls)._getOverlayType(item)
        if item.itemTypeName == SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER_NAME:
            if not item.isCrewBooster():
                result[AWARDS_SIZES.BIG] = SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER_BIG
                result[AWARDS_SIZES.SMALL] = SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER
            else:
                result[AWARDS_SIZES.BIG] = result[AWARDS_SIZES.SMALL] = SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT
        return result

    @classmethod
    def _getOverlayIcon(cls, item):
        result = super(EpicItemsBonusFormatter, cls)._getOverlayIcon(item)
        itemTypeName = item.itemTypeName
        for size in AWARDS_SIZES.ALL():
            if itemTypeName == SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER_NAME:
                if not item.isCrewBooster():
                    result[size] = RES_ICONS.getBonusOverlay(size, SLOT_HIGHLIGHT_TYPES.BATTLE_BOOSTER)
                else:
                    result[size] = SLOT_HIGHLIGHT_TYPES.NO_HIGHLIGHT

        return result


class RankedItemsBonusFormatter(ItemsBonusFormatter):

    @classmethod
    def _getHighlightType(cls, item):
        if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE and item.isDeluxe:
            return {}
        return super(RankedItemsBonusFormatter, cls)._getHighlightType(item)


class EpicDossierBonusFormatter(DossierBonusFormatter):

    @classmethod
    def _getImages(cls, bonus):
        if isinstance(bonus, Badge):
            return {(AWARDS_SIZES.SMALL): (bonus.getSmallIcon()), 
               (AWARDS_SIZES.BIG): (bonus.getBigIcon())}
        bonus, record = bonus.getRecordName()
        return {(AWARDS_SIZES.SMALL): (RES_ICONS.getEpicAchievementIcon(ICONS_SIZES.X48, record)), 
           (AWARDS_SIZES.BIG): (RES_ICONS.getEpicAchievementIcon(ICONS_SIZES.X80, record))}


class BlueprintBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonuses):
        isPackedBonuses = bonuses.canPacked()
        bonus = [
         PreformattedBonus(bonusName=bonuses.getBlueprintName(), label=formatCountLabel(bonuses.getCount()) if isPackedBonuses else bonuses.formatBlueprintValue(), userName=bonuses.getBlueprintTooltipName(), labelFormatter=self._getLabelFormatter(bonuses), images=self._getIcons(bonuses), tooltip=bonuses.getTooltip(), align=LABEL_ALIGN.CENTER, isCompensation=self._isCompensation(bonuses), specialArgs=[
          bonuses.getBlueprintSpecialArgs()], isSpecial=True, specialAlias=bonuses.getBlueprintSpecialAlias())]
        if not isPackedBonuses:
            return bonus * bonuses.getCount()
        return bonus

    def _getIcons(self, bonus):
        res = {}
        for size in AWARDS_SIZES.ALL():
            res[size] = bonus.getImage(size)

        return res


class BlueprintGroupBonusFormatter(BlueprintBonusFormatter):

    def _format(self, bonuses):
        return [
         PreformattedBonus(bonusName=bonuses.getBlueprintName(), label=formatCountLabel(bonuses.getCount()), userName=bonuses.getBlueprintTooltipName(), labelFormatter=self._getLabelFormatter(bonuses), images=self._getIcons(bonuses), tooltip=bonuses.getTooltip(), align=LABEL_ALIGN.RIGHT, isCompensation=self._isCompensation(bonuses), specialArgs=[
          bonuses.getBlueprintSpecialArgs()], isSpecial=True, specialAlias=bonuses.getBlueprintSpecialAlias(), postProcessTags=b'blueprints')]


class BlueprintGroupEpicBonusFormatter(BlueprintGroupBonusFormatter):

    @classmethod
    def _getLabelFormatter(cls, bonus):
        return text_styles.textEpic

    def _getIcons(self, bonuses):
        size = EPIC_AWARD_SIZE
        return {size: (RES_ICONS.getBonusIcon(size, bonuses.getImageCategory()))}


class CrewSkinsBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        compensationFormatter = SimpleBonusFormatter()
        for item, count, customCompensation, compensatedNumber in bonus.getItems():
            compensations = bonus.compensation(compensatedNumber, customCompensation, bonus)
            if compensations:
                for bonusComp in compensations:
                    formattedComp = compensationFormatter.format(bonusComp)
                    result.extend(formattedComp)

            elif item is not None and count:
                result.append(PreformattedBonus(bonusName=bonus.getName(), images=self._getImages(item), isSpecial=True, label=formatCountLabel(count), labelFormatter=self._getLabelFormatter(bonus), userName=self._getUserName(item), align=self._getLabelAlign(count), isCompensation=self._isCompensation(bonus), specialAlias=TOOLTIPS_CONSTANTS.CREW_SKIN, specialArgs=[
                 item.getID(), count], postProcessTags=b'crewSkin'))

        return result

    @classmethod
    def _getLabelAlign(cls, count):
        if count > 1:
            return LABEL_ALIGN.RIGHT
        return LABEL_ALIGN.CENTER

    @classmethod
    def _getUserName(cls, item):
        return localizedFullName(item)

    @classmethod
    def _getImages(cls, item):
        result = {}
        rarity = item.getRarity()
        for size in AWARDS_SIZES.ALL():
            sizePath = R.images.gui.maps.icons.quests.bonuses.dyn(size, None)
            if sizePath is not None:
                img = sizePath.dyn(item.itemTypeName + str(rarity))
                if img is not None and img.exists():
                    result[size] = backport.image(img())

        return result


class CrewBooksBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        result = []
        for item, count in bonus.getItems():
            if item is not None and count:
                result.append(PreformattedBonus(bonusName=bonus.getName(), images=self._getImages(item), isSpecial=True, label=formatCountLabel(count), labelFormatter=self._getLabelFormatter(bonus), userName=self._getUserName(item), align=self._getLabelAlign(count), isCompensation=self._isCompensation(bonus), specialAlias=TOOLTIPS_CONSTANTS.CREW_BOOK, specialArgs=[
                 item.intCD, count]))

        return result

    @classmethod
    def _getLabelAlign(cls, count):
        if count > 1:
            return LABEL_ALIGN.RIGHT
        return LABEL_ALIGN.CENTER

    @classmethod
    def _getUserName(cls, item):
        return item.userName

    @classmethod
    def _getImages(cls, item):
        result = {}
        for size in AWARDS_SIZES.ALL():
            sizePath = R.images.gui.maps.icons.crewBooks.books.dyn(size, None)
            if sizePath is not None:
                img = sizePath.dyn(item.getBonusIconName())
                if img is not None and img.exists():
                    result[size] = backport.image(img())

        return result


class CrewBooksEpicBonusFormatter(CrewBooksBonusFormatter):

    @classmethod
    def _getImages(cls, item):
        result = {}
        size = EPIC_AWARD_SIZE
        sizePath = R.images.gui.maps.icons.quests.bonuses.dyn(size, None)
        if sizePath is not None:
            img = sizePath.dyn(item.getBonusIconName())
            if img is not None and img.exists():
                result[size] = backport.image(img())
        return result


class CrewSkinsCompensationFormatter(CrewSkinsBonusFormatter):

    def _format(self, bonus):
        result = []
        for item, count, _, compensatedNumber in bonus.getItems():
            if item is not None and compensatedNumber > 0:
                result.append(PreformattedBonus(bonusName=bonus.getName(), images=self._getImages(item), isSpecial=True, label=self._formatBonusLabel(item, count, compensatedNumber), labelFormatter=self._getLabelFormatter(bonus), userName=self._getUserName(item), align=self._getLabelAlign(compensatedNumber), isCompensation=self._isCompensation(bonus), specialAlias=TOOLTIPS_CONSTANTS.CREW_SKIN, specialArgs=[
                 item.getID(), compensatedNumber]))

        return result

    def _formatBonusLabel(self, item, _, compensatedNumber):
        defaultStr = text_styles.stats(backport.text(R.strings.item_types.crewSkins.itemType.dyn(Rarity.STRINGS[item.getRarity()])()))
        formattedStr = formatCountLabel(count=compensatedNumber, defaultStr=defaultStr)
        return formattedStr


class EntitlementFormatter(SimpleBonusFormatter):

    @classmethod
    def _getImages(cls, bonus):
        images = {}
        for size in AWARDS_SIZES.ALL():
            images[size] = bonus.getIconBySize(size)

        return images

    def _format(self, bonus):
        result = []
        if bonus.isShowInGUI():
            result.append(self.__formatEntitlement(bonus))
        return result

    def __formatEntitlement(self, bonus):
        value = bonus.getValue()
        isFormattedAmount = bonus.isFormattedAmount(value.id)
        return PreformattedBonus(bonusName=bonus.getName(), userName=bonus.getUserName(value.id), label=formatCountLabel(value.amount) if isFormattedAmount else backport.getIntegralFormat(value.amount), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), tooltip=bonus.getTooltip(), align=LABEL_ALIGN.RIGHT if isFormattedAmount else LABEL_ALIGN.CENTER, isCompensation=self._isCompensation(bonus))


class EntitlementWulfTooltipFormatter(EntitlementFormatter):
    ENTITLEMENTS = {}

    def _format(self, bonus):
        result = []
        if bonus.isShowInGUI():
            if bonus.getValue().id in self.ENTITLEMENTS:
                result.append(self.__formatEnt(bonus))
            else:
                result.extend(super(EntitlementWulfTooltipFormatter, self)._format(bonus))
        return result

    def __formatEnt(self, bonus):
        value = bonus.getValue()
        isFormattedAmount = bonus.isFormattedAmount(value.id)
        return PreformattedBonus(bonusName=bonus.getName(), label=formatCountLabel(value.amount) if isFormattedAmount else backport.getIntegralFormat(value.amount), userName=bonus.getUserName(value.id), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), align=LABEL_ALIGN.RIGHT if isFormattedAmount else LABEL_ALIGN.CENTER, isCompensation=self._isCompensation(bonus), compensationReason=self._getCompensationReason(bonus), tooltip=self.ENTITLEMENTS.get(value.id), specialArgs=[], isWulfTooltip=True)


def registerEntitlementWulfTooltipFormatter(key, value):
    EntitlementWulfTooltipFormatter.ENTITLEMENTS[key] = value
    return


class BattlePassBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=bonus.getName(), label=self._getLabel(bonus), userName=self._getUserName(bonus), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), align=self._getLabelAlign(bonus), isCompensation=self._isCompensation(bonus), compensationReason=self._getCompensationReason(bonus), isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.BATTLE_PASS_POINTS, specialArgs=[])]

    @classmethod
    def _getImages(cls, bonus):
        images = {}
        for size in AWARDS_SIZES.ALL():
            image = bonus.getIconBySize(size)
            if image is not None:
                images[size] = image

        return images


class BattlePassEpicBonusFormatter(BattlePassBonusFormatter):

    @classmethod
    def _getLabelFormatter(cls, bonus):
        return text_styles.textEpic

    @classmethod
    def _getImages(cls, bonus):
        images = {}
        size = EPIC_AWARD_SIZE
        image = bonus.getIconBySize(size)
        if image is not None:
            images[size] = image
        return images


class CurrenciesBonusFormatter(SimpleBonusFormatter):

    @classmethod
    def _getUserName(cls, bonus):
        return i18n.makeString(QUESTS.getBonusName(bonus.getCode()))

    @classmethod
    def _getImages(cls, bonus):
        return {(AWARDS_SIZES.SMALL): (bonus.getIconBySize(AWARDS_SIZES.SMALL)), 
           (AWARDS_SIZES.BIG): (bonus.getIconBySize(AWARDS_SIZES.BIG))}


class EpicSelectTokenFormatter(SimpleBonusFormatter):

    @classmethod
    def _getImages(cls, bonus):
        result = {(AWARDS_SIZES.SMALL): (backport.image(R.images.gui.maps.icons.epicBattles.awards.c_48x48.abilityToken())), 
           (AWARDS_SIZES.BIG): (backport.image(R.images.gui.maps.icons.epicBattles.awards.c_80x80.abilityToken()))}
        return result


class PreferredMapSlotBonusFormatter(SimpleBonusFormatter):

    def _format(self, bonus):
        return [
         PreformattedBonus(bonusName=bonus.getName(), label=self._getLabel(bonus), userName=self._getUserName(bonus), labelFormatter=self._getLabelFormatter(bonus), images=self._getImages(bonus), tooltip=TOOLTIPS_CONSTANTS.PREFERRED_MAP_SLOT_TOOLTIP, align=self._getLabelAlign(bonus), isCompensation=self._isCompensation(bonus), highlightType=self._getHighlightType(bonus), overlayType=self._getOverlayType(bonus), highlightIcon=self._getHighlightIcon(bonus), overlayIcon=self._getOverlayIcon(bonus), compensationReason=self._getCompensationReason(bonus), isWulfTooltip=True, specialArgs=[
          bonus.getSlotName(), str(bonus.getValue())])]

    @classmethod
    def _getLabel(cls, bonus):
        return backport.text(R.strings.tooltips.template.days.short(), value=bonus.getValue())

    @classmethod
    def _getUserName(cls, bonus):
        return i18n.makeString(QUESTS.getBonusName(bonus.getSlotName()))

    @classmethod
    def _getImages(cls, bonus):
        return {(AWARDS_SIZES.SMALL): (bonus.getIconBySize(AWARDS_SIZES.SMALL)), 
           (AWARDS_SIZES.BIG): (bonus.getIconBySize(AWARDS_SIZES.BIG))}
