from __future__ import absolute_import
import logging, typing
from future.utils import viewitems
from constants import PREMIUM_ENTITLEMENTS
from gui.Scaleform.daapi.view.lobby.missions import missions_helper
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.customization.shared import getSingleVehicleForCustomization
from gui.impl import backport
from gui.impl.backport import TooltipData
from gui.impl.gen import R
from gui.server_events.awards_formatters import BATTLE_BONUS_X5_TOKEN, AWARDS_SIZES
from gui.server_events.bonuses import SimpleBonus, ItemsBonus, TokensBonus, CrewBooksBonus, CustomizationsBonus, BlueprintsBonusSubtypes, TmanTemplateTokensBonus
from gui.server_events.finders import isPMPoints, PM_POINTS_TOKEN
from gui.server_events.formatters import parseComplexToken
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.gui_items import GUI_ITEM_TYPE, getItemTypeID
from gui.shared.gui_items.customization import CustomizationTooltipContext
from gui.shared.missions.packers.bonus import CustomizationBonusUIPacker, getLocalizedBonusName, DossierBonusUIPacker, DOSSIER_BADGE_ICON_PREFIX, DOSSIER_BADGE_POSTFIX, ItemBonusUIPacker, TokenBonusUIPacker, CrewBookBonusUIPacker, getDefaultBonusPackersMap, BonusUIPacker, SimpleBonusUIPacker, BlueprintBonusUIPacker, GoodiesBonusUIPacker, BACKPORT_TOOLTIP_CONTENT_ID, BaseBonusUIPacker
from gui.shared.money import Currency
from helpers import dependency
from items.components.c11n_constants import Rarity
from items.components.crew_books_constants import CREW_BOOK_RARITY
from items.tankmen import RECRUIT_TMAN_TOKEN_PREFIX
from personal_missions import PM_BRANCH, PM_BRANCH_TO_FREE_TOKEN_NAME
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.style_bonus_model import StyleBonusModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.tooltips.umg_reward_model import UmgRewardModel
if typing.TYPE_CHECKING:
    from frameworks.wulf.view.array import Array
    from typing import List, Dict
    from gui.impl.gen.view_models.common.bonus_model import BonusModel
    from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
    from gui.shared.gui_items.customization.c11n_items import Customization
_logger = logging.getLogger(__name__)
REWARDS_ORDER = (
 PM_POINTS_TOKEN,
 b'vehicles',
 b'premiumYear',
 Rarity.LEGENDARY,
 b'campaignWithHonorBadge',
 Rarity.EPIC,
 b'operationWithHonorBadge',
 b'operationWithoutHonorBadge',
 Rarity.RARE,
 b'crewSkins',
 b'tankmen',
 b'2DStyle',
 b'decal',
 b'projection_decal',
 b'inscriptions',
 b'emblems',
 Currency.GOLD,
 Currency.CRYSTAL,
 Currency.CREDITS,
 b'freeXP',
 b'premium',
 b'improvedEquipment',
 b'experimentalEquipment',
 Currency.EQUIP_COIN,
 CREW_BOOK_RARITY.UNIVERSAL,
 CREW_BOOK_RARITY.UNIVERSAL_GUIDE,
 b'standardEquipment',
 BATTLE_BONUS_X5_TOKEN,
 b'personalReserves',
 b'blueprintsNational',
 b'blueprintsUniversal',
 CREW_BOOK_RARITY.CREW_RARE,
 CREW_BOOK_RARITY.UNIVERSAL_BROCHURE,
 CREW_BOOK_RARITY.CREW_COMMON,
 b'equipmentDirectives',
 b'crewDirectives',
 b'largeRepairkit',
 b'autoExtinguishers',
 b'largeMedkit',
 b'slots')
LAST_ORDER = len(REWARDS_ORDER)

def getRewardOrder(rewardName):
    try:
        order = REWARDS_ORDER.index(rewardName)
    except ValueError:
        order = LAST_ORDER

    return order


def getNotificationBonusOrder(bonus):
    if bonus.isShowInGUI():
        packer = getBonusPacker()
        bonusList = packer.pack(bonus)
        for packedBonus in bonusList:
            if isinstance(packedBonus, list):
                return packedBonus[-1]
            return getRewardOrder(packedBonus.getName())

    return LAST_ORDER


