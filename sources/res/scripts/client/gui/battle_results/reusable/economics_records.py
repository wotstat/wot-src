import itertools
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from constants import PREMIUM_TYPE
from ValueReplay import ValueReplay, ValueReplayConnector
from debug_utils import LOG_ERROR
from dossiers2.custom.records import RECORD_DB_IDS
from gui.battle_results.reusable import records
from gui.battle_results.settings import FACTOR_VALUE
from gui.shared.money import Currency
from helpers import dependency
from helpers.rest_bonus import getRestBonusData
from renewable_subscription_common.settings_constants import WotPlusTier
from renewable_subscription_common.settings_helpers import SubscriptionSettingsStorage
from skeletons.gui.game_control import IWotPlusController, IRestBonusController
from skeletons.gui.lobby_context import ILobbyContext
_DEFAULT_FACTORS = {(_CAPS.PREM_CREDITS): (FACTOR_VALUE.BASE_CREDITS_FACTOR), 
   (_CAPS.PREM_XP): (FACTOR_VALUE.BASE_XP_FACTOR), 
   (_CAPS.PREM_TMEN_XP): (FACTOR_VALUE.BASE_TMEN_XP_FACTOR)}

def _getPremiumBonusFactor(factor, bonusCaps, isPremBonusEnabled):
    if isPremBonusEnabled:
        return factor
    return _DEFAULT_FACTORS[bonusCaps]


@dependency.replace_none_kwargs(restBonusCtrl=IRestBonusController)
def _applyRestBonusToDaily(replay, results, restBonusCtrl=None):
    if b'dailyXPFactor10' not in replay:
        return
    restBonusQuests = restBonusCtrl.restBonusQuests if restBonusCtrl else {}
    restBonusFactor, restBonusQuestIDs = getRestBonusData(results.get(b'questsProgress', {}), restBonusQuests)
    if restBonusFactor:
        replay[b'dailyXPFactor10'] = results[b'dailyXPFactor10'] + int(restBonusFactor * 10)
        keysToZero = [appliedName for _, (appliedName, _), _ in replay for questID in restBonusQuestIDs if appliedName.startswith(b'eventXPFactor100List_' + questID) or appliedName.startswith(b'eventFreeXPFactor100List_' + questID)]
        for key in keysToZero:
            replay[key] = 0

    return


def _updateAdditionalFactorFromReplay(replay, results, setDefault=False):
    if b'additionalXPFactor10' not in replay:
        return
    if setDefault:
        if b'dailyXPFactor10' in replay:
            replay[b'additionalXPFactor10'] = FACTOR_VALUE.ADDITIONAL_BONUS_ZERO_FACTOR
        else:
            replay[b'additionalXPFactor10'] = FACTOR_VALUE.ADDITIONAL_BONUS_ONE_FACTOR
    else:
        replay[b'additionalXPFactor10'] = results[b'additionalXPFactor10']
    return


class _AdditionalRecords(records.RawRecords):
    __slots__ = ()

    def __init__(self, results):
        rawRecords = {}
        if b'autoRepairCost' in results:
            cost = results[b'autoRepairCost']
            if cost is not None:
                rawRecords[b'autoRepairCost'] = -cost
        if b'autoLoadCost' in results:
            cost = results[b'autoLoadCost']
            if cost is not None:
                rawRecords[b'autoLoadCredits'] = -cost[0]
                rawRecords[b'autoLoadGold'] = -cost[1]
        if b'autoEquipCost' in results:
            cost = results[b'autoEquipCost']
            if cost is not None:
                rawRecords[b'autoEquipCredits'] = -cost[0]
                rawRecords[b'autoEquipGold'] = -cost[1]
                rawRecords[b'autoEquipCrystals'] = -cost[2]
        if b'piggyBank' in results:
            cost = results[b'piggyBank']
            if cost is not None:
                rawRecords[b'piggyBank'] = cost
        super(_AdditionalRecords, self).__init__(rawRecords)
        return


