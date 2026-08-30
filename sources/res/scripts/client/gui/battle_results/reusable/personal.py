import itertools
from collections import namedtuple
import typing
from ValueReplay import ValueReplay, ValueReplayConnector
from constants import PREMIUM_TYPE
from debug_utils import LOG_ERROR
from dossiers2.custom.records import RECORD_DB_IDS
from gui.battle_results.reusable import records, ReusableInfoFactory
from gui.battle_results.reusable import shared
from gui.battle_results.reusable import sort_keys
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.battle_results.settings import FACTOR_VALUE
from gui.ranked_battles.ranked_models import PostBattleRankInfo
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable.vehicles import VehiclesInfo
    from gui.shared.utils.requesters.StatsRequester import _ControllableXPData
_LifeTimeInfo = namedtuple(b'_LifeTimeInfo', (
 b'isKilled',
 b'lifeTime'))

class SquadBonusInfo(object):
    itemsCache = dependency.descriptor(IItemsCache)
    eventsCache = dependency.descriptor(IEventsCache)
    __slots__ = (b'__vehicles', b'__joinedOnArena', b'__size')

    def __init__(self, vehicles=None, joinedOnArena=None, size=0, **kwargs):
        super(SquadBonusInfo, self).__init__()
        self.__vehicles = vehicles or set()
        self.__joinedOnArena = joinedOnArena or []
        self.__size = size
        return

    def getVehiclesLevelsDistance(self):
        getter = self.itemsCache.items.getItemByCD
        levels = [getter(typeCompDescr).level for typeCompDescr in self.__vehicles]
        levels.sort()
        if levels:
            return levels[-1] - levels[0]
        return -1

    def getSquadFlags(self, vehicleID, intCD):
        showSquadLabels = True
        squadHasBonus = False
        if self.eventsCache.isSquadXpFactorsEnabled() and self.__size > 1:
            if vehicleID in self.__joinedOnArena:
                showSquadLabels = False
            else:
                distance = self.getVehiclesLevelsDistance()
                if intCD:
                    level = self.itemsCache.items.getItemByCD(intCD).level
                    key = (distance, level)
                    showSquadLabels = key not in self.eventsCache.getSquadZeroBonuses()
                squadHasBonus = distance in self.eventsCache.getSquadBonusLevelDistance()
        else:
            showSquadLabels = False
        return (showSquadLabels, squadHasBonus)


class PersonalAvatarInfo(object):
    __slots__ = (b'__accountDBID', b'__clanDBID', b'__team', b'__isPrematureLeave', b'__fairplayViolations', b'__squadBonusInfo', b'__winnerIfDraw', b'__eligibleForCrystalRewards', b'__extInfo')

    def __init__(self, bonusType, accountDBID=0, clanDBID=0, team=0, isPrematureLeave=False, fairplayViolations=None, squadBonusInfo=None, winnerIfDraw=0, eligibleForCrystalRewards=False, **kwargs):
        super(PersonalAvatarInfo, self).__init__()
        self.__accountDBID = accountDBID
        self.__clanDBID = clanDBID
        self.__team = team
        self.__isPrematureLeave = isPrematureLeave
        self.__eligibleForCrystalRewards = eligibleForCrystalRewards
        fairplayViolationsCls = ReusableInfoFactory.fairplayViolationForBonusType(bonusType)
        self.__fairplayViolations = fairplayViolationsCls(*(fairplayViolations or ()))
        squadBonusInfoCls = ReusableInfoFactory.squadBonusInfoForBonusType(bonusType)
        self.__squadBonusInfo = squadBonusInfoCls(**(squadBonusInfo or {}))
        self.__winnerIfDraw = winnerIfDraw
        self.__extInfo = kwargs
        return

    @property
    def accountDBID(self):
        return self.__accountDBID

    @property
    def clanDBID(self):
        return self.__clanDBID

    @property
    def team(self):
        return self.__team

    @property
    def isPrematureLeave(self):
        return self.__isPrematureLeave

    @property
    def winnerIfDraw(self):
        return self.__winnerIfDraw

    @property
    def eligibleForCrystalRewards(self):
        return self.__eligibleForCrystalRewards

    @property
    def extensionInfo(self):
        return self.__extInfo

    def getPersonalSquadFlags(self, vehicles):
        vehicleID = vehicles.getVehicleID(self.__accountDBID)
        return self.__squadBonusInfo.getSquadFlags(vehicleID, vehicles.getVehicleInfo(vehicleID).intCD)

    def hasPenalties(self):
        return self.__fairplayViolations.hasPenalties()

    def getPenaltyDetails(self):
        return self.__fairplayViolations.getPenaltyDetails()


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


