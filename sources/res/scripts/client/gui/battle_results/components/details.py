import operator, typing
from constants import IGR_TYPE, PREMIUM_TYPE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui import makeHtmlString
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.battle_results.components import base
from gui.battle_results.components import style
from gui.battle_results.pbs_helpers.additional_bonuses import isWotPlusBonusEnabledInConfig, isGoldPiggyBankAvailaible, getAdditionalXpBonusStatus, getLeftAdditionalBonus, getAdditionalXPFactor10FromResult
from gui.battle_results.pbs_helpers.economics import getCreditsToShow
from gui.battle_results.reusable.records import convertFactorToPercent
from gui.impl import backport
from gui.impl.backport.backport_system_locale import getIntegralFormat
from gui.impl.lobby.premacc import premacc_helpers
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.views.lobby.battle_results.additional_bonus_model import PremiumXpBonusRestriction
from gui.shared.formatters import icons, text_styles
from gui.shared.formatters.icons import makeImageTag
from gui.shared.money import Currency
from gui.shared.utils.functions import makeTooltip
from helpers import i18n, dependency
from shared_utils import first
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable.records import RecordsIterator

class _GainResourceInBattleItem(base.StatsItem):
    __slots__ = (b'__records', b'__method', b'__styler')

    def __init__(self, records, method, styler, field, *path):
        super(_GainResourceInBattleItem, self).__init__(field, *path)
        self.__records = records
        self.__method = method
        self.__styler = styler
        return

    def _convert(self, value, reusable):
        personal = reusable.personal
        baseRecords, premiumRecords = first(operator.methodcaller(self.__method)(personal), default=(None, None))[:2]
        resource = 0
        if baseRecords is not None and not personal.avatar.hasPenalties():
            if reusable.hasAnyPremiumInPostBattle:
                records = premiumRecords
            else:
                records = baseRecords
            for append, name in self.__records:
                if append:
                    resource += records.getRecord(name)
                else:
                    resource -= records.getRecord(name)

        return self.__styler(resource)


class GainCreditsInBattleItem(_GainResourceInBattleItem):
    __slots__ = ()

    def __init__(self, field, *path):
        super(GainCreditsInBattleItem, self).__init__((
         (
          True, b'credits'),
         (
          True, b'originalCreditsToDraw')), b'getMoneyRecords', getIntegralFormat, field, *path)
        return


class GainCreditsValueInBattleItem(_GainResourceInBattleItem):
    __slots__ = ()

    def __init__(self, field, *path):
        super(GainCreditsValueInBattleItem, self).__init__((
         (
          True, b'credits'),
         (
          True, b'originalCreditsToDraw')), b'getMoneyRecords', (lambda x: x), field, *path)
        return


class GainCrystalInBattleItem(_GainResourceInBattleItem):
    __slots__ = ()

    def __init__(self, field, *path):
        super(GainCrystalInBattleItem, self).__init__((
         (
          True, Currency.CRYSTAL),), b'getCrystalRecords', getIntegralFormat, field, *path)
        return


class GainCrystalValueInBattleItem(_GainResourceInBattleItem):
    __slots__ = ()

    def __init__(self, field, *path):
        super(GainCrystalValueInBattleItem, self).__init__((
         (
          True, Currency.CRYSTAL),), b'getCrystalRecords', (lambda x: x), field, *path)
        return


class GainXPInBattleItem(_GainResourceInBattleItem):
    __slots__ = ()

    def __init__(self, field, *path):
        super(GainXPInBattleItem, self).__init__((
         (
          True, b'xpToShow'),), b'getXPRecords', getIntegralFormat, field, *path)
        return


class GainXPValueInBattleItem(_GainResourceInBattleItem):
    __slots__ = ()

    def __init__(self, field, *path):
        super(GainXPValueInBattleItem, self).__init__((
         (
          True, b'xpToShow'),), b'getXPRecords', (lambda x: x), field, *path)
        return


class TotalBRReward(base.StatsItem):
    __slots__ = (b'__record',)

    def __init__(self, record, field, *path):
        super(TotalBRReward, self).__init__(field, *path)
        self.__record = record
        return

    def _convert(self, value, reusable):
        infoAvatar = value[b'avatar']
        return infoAvatar.get(self.__record)


class BRCredits(TotalBRReward):
    __slots__ = ()

    def __init__(self, field, *path):
        super(BRCredits, self).__init__(b'credits', field, *path)
        return


class BRXp(TotalBRReward):
    __slots__ = ()

    def __init__(self, field, *path):
        super(BRXp, self).__init__(b'xp', field, *path)
        return


class BRCrystal(TotalBRReward):
    __slots__ = ()

    def __init__(self, field, *path):
        super(BRCrystal, self).__init__(b'crystal', field, *path)
        return


class BaseCreditsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        canBeFaded = not reusable.isPostBattlePremium and reusable.canResourceBeFaded
        for records in reusable.personal.getBaseCreditsRecords():
            value = style.makeCreditsLabel(records.getRecord(b'credits', b'originalCreditsToDraw'), canBeFaded=canBeFaded)
            self.addNextComponent(base.DirectStatsItem(b'', value))

        return


class PremiumCreditsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        canBeFaded = reusable.hasAnyPremiumInPostBattle and reusable.canResourceBeFaded
        isDiffShow = reusable.canUpgradeToPremiumPlus
        values = getCreditsToShow(reusable, isDiffShow)
        for value in values:
            value = style.makeCreditsLabel(value, canBeFaded=canBeFaded, isDiff=isDiffShow)
            self.addNextComponent(base.DirectStatsItem(b'', value))

        return


class XPTitleBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        showSquadLabels, squadHasBonus = reusable.getPersonalSquadFlags()
        for records in reusable.personal.getBaseXPRecords():
            factor = int(records.getFactor(b'dailyXPFactor10'))
            if factor == 1 and showSquadLabels and squadHasBonus:
                value = i18n.makeString(backport.text(R.strings.battle_results.common.details.xpTitleSquad()), img=icons.makeImageTag(backport.image(R.images.gui.maps.icons.library.prebattleInviteIcon_1())))
            else:
                value = backport.text(R.strings.battle_results.common.details.xpTitle())
            if factor > 1:
                value = (b' ').join((
                 value,
                 icons.makeImageTag(backport.image(R.images.gui.maps.icons.library.dyn((b'bonus_x{}').format(factor))()), 46, 18)))
            self.addNextComponent(base.DirectStatsItem(b'', value))

        return


class XPTitleTooltipBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        showSquadLabels, squadHasBonus = reusable.getPersonalSquadFlags()
        for records in reusable.personal.getBaseXPRecords():
            factor = int(records.getFactor(b'dailyXPFactor10'))
            value = None
            if factor == 1 and showSquadLabels and squadHasBonus:
                value = backport.text(R.strings.battle_results.common.tooltip.xpTitleSquad())
            self.addNextComponent(base.DirectStatsItem(b'', value))

        return


class BaseXPBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        isPremium = not reusable.hasAnyPremiumInPostBattle and reusable.canResourceBeFaded
        for records in reusable.personal.getBaseXPRecords():
            value = style.makeXpLabel(records.getRecord(b'xpToShow'), canBeFaded=isPremium)
            self.addNextComponent(base.DirectStatsItem(b'', value))

        return


class PremiumXPBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        canBeFaded = reusable.hasAnyPremiumInPostBattle and reusable.canResourceBeFaded
        isDiffShow = reusable.canUpgradeToPremiumPlus
        for records in reusable.personal.getXPRecords():
            baseXP, premiumXP = records[:2]
            xp = premiumXP.getRecord(b'xpToShow')
            if isDiffShow:
                value = xp - baseXP.getRecord(b'xpToShow')
            else:
                value = xp
            value = style.makeXpLabel(value, canBeFaded=canBeFaded, isDiff=isDiffShow)
            self.addNextComponent(base.DirectStatsItem(b'', value))

        return


class _EconomicsDetailsBlock(base.StatsBlock):
    __slots__ = (b'premiumMask', b'hasAnyPremium', b'isWotPlus', b'canResourceBeFaded', b'igrType', b'penaltyDetails')
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _wotPlusCtrl = dependency.descriptor(IWotPlusController)

    def __init__(self, meta=None, field=b'', *path):
        super(_EconomicsDetailsBlock, self).__init__(meta, field, *path)
        self.hasAnyPremium = False
        self.isWotPlus = False
        self.canResourceBeFaded = True
        self.penaltyDetails = None
        self.igrType = IGR_TYPE.NONE
        return

    def _addEmptyRow(self):
        self.addNextComponent(style.EmptyStatRow())
        return

    def _addStatsRow(self, label, labelArgs=None, column1=None, column2=None, column3=None, column4=None, htmlKey=b''):
        value = style.makeStatRow(label, labelArgs=labelArgs, column1=column1, column2=column2, column3=column3, column4=column4, htmlKey=htmlKey)
        self.addNextComponent(base.DirectStatsItem(b'', value))
        return

    def _addAOGASFactor(self, baseRecords, allColumns=True):
        factor = baseRecords.getFactor(b'aogasFactor10')
        if factor < 1:
            value = style.makeAOGASFactorValue(factor)
            if allColumns:
                self._addStatsRow(b'aogasFactor', column1=value, column2=value, column3=value, column4=value)
            else:
                self._addStatsRow(b'aogasFactor', column1=value, column3=value)
            return True
        return False