def getBonusPacker(isRewardScreen=False, isOperationCompleted=False):
    mapping = getDefaultBonusPackersMap()
    premiumPacker = PM3PremiumPacker()
    blueprintBonusPacker = PM3BlueprintBonusUIPacker()
    customizationPacker = PM3CustomizationBonusUIPacker() if isRewardScreen else PM3DashboardCustomizationBonusUIPacker()
    tokensBonusPacker = PM3TokenBonusUIPacker()
    tokensBonusPacker.setIsOperationCompleted(isOperationCompleted)
    pawnedBonusPacker = PawnedBonusPacker()
    mapping.update({(PREMIUM_ENTITLEMENTS.BASIC): premiumPacker, 
       (PREMIUM_ENTITLEMENTS.PLUS): premiumPacker, 
       b'blueprints': blueprintBonusPacker, 
       b'goodies': (PM3GoodiesBonusUIPacker()), 
       b'tokens': tokensBonusPacker, 
       b'customizations': customizationPacker, 
       b'items': (PM3ItemBonusUIPacker()), 
       b'dossier': (PM3DossierBonusUIPacker()), 
       b'crewBooks': (PM3CrewBookBonusUIPacker()), 
       b'tmanToken': (PM3TmanTemplateBonusPacker()), 
       b'completionTokens': pawnedBonusPacker, 
       b'tankwomanBonus': pawnedBonusPacker, 
       b'freeTokens': pawnedBonusPacker})
    return BonusUIPacker(mapping)


def packMissionsBonusModelAndTooltipData(bonuses, packer, model, tooltipData=None):
    bonusIndexTotal = 0
    if tooltipData is not None:
        bonusIndexTotal = len(tooltipData)
    totalBonusesList = []
    for bonus in bonuses:
        if bonus.isShowInGUI():
            bonusList = packer.pack(bonus)
            bonusTooltipList = packer.getToolTip(bonus)
            for packedBonus, bonusTooltip in zip(bonusList, bonusTooltipList):
                if isinstance(packedBonus, list):
                    packedBonus.append(bonusTooltip)
                    totalBonusesList.append(packedBonus)
                else:
                    totalBonusesList.append((
                     packedBonus,
                     getRewardOrder(packedBonus.getName()),
                     bonusTooltip))

    totalBonusesList.sort(key=(lambda b: b[1]))
    for bonusIndex, bonusData in enumerate(totalBonusesList):
        bonusData[0].setIndex(bonusIndexTotal)
        tooltipIdx = str(bonusIndexTotal)
        if hasattr(bonusData[0], b'setTooltipId'):
            bonusData[0].setTooltipId(tooltipIdx)
        model.addViewModel(bonusData[0])
        if tooltipData is not None:
            tooltipData[tooltipIdx] = totalBonusesList[bonusIndex][2]
        bonusIndexTotal += 1

    return


class PM3GoodiesBonusUIPacker(GoodiesBonusUIPacker):

    @classmethod
    def _pack(cls, bonus):
        result = []
        for booster, count in sorted(viewitems(bonus.getBoosters()), key=(lambda b: b[0].boosterID)):
            if booster is None or not count:
                continue
            result.append([cls._packSingleBoosterBonus(bonus, booster, count), getRewardOrder(b'personalReserves')])

        for demountkit, count in sorted(viewitems(bonus.getDemountKits())):
            if demountkit is None or not count:
                continue
            result.append([cls._packSingleDemountKitBonus(bonus, demountkit, count), LAST_ORDER])

        for form, count in sorted(viewitems(bonus.getRecertificationForms())):
            if form is None or not count:
                continue
            result.append([cls._packRecertificationFormsBonus(bonus, form, count), LAST_ORDER])

        for item, count in sorted(viewitems(bonus.getMentoringLicenses())):
            if item is None or not count:
                continue
            result.append([cls._packMentorLicensesBonus(bonus, item, count), LAST_ORDER])

        return result


