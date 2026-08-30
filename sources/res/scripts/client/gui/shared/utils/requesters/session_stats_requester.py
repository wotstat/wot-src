from collections import namedtuple
import BigWorld
from adisp import adisp_async
from constants import ARENA_BONUS_TYPE
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.shared.utils.requesters import IRandomAccountStats, IRandomVehStats, ISessionStatsRequester
ValueWithDelta = namedtuple(b'ValueWithDelta', [b'value', b'delta'])
RatioValue = namedtuple(b'RatioValue', [b'ratio', b'dealt', b'received'])
CreditsDetails = namedtuple(b'CreditsDetails', [
 17, 18, 19, 20, 21, 22, 
 23, 24, 25, 26, 27, 28])
CrystalDetails = namedtuple(b'CrystalDetails', [b'base', b'achievement', b'event', b'autoEquip'])

class _StatKind(object):
    DAY_STAT = b'dayStat'
    VEHICLE_DAY_STAT = b'vehDayStat'


class BaseStats(object):

    def __init__(self, data):
        super(BaseStats, self).__init__()
        self.data = data
        return

    @property
    def battleCnt(self):
        return self.data.get(b'battle_cnt', {}).get(b'value', None)

    @property
    def incomeCredits(self):
        return self.data.get(b'income_credits', {}).get(b'value', None)

    @property
    def xp(self):
        return self.data.get(b'xp', {}).get(b'value', None)

    @property
    def incomeCrystal(self):
        return self.data.get(b'income_crystal', {}).get(b'value', None)

    @property
    def freeXP(self):
        return self.data.get(b'freeXP', {}).get(b'value', None)

    @property
    def averageXp(self):
        return ValueWithDelta(self.data.get(b'average_xp', {}).get(b'value', (None, None))[0], self.data.get(b'average_xp', {}).get(b'diff', None))

    @property
    def ratioDamage(self):
        ratio, dealt, received = self.data.get(b'ratio_damage', {}).get(b'value', (None, None, None))
        return ValueWithDelta(value=RatioValue(ratio, dealt, received), delta=self.data.get(b'ratio_damage', {}).get(b'diff', None))

    @property
    def helpDamage(self):
        return ValueWithDelta(value=self.data.get(b'help_damage', {}).get(b'value', (None, None))[0], delta=self.data.get(b'help_damage', {}).get(b'diff', None))

    @property
    def ratioKill(self):
        ratio, dealt, received = self.data.get(b'ratio_kill', {}).get(b'value', (None, None, None))
        return ValueWithDelta(value=RatioValue(ratio, dealt, received), delta=self.data.get(b'ratio_kill', {}).get(b'diff', None))

    @property
    def averageDamage(self):
        return ValueWithDelta(value=self.data.get(b'average_damage', {}).get(b'value', (None, None))[0], delta=self.data.get(b'average_damage', {}).get(b'diff', None))

    @property
    def blockedDamage(self):
        return ValueWithDelta(value=self.data.get(b'blocked_damage', {}).get(b'value', (None, None))[0], delta=self.data.get(b'blocked_damage', {}).get(b'diff', None))

    @property
    def winRate(self):
        ratio, dealt, received = self.data.get(b'winner_ratio', {}).get(b'value', (None, None, None))
        return ValueWithDelta(value=RatioValue(ratio, dealt, received), delta=self.data.get(b'winner_ratio', {}).get(b'diff', None))

    @property
    def wins(self):
        return ValueWithDelta(value=self.data.get(b'winner_ratio', {}).get(b'value', (None, None, None))[1], delta=None)

    @property
    def averageFrags(self):
        return self.data.get(b'average_frags', {}).get(b'value', (None, None))[0]

    @property
    def survivedRatio(self):
        ratio, dealt, received = self.data.get(b'survived_rate', {}).get(b'value', (None, None, None))
        return ValueWithDelta(value=RatioValue(ratio, dealt, received), delta=self.data.get(b'survived_rate', {}).get(b'diff', None))

    @property
    def spotted(self):
        return ValueWithDelta(value=self.data.get(b'spotted', {}).get(b'value', (None, None))[0], delta=self.data.get(b'spotted', {}).get(b'diff', None))

    @property
    def netCredits(self):
        return self.data.get(b'net_credits', {}).get(b'value', None)

    @property
    def netCrystal(self):
        return self.data.get(b'net_crystal', {}).get(b'value', None)


