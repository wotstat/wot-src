from collections import namedtuple
import typing
from helpers import dependency
from shared_utils import first
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from gui.battle_results.pbs_helpers.additional_bonuses import isGoldPiggyBankAvailaible
from skeletons.gui.game_control import IWotPlusController
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo
    from gui.battle_results.stats_ctrl import BattleResults
FinancialRecordValues = namedtuple(b'FinancialRecordValues', (b'baseAccountValue', b'premiumAccountValue', b'additionalValue', b'extraValue', b'baseAccountValueWithWotPlus', b'premiumAccountValueWithWotPlus'))

def getTotalCrystalsToShow(reusable):
    record = first(reusable.personal.getCrystalRecords())
    if record:
        _, crystals = record[:2]
        return crystals.getRecord(b'crystal')
    return 0


def getTotalXPToShow(reusable):
    hasPremium = reusable.personal.hasAnyPremium
    xpRecords = getDirectXpRecords(reusable)
    if hasPremium:
        return xpRecords.premiumAccountValue.getRecord(b'xpToShow')
    return xpRecords.baseAccountValue.getRecord(b'xpToShow')


def getTotalFreeXPToShow(reusable):
    hasPremium = reusable.personal.hasAnyPremium
    freeXpRecords = getDirectFreeXpRecords(reusable)
    if hasPremium:
        return freeXpRecords.premiumAccountValue.getRecord(b'freeXP')
    return freeXpRecords.baseAccountValue.getRecord(b'freeXP')


def getCreditsToShow(reusable, isDiffShow=False):
    values = []
    for creditRecords in reusable.personal.getMoneyRecords():
        baseCredits, premiumCredits = creditRecords[:2]
        value = premiumCredits.getRecord(b'credits', b'originalCreditsToDraw')
        if isDiffShow and value > 0:
            value -= baseCredits.getRecord(b'credits', b'originalCreditsToDraw')
        values.append(value)

    return values


def getTotalCreditsToShow(reusable):
    hasPremium = reusable.personal.hasAnyPremium
    moneyRecords = getDirectMoneyRecords(reusable)
    if hasPremium:
        return moneyRecords.premiumAccountValue.getRecord(b'credits', b'originalCreditsToDraw')
    return moneyRecords.baseAccountValue.getRecord(b'credits', b'originalCreditsToDraw')


def getDirectMoneyRecords(reusable):
    personalResults = reusable.personal
    base, premium, gold, additional, baseWithWotPlus, premiumWithWotPlus = first(personalResults.getMoneyRecords())
    return FinancialRecordValues(baseAccountValue=base, premiumAccountValue=premium, additionalValue=additional, extraValue=gold, baseAccountValueWithWotPlus=baseWithWotPlus, premiumAccountValueWithWotPlus=premiumWithWotPlus)


def getDirectXpRecords(reusable):
    personalResults = reusable.personal
    baseXP, premiumXP, _, _, baseXPWithWotPlus, premiumXPWithWotPlus, _, _ = first(personalResults.getXPRecords())
    return FinancialRecordValues(baseAccountValue=baseXP, premiumAccountValue=premiumXP, additionalValue=None, extraValue=None, baseAccountValueWithWotPlus=baseXPWithWotPlus, premiumAccountValueWithWotPlus=premiumXPWithWotPlus)


def getDirectFreeXpRecords(reusable):
    personalResults = reusable.personal
    _, _, baseFreeXP, premiumFreeXP, _, _, baseFreeXPWithWotPlus, premiumFreeXPWithWotPlus = first(personalResults.getXPRecords())
    return FinancialRecordValues(baseAccountValue=baseFreeXP, premiumAccountValue=premiumFreeXP, additionalValue=None, extraValue=None, baseAccountValueWithWotPlus=baseFreeXPWithWotPlus, premiumAccountValueWithWotPlus=premiumFreeXPWithWotPlus)


def hasAogasFine(battleResults):
    factor = b'aogasFactor10'
    xpRecords = getDirectXpRecords(battleResults.reusable)
    moneyRecords = getDirectMoneyRecords(battleResults.reusable)
    if battleResults.reusable.personal.hasAnyPremium:
        return (b'hasAogasFine',
         moneyRecords.premiumAccountValue.getFactor(factor) < 1 or xpRecords.premiumAccountValue.getFactor(factor) < 1)
    return (
     b'hasAogasFine',
     moneyRecords.baseAccountValue.getFactor(factor) < 1 or xpRecords.baseAccountValue.getFactor(factor) < 1)


def hasHighScope(battleResults):
    personalResults = battleResults.reusable.personal
    baseXP, _, _, _, _, _, _, _ = first(personalResults.getXPRecords())
    if baseXP:
        return (b'isHighScope', baseXP.getRecord(b'isHighScope'))
    return (
     b'isHighScope', False)


def hasXpReferralFactor(battleResults):
    personalResults = battleResults.reusable.personal
    baseXP, _, _, _, _, _, _, _ = first(personalResults.getXPRecords())
    if baseXP:
        referralFactor = baseXP.getFactor(b'referral20XPFactor100')
        if referralFactor > 0 and baseXP.getRecord(b'referral20XPFactor100'):
            return (b'referralFactor', referralFactor)
    return (b'referralFactor', 0)


def hasCreditsReferralFactor(battleResults):
    personalResults = battleResults.reusable.personal
    baseCredits, _, _, _, _, _ = first(personalResults.getMoneyRecords())
    referralFactor = 0
    if baseCredits:
        referralFactor = baseCredits.getFactor(b'referral20CreditsFactor100')
    return (
     b'referralFactor', max(referralFactor, 0))


def isPiggyBankCreditsAvailable(battleResults):
    isAvailable = battleResults.reusable.common.checkBonusCaps(_CAPS.PIGGY_BANK_CREDITS)
    return (b'isAvailable', isAvailable)


def isPiggyBankGoldAvailable(battleResults):
    isAvailable = isGoldPiggyBankAvailaible(battleResults.reusable)
    return (b'isAvailable', isAvailable)


def isCreditsAvailable(battleResults):
    isAvailable = battleResults.reusable.common.checkBonusCaps(_CAPS.CREDITS)
    return (b'isAvailable', isAvailable)


def isXpAvailable(battleResults):
    isAvailable = battleResults.reusable.common.checkBonusCaps(_CAPS.XP)
    return (b'isAvailable', isAvailable)


def isFreeXpAvailable(battleResults):
    isAvailable = battleResults.reusable.common.checkBonusCaps(_CAPS.FREE_XP)
    return (b'isAvailable', isAvailable)


@dependency.replace_none_kwargs(wotPlusCtrl=IWotPlusController)
def isWotPlusBonusEnabled(_, wotPlusCtrl=None):
    isWotPlusBattleBonusesEnabled = wotPlusCtrl.getSettingsStorage().isBattleBonusesEnabled()
    return (b'isEnabled', isWotPlusBattleBonusesEnabled)


def hasCreditsPetFactor(battleResults):
    personalResults = battleResults.reusable.personal
    baseCredits, _, _, _, _, _ = first(personalResults.getMoneyRecords())
    petBonusFactor = 0
    if baseCredits:
        petBonusFactor = baseCredits.getFactor(b'petSystemCreditsFactor100')
    return (
     b'bonusFactor', max(int(petBonusFactor * 100), 0))