class MoneyDetailsBlock(_EconomicsDetailsBlock):
    __slots__ = ()
    __intermediateTotalRecords = (b'credits', b'originalCreditsToDraw', b'originalCreditsToDrawSquad')

    def setRecord(self, result, reusable):
        baseCredits, premiumCredits, goldRecords, additionalRecords, baseCreditsWithWotPlus, premiumCreditsWithWotPlus = result
        isTotalShown = False
        self.__addBaseCredits(baseCredits, premiumCredits)
        showSquadLabels, _ = reusable.getPersonalSquadFlags()
        if showSquadLabels:
            self.__addSquadBonus(baseCredits, premiumCredits)
        isTotalShown |= self.__addStatsItemIfExists(b'noPenalty', baseCredits, premiumCredits, False, None, b'achievementCredits')
        isTotalShown |= self.__addStatsItemIfExists(b'boosters', baseCredits, premiumCredits, False, None, b'boosterCredits', b'boosterCreditsFactor100')
        isTotalShown |= self.__addStatsItemIfExists(b'battlePayments', baseCredits, premiumCredits, False, None, b'orderCreditsFactor100')
        isTotalShown |= self.__addEventsMoney(baseCredits, premiumCredits, goldRecords)
        isTotalShown |= self.__addReferralSystemFactor(baseCredits, premiumCredits)
        wotPlusSettings = self._wotPlusCtrl.getSettingsStorage()
        showWotPlusBattleBonuses = wotPlusSettings.isBattleBonusesEnabled()
        if showWotPlusBattleBonuses:
            self.__addWotPlusBattleBonusCredits(baseCredits, premiumCredits, baseCreditsWithWotPlus, premiumCreditsWithWotPlus)
            isTotalShown = True
        if self.isWotPlus and wotPlusSettings.isProBoostFeatureEnabled():
            self.__addWotPlusProboostBonusCredits(baseCredits, premiumCredits)
            isTotalShown = True
        self._addEmptyRow()
        isPenaltyAdded = False
        isPenaltyAdded |= self.__addViolationPenalty()
        isPenaltyAdded |= self.__addStatsItemIfExists(b'friendlyFirePenalty', baseCredits, premiumCredits, False, None, b'originalCreditsPenalty', b'originalCreditsContributionOut', b'originalCreditsPenaltySquad', b'originalCreditsContributionOutSquad')
        isPenaltyAdded |= self.__addStatsItemIfExists(b'friendlyFireCompensation', baseCredits, premiumCredits, False, None, b'originalCreditsContributionIn', b'originalCreditsContributionInSquad')
        if isPenaltyAdded:
            self._addEmptyRow()
        isTotalShown |= isPenaltyAdded
        isTotalShown |= self.__addAOGASFactor(baseCredits)
        baseCreditsToUse = baseCredits
        premiumCreditsToUse = premiumCredits
        if showWotPlusBattleBonuses and not self.isWotPlus:
            if self.hasAnyPremium:
                baseCreditsToUse = baseCreditsWithWotPlus
            else:
                premiumCreditsToUse = premiumCreditsWithWotPlus
        if isTotalShown:
            self.__addBattleResults(baseCreditsToUse, premiumCreditsToUse, goldRecords)
            self._addEmptyRow()
        self.__addStatsItem(b'autoRepair', additionalRecords, additionalRecords, b'autoRepairCost')
        self.__addAutoCompletion(b'autoLoad', additionalRecords, b'autoLoadCredits', b'autoLoadGold')
        self.__addAutoCompletion(b'autoEquip', additionalRecords, b'autoEquipCredits', b'autoEquipGold')
        self._addEmptyRow()
        self.__addTotalResults(baseCreditsToUse, premiumCreditsToUse, goldRecords, additionalRecords)
        self._addEmptyRow()
        isCreditsPiggyBankAvailable = reusable.common.checkBonusCaps(_CAPS.PIGGY_BANK_CREDITS)
        if isCreditsPiggyBankAvailable or isGoldPiggyBankAvailaible(reusable):
            self.__addPiggyBankInfo(premiumCreditsToUse, additionalRecords, reusable)
        return

    def __addStatsItem(self, label, baseRecords, premiumRecords, *names):
        baseValue = baseRecords.getRecord(*names)
        premiumValue = premiumRecords.getRecord(*names)
        baseLabel = style.makeCreditsLabel(baseValue, canBeFaded=not self.hasAnyPremium)
        premiumLabel = style.makeCreditsLabel(premiumValue, canBeFaded=self.hasAnyPremium)
        self._addStatsRow(label, column1=baseLabel, column3=premiumLabel)
        return baseValue != 0 or premiumValue != 0

    def __addStatsItemIfExists(self, label, baseRecords, premiumRecords, acceptAllIfExist, labelArgs=None, *names):
        baseValue = baseRecords.getRecord(*names)
        premiumValue = premiumRecords.getRecord(*names)
        result = False
        if acceptAllIfExist:
            isToAdd = baseRecords.getFactor(*names) > 1.0 or premiumRecords.getFactor(*names) > 1.0
        else:
            isToAdd = baseValue or premiumValue
        if isToAdd:
            result = True
            baseValue = style.makeCreditsLabel(baseValue, canBeFaded=not self.hasAnyPremium)
            premiumValue = style.makeCreditsLabel(premiumValue, canBeFaded=self.hasAnyPremium)
            self._addStatsRow(label, labelArgs, column1=baseValue, column3=premiumValue)
        return result

    def __addBaseCredits(self, baseRecords, premiumRecords):
        baseCredits = baseRecords.getRecord(b'originalCredits')
        baseCredits += baseRecords.getRecord(b'originalCreditsToDraw')
        baseCredits -= baseRecords.getRecord(b'achievementCredits')
        premiumCredits = premiumRecords.getRecord(b'originalCredits', b'appliedPremiumCreditsFactor100')
        premiumCredits += premiumRecords.getRecord(b'originalCreditsToDraw')
        premiumCredits -= premiumRecords.getRecord(b'achievementCredits')
        self._addStatsRow(b'base', column1=style.makeCreditsLabel(baseCredits, canBeFaded=not self.hasAnyPremium), column3=style.makeCreditsLabel(premiumCredits, canBeFaded=self.hasAnyPremium))
        return

    def __addSquadBonus(self, baseRecords, premiumRecords):
        baseCredits = baseRecords.getRecord(b'originalPremSquadCredits', b'originalCreditsToDrawSquad')
        premiumCredits = premiumRecords.getRecord(b'originalPremSquadCredits', b'originalCreditsToDrawSquad')
        if not self.hasAnyPremium and baseCredits or self.hasAnyPremium and premiumCredits:
            self._addStatsRow(b'squadBonus', column1=style.makeCreditsLabel(baseCredits, canBeFaded=not self.hasAnyPremium), column3=style.makeCreditsLabel(premiumCredits, canBeFaded=self.hasAnyPremium))
        return

    def __addPiggyBankInfo(self, premiumRecords, additionalRecords, reusable):
        baseCredits = 0
        baseGold = 0
        premiumGold = 0
        goldGain = reusable.personal.getGoldBankGain()
        if self.hasAnyPremium:
            premiumCredits = additionalRecords.getRecord(b'piggyBank')
            premiumGold = goldGain
        else:
            piggyBankMultiplier = self._lobbyContext.getServerSettings().getPiggyBankConfig().get(b'multiplier')
            premiumCredits = premiumRecords.getRecord(b'credits') * piggyBankMultiplier
            baseGold = goldGain
        column2 = None
        column4 = None
        if self._wotPlusCtrl.getSettingsStorage().isGoldReserveFeatureEnabled():
            column2 = style.makeGoldLabel(baseGold, canBeFaded=True, isDiff=baseGold > 0)
            column4 = style.makeGoldLabel(premiumGold, canBeFaded=True, isDiff=premiumGold > 0)
        self._addStatsRow(b'piggyBankInfo', column1=style.makeCreditsLabel(baseCredits, canBeFaded=not self.hasAnyPremium, isDiff=baseCredits > 0), column2=column2, column3=style.makeCreditsLabel(premiumCredits, canBeFaded=self.hasAnyPremium, isDiff=premiumCredits > 0), column4=column4)
        return

    def __addReferralSystemFactor(self, baseCredits, premiumCredits):
        referralFactor = baseCredits.getFactor(b'referral20CreditsFactor100')
        labelArgs = {b'bonusFactor': (convertFactorToPercent(referralFactor))}
        return self.__addStatsItemIfExists(b'referralBonus', baseCredits, premiumCredits, False, labelArgs, b'referral20CreditsFactor100')

    def __addEventsMoney(self, baseCredits, premiumCredits, goldRecords):
        baseEventCredits = baseCredits.findRecord(b'eventCreditsList_') + baseCredits.findRecord(b'eventCreditsFactor100List_')
        premiumEventCredits = premiumCredits.findRecord(b'eventCreditsList_') + premiumCredits.findRecord(b'eventCreditsFactor100List_')
        baseEventGold = goldRecords.findRecord(b'eventGoldList_')
        result = False
        if baseEventCredits or premiumEventCredits or baseEventGold:
            result = True
            columns = {}
            if baseEventCredits:
                columns[b'column1'] = style.makeCreditsLabel(baseEventCredits, canBeFaded=not self.hasAnyPremium)
            if premiumEventCredits:
                columns[b'column3'] = style.makeCreditsLabel(premiumEventCredits, canBeFaded=self.hasAnyPremium)
            if baseEventGold:
                columns[b'column2'] = style.makeGoldLabel(baseEventGold, canBeFaded=not self.hasAnyPremium)
                columns[b'column4'] = style.makeGoldLabel(baseEventGold, canBeFaded=self.hasAnyPremium)
            self._addStatsRow(b'event', **columns)
        return result

    def __addViolationPenalty(self):
        if self.penaltyDetails is not None:
            name, penalty = self.penaltyDetails
            penalty = style.makePercentLabel(penalty)
            value = style.makeStatRow((b'fairPlayViolation/{}').format(name), column1=penalty, column3=penalty)
            self.addNextComponent(base.DirectStatsItem(b'', value))
            return True
        else:
            return False

    def __addAOGASFactor(self, baseRecords):
        result = self._addAOGASFactor(baseRecords, allColumns=False)
        if result:
            self._addEmptyRow()
        return result

    def __addBattleResults(self, baseRecords, premiumRecords, goldRecords):
        baseCredits = baseRecords.getRecord(*self.__intermediateTotalRecords)
        premiumCredits = premiumRecords.getRecord(*self.__intermediateTotalRecords)
        baseCreditsLabel = style.makeCreditsLabel(baseCredits, canBeFaded=not self.hasAnyPremium)
        premiumCreditsLabel = style.makeCreditsLabel(premiumCredits, canBeFaded=self.hasAnyPremium)
        gold = goldRecords.getRecord(b'gold')
        if gold != 0:
            baseGoldLabel = style.makeGoldLabel(gold, canBeFaded=not self.hasAnyPremium)
            premiumGoldLabel = style.makeGoldLabel(gold, canBeFaded=self.hasAnyPremium)
        else:
            baseGoldLabel = None
            premiumGoldLabel = None
        self._addStatsRow(b'intermediateTotal', column1=baseCreditsLabel, column3=premiumCreditsLabel, column2=baseGoldLabel, column4=premiumGoldLabel)
        return

    def __addAutoCompletion(self, label, additionalRecords, creditsRecord, goldRecord):
        credit = additionalRecords.getRecord(creditsRecord)
        gold = additionalRecords.getRecord(goldRecord)
        columns = {b'column1': (style.makeCreditsLabel(credit, canBeFaded=not self.hasAnyPremium)), 
           b'column3': (style.makeCreditsLabel(credit, canBeFaded=self.hasAnyPremium))}
        if gold:
            columns.update({b'column2': (style.makeGoldLabel(gold, canBeFaded=not self.hasAnyPremium)), 
               b'column4': (style.makeGoldLabel(gold, canBeFaded=self.hasAnyPremium))})
        self._addStatsRow(label, **columns)
        return

    def __addTotalResults(self, baseCredits, premiumCredits, goldRecords, additionalRecords):
        baseCanBeFaded = not self.hasAnyPremium and self.canResourceBeFaded
        premiumCanBeFaded = self.hasAnyPremium and self.canResourceBeFaded
        autoCredits = additionalRecords.getRecord(b'autoRepairCost', b'autoLoadCredits', b'autoEquipCredits')
        autoGold = additionalRecords.getRecord(b'autoLoadGold', b'autoEquipGold')
        columns = {b'column1': (style.makeCreditsLabel(baseCredits.getRecord(*self.__intermediateTotalRecords) + autoCredits, canBeFaded=baseCanBeFaded)), 
           b'column3': (style.makeCreditsLabel(premiumCredits.getRecord(*self.__intermediateTotalRecords) + autoCredits, canBeFaded=premiumCanBeFaded)), 
           b'column2': (style.makeGoldLabel(goldRecords.getRecord(b'gold') + autoGold, canBeFaded=not self.hasAnyPremium)), 
           b'column4': (style.makeGoldLabel(goldRecords.getRecord(b'gold') + autoGold, canBeFaded=self.hasAnyPremium))}
        self._addStatsRow(b'total', htmlKey=b'lightText', **columns)
        return

    def __addWotPlusBattleBonusCredits(self, baseRecords, premiumRecords, baseCreditsWithWotPlus, premiumCreditsWithWotPlus):
        names = (b'wotPlusCredits', b'wotPlusCreditsFactor100')
        baseValue = (baseRecords if self.isWotPlus else baseCreditsWithWotPlus).getRecord(*names)
        premiumValue = (premiumRecords if self.isWotPlus else premiumCreditsWithWotPlus).getRecord(*names)
        baseLabel = style.makeCreditsLabel(baseValue, canBeFaded=not self.hasAnyPremium, forceFade=not self.isWotPlus)
        premiumLabel = style.makeCreditsLabel(premiumValue, canBeFaded=self.hasAnyPremium, forceFade=not self.isWotPlus)
        htmlKey = b'wotplus_active_label' if self.isWotPlus else b'wotplus_inactive_label'
        self._addStatsRow(b'wotPlus', column1=baseLabel, column3=premiumLabel, htmlKey=htmlKey)
        return

    def __addWotPlusProboostBonusCredits(self, baseCredits, premiumCredits):
        wotPlusRecords = (b'wotPlusProBoostCredits', b'wotPlusProBoostCreditsFactor100')
        baseVal = baseCredits.getRecord(*wotPlusRecords)
        premVal = premiumCredits.getRecord(*wotPlusRecords)
        if baseVal > 0 or premVal > 0:
            self._addStatsRow(b'wotPlusProBoost', column1=style.makeCreditsLabel(baseVal, canBeFaded=not self.hasAnyPremium), column3=style.makeCreditsLabel(premVal, canBeFaded=self.hasAnyPremium), htmlKey=b'wotplus_active_label')
        return