class PM3BlueprintBonusUIPacker(BlueprintBonusUIPacker):

    @classmethod
    def _pack(cls, bonus):
        model = cls._getBonusModel()
        cls._packCommon(bonus, model)
        model.setValue(str(bonus.getCount()))
        model.setType(bonus.getBlueprintName())
        model.setIcon(bonus.getImageCategory())
        blueprintName = bonus.getBlueprintName()
        if blueprintName == BlueprintsBonusSubtypes.NATION_FRAGMENT:
            label = cls._getNationalLabel(bonus)
        else:
            label = bonus.getBlueprintTooltipName()
        model.setLabel(label)
        return [[model, cls._blueprintsChecker(bonus)]]

    @classmethod
    def _getNationalLabel(cls, bonus):
        nation = bonus.getImageCategory()
        nationName = backport.text(R.strings.blueprints.nations.dyn(nation)())
        return backport.text(R.strings.quests.bonusName.blueprints.nation(), nationName=nationName)

    @classmethod
    def _blueprintsChecker(cls, bonus):
        blueprintName = bonus.getBlueprintName()
        if blueprintName == BlueprintsBonusSubtypes.UNIVERSAL_FRAGMENT:
            return getRewardOrder(b'blueprintsUniversal')
        if blueprintName == BlueprintsBonusSubtypes.NATION_FRAGMENT:
            return getRewardOrder(b'blueprintsNational')
        return LAST_ORDER


class PM3PremiumPacker(SimpleBonusUIPacker):
    __PREMIUM_YEAR = 360

    @classmethod
    def _pack(cls, bonus):
        label = getLocalizedBonusName(bonus.getName())
        return [
         [cls._packSingleBonus(bonus, label if label else b''),
          getRewardOrder(b'premiumYear') if bonus.getValue() >= cls.__PREMIUM_YEAR else getRewardOrder(b'premium')]]


class PM3DashboardCustomizationBonusUIPacker(CustomizationBonusUIPacker):
    __c11n = dependency.descriptor(ICustomizationService)

    @classmethod
    def _getBonusModel(cls):
        return StyleBonusModel()

    @classmethod
    def _pack(cls, bonus):
        result = []
        for item in bonus.getCustomizations():
            if item is None:
                continue
            label = getLocalizedBonusName(bonus.getC11nItem(item).itemTypeName)
            result.append([cls._packSingleBonus(bonus, item, label if label else b''),
             cls._customizationsChecker(item)])

        return result

    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        model = cls._getBonusModel()
        c11nItem = bonus.getC11nItem(item)
        if c11nItem.itemTypeName == b'style' and c11nItem.is3D:
            model.setName(StyleBonusModel.STYLE_3D_REWARD_NAME)
        else:
            model.setName(bonus.getName())
            model.setValue(str(item.get(b'value', 0)))
        model.setIsCompensation(bonus.isCompensation())
        model.setIcon(str(c11nItem.itemTypeName))
        model.setLabel(label)
        model.setId(item.get(b'id', 0))
        return model

    @classmethod
    def _customizationsChecker(cls, item):
        itemTypeName = item.get(b'custType')
        itemID = item.get(b'id')
        itemTypeID = getItemTypeID(itemTypeName)
        customizationBonus = cls.__c11n.getItemByID(itemTypeID, itemID)
        if customizationBonus.itemTypeName == b'style' and not customizationBonus.is3D:
            return getRewardOrder(b'2DStyle')
        if customizationBonus.itemTypeName == b'attachment':
            return getRewardOrder(customizationBonus.rarity)
        return getRewardOrder(itemTypeName)

    @classmethod
    def _getToolTipData(cls, itemCustomization):
        specialAlias = TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_AWARD
        specialArgs = CustomizationTooltipContext(itemCD=itemCustomization.intCD)
        if itemCustomization.itemTypeName in (b'camouflage', b'style'):
            vehicle = getSingleVehicleForCustomization(itemCustomization)
            if vehicle is not None:
                specialAlias = TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM
                specialArgs = CustomizationTooltipContext(itemCD=itemCustomization.intCD, vehicleIntCD=vehicle)
        return TooltipData(tooltip=None, isSpecial=True, specialAlias=specialAlias, specialArgs=specialArgs)