class _CrystalRecords(records.RawRecords):
    __slots__ = ()

    def __init__(self, replay, results):
        rawRecords = {}
        eventToken = b'eventCrystalList_'
        eventsCrystals = 0
        for _, (appliedName, appliedValue), (_, _) in replay:
            if appliedName == b'originalCrystal' and appliedValue:
                rawRecords[appliedName] = appliedValue
            elif appliedName.startswith(eventToken):
                eventsCrystals += appliedValue

        if eventsCrystals:
            rawRecords[b'events'] = eventsCrystals
        if b'autoEquipCost' in results:
            cost = results[b'autoEquipCost']
            if cost is not None:
                rawRecords[b'autoEquipCrystals'] = -cost[2]
        super(_CrystalRecords, self).__init__(rawRecords)
        return


class _CreditsReplayRecords(records.ReplayRecords):
    __slots__ = ()

    def __init__(self, replay, results, squadCreditsFactor=0):
        super(_CreditsReplayRecords, self).__init__(replay, b'credits')
        self._addRecord(ValueReplay.SUB, b'originalCreditsToDraw', results[b'originalCreditsToDraw'], 0)
        self._addRecord(ValueReplay.SET, b'achievementCredits', results[b'achievementCredits'], 0)
        self._addRecord(ValueReplay.FACTOR, b'premSquadCreditsFactor100', squadCreditsFactor, 0)
        self._addRecord(ValueReplay.SUBCOEFF, b'originalCreditsToDrawSquad', results[b'originalCreditsToDrawSquad'], results[b'originalCreditsToDrawSquad'] * self.getFactor(b'premSquadCreditsFactor100') * -1)
        return

    def _getRecord(self, name):
        value = super(_CreditsReplayRecords, self)._getRecord(name)
        if name in (b'originalCreditsToDraw', b'achievementCredits'):
            value = records.makeReplayValueRound(value * self.getFactor(b'appliedPremiumCreditsFactor100'))
        return value


class _XPReplayRecords(records.ReplayRecords):
    __slots__ = ()

    def __init__(self, replay, isHighScope, achievementXP):
        super(_XPReplayRecords, self).__init__(replay, b'xp')
        if isHighScope:
            self._addRecord(ValueReplay.SET, b'isHighScope', 1, 0)
        self._addRecord(ValueReplay.SET, b'achievementXP', achievementXP, 0)
        self._addRecord(ValueReplay.SET, b'xpToShow', max(0, self.getRecord(b'xp')), 0)
        return

    def _getRecord(self, name):
        value = super(_XPReplayRecords, self)._getRecord(name)
        if name in (b'achievementXP',):
            value = records.makeReplayValueRound(value * self.getFactor(b'appliedPremiumXPFactor100'))
        return value


class _FreeXPReplayRecords(records.ReplayRecords):
    __slots__ = ()

    def __init__(self, replay, achievementFreeXP):
        super(_FreeXPReplayRecords, self).__init__(replay, b'freeXP')
        self._addRecord(ValueReplay.SET, b'achievementFreeXP', achievementFreeXP, 0)
        return

    def _getRecord(self, name):
        value = super(_FreeXPReplayRecords, self)._getRecord(name)
        if name in (b'achievementFreeXP',):
            value = records.makeReplayValueRound(value * self.getFactor(b'appliedPremiumXPFactor100'))
        return value