class _EconomicsRecordsChains(object):
    __slots__ = (b'_baseCredits', b'_premiumCredits', b'_premiumPlusCredits', b'_goldRecords', b'_additionalRecords', b'_baseXP', b'_premiumXP', b'_premiumPlusXP', b'_baseXPAdd', b'_premiumXPAdd', b'_premiumPlusXPAdd', b'_baseFreeXP', b'_premiumFreeXP', b'_premiumPlusFreeXP', b'_baseFreeXPAdd', b'_premiumFreeXPAdd', b'_premiumPlusFreeXPAdd', b'_crystal', b'_crystalDetails')

    def __init__(self):
        super(_EconomicsRecordsChains, self).__init__()
        self._baseCredits = records.RecordsIterator()
        self._premiumCredits = records.RecordsIterator()
        self._premiumPlusCredits = records.RecordsIterator()
        self._goldRecords = records.RecordsIterator()
        self._additionalRecords = records.RecordsIterator()
        self._baseXP = records.RecordsIterator()
        self._premiumXP = records.RecordsIterator()
        self._premiumPlusXP = records.RecordsIterator()
        self._baseXPAdd = records.RecordsIterator()
        self._premiumXPAdd = records.RecordsIterator()
        self._premiumPlusXPAdd = records.RecordsIterator()
        self._baseFreeXP = records.RecordsIterator()
        self._premiumFreeXP = records.RecordsIterator()
        self._premiumPlusFreeXP = records.RecordsIterator()
        self._baseFreeXPAdd = records.RecordsIterator()
        self._premiumFreeXPAdd = records.RecordsIterator()
        self._premiumPlusFreeXPAdd = records.RecordsIterator()
        self._crystal = records.RecordsIterator()
        self._crystalDetails = records.RecordsIterator()
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
        else:
            resultPremiumData = self._premiumCredits
        return itertools.izip(self._baseCredits, resultPremiumData, self._goldRecords, self._additionalRecords)

    def getCrystalRecords(self):
        return itertools.izip(self._crystal, self._crystal)

    def getCrystalDetails(self):
        return self._crystalDetails

    def getXPRecords(self, premiumType=PREMIUM_TYPE.NONE, addBonusApplied=False):
        if premiumType == PREMIUM_TYPE.NONE or premiumType & (PREMIUM_TYPE.VIP | PREMIUM_TYPE.PLUS):
            if addBonusApplied:
                secondXPData = self._premiumPlusXPAdd
                secondFreeXPData = self._premiumPlusFreeXPAdd
            else:
                secondXPData = self._premiumPlusXP
                secondFreeXPData = self._premiumPlusFreeXP
        elif addBonusApplied:
            secondXPData = self._premiumXPAdd
            secondFreeXPData = self._premiumFreeXPAdd
        else:
            secondXPData = self._premiumXP
            secondFreeXPData = self._premiumFreeXP
        if addBonusApplied:
            firstXPData = self._baseXPAdd
            firstFreeXPData = self._baseFreeXPAdd
        else:
            firstXPData = self._baseXP
            firstFreeXPData = self._baseFreeXP
        return itertools.izip(firstXPData, secondXPData, firstFreeXPData, secondFreeXPData)

    def getXPDiff(self):
        return self._premiumXP.getRecord(b'xp') - self._baseXP.getRecord(b'xp')

    def addResults(self, _, results):
        connector = ValueReplayConnector(results)
        self._addMoneyResults(connector, results)
        self._addXPResults(connector, results)
        self._addCrystalResults(connector, results)
        return

    def addAvatarResults(self, infoAvatar):
        avatarCreditsEvent = sum(creditEvent[1] for creditEvent in infoAvatar.get(b'eventCreditsList', []))
        self._baseCredits.addRecords(records.RawRecords({b'avatarCreditsEvent': avatarCreditsEvent}))
        self._premiumCredits.addRecords(records.RawRecords({b'avatarCreditsEvent': avatarCreditsEvent}))
        self._premiumPlusCredits.addRecords(records.RawRecords({b'avatarCreditsEvent': avatarCreditsEvent}))
        avatarFreeXPEvent = sum(eventFreeXP[1] for eventFreeXP in infoAvatar.get(b'eventFreeXPList', []))
        self._premiumPlusFreeXPAdd.addRecords(records.RawRecords({b'avatarFreeXPEvent': avatarFreeXPEvent}))
        self._premiumPlusFreeXP.addRecords(records.RawRecords({b'avatarFreeXPEvent': avatarFreeXPEvent}))
        self._premiumFreeXPAdd.addRecords(records.RawRecords({b'avatarFreeXPEvent': avatarFreeXPEvent}))
        self._premiumFreeXP.addRecords(records.RawRecords({b'avatarFreeXPEvent': avatarFreeXPEvent}))
        self._baseFreeXPAdd.addRecords(records.RawRecords({b'avatarFreeXPEvent': avatarFreeXPEvent}))
        self._baseFreeXP.addRecords(records.RawRecords({b'avatarFreeXPEvent': avatarFreeXPEvent}))
        crystalEvent = sum(eventCrystal[1] for eventCrystal in infoAvatar.get(b'eventCrystalList', []))
        self._crystal.addRecords(records.RawRecords({b'avatarCrystalEvent': crystalEvent}))
        self._crystalDetails.addRecords(records.RawRecords({b'avatarCrystalEvent': crystalEvent}))
        return

    def _addMoneyResults(self, connector, results):
        if b'creditsReplay' in results and results[b'creditsReplay'] is not None:
            replay = ValueReplay(connector, recordName=b'credits', replay=results[b'creditsReplay'])
            appliedPremiumCreditsFactor100Exists = b'appliedPremiumCreditsFactor100' in replay
            if appliedPremiumCreditsFactor100Exists:
                replay[b'appliedPremiumCreditsFactor100'] = FACTOR_VALUE.BASE_CREDITS_FACTOR
            self._baseCredits.addRecords(self.__buildCreditsReplayForPremType(PREMIUM_TYPE.NONE, results, replay))
            if appliedPremiumCreditsFactor100Exists:
                replay[b'appliedPremiumCreditsFactor100'] = results[b'premiumCreditsFactor100']
            self._premiumCredits.addRecords(self.__buildCreditsReplayForPremType(PREMIUM_TYPE.BASIC, results, replay))
            if appliedPremiumCreditsFactor100Exists:
                replay[b'appliedPremiumCreditsFactor100'] = results[b'premiumPlusCreditsFactor100']
            self._premiumPlusCredits.addRecords(self.__buildCreditsReplayForPremType(PREMIUM_TYPE.PLUS, results, replay))
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
            self.__updateAdditionalFactorFromReplay(replay, results, setDefault=True)
            isHighScope = RECORD_DB_IDS[(b'max15x15', b'maxXP')] in [recordID for recordID, _ in results.get(b'dossierPopUps', [])]
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseXP.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumXP.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusXP.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self.__updateAdditionalFactorFromReplay(replay, results, setDefault=hasPremiumPlus)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseXPAdd.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumXPAdd.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
            self.__updateAdditionalFactorFromReplay(replay, results, setDefault=False)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusXPAdd.addRecords(_XPReplayRecords(replay, isHighScope, results[b'achievementXP']))
        else:
            LOG_ERROR(b'XP replay is not found', results)
        if b'freeXPReplay' in results and results[b'freeXPReplay'] is not None:
            replay = ValueReplay(connector, recordName=b'freeXP', replay=results[b'freeXPReplay'])
            self.__updateAdditionalFactorFromReplay(replay, results, setDefault=True)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseFreeXP.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumFreeXP.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusFreeXP.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self.__updateAdditionalFactorFromReplay(replay, results, setDefault=hasPremiumPlus)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE)
            self._baseFreeXPAdd.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.BASIC)
            self._premiumFreeXPAdd.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
            self.__updateAdditionalFactorFromReplay(replay, results, setDefault=False)
            self.__updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.PLUS)
            self._premiumPlusFreeXPAdd.addRecords(_FreeXPReplayRecords(replay, results[b'achievementFreeXP']))
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

    @staticmethod
    def __updateAdditionalFactorFromReplay(replay, results, setDefault=False):
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

    @staticmethod
    def __updatePremiumXPFactor(replay, results, premType=PREMIUM_TYPE.NONE):
        if b'appliedPremiumXPFactor100' not in replay:
            return
        if premType == PREMIUM_TYPE.PLUS:
            replay[b'appliedPremiumXPFactor100'] = results[b'premiumPlusXPFactor100']
        elif premType == PREMIUM_TYPE.BASIC:
            replay[b'appliedPremiumXPFactor100'] = results[b'premiumXPFactor100']
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