class PM3CustomizationBonusUIPacker(PM3DashboardCustomizationBonusUIPacker):

    @classmethod
    def _packSingleBonus(cls, bonus, item, label):
        model = cls._getBonusModel()
        cls._packCommon(bonus, model)
        c11nItem = bonus.getC11nItem(item)
        model.setValue(str(item.get(b'value', 0)))
        icon = str(c11nItem.itemTypeName)
        if c11nItem.itemTypeName == b'style':
            if c11nItem.is3D:
                model.setName(StyleBonusModel.STYLE_3D_REWARD_NAME)
            label = c11nItem.userName
            icon = str(item.get(b'id'))
        if c11nItem.itemTypeName == b'attachment':
            label = backport.text(R.strings.item_types.customization.attachment.rarity(), rarity=backport.text(R.strings.vehicle_customization.customization.rarity.dyn(c11nItem.rarity)()))
            icon = c11nItem.name
            model.setName(c11nItem.itemTypeName)
        model.setIcon(icon)
        model.setLabel(label)
        return model


class PM3DossierBonusUIPacker(DossierBonusUIPacker):

    @classmethod
    def _packAchievements(cls, bonus):
        return [[cls._packSingleAchievement(achievement, bonus), LAST_ORDER] for achievement in bonus.getAchievements()]

    @classmethod
    def _packBadges(cls, bonus):
        result = []
        for badge in bonus.getBadges():
            dossierIconName = DOSSIER_BADGE_ICON_PREFIX + str(badge.badgeID)
            dossierValue = 0
            dossierLabel = badge.getUserName()
            result.append([
             cls._packSingleBonus(bonus, dossierIconName, DOSSIER_BADGE_POSTFIX, dossierValue, dossierLabel),
             cls._dossierChecker(badge)])

        return result

    @staticmethod
    def _dossierChecker(badge):
        if badge.getName().startswith(b'personal_missions_3'):
            if badge.getName().endswith(b'all'):
                return getRewardOrder(b'campaignWithHonorBadge')
            if badge.getName().endswith(b'1'):
                return getRewardOrder(b'operationWithoutHonorBadge')
            if badge.getName().endswith(b'2'):
                return getRewardOrder(b'operationWithHonorBadge')
        return LAST_ORDER


class PM3ItemBonusUIPacker(ItemBonusUIPacker):

    @classmethod
    def _pack(cls, bonus):
        bonusItems = bonus.getItems()
        result = []
        for item, count in sorted(viewitems(bonusItems), key=cls._itemsSortFunction):
            if item is None or not count:
                continue
            result.append([cls._packSingleBonus(bonus, item, count), cls._itemsChecker(item)])

        return result

    @staticmethod
    def _itemsChecker(item):
        if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
            if item.isModernized:
                return getRewardOrder(b'improvedEquipment')
            if item.isDeluxe:
                return getRewardOrder(b'experimentalEquipment')
            return getRewardOrder(b'standardEquipment')
        if item.itemTypeID == GUI_ITEM_TYPE.EQUIPMENT:
            return getRewardOrder(item.name)
        if item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER:
            if item.isCrewBooster():
                return getRewardOrder(b'crewDirectives')
            return getRewardOrder(b'equipmentDirectives')
        return LAST_ORDER


class PM3TokenBonusUIPacker(TokenBonusUIPacker):
    __isOperationCompleted = False

    @classmethod
    def setIsOperationCompleted(cls, isOperationCompleted):
        cls.__isOperationCompleted = isOperationCompleted
        return

    @classmethod
    def _pack(cls, bonus):
        bonusTokens = bonus.getTokens()
        result = []
        bonusPackers = cls._getTokenBonusPackers()
        for tokenID, token in viewitems(bonusTokens):
            complexToken = parseComplexToken(tokenID)
            tokenType = cls._getTokenBonusType(tokenID, complexToken)
            specialPacker = bonusPackers.get(tokenType)
            if specialPacker is None or isPMPoints(tokenID) and cls.__isOperationCompleted:
                continue
            packedBonus = cls._packToken(specialPacker, bonus, complexToken, token)
            if packedBonus is not None:
                result.append([packedBonus, cls._tokensChecker(token)])

        return result

    @staticmethod
    def _tokensChecker(token):
        if isPMPoints(token.id):
            return getRewardOrder(PM_POINTS_TOKEN)
        if token.id.startswith(BATTLE_BONUS_X5_TOKEN):
            return getRewardOrder(BATTLE_BONUS_X5_TOKEN)
        return LAST_ORDER