class BaseAccountStats(BaseStats):

    @property
    def creditsDetails(self):
        replayCreditsData = self.data.get(b'credits_replay', {})
        data = self.data.get(b'credits_to_draw', {}).get(b'value', 0)
        creditsToDraw = data if data is not None else 0
        data = self.data.get(b'achievement_credits', {}).get(b'value', 0)
        achievementCredits = data if data is not None else 0
        return CreditsDetails(base=replayCreditsData.get(b'originalCredits', 0) + self._sumRecords(replayCreditsData, b'appliedPremiumCreditsFactor') - creditsToDraw - achievementCredits, noPenalty=self.data.get(b'achievement_credits', {}).get(b'value', 0), boosters=replayCreditsData.get(b'boosterCredits', 0) + replayCreditsData.get(b'boosterCreditsFactor100', 0), event=self._sumRecords(replayCreditsData, b'eventCreditsList_', b'eventCreditsFactor100List_'), battlePayments=replayCreditsData.get(b'orderCreditsFactor100', 0), friendlyFirePenalty=replayCreditsData.get(b'originalCreditsPenalty', 0) + replayCreditsData.get(b'originalCreditsContributionOut', 0) + replayCreditsData.get(b'originalCreditsPenaltySquad', 0) + replayCreditsData.get(b'originalCreditsContributionOutSquad', 0), friendlyFireCompensation=replayCreditsData.get(b'originalCreditsContributionIn', 0) + replayCreditsData.get(b'originalCreditsContributionInSquad', 0), aogasFactor=replayCreditsData.get(b'aogasFactor10', 0), autoRepair=self.data.get(b'auto_repair_cost_credits', {}).get(b'value', 0), autoLoad=self.data.get(b'auto_load_cost_credits', {}).get(b'value', 0), autoEquip=self.data.get(b'auto_equip_cost_credits', {}).get(b'value', 0), squadBonus=replayCreditsData.get(b'originalPremSquadCredits', 0) + replayCreditsData.get(b'premSquadCreditsFactor100', 0) + replayCreditsData.get(b'originalCreditsToDrawSquad', 0))

    @property
    def crystalDetails(self):
        replayCrystalData = self.data.get(b'crystals_replay', {})
        return CrystalDetails(base=replayCrystalData.get(b'originalCrystal', 0), achievement=self._sumRecords(replayCrystalData, b'eventCrystalList_'), event=0, autoEquip=self.data.get(b'auto_equip_cost_crystal', {}).get(b'value', 0))

    @property
    def averageVehicleLevel(self):
        return self.data.get(b'average_level', {}).get(b'value', (None, None))[0]

    @staticmethod
    def _sumRecords(data, *startWithStrings):
        result = 0
        for key, val in data.iteritems():
            if key.startswith(startWithStrings):
                result += val

        return result


class BaseVehicleStats(BaseStats):
    pass


class RandomAccountStats(BaseAccountStats, IRandomAccountStats):

    @property
    def wtr(self):
        return ValueWithDelta(value=self.data.get(b'wtr', {}).get(b'value', None), delta=self.data.get(b'wtr', {}).get(b'diff', None))


class RandomVehStats(BaseVehicleStats, IRandomVehStats):

    @property
    def wtr(self):
        return ValueWithDelta(value=self.data.get(b'wtr', {}).get(b'value', None), delta=self.data.get(b'wtr', {}).get(b'diff', None))


_ARENA_TYPE_TO_RETURN_CLASS_MAP = {(ARENA_BONUS_TYPE.REGULAR): (
                              RandomAccountStats, RandomVehStats)}

class SessionStatsRequester(AbstractSyncDataRequester, ISessionStatsRequester):
    settingsCore = dependency.descriptor(ISettingsCore)

    def getAccountStats(self, arenaType):
        return self.__getStats(arenaType, statsKind=_StatKind.DAY_STAT, isVehStats=False)

    def getVehiclesStats(self, arenaType, vehId):
        return self.__getStats(arenaType, statsKind=_StatKind.VEHICLE_DAY_STAT, isVehStats=True, vehicleId=vehId)

    def getStatsVehList(self, arenaType):
        statsDictData = self.getCacheValue(b'sessionStats', {})
        return statsDictData.get(arenaType, {}).get(_StatKind.VEHICLE_DAY_STAT, {}).keys()

    def getAccountWtr(self):
        return self.getCacheValue(b'wtr', {}).get(b'wtr_general', None)

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().sessionStats.getCache((lambda res_id, value: self._response(res_id, value, callback)))
        return

    def __getStats(self, arenaType, statsKind=_StatKind.DAY_STAT, isVehStats=False, vehicleId=None):
        statsDictData = self.getCacheValue(b'sessionStats', {})
        statsDictData = statsDictData.get(arenaType, {})
        wtr = self.__getWtr(statsDictData, arenaType, statsKind, vehicleId)
        outputDict = statsDictData.get(statsKind, {}).copy()
        if statsKind is _StatKind.VEHICLE_DAY_STAT:
            outputDict = outputDict.get(vehicleId, {})
        outputDict.update(wtr)
        mapTupleIndex = 1 if isVehStats else 0
        return _ARENA_TYPE_TO_RETURN_CLASS_MAP[arenaType][mapTupleIndex](outputDict)

    @staticmethod
    def __getWtr(data, arenaType, statsKind, vehicleId=None):
        if arenaType == ARENA_BONUS_TYPE.REGULAR:
            buff = data.get(b'wtrDayStat', {b'value': None, b'diff': None})
            if statsKind == _StatKind.VEHICLE_DAY_STAT:
                buff = buff.get(b'wtrForVeh', {}).get(vehicleId, {b'value': None, b'diff': None})
            return {b'wtr': {b'value': (buff.get(b'value', None)), b'diff': (buff.get(b'diff', None))}}
        else:
            return {}