class PersonalInfo(shared.UnpackedInfo):
    __slots__ = (b'__avatar', b'__vehicles', b'__lifeTimeInfo', b'__isObserver', b'_economicsRecords', b'__questsProgress', b'__PMProgress', b'__rankInfo', b'__isTeamKiller', b'__progressiveReward', b'__premiumMask', b'__isAddXPBonusApplied', b'__c11nProgress', b'__dogTags', b'__goldBankGain', b'__xpProgress')
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, bonusType, personal):
        super(PersonalInfo, self).__init__()
        if _RECORD.PERSONAL_AVATAR in personal and personal[_RECORD.PERSONAL_AVATAR] is not None:
            self.__avatar = PersonalAvatarInfo(bonusType, **personal[_RECORD.PERSONAL_AVATAR])
        else:
            self.__avatar = PersonalAvatarInfo(bonusType)
            self._addUnpackedItemID(_RECORD.PERSONAL_AVATAR)
        self.__vehicles = []
        self.__isObserver = False
        self.__isTeamKiller = False
        self.__premiumMask = 0
        self.__isAddXPBonusApplied = False
        self._economicsRecords = _EconomicsRecordsChains()
        self.__lifeTimeInfo = _LifeTimeInfo(False, 0)
        self.__questsProgress = {}
        self.__PMProgress = {}
        self.__c11nProgress = {}
        self.__xpProgress = {}
        self.__rankInfo = PostBattleRankInfo(0, 0, 0, 0, 0, 0, 0, 0, {}, {}, False, 0, 0)
        self.__dogTags = {}
        self.__goldBankGain = 0
        if not self.hasUnpackedItems():
            self.__collectRequiredData(personal)
        return

    @property
    def avatar(self):
        return self.__avatar

    @property
    def isObserver(self):
        return self.__isObserver

    @property
    def hasAnyPremium(self):
        return bool(self.__premiumMask & PREMIUM_TYPE.ANY)

    @property
    def isPremium(self):
        return bool(PREMIUM_TYPE.activePremium(self.__premiumMask) & PREMIUM_TYPE.BASIC)

    @property
    def isPremiumPlus(self):
        return bool(PREMIUM_TYPE.activePremium(self.__premiumMask) & PREMIUM_TYPE.PLUS)

    @property
    def isPremiumVIP(self):
        return bool(PREMIUM_TYPE.activePremium(self.__premiumMask) & PREMIUM_TYPE.VIP)

    @property
    def isAddXPBonusApplied(self):
        return self.__isAddXPBonusApplied

    @isAddXPBonusApplied.setter
    def isAddXPBonusApplied(self, state):
        self.__isAddXPBonusApplied = state
        return

    @property
    def isTeamKiller(self):
        return self.__isTeamKiller

    @property
    def xpProgress(self):
        return self.__xpProgress

    def getVehicleCDsIterator(self, result):
        for intCD in self.__vehicles:
            if intCD not in result:
                continue
            yield (
             intCD, result[intCD])

        return

    def getVehicleItemsIterator(self):
        getItemByCD = self.itemsCache.items.getItemByCD
        for intCD in self.__vehicles:
            yield (intCD, getItemByCD(intCD))

        return

    def getAchievements(self, result):
        left = []
        right = []
        for intCD in self.__vehicles:
            if intCD not in result:
                continue
            data = result[intCD]
            achievements = shared.makeAchievementFromPersonal(data)
            for direction, achievement in achievements:
                if direction == 1:
                    right.append((achievement, True))
                else:
                    left.append((achievement, True))

            achievement = shared.makeMarkOfMasteryFromPersonal(data)
            if achievement is not None:
                left.append((achievement, False))

        return (
         left, sorted(right, key=sort_keys.AchievementSortKey))

    def getLifeTimeInfo(self):
        return self.__lifeTimeInfo

    def getQuestsProgress(self):
        return self.__questsProgress

    def getDogTagsProgress(self):
        return self.__dogTags

    def getGoldBankGain(self):
        return self.__goldBankGain

    def getPMProgress(self):
        return self.__PMProgress

    def getC11nProgress(self):
        return self.__c11nProgress

    def getRankInfo(self):
        return self.__rankInfo

    def getProgressiveReward(self):
        return self.__progressiveReward

    def getBaseCreditsRecords(self):
        return self._economicsRecords.getBaseCreditsRecords()

    def getPremiumCreditsRecords(self):
        return self._economicsRecords.getPremiumCreditsRecords()

    def getCreditsDiff(self):
        return self._economicsRecords.getCreditsDiff()

    def getMoneyRecords(self):
        return self._economicsRecords.getMoneyRecords(self.__premiumMask)

    def getCrystalRecords(self):
        return self._economicsRecords.getCrystalRecords()

    def getBaseXPRecords(self):
        return self._economicsRecords.getBaseXPRecords()

    def getPremiumXPRecords(self):
        return self._economicsRecords.getPremiumXPRecords()

    def getPremiumXPAddRecords(self):
        return self._economicsRecords.getPremiumXPAddRecords()

    def getXPRecords(self):
        return self._economicsRecords.getXPRecords(self.__premiumMask, self.__isAddXPBonusApplied)

    def getXPDiff(self):
        return self._economicsRecords.getXPDiff()

    def getCrystalDetailsRecords(self):
        return self._economicsRecords.getCrystalDetails()

    def updateXPEarnings(self, extraXPData):
        vehProgress = self.__xpProgress[extraXPData.vehicleID]
        vehProgress[b'xp'] += extraXPData.extraXP
        newTankmenXp = []
        for (oldID, oldValue), (newID, newValue) in zip(vehProgress[b'xpByTmen'], extraXPData.extraTmenXP):
            newTankmenXp.append((newID, oldValue + newValue))

        vehProgress[b'xpByTmen'] = newTankmenXp
        return

    def __collectRequiredData(self, info):
        getItemByCD = self.itemsCache.items.getItemByCD
        itemCDs = [key for key in info.keys() if isinstance(key, (int, long, float))]
        items = sorted(getItemByCD(itemCD) for itemCD in itemCDs)
        lifeTimes = []
        infoAvatar = info[b'avatar']
        if infoAvatar:
            self.__questsProgress.update(infoAvatar.get(b'questsProgress', {}))
            self.__PMProgress.update(infoAvatar.get(b'PMProgress', {}))
            self.__rankInfo = PostBattleRankInfo.fromDict(infoAvatar)
            self.__progressiveReward = infoAvatar.get(b'progressiveReward')
            self.__dogTags.update(infoAvatar.get(b'dogTags', {}))
            self.__goldBankGain = infoAvatar.get(b'goldBankGain', 0)
        for item in items:
            intCD = item.intCD
            data = info[intCD]
            if data is None:
                self._addUnpackedItemID(intCD)
                continue
            self.__vehicles.append(intCD)
            self._economicsRecords.addResults(intCD, data)
            if not self.__isObserver:
                self.__isObserver = item.isObserver
            killerID = data[b'killerID'] if b'killerID' in data else 0
            lifeTime = data[b'lifeTime'] if b'lifeTime' in data else 0
            if killerID and lifeTime:
                lifeTimes.append(lifeTime)
            self.__isTeamKiller = data[b'isTeamKiller'] if b'isTeamKiller' in data else False
            self.__premiumMask = data.get(b'premMask', PREMIUM_TYPE.NONE)
            self.__questsProgress.update(data.get(b'questsProgress', {}))
            self.__PMProgress.update(data.get(b'PMProgress', {}))
            self.__c11nProgress[intCD] = data.get(b'c11nProgress', {})
            self.__xpProgress[intCD] = {b'xp': (data.get(b'xp', 0)), 
               b'xpByTmen': (data.get(b'xpByTmen', []))}

        self._economicsRecords.addAvatarResults(infoAvatar)
        if lifeTimes:
            self.__lifeTimeInfo = _LifeTimeInfo(True, min(lifeTimes))
        return