class PM3CrewBookBonusUIPacker(CrewBookBonusUIPacker):
    __itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def _pack(cls, bonus):
        result = []
        for book, count in sorted(bonus.getItems(), key=(lambda b: b[0].nationID)):
            if book is None or not count:
                continue
            result.append([cls._packSingleBonus(bonus, book, count), cls._crewBooksChecker(book)])

        return result

    @classmethod
    def _getToolTip(cls, bonus):
        tooltipData = []
        for item, count in sorted(bonus.getItems(), key=(lambda b: b[0].nationID)):
            tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.CREW_BOOK, specialArgs=[
             item.intCD, count]))

        return tooltipData

    @classmethod
    def _crewBooksChecker(cls, book):
        crewBook = cls.__itemsCache.items.getItemByCD(book.intCD)
        if crewBook is not None:
            return getRewardOrder(crewBook.getBookType())
        else:
            return LAST_ORDER


class PM3TmanTemplateBonusPacker(BaseBonusUIPacker):

    @classmethod
    def _pack(cls, bonus):
        result = []
        for tokenID in bonus.getTokens():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                packed = cls.__packTmanTemplateToken(tokenID, bonus)
                if packed is None:
                    _logger.error(b'Received wrong tman_template token from server: %s', tokenID)
                else:
                    result.append([packed, getRewardOrder(b'tankmen')])

        return result

    @classmethod
    def __packTmanTemplateToken(cls, tokenID, bonus):
        recruitInfo = getRecruitInfo(tokenID)
        if recruitInfo is None:
            return
        else:
            recruitGroupName = recruitInfo.getGroupName()
            if any(branchName in recruitGroupName for branchName in PM_BRANCH.WITHOUT_AWARD_LIST_BRANCHES):
                bonusImageName = b'tankman_' + recruitInfo.getGroupName().split(b'_', 1)[1]
            else:
                bonusImageName = b'tankman'
            tankManFullName = recruitInfo.getFullUserName()
            model = IconBonusModel()
            cls._packCommon(bonus, model)
            model.setName(bonusImageName)
            model.setIcon(bonusImageName)
            model.setLabel(tankManFullName)
            return model

    @classmethod
    def _getToolTip(cls, bonus):
        tooltipData = []
        for tokenID in bonus.getTokens():
            if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX):
                tooltipData.append(TooltipData(tooltip=None, isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.TANKMAN_NOT_RECRUITED, specialArgs=[
                 tokenID]))

        return tooltipData

    @classmethod
    def _getContentId(cls, bonus):
        return [BACKPORT_TOOLTIP_CONTENT_ID for tokenID in bonus.getTokens() if tokenID.startswith(RECRUIT_TMAN_TOKEN_PREFIX)]


class PawnedBonusPacker(BaseBonusUIPacker):
    eventsCache = dependency.descriptor(IEventsCache)

    @classmethod
    def _pack(cls, bonus):
        result = []
        ctx = bonus.getContext()
        branchID = ctx[b'branchID']
        quest = cls.eventsCache.getPersonalMissions().getQuestsForBranch(branchID)[ctx[b'questID']]
        pawnedTokensCount = quest.getPawnCost() if quest.areTokensPawned() else 0
        formattedBonuses = missions_helper.getPersonalMissionAwardsFormatter().getPawnedQuestBonuses([
         bonus], size=AWARDS_SIZES.SMALL, pawnedTokensCount=pawnedTokensCount, freeTokenName=PM_BRANCH_TO_FREE_TOKEN_NAME.get(branchID))
        for frmtBonus in formattedBonuses:
            packedBonus = UmgRewardModel()
            packedBonus.setName(bonus.getName())
            packedBonus.setIcon(frmtBonus.get(b'imgSource', b''))
            if frmtBonus.get(b'specialAlias', b'') == TOOLTIPS_CONSTANTS.FREE_SHEET_USED:
                packedBonus.setIsLocked(True)
            result.append(packedBonus)

        return result