class _TmenXPRecordsChains(object):
    __slots__ = (b'__baseTmenXP', b'__premiumTmenXP', b'__premiumPlusTmenXP', b'__baseTmenXPAdd', b'__premiumTmenXPAdd', b'__premiumPlusTmenXPAdd', b'__isPremTmenXpBonuxEnabled')

    def __init__(self, bonusType, bonusCapsOverrides):
        super(_TmenXPRecordsChains, self).__init__()
        self.__baseTmenXP = records.RecordsIterator()
        self.__premiumTmenXP = records.RecordsIterator()
        self.__premiumPlusTmenXP = records.RecordsIterator()
        self.__baseTmenXPAdd = records.RecordsIterator()
        self.__premiumTmenXPAdd = records.RecordsIterator()
        self.__premiumPlusTmenXPAdd = records.RecordsIterator()
        self.__isPremTmenXpBonuxEnabled = _CAPS.checkAny(bonusType, _CAPS.PREM_TMEN_XP, specificOverrides=bonusCapsOverrides)
        return

    def addResults(self, connector, results):
        premiumType = results.get(b'premMask', PREMIUM_TYPE.NONE)
        hasPremiumPlus = bool(premiumType & PREMIUM_TYPE.PLUS)
        if b'tmenXPReplay' in results and results[b'tmenXPReplay'] is not None:
            replay = ValueReplay(connector, recordName=b'tmenXP', replay=results[b'tmenXPReplay'])
            _applyRestBonusToDaily(replay, results)
            _updateAdditionalFactorFromReplay(replay, results, setDefault=True)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self.__baseTmenXP.addRecords(records.ReplayRecords(replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self.__premiumTmenXP.addRecords(records.ReplayRecords(replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self.__premiumPlusTmenXP.addRecords(records.ReplayRecords(replay))
            _updateAdditionalFactorFromReplay(replay, results, setDefault=hasPremiumPlus)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self.__baseTmenXPAdd.addRecords(records.ReplayRecords(replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self.__premiumTmenXPAdd.addRecords(records.ReplayRecords(replay))
            _updateAdditionalFactorFromReplay(replay, results, setDefault=False)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self.__premiumPlusTmenXPAdd.addRecords(records.ReplayRecords(replay))
        else:
            LOG_ERROR(b'TmenXP replay is not found', results)
        return

    def getRecords(self, premiumType, addBonusApplied):
        if premiumType == PREMIUM_TYPE.NONE or premiumType & (PREMIUM_TYPE.VIP | PREMIUM_TYPE.PLUS):
            secondTmenXPData = self.__premiumPlusTmenXPAdd if addBonusApplied else self.__premiumPlusTmenXP
        else:
            secondTmenXPData = self.__premiumTmenXPAdd if addBonusApplied else self.__premiumTmenXP
        firstTmenXPData = self.__baseTmenXPAdd if addBonusApplied else self.__baseTmenXP
        return itertools.izip(firstTmenXPData, secondTmenXPData)

    def __updatePremiumXPFactor(self, replay, results, premType=PREMIUM_TYPE.NONE):
        if b'appliedPremiumTmenXPFactor100' not in replay:
            return
        if premType == PREMIUM_TYPE.PLUS:
            replay[b'appliedPremiumTmenXPFactor100'] = _getPremiumBonusFactor(results[b'premiumPlusTmenXPFactor100'], _CAPS.PREM_TMEN_XP, self.__isPremTmenXpBonuxEnabled)
        elif premType == PREMIUM_TYPE.BASIC:
            replay[b'appliedPremiumTmenXPFactor100'] = _getPremiumBonusFactor(results[b'premiumTmenXPFactor100'], _CAPS.PREM_TMEN_XP, self.__isPremTmenXpBonuxEnabled)
        else:
            replay[b'appliedPremiumTmenXPFactor100'] = FACTOR_VALUE.BASE_XP_FACTOR
        return


class EconomicsRecordsChains(object):
    __slots__ = (b'_baseCredits', b'_premiumCredits', b'_premiumPlusCredits', b'_baseCreditsWithWotPlus', b'_premiumCreditsWithWotPlus', b'_premiumPlusCreditsWithWotPlus', b'_goldRecords', b'_additionalRecords', b'_baseXP', b'_premiumXP', b'_premiumPlusXP', b'_baseXPWithWotPlus', b'_premiumXPWithWotPlus', b'_premiumPlusXPWithWotPlus', b'_baseXPAdd', b'_premiumXPAdd', b'_premiumPlusXPAdd', b'_baseXPAddWithWotPlus', b'_premiumXPAddWithWotPlus', b'_premiumPlusXPAddWithWotPlus', b'_baseFreeXP', b'_premiumFreeXP', b'_premiumPlusFreeXP', b'_baseFreeXPWithWotPlus', b'_premiumFreeXPWithWotPlus', b'_premiumPlusFreeXPWithWotPlus', b'_baseFreeXPAdd', b'_premiumFreeXPAdd', b'_premiumPlusFreeXPAdd', b'_baseFreeXPAddWithWotPlus', b'_premiumFreeXPAddWithWotPlus', b'_premiumPlusFreeXPAddWithWotPlus', b'_crystal', b'_crystalDetails', b'_tmenXPRecordsChains', b'__isPremCreditsBonusEnabled', b'__isPremXpBonusEnabled')

    def __init__(self, bonusType, bonusCapsOverrides):
        super(EconomicsRecordsChains, self).__init__()
        self._baseCredits = records.RecordsIterator()
        self._premiumCredits = records.RecordsIterator()
        self._premiumPlusCredits = records.RecordsIterator()
        self._baseCreditsWithWotPlus = records.RecordsIterator()
        self._premiumCreditsWithWotPlus = records.RecordsIterator()
        self._premiumPlusCreditsWithWotPlus = records.RecordsIterator()
        self._goldRecords = records.RecordsIterator()
        self._additionalRecords = records.RecordsIterator()
        self._baseXP = records.RecordsIterator()
        self._premiumXP = records.RecordsIterator()
        self._premiumPlusXP = records.RecordsIterator()
        self._baseXPWithWotPlus = records.RecordsIterator()
        self._premiumXPWithWotPlus = records.RecordsIterator()
        self._premiumPlusXPWithWotPlus = records.RecordsIterator()
        self._baseXPAdd = records.RecordsIterator()
        self._premiumXPAdd = records.RecordsIterator()
        self._premiumPlusXPAdd = records.RecordsIterator()
        self._baseXPAddWithWotPlus = records.RecordsIterator()
        self._premiumXPAddWithWotPlus = records.RecordsIterator()
        self._premiumPlusXPAddWithWotPlus = records.RecordsIterator()
        self._baseFreeXP = records.RecordsIterator()
        self._premiumFreeXP = records.RecordsIterator()
        self._premiumPlusFreeXP = records.RecordsIterator()
        self._baseFreeXPWithWotPlus = records.RecordsIterator()
        self._premiumFreeXPWithWotPlus = records.RecordsIterator()
        self._premiumPlusFreeXPWithWotPlus = records.RecordsIterator()
        self._baseFreeXPAdd = records.RecordsIterator()
        self._premiumFreeXPAdd = records.RecordsIterator()
        self._premiumPlusFreeXPAdd = records.RecordsIterator()
        self._baseFreeXPAddWithWotPlus = records.RecordsIterator()
        self._premiumFreeXPAddWithWotPlus = records.RecordsIterator()
        self._premiumPlusFreeXPAddWithWotPlus = records.RecordsIterator()
        self._tmenXPRecordsChains = _TmenXPRecordsChains(bonusType, bonusCapsOverrides)
        self._crystal = records.RecordsIterator()
        self._crystalDetails = records.RecordsIterator()
        self.__isPremCreditsBonusEnabled = _CAPS.checkAny(bonusType, _CAPS.PREM_CREDITS, specificOverrides=bonusCapsOverrides)
        self.__isPremXpBonusEnabled = _CAPS.checkAny(bonusType, _CAPS.PREM_XP, specificOverrides=bonusCapsOverrides)
        return

    def getBaseCreditsRecords(self):
        return self._baseCredits

    def getPremiumCreditsRecords(self):
        return self._premiumCredits

    def getCreditsDiff(self):
        return self._premiumCredits.getRecord(b'credits', b'originalCreditsToDraw') - self._baseCredits.getRecord(b'credits', b'originalCreditsToDraw')

    def getBaseXPRecords(self):
        return self._baseXP

    def getPremiumXPRecords(self):
        return self._premiumXP

    def getPremiumXPAddRecords(self):
        return self._premiumXPAdd

    def getMoneyRecords(self, premiumType=PREMIUM_TYPE.NONE):
        if premiumType == PREMIUM_TYPE.NONE or premiumType & (PREMIUM_TYPE.VIP | PREMIUM_TYPE.PLUS):
            resultPremiumData = self._premiumPlusCredits
            resultPremiumDataWithWotPlus = self._premiumPlusCreditsWithWotPlus
        else:
            resultPremiumData = self._premiumCredits
            resultPremiumDataWithWotPlus = self._premiumCreditsWithWotPlus
        return itertools.izip(self._baseCredits, resultPremiumData, self._goldRecords, self._additionalRecords, self._baseCreditsWithWotPlus, resultPremiumDataWithWotPlus)

    def getCrystalRecords(self):
        return itertools.izip(self._crystal, self._crystal)

    def getCrystalDetails(self):
        return self._crystalDetails

    def getXPRecords(self, premiumType=PREMIUM_TYPE.NONE, addBonusApplied=False):
        if premiumType == PREMIUM_TYPE.NONE or premiumType & (PREMIUM_TYPE.VIP | PREMIUM_TYPE.PLUS):
            if addBonusApplied:
                secondXPData = self._premiumPlusXPAdd
                secondFreeXPData = self._premiumPlusFreeXPAdd
                secondXPDataWithWotPlus = self._premiumPlusXPAddWithWotPlus
                secondFreeXPDataWithWotPlus = self._premiumPlusFreeXPAddWithWotPlus
            else:
                secondXPData = self._premiumPlusXP
                secondFreeXPData = self._premiumPlusFreeXP
                secondXPDataWithWotPlus = self._premiumPlusXPWithWotPlus
                secondFreeXPDataWithWotPlus = self._premiumPlusFreeXPWithWotPlus
        elif addBonusApplied:
            secondXPData = self._premiumXPAdd
            secondFreeXPData = self._premiumFreeXPAdd
            secondXPDataWithWotPlus = self._premiumXPAddWithWotPlus
            secondFreeXPDataWithWotPlus = self._premiumFreeXPAddWithWotPlus
        else:
            secondXPData = self._premiumXP
            secondFreeXPData = self._premiumFreeXP
            secondXPDataWithWotPlus = self._premiumXPWithWotPlus
            secondFreeXPDataWithWotPlus = self._premiumFreeXPWithWotPlus
        if addBonusApplied:
            firstXPData = self._baseXPAdd
            firstFreeXPData = self._baseFreeXPAdd
            firstXPDataWithWotPlus = self._baseXPAddWithWotPlus
            firstFreeXPDataWithWotPlus = self._baseFreeXPAddWithWotPlus
        else:
            firstXPData = self._baseXP
            firstFreeXPData = self._baseFreeXP
            firstXPDataWithWotPlus = self._baseXPWithWotPlus
            firstFreeXPDataWithWotPlus = self._baseFreeXPWithWotPlus
        return itertools.izip(firstXPData, secondXPData, firstFreeXPData, secondFreeXPData, firstXPDataWithWotPlus, secondXPDataWithWotPlus, firstFreeXPDataWithWotPlus, secondFreeXPDataWithWotPlus)

    def getXPDiff(self):
        return self._premiumXP.getRecord(b'xp') - self._baseXP.getRecord(b'xp')

    def getTmenXPRecords(self, premiumType=PREMIUM_TYPE.NONE, addBonusApplied=False):
        return self._tmenXPRecordsChains.getRecords(premiumType, addBonusApplied)

    def addResults(self, _, results):
        connector = ValueReplayConnector(results)
        self._addMoneyResults(connector, results)
        self._addXPResults(connector, results)
        self._addCrystalResults(connector, results)
        self._tmenXPRecordsChains.addResults(connector, results)
        return

    def _addMoneyResults(self, connector, results):
        if b'creditsReplay' in results and results[b'creditsReplay'] is not None:
            replay = ValueReplay(connector, recordName=b'credits', replay=results[b'creditsReplay'])
            appliedPremiumCreditsFactor100Exists = b'appliedPremiumCreditsFactor100' in replay
            if appliedPremiumCreditsFactor100Exists:
                replay[b'appliedPremiumCreditsFactor100'] = FACTOR_VALUE.BASE_CREDITS_FACTOR
            self._baseCredits.addRecords(self.__buildCreditsReplayForPremType(PREMIUM_TYPE.NONE, results, replay))
            self._baseCreditsWithWotPlus.addRecords(self.__buildCreditsReplayForWotPlus(PREMIUM_TYPE.NONE, results, replay))
            if appliedPremiumCreditsFactor100Exists:
                replay[b'appliedPremiumCreditsFactor100'] = _getPremiumBonusFactor(results[b'premiumCreditsFactor100'], _CAPS.PREM_CREDITS, self.__isPremCreditsBonusEnabled)
            self._premiumCredits.addRecords(self.__buildCreditsReplayForPremType(PREMIUM_TYPE.BASIC, results, replay))
            self._premiumCreditsWithWotPlus.addRecords(self.__buildCreditsReplayForWotPlus(PREMIUM_TYPE.BASIC, results, replay))
            if appliedPremiumCreditsFactor100Exists:
                replay[b'appliedPremiumCreditsFactor100'] = _getPremiumBonusFactor(results[b'premiumPlusCreditsFactor100'], _CAPS.PREM_CREDITS, self.__isPremCreditsBonusEnabled)
            self._premiumPlusCredits.addRecords(self.__buildCreditsReplayForPremType(PREMIUM_TYPE.PLUS, results, replay))
            self._premiumPlusCreditsWithWotPlus.addRecords(self.__buildCreditsReplayForWotPlus(PREMIUM_TYPE.PLUS, results, replay))
        else:
            LOG_ERROR(b'Credits replay is not found', results)
        if b'goldReplay' in results and results[b'goldReplay'] is not None:
            replay = ValueReplay(connector, recordName=b'gold', replay=results[b'goldReplay'])
            self._goldRecords.addRecords(records.ReplayRecords(replay, b'gold'))
        else:
            LOG_ERROR(b'Gold replay is not found', results)
        self._additionalRecords.addRecords(_AdditionalRecords(results))
        return

    def _addXPResults(self, connector, results):
        premiumType = results.get(b'premMask', PREMIUM_TYPE.NONE)
        hasPremiumPlus = bool(premiumType & PREMIUM_TYPE.PLUS)
        if b'xpReplay' in results and results[b'xpReplay'] is not None:
            replay = ValueReplay(connector, recordName=b'xp', replay=results[b'xpReplay'])
            _applyRestBonusToDaily(replay, results)
            _updateAdditionalFactorFromReplay(replay, results, setDefault=True)
            isHighScope = RECORD_DB_IDS[(b'max15x15', b'maxXP')] in [recordID for recordID, _ in results.get(b'dossierPopUps', [])]
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseXP.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self._baseXPWithWotPlus.addRecords(self.__buildXPReplayForWotPlus(isHighScope, results, replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumXP.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self._premiumXPWithWotPlus.addRecords(self.__buildXPReplayForWotPlus(isHighScope, results, replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusXP.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self._premiumPlusXPWithWotPlus.addRecords(self.__buildXPReplayForWotPlus(isHighScope, results, replay))
            _updateAdditionalFactorFromReplay(replay, results, setDefault=hasPremiumPlus)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseXPAdd.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self._baseXPAddWithWotPlus.addRecords(self.__buildXPReplayForWotPlus(isHighScope, results, replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumXPAdd.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self._premiumXPAddWithWotPlus.addRecords(self.__buildXPReplayForWotPlus(isHighScope, results, replay))
            _updateAdditionalFactorFromReplay(replay, results, setDefault=False)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusXPAdd.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self._premiumPlusXPAddWithWotPlus.addRecords(self.__buildXPReplayForWotPlus(isHighScope, results, replay))
        else:
            LOG_ERROR(b'XP replay is not found', results)
        if b'freeXPReplay' in results and results[b'freeXPReplay'] is not None:
            replay = ValueReplay(connector, recordName=b'freeXP', replay=results[b'freeXPReplay'])
            _applyRestBonusToDaily(replay, results)
            _updateAdditionalFactorFromReplay(replay, results, setDefault=True)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseFreeXP.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self._baseFreeXPWithWotPlus.addRecords(self.__buildFreeXPReplayForWotPlus(results, replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumFreeXP.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self._premiumFreeXPWithWotPlus.addRecords(self.__buildFreeXPReplayForWotPlus(results, replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusFreeXP.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self._premiumPlusFreeXPWithWotPlus.addRecords(self.__buildFreeXPReplayForWotPlus(results, replay))
            _updateAdditionalFactorFromReplay(replay, results, setDefault=hasPremiumPlus)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseFreeXPAdd.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self._baseFreeXPAddWithWotPlus.addRecords(self.__buildFreeXPReplayForWotPlus(results, replay))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumFreeXPAdd.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self._premiumFreeXPAddWithWotPlus.addRecords(self.__buildFreeXPReplayForWotPlus(results, replay))
            _updateAdditionalFactorFromReplay(replay, results, setDefault=False)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusFreeXPAdd.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self._premiumPlusFreeXPAddWithWotPlus.addRecords(self.__buildFreeXPReplayForWotPlus(results, replay))
        else:
            LOG_ERROR(b'Free XP replay is not found', results)
        return

    def _addCrystalResults(self, connector, results):
        if b'crystalReplay' in results and results[b'crystalReplay'] is not None:
            replay = ValueReplay(connector, recordName=Currency.CRYSTAL, replay=results[b'crystalReplay'])
            self._crystal.addRecords(records.ReplayRecords(replay, Currency.CRYSTAL))
            self._crystalDetails.addRecords(_CrystalRecords(replay, results))
        else:
            LOG_ERROR(b'crystalReplay is not found', results)
        return

    def __buildCreditsReplayForPremType(self, targetPremiumType, results, replay):
        initialSquadFactor = results[b'premSquadCreditsFactor100']
        squadCreditsFactor = self.__getPremiumSquadCreditsFactor(results, targetPremiumType)
        results[b'premSquadCreditsFactor100'] = squadCreditsFactor
        creditsReplayToUse = _CreditsReplayRecords(replay, results, squadCreditsFactor)
        results[b'premSquadCreditsFactor100'] = initialSquadFactor
        return creditsReplayToUse

    def __buildCreditsReplayForWotPlus(self, targetPremiumType, results, replay):
        initialWotPlusCreditsFactor = results[b'wotPlusCreditsFactor100']
        results[b'wotPlusCreditsFactor100'] = self.__getWotPlusFactor(results, b'creditsFactor')
        creditsReplayToUse = self.__buildCreditsReplayForPremType(targetPremiumType, results, replay)
        results[b'wotPlusCreditsFactor100'] = initialWotPlusCreditsFactor
        return creditsReplayToUse

    def __buildXPReplayForWotPlus(self, isHighScope, results, replay):
        initialWotPlusXPFactor = results[b'wotPlusXPFactor100']
        results[b'wotPlusXPFactor100'] = self.__getWotPlusFactor(results, b'xpFactor')
        xpReplayToUse = _XPReplayRecords(replay, isHighScope, results[b'achievementXP'])
        results[b'wotPlusXPFactor100'] = initialWotPlusXPFactor
        return xpReplayToUse

    def __buildFreeXPReplayForWotPlus(self, results, replay):
        initialWotPlusFreeXPFactor = results[b'wotPlusFreeXPFactor100']
        results[b'wotPlusFreeXPFactor100'] = self.__getWotPlusFactor(results, b'freeXPFactor')
        freeXPReplayToUse = _FreeXPReplayRecords(replay, results[b'achievementFreeXP'])
        results[b'wotPlusFreeXPFactor100'] = initialWotPlusFreeXPFactor
        return freeXPReplayToUse

    def __updatePremiumXPFactor(self, replay, results, premType=PREMIUM_TYPE.NONE):
        if b'appliedPremiumXPFactor100' not in replay:
            return
        if premType == PREMIUM_TYPE.PLUS:
            replay[b'appliedPremiumXPFactor100'] = _getPremiumBonusFactor(results[b'premiumPlusXPFactor100'], _CAPS.PREM_XP, self.__isPremXpBonusEnabled)
        elif premType == PREMIUM_TYPE.BASIC:
            replay[b'appliedPremiumXPFactor100'] = _getPremiumBonusFactor(results[b'premiumXPFactor100'], _CAPS.PREM_XP, self.__isPremXpBonusEnabled)
        else:
            replay[b'appliedPremiumXPFactor100'] = FACTOR_VALUE.BASE_XP_FACTOR
        return

    @staticmethod
    @dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
    def __getPremiumSquadCreditsFactor(results, targetPremiumType, lobbyContext=None):
        premiumType = PREMIUM_TYPE.activePremium(results.get(b'premMask', PREMIUM_TYPE.NONE))
        if targetPremiumType > premiumType:
            return lobbyContext.getServerSettings().squadPremiumBonus.ownCredits * 100
        if targetPremiumType < premiumType:
            return 0
        return results.get(b'premSquadCreditsFactor100', 0)

    @staticmethod
    @dependency.replace_none_kwargs(wotPlusCtrl=IWotPlusController)
    def __getWotPlusFactor(results, factorName, wotPlusCtrl=None):
        battleResultsWotPlusTier = results.get(b'wotPlusTier', WotPlusTier.NONE)
        if battleResultsWotPlusTier == WotPlusTier.NONE:
            settingsStorage = wotPlusCtrl.getSettingsStorage()
            if not settingsStorage.isBattleBonusesEnabled():
                return 0.0
            for tierID, tier in settingsStorage.reverseIterTiers():
                if tier.battleBonusesFeature.available:
                    battleResultsWotPlusTier = tierID
                    break

        config = SubscriptionSettingsStorage(battleResultsWotPlusTier).getBattleBonusesFeatureFactors()
        if config:
            return getattr(config, factorName) * 100
        return 0.0