class XPDetailsBlock(_EconomicsDetailsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        baseXP, premiumXP, baseFreeXP, premiumFreeXP, _, _, _, _ = result
        self.__addBaseXPs(baseXP, premiumXP, baseFreeXP, premiumFreeXP)
        self.__addComplexXPsItemIfExists(b'noPenalty', baseXP, premiumXP, baseFreeXP, premiumFreeXP, b'achievementXP', b'achievementFreeXP')
        penaltyKey = b'friendlyFirePenalty'
        if reusable.common.arenaVisitor.gui.isRankedBattle():
            penaltyKey = b'friendlyFireRankedXpPenalty'
        self.__addXPsItemIfExists(penaltyKey, baseXP, premiumXP, b'originalXPPenalty')
        if reusable.common.arenaVisitor.gui.isInEpicRange():
            self.__addXPsItem(b'playerRankXP', baseXP, premiumXP, b'playerRankXPFactor100')
        self.__addIGRFactor(baseXP)
        self.__addDailyXPFactor(baseXP)
        self.__addAdditionalXPBonus(baseXP, premiumXP, baseFreeXP, premiumFreeXP)
        self.__addBoosterXPs(baseXP, premiumXP, baseFreeXP, premiumFreeXP)
        self.__addXPsItemIfExists(b'tacticalTraining', baseXP, premiumXP, b'orderXPFactor100')
        self.__addFreeXPsItemIfExists(b'militaryManeuvers', baseFreeXP, premiumFreeXP, b'orderFreeXPFactor100')
        self.__addEventXPs(baseXP, premiumXP, baseFreeXP, premiumFreeXP)
        self.__addReferralSystemFactor(baseXP, premiumXP)
        self.__addComplexXPsItemIfExists(b'premiumVehicleXP', baseXP, premiumXP, baseFreeXP, premiumFreeXP, b'premiumVehicleXPFactor100', b'premiumVehicleXPFactor100')
        showSquadLabels, _ = reusable.getPersonalSquadFlags()
        if showSquadLabels:
            self.__addSquadXPDetails(baseXP, premiumXP)
        self._addAOGASFactor(baseXP)
        wotPlusSettings = self._wotPlusCtrl.getSettingsStorage()
        if wotPlusSettings.isBattleBonusesEnabled():
            self.__addWotPlusBattleBonusXPs(result)
        if self.isWotPlus and wotPlusSettings.isProBoostFeatureEnabled():
            self.__addWotPlusProboostBonusXPs(baseFreeXP, baseXP, premiumFreeXP, premiumXP)
        if self.getNextComponentIndex() < 7:
            self._addEmptyRow()
        self.__addXPsViolationPenalty()
        self.__addTotalResults(result)
        self._addEmptyRow()
        return

    def __addXPsItem(self, label, baseXP, premiumXP, xpRecord, labelArgs=None):
        columns = {b'column1': (style.makeXpLabel(baseXP.getRecord(xpRecord), canBeFaded=not self.hasAnyPremium)), 
           b'column3': (style.makeXpLabel(premiumXP.getRecord(xpRecord), canBeFaded=self.hasAnyPremium))}
        self._addStatsRow(label, labelArgs=labelArgs, **columns)
        return

    def __addWotPlusBattleBonusXPs(self, result):
        baseXP, premiumXP, baseFreeXP, premiumFreeXP, baseXPWithWotPlus, premiumXPWithWotPlus, baseFreeXPWithWotPlus, premiumFreeXPWithWotPlus = result
        namesXP = (b'wotPlusXP', b'wotPlusXPFactor100')
        namesFreeXP = (b'wotPlusFreeXP', b'wotPlusFreeXPFactor100')
        baseXPValue = (baseXP if self.isWotPlus else baseXPWithWotPlus).getRecord(*namesXP)
        premiumXPValue = (premiumXP if self.isWotPlus else premiumXPWithWotPlus).getRecord(*namesXP)
        baseFreeXPValue = (baseFreeXP if self.isWotPlus else baseFreeXPWithWotPlus).getRecord(*namesFreeXP)
        premiumFreeXPValue = (premiumFreeXP if self.isWotPlus else premiumFreeXPWithWotPlus).getRecord(*namesFreeXP)
        baseXPLabel = style.makeXpLabel(baseXPValue, canBeFaded=not self.hasAnyPremium, forceFade=not self.isWotPlus)
        baseFreeXPLabel = style.makeFreeXpLabel(baseFreeXPValue, canBeFaded=not self.hasAnyPremium, forceFade=not self.isWotPlus)
        premiumXPLabel = style.makeXpLabel(premiumXPValue, canBeFaded=self.hasAnyPremium, forceFade=not self.isWotPlus)
        premiumFreeXPLabel = style.makeFreeXpLabel(premiumFreeXPValue, canBeFaded=self.hasAnyPremium, forceFade=not self.isWotPlus)
        htmlKey = b'wotplus_active_label' if self.isWotPlus else b'wotplus_inactive_label'
        self._addStatsRow(b'wotPlus', column1=baseXPLabel, column2=baseFreeXPLabel, column3=premiumXPLabel, column4=premiumFreeXPLabel, htmlKey=htmlKey)
        return

    def __addWotPlusProboostBonusXPs(self, baseFreeXP, baseXP, premiumFreeXP, premiumXP):
        namesXP = (b'wotPlusProBoostXP', b'wotPlusProBoostXPFactor100')
        namesFreeXP = (b'wotPlusProBoostFreeXP', b'wotPlusProBoostFreeXPFactor100')
        baseXPValue = baseXP.getRecord(*namesXP)
        baseFreeXPValue = baseFreeXP.getRecord(*namesFreeXP)
        premiumXPValue = premiumXP.getRecord(*namesXP)
        premiumFreeXPValue = premiumFreeXP.getRecord(*namesFreeXP)
        if baseXPValue > 0 or baseFreeXPValue > 0 or premiumXPValue > 0 or premiumFreeXPValue > 0:
            self._addStatsRow(b'wotPlusProBoost', column1=style.makeXpLabel(baseXPValue, canBeFaded=not self.hasAnyPremium), column2=style.makeFreeXpLabel(baseFreeXPValue, canBeFaded=not self.hasAnyPremium), column3=style.makeXpLabel(premiumXPValue, canBeFaded=self.hasAnyPremium), column4=style.makeFreeXpLabel(premiumFreeXPValue, canBeFaded=self.hasAnyPremium), htmlKey=b'wotplus_active_label')
        return

    def __addFreeXPsItem(self, label, baseFreeXP, premiumFreeXP, freeXPRecord):
        columns = {b'column2': (style.makeFreeXpLabel(baseFreeXP.getRecord(freeXPRecord), canBeFaded=not self.hasAnyPremium)), 
           b'column4': (style.makeFreeXpLabel(premiumFreeXP.getRecord(freeXPRecord), canBeFaded=self.hasAnyPremium))}
        self._addStatsRow(label, **columns)
        return

    def __addComplexXPsItem(self, label, baseXP, premiumXP, baseFreeXP, premiumFreeXP, xpRecord, freeXPRecord, htmlKey=b''):
        baseCanBeFaded = not self.hasAnyPremium
        premiumCanBeFaded = self.hasAnyPremium
        columns = {b'column1': (style.makeXpLabel(baseXP.getRecord(xpRecord), canBeFaded=baseCanBeFaded)), 
           b'column3': (style.makeXpLabel(premiumXP.getRecord(xpRecord), canBeFaded=premiumCanBeFaded)), 
           b'column2': (style.makeFreeXpLabel(baseFreeXP.getRecord(freeXPRecord), canBeFaded=baseCanBeFaded)), 
           b'column4': (style.makeFreeXpLabel(premiumFreeXP.getRecord(freeXPRecord), canBeFaded=premiumCanBeFaded))}
        self._addStatsRow(label, htmlKey=htmlKey, **columns)
        return

    def __addXPsItemIfExists(self, label, baseXP, premiumXP, xpRecord):
        if baseXP.getRecord(xpRecord) or premiumXP.getRecord(xpRecord):
            self.__addXPsItem(label, baseXP, premiumXP, xpRecord)
        return

    def __addFreeXPsItemIfExists(self, label, baseFreeXP, premiumFreeXP, freeXPRecord):
        if baseFreeXP.getRecord(freeXPRecord) or premiumFreeXP.getRecord(freeXPRecord):
            self.__addFreeXPsItem(label, baseFreeXP, premiumFreeXP, freeXPRecord)
        return

    def __addComplexXPsItemIfExists(self, label, baseXP, premiumXP, baseFreeXP, premiumFreeXP, xpRecord, freeXPRecord):
        value = baseXP.getRecord(xpRecord)
        value += premiumXP.getRecord(xpRecord)
        value += baseFreeXP.getRecord(freeXPRecord)
        value += premiumFreeXP.getRecord(freeXPRecord)
        if value:
            self.__addComplexXPsItem(label, baseXP, premiumXP, baseFreeXP, premiumFreeXP, xpRecord, freeXPRecord)
        return

    def __addBaseXPs(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):
        if baseXP.getRecord(b'isHighScope'):
            label, htmlKey = (b'', b'xpRecord')
        else:
            label, htmlKey = (b'base', b'')
        baseXPValue = baseXP.getRecord(b'originalXP')
        baseXPValue -= baseXP.getRecord(b'achievementXP')
        premiumXPValue = premiumXP.getRecord(b'originalXP', b'appliedPremiumXPFactor100')
        premiumXPValue -= premiumXP.getRecord(b'achievementXP')
        baseFreeXPValue = baseFreeXP.getRecord(b'originalFreeXP')
        baseFreeXPValue -= baseFreeXP.getRecord(b'achievementFreeXP')
        premiumFreeXPValue = premiumFreeXP.getRecord(b'originalFreeXP', b'appliedPremiumXPFactor100')
        premiumFreeXPValue -= premiumFreeXP.getRecord(b'achievementFreeXP')
        baseCanBeFaded = not self.hasAnyPremium
        premiumCanBeFaded = self.hasAnyPremium
        columns = {b'column1': (style.makeXpLabel(baseXPValue, canBeFaded=baseCanBeFaded)), 
           b'column3': (style.makeXpLabel(premiumXPValue, canBeFaded=premiumCanBeFaded)), 
           b'column2': (style.makeFreeXpLabel(baseFreeXPValue, canBeFaded=baseCanBeFaded)), 
           b'column4': (style.makeFreeXpLabel(premiumFreeXPValue, canBeFaded=premiumCanBeFaded))}
        self._addStatsRow(label, htmlKey=htmlKey, **columns)
        return

    def __addBoosterXPs(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):
        baseXPValue = baseXP.getRecord(b'boosterXP', b'boosterXPFactor100')
        premiumXPValue = premiumXP.getRecord(b'boosterXP', b'boosterXPFactor100')
        baseFreeXPValue = baseFreeXP.getRecord(b'boosterFreeXP', b'boosterFreeXPFactor100')
        premiumFreeXPValue = premiumFreeXP.getRecord(b'boosterFreeXP', b'boosterFreeXPFactor100')
        if baseXPValue or premiumXPValue or baseFreeXPValue or premiumFreeXPValue:
            baseCanBeFaded = not self.hasAnyPremium
            premiumCanBeFaded = self.hasAnyPremium
            columns = {b'column1': (style.makeXpLabel(baseXPValue, canBeFaded=baseCanBeFaded)), 
               b'column3': (style.makeXpLabel(premiumXPValue, canBeFaded=premiumCanBeFaded)), 
               b'column2': (style.makeFreeXpLabel(baseFreeXPValue, canBeFaded=baseCanBeFaded)), 
               b'column4': (style.makeFreeXpLabel(premiumFreeXPValue, canBeFaded=premiumCanBeFaded))}
            self._addStatsRow(b'boosters', **columns)
        return

    def __addEventXPs(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):
        baseXPValue = baseXP.findRecord(b'eventXPList_') + baseXP.findRecord(b'eventXPFactor100List_')
        premiumXPValue = premiumXP.findRecord(b'eventXPList_') + premiumXP.findRecord(b'eventXPFactor100List_')
        baseFreeXPValue = baseFreeXP.findRecord(b'eventFreeXPList_') + baseFreeXP.findRecord(b'eventFreeXPFactor100List_')
        premiumFreeXPValue = premiumFreeXP.findRecord(b'eventFreeXPList_') + premiumFreeXP.findRecord(b'eventFreeXPFactor100List_')
        if baseXPValue or premiumXPValue or baseFreeXPValue or premiumFreeXPValue:
            baseCanBeFaded = not self.hasAnyPremium
            premiumCanBeFaded = self.hasAnyPremium
            columns = {b'column1': (style.makeXpLabel(baseXPValue, canBeFaded=baseCanBeFaded)), 
               b'column3': (style.makeXpLabel(premiumXPValue, canBeFaded=premiumCanBeFaded)), 
               b'column2': (style.makeFreeXpLabel(baseFreeXPValue, canBeFaded=baseCanBeFaded)), 
               b'column4': (style.makeFreeXpLabel(premiumFreeXPValue, canBeFaded=premiumCanBeFaded))}
            self._addStatsRow(b'event', **columns)
        return

    def __addXPsViolationPenalty(self):
        if self.penaltyDetails is not None:
            name, penalty = self.penaltyDetails
            penalty = style.makePercentLabel(penalty)
            self._addStatsRow((b'fairPlayViolation/{}').format(name), column1=penalty, column2=penalty, column3=penalty, column4=penalty)
        return

    def __addIGRFactor(self, baseXP):
        factor = baseXP.getFactor(b'igrXPFactor10')
        if factor > 1:
            icon = style.makeIGRIcon(self.igrType)
            value = style.makeIGRBonusValue(factor)
            self.addNextComponent(style.StatRow(style.makeIGRBonusLabel(b''), style.makeIGRBonusLabel(icon), style.WIDE_STAT_ROW, column1=value, column2=value, column3=value, column4=value))
        return

    def __addDailyXPFactor(self, baseXP):
        factor = baseXP.getFactor(b'dailyXPFactor10')
        if factor > 1:
            columns = self.__getFormattedColumnsWithFreeXP([factor] * 4)
            self._addStatsRow(b'firstWin', **columns)
        return

    def __addAdditionalXPBonus(self, baseXP, premiumXP, baseFreeXP, premiumFreeXP):

        def getAdditionalXPFactor(item):
            factor = item.getFactor(b'additionalXPFactor10')
            if factor > 1:
                return factor
            return 0

        factors = tuple(getAdditionalXPFactor(xp) for xp in (baseXP, baseFreeXP, premiumXP, premiumFreeXP))
        if any(factors):
            columns = self.__getFormattedColumnsWithFreeXP(factors)
            self._addStatsRow(b'additionalBonus', **columns)
        return

    def __addSquadXPDetails(self, baseXP, premiumXP):
        squadXP = baseXP.getRecord(b'squadXPFactor100')
        premiumSquadXP = premiumXP.getRecord(b'squadXPFactor100')
        baseLabel = style.makeXpLabel(squadXP, canBeFaded=not self.hasAnyPremium)
        premiumLabel = style.makeXpLabel(premiumSquadXP, canBeFaded=not self.hasAnyPremium)
        if squadXP < 0 or premiumSquadXP < 0:
            label = b'squadXPPenalty'
            if self.hasAnyPremium:
                baseLabel = None
            else:
                premiumLabel = None
        else:
            label = b'squadXP'
        columns = {b'column1': baseLabel, 
           b'column3': premiumLabel}
        self._addStatsRow(label, **columns)
        return

    def __addReferralSystemFactor(self, baseXP, premiumXP):
        referralFactor = baseXP.getFactor(b'referral20XPFactor100')
        if referralFactor > 0 and baseXP.getRecord(b'referral20XPFactor100'):
            labelArgs = {b'bonusFactor': (convertFactorToPercent(referralFactor))}
            self.__addXPsItem(b'referralBonus', baseXP, premiumXP, b'referral20XPFactor100', labelArgs=labelArgs)
        return

    def __addTotalResults(self, result):
        baseXP, premiumXP, baseFreeXP, premiumFreeXP, baseXPWithWotPlus, premiumXPWithWotPlus, baseFreeXPWithWotPlus, premiumFreeXPWithWotPlus = result
        baseXPToUse = baseXP
        premiumXPToUse = premiumXP
        baseFreeXPToUse = baseFreeXP
        premiumFreeXPToUse = premiumFreeXP
        showWotPlusBattleBonuses = self._wotPlusCtrl.getSettingsStorage().isBattleBonusesEnabled()
        if showWotPlusBattleBonuses and not self.isWotPlus:
            if self.hasAnyPremium:
                baseXPToUse = baseXPWithWotPlus
                baseFreeXPToUse = baseFreeXPWithWotPlus
            else:
                premiumXPToUse = premiumXPWithWotPlus
                premiumFreeXPToUse = premiumFreeXPWithWotPlus
        baseCanBeFaded = not self.hasAnyPremium and self.canResourceBeFaded
        premiumCanBeFaded = self.hasAnyPremium and self.canResourceBeFaded
        columns = {b'column1': (style.makeXpLabel(baseXPToUse.getRecord(b'xp'), canBeFaded=baseCanBeFaded)), 
           b'column3': (style.makeXpLabel(premiumXPToUse.getRecord(b'xp'), canBeFaded=premiumCanBeFaded)), 
           b'column2': (style.makeFreeXpLabel(baseFreeXPToUse.getRecord(b'freeXP'), canBeFaded=baseCanBeFaded)), 
           b'column4': (style.makeFreeXpLabel(premiumFreeXPToUse.getRecord(b'freeXP'), canBeFaded=premiumCanBeFaded))}
        self._addStatsRow(b'total', htmlKey=b'lightText', **columns)
        return

    @staticmethod
    def __getFormattedColumnsWithFreeXP(factors):
        return {(b'column{}').format(n): style.makeMultiXPFactorValue(factor, useFreeXPStyle=not bool(n % 2)) for n, factor in enumerate(factors, 1)}


class CrystalDetailsBlock(_EconomicsDetailsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        label = backport.text(R.strings.battle_results.details.calculations.crystal.total())
        earned = self.__addRecordField(b'originalCrystal', result, label)
        label = backport.text(R.strings.battle_results.details.calculations.crystal.events())
        earned += self.__addRecordField(b'events', result, label)
        label = backport.text(R.strings.battle_results.details.calculations.autoBoosters())
        expenses = self.__addRecordField(b'autoEquipCrystals', result, label)
        if earned or expenses:
            self.__addTotalResults(earned + expenses)
        return

    def __addRecordField(self, key, result, label, force=False):
        value = result.getRecord(key)
        if force or value:
            self._addRecord(label, value)
        return value

    def __addTotalResults(self, value):
        self.addNextComponent(style.EmptyStatRow())
        i18nText = backport.text(R.strings.battle_results.details.calculations.total())
        totalStr = makeHtmlString(b'html_templates:lobby/battle_results', b'lightText', {b'value': i18nText})
        self._addRecord(totalStr, value)
        return

    def _addRecord(self, res, value):
        self.addNextComponent(style.StatRow(res, res, style.SMALL_STAT_LINE, column1=style.makeCrystalLabel(value)))
        return


class _TotalEconomicsDetailsBlock(base.StatsBlock):
    __slots__ = (b'__iteratorName', b'__blockClass')

    def __init__(self, iterator, block, meta=None, field=b'', *path):
        super(_TotalEconomicsDetailsBlock, self).__init__(meta, field, *path)
        self.__iteratorName = iterator
        self.__blockClass = block
        return

    def setRecord(self, result, reusable):
        igrType = reusable.getPlayerInfo().igrType
        personal = reusable.personal
        penaltyDetails = personal.avatar.getPenaltyDetails()
        hasAnyPremium = reusable.hasAnyPremiumInPostBattle
        isWotPlus = reusable.isWotPlusInPostBattle
        canResourceBeFaded = reusable.canResourceBeFaded
        for records in operator.methodcaller(self.__iteratorName)(personal):
            block = self.__blockClass(base.ListMeta(registered=True))
            block.hasAnyPremium = hasAnyPremium
            block.isWotPlus = isWotPlus
            block.canResourceBeFaded = canResourceBeFaded
            block.igrType = igrType
            block.penaltyDetails = penaltyDetails
            block.setRecord(records, reusable)
            self.addNextComponent(block)

        return


class TotalMoneyDetailsBlock(_TotalEconomicsDetailsBlock):
    __slots__ = ()

    def __init__(self, meta=None, field=b'', *path):
        super(TotalMoneyDetailsBlock, self).__init__(b'getMoneyRecords', MoneyDetailsBlock, meta, field, *path)
        return


class TotalXPDetailsBlock(_TotalEconomicsDetailsBlock):
    __slots__ = ()

    def __init__(self, meta=None, field=b'', *path):
        super(TotalXPDetailsBlock, self).__init__(b'getXPRecords', XPDetailsBlock, meta, field, *path)
        return


class TotalCrystalDetailsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        personal = reusable.personal
        for record in personal.getCrystalDetailsRecords():
            block = CrystalDetailsBlock(base.ListMeta(registered=True))
            block.setRecord(record, reusable)
            self.addNextComponent(block)

        return


class PremiumBonusDetailsBlock(base.StatsBlock):
    __slots__ = (b'description', b'bonusLeft', b'xpValue', b'statusBonusLabel', b'statusBonusTooltip', b'bonusIcon', b'__isPersonalTeamWin', b'__arenaUniqueID', b'__arenaBonusType', b'__isBonusAvailable', b'__xpFactor', b'__vehicleCD', b'detailsLink', b'additionalBonusLeft', b'wotPlusBonusLeft', b'premiumAndPlusExhausted', b'hasWotPremium', b'hasWotPlus')
    __itemsCache = dependency.descriptor(IItemsCache)
    __battleResults = dependency.descriptor(IBattleResultsService)
    __wotPlusController = dependency.descriptor(IWotPlusController)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, meta=None, field=b'', *path):
        super(PremiumBonusDetailsBlock, self).__init__(meta, field, *path)
        self.__arenaUniqueID = 0
        self.__isPersonalTeamWin = False
        self.__arenaBonusType = None
        self.__isBonusAvailable = False
        self.__xpFactor = 1
        self.__vehicleCD = None
        self.bonusIcon = b''
        self.description = b''
        self.bonusLeft = b''
        self.detailsLink = b''
        self.additionalBonusLeft = b''
        self.wotPlusBonusLeft = b''
        self.xpValue = b''
        self.statusBonusLabel = b''
        self.statusBonusTooltip = b''
        self.premiumAndPlusExhausted = b''
        self.hasWotPremium = False
        self.hasWotPlus = False
        return

    def getVO(self):
        self.__updateStatus()
        return super(PremiumBonusDetailsBlock, self).getVO()

    def setRecord(self, result, reusable):
        self.__arenaUniqueID = reusable.arenaUniqueID
        self.__arenaBonusType = reusable.common.arenaBonusType
        self.__isPersonalTeamWin = reusable.isPersonalTeamWin()
        self.__isBonusAvailable = reusable.common.checkBonusCaps(_CAPS.ADDITIONAL_XP_POSTBATTLE)
        self.__xpFactor = getAdditionalXPFactor10FromResult(result, reusable)
        _, vehicle = first(reusable.personal.getVehicleItemsIterator())
        self.__vehicleCD = vehicle.intCD
        return

    def __getIsApplied(self):
        return self.__battleResults.isAddXPBonusApplied(self.__arenaUniqueID)

    def __updateStatus(self):
        self.__setBonusLeft()
        if self.__arenaUniqueID == 0:
            return
        self.__setBaseState()
        addXpStatus = getAdditionalXpBonusStatus(self.__arenaUniqueID, self.__isPersonalTeamWin, self.__vehicleCD, self.__isBonusAvailable)
        if addXpStatus == PremiumXpBonusRestriction.ISAPPLIED:
            self.__setAppliedState()
        elif addXpStatus == PremiumXpBonusRestriction.INVALIDBATTLETYPE:
            self.__setBlockedByArenaType()
        elif not self.__isPersonalTeamWin:
            self.__setLostBattleState()
        elif addXpStatus == PremiumXpBonusRestriction.DEPRECATEDRESULTS:
            self.__setExcludedState()
        elif addXpStatus == PremiumXpBonusRestriction.NOVEHICLE:
            self.__setBlockedByVehicle()
        elif addXpStatus in (
         PremiumXpBonusRestriction.FASTEREDUCATIONCREWNOTACTIVE,
         PremiumXpBonusRestriction.FASTEREDUCATIONCREWACTIVE):
            self.__setBlockedByXPToTman(addXpStatus)
        elif addXpStatus == PremiumXpBonusRestriction.NOCREW:
            self.__setBlockedByCrew()
        else:
            self.__setShowButtonState()
        return

    def __setBlockedByArenaType(self):
        self.xpValue = b''
        self.bonusLeft = b''
        self.bonusIcon = self.__getAddXPBonusIcon(premacc_helpers.BattleResultsBonusConstants.LOST_BATTLE_BACKGROUND_MULTIPLIER)
        self.statusBonusLabel = (b'{}{}').format(makeImageTag(source=backport.image(R.images.gui.maps.icons.library.alertIcon()), vSpace=-3), text_styles.neutral(backport.text(R.strings.battle_results.common.premiumBonus.unavailable())))
        return

    def __setBlockedByVehicle(self):
        self.xpValue = b''
        self.statusBonusLabel = text_styles.neutral(backport.text(R.strings.battle_results.common.premiumBonus.tankStateChanged()))
        self.statusBonusTooltip = TOOLTIPS.BATTLERESULTS_PREMIUMBONUS_TANKSTATECHANGED
        return

    def __setBlockedByXPToTman(self, status):
        self.xpValue = b''
        if status == PremiumXpBonusRestriction.FASTEREDUCATIONCREWACTIVE:
            textKey = R.strings.battle_results.common.premiumBonus.isXPToTmenEnabled()
        else:
            textKey = R.strings.battle_results.common.premiumBonus.isXPToTmenDisabled()
        self.statusBonusLabel = text_styles.neutral(backport.text(textKey))
        self.statusBonusTooltip = makeTooltip(body=TOOLTIPS.BATTLERESULTS_PREMIUMBONUS_XPTOTMENCHANGED_BODY)
        return

    def __setBlockedByCrew(self):
        self.xpValue = b''
        self.statusBonusLabel = text_styles.neutral(backport.text(R.strings.battle_results.common.premiumBonus.tankmenStateChanged()))
        self.statusBonusTooltip = TOOLTIPS.BATTLERESULTS_PREMIUMBONUS_TANKMENSTATECHANGED
        return

    def __setBaseState(self):
        self.bonusIcon = self.__getAddXPBonusIcon(self.__xpFactor)
        self.description = text_styles.highlightText(backport.text(R.strings.battle_results.common.premiumBonus.description()))
        return

    def __setBonusLeft(self):
        isWotPlusBonusEnabled = isWotPlusBonusEnabledInConfig()
        hasWotPlus = self.__wotPlusController.hasSubscription()
        hasPremiumPlus = self.__itemsCache.items.stats.isActivePremium(PREMIUM_TYPE.PLUS)
        hasAccessToAdditionalBonus, applyAdditionalXPCount, _ = getLeftAdditionalBonus(hasWotPlus, hasPremiumPlus)
        if hasAccessToAdditionalBonus:
            self.bonusLeft = self.__getBonusLeftStr(applyAdditionalXPCount)
        else:
            self.bonusLeft = self.__getBonusLeftStr(b'-')
        self.additionalBonusLeft = self.__getAdditionalBonusLeftStr(hasPremiumPlus, hasWotPlus, isWotPlusBonusEnabled)
        self.detailsLink = self.__getDetailsLinkStr(hasPremiumPlus, hasWotPlus, isWotPlusBonusEnabled)
        self.wotPlusBonusLeft = b'-'
        if isWotPlusBonusEnabled:
            self.wotPlusBonusLeft = self.__getWotPlusBonusEarningsStr(self.__itemsCache.items.stats.dailyAppliedAdditionalXP)
            self.premiumAndPlusExhausted = self.__getPremiumAndPlusExhaustedStr()
        self.hasWotPremium = hasPremiumPlus
        self.hasWotPlus = hasWotPlus
        return

    def __setAppliedState(self):
        self.xpValue = b''
        self.statusBonusLabel = (b'{}{}').format(makeImageTag(source=backport.image(R.images.gui.maps.icons.library.ConfirmIcon_1())), text_styles.bonusAppliedText(backport.text(R.strings.battle_results.common.premiumBonus.appliedBonus())))
        return

    def __setExcludedState(self):
        self.xpValue = b''
        self.statusBonusLabel = (b'{}{}').format(makeImageTag(source=backport.image(R.images.gui.maps.icons.library.alertIcon()), vSpace=-3), text_styles.neutral(backport.text(R.strings.battle_results.common.premiumBonus.expiredBattleResult())))
        self.bonusIcon = self.__getAddXPBonusIcon(premacc_helpers.BattleResultsBonusConstants.LOST_BATTLE_BACKGROUND_MULTIPLIER)
        return

    def __setLostBattleState(self):
        self.xpValue = b''
        self.bonusIcon = self.__getAddXPBonusIcon(premacc_helpers.BattleResultsBonusConstants.LOST_BATTLE_BACKGROUND_MULTIPLIER)
        self.statusBonusLabel = (b'{}{}').format(makeImageTag(source=backport.image(R.images.gui.maps.icons.library.alertIcon()), vSpace=-3), text_styles.neutral(backport.text(R.strings.battle_results.common.premiumBonus.rule())))
        return

    def __setShowButtonState(self):
        self.statusBonusLabel = b''
        self.statusBonusTooltip = b''
        bonusValue = self.__battleResults.getAdditionalXPValue(self.__arenaUniqueID)
        self.xpValue = style.makeXpLabel(bonusValue, isDiff=True, useBigIcon=True)
        return

    def __getAddXPBonusIcon(self, multiplier):
        multiplier = premacc_helpers.validateAdditionalBonusMultiplier(multiplier)
        isWotPlusBonusEnabled = isWotPlusBonusEnabledInConfig()
        if isWotPlusBonusEnabled:
            icon = backport.image(R.images.gui.maps.icons.premacc.battleResult.dyn((b'plus_bonus_x{}').format(multiplier))())
        else:
            icon = backport.image(R.images.gui.maps.icons.premacc.battleResult.dyn((b'bonus_x{}').format(multiplier))())
        return icon

    @staticmethod
    def __getBonusLeftStr(applyAdditionalXPCount):
        return text_styles.main(backport.text(R.strings.battle_results.common.premiumBonus.bonusLeft(), count=text_styles.stats(applyAdditionalXPCount)))

    @staticmethod
    def __getAdditionalBonusLeftStr(hasPremiumPlus, hasWotPlus, isWotPlusBonusEnabled):
        additionalBonusLeftStr = b''
        if isWotPlusBonusEnabled:
            if hasWotPlus and not hasPremiumPlus:
                additionalBonusLeftStr = style.LINE_BRAKE_STR + text_styles.main(backport.text(R.strings.battle_results.common.plusBonus.bonusLeftAdditionalText()))
            elif not hasWotPlus and hasPremiumPlus:
                additionalBonusLeftStr = style.LINE_BRAKE_STR + text_styles.main(backport.text(R.strings.battle_results.common.plusBonus.bonusLeftAdditionalText()))
        return additionalBonusLeftStr

    @staticmethod
    def __getWotPlusBonusEarningsStr(applyWoTPlusAdditionalXPCount):
        return style.LINE_BRAKE_STR + text_styles.main(backport.text(R.strings.battle_results.common.plusBonus.earningsInformation(), count=text_styles.earningsInformation(backport.getIntegralFormat(int(applyWoTPlusAdditionalXPCount)))))

    @staticmethod
    def __getPremiumAndPlusExhaustedStr():
        return text_styles.goldColor(backport.text(R.strings.battle_results.common.plusBonus.youRock()))

    @staticmethod
    def __getDetailsLinkStr(hasPremiumPlus, hasWotPlus, isWotPlusBonusEnabled):
        detailsLinkStr = b''
        if isWotPlusBonusEnabled:
            if hasWotPlus and not hasPremiumPlus:
                detailsLinkStr = b' ' + text_styles.linkText(backport.text(R.strings.battle_results.common.plusBonus.wotPremium()))
            elif not hasWotPlus and hasPremiumPlus:
                detailsLinkStr = b' ' + text_styles.linkText(backport.text(R.strings.battle_results.common.plusBonus.wotPlus()))
        return detailsLinkStr
