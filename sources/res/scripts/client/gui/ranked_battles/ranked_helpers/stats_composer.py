from collections import namedtuple
import time, typing
from gui.ranked_battles.constants import RankedDossierKeys, ARCHIVE_SEASON_ID, ZERO_DIVISION_ID
from helpers import dependency
from skeletons.gui.shared import IItemsCache
EfficiencyStamp = namedtuple(b'EfficiencyStamp', b'efficiency, time')

class RankedBattlesStatsComposer(object):
    itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = (b'__settings', b'__currentSeason')

    def __init__(self, settings, currentSeason):
        super(RankedBattlesStatsComposer, self).__init__()
        self.__settings = settings
        self.__currentSeason = currentSeason
        return

    @property
    def amountBattles(self):
        return self.__getSeasonDossier().getBattlesCount()

    @property
    def amountBattlesInLeagues(self):
        result = 0
        if self.divisionsStats is not None and self.__settings is not None and self.amountBattles is not None:
            for divisionID, division in self.__settings.divisions.iteritems():
                if not division[b'isLeague']:
                    result += self.divisionsStats.get(divisionID, {}).get(b'battles', 0)

            result = max(0, self.amountBattles - result)
        else:
            result = None
        return result

    @property
    def amountSteps(self):
        return self.__getSeasonDossier().getStepsCount()

    @property
    def amountStepsInLeagues(self):
        if self.divisionsStats is not None and self.amountSteps is not None:
            result = 0
            for divisionID, division in self.__settings.divisions.iteritems():
                if division[b'isLeague']:
                    result += self.divisionsStats.get(divisionID, {}).get(b'rankChanges', 0)

        else:
            result = None
        return result

    @property
    def bonusBattlesCount(self):
        return self.itemsCache.items.ranked.persistentBonusBattles + self.itemsCache.items.ranked.dailyBonusBattles

    @property
    def persistentBonusBattles(self):
        return self.itemsCache.items.ranked.persistentBonusBattles

    @property
    def dailyBonusBattles(self):
        return self.itemsCache.items.ranked.dailyBonusBattles

    @property
    def dailyBonusBattlesIncome(self):
        steps = self.divisionsStats.get(ZERO_DIVISION_ID, {}).get(b'stepsCount', 0)
        settings = self.__settings.leaguesBonusBattles
        bonusBattles = {item[b'battlesCount']: item[b'steps'] for item in settings if item[b'steps'] <= steps}
        return max(bonusBattles or (0,))

    @property
    def cachedSeasonEfficiency(self):
        efficiencyStamp = self.itemsCache.items.ranked.seasonEfficiencyStamp
        efficiency = efficiencyStamp.get(b'efficiency', self.currentSeasonEfficiency.efficiency)
        timeStamp = efficiencyStamp.get(b'timestamp', time.time())
        return EfficiencyStamp(efficiency, timeStamp)

    @property
    def currentSeasonEfficiency(self):
        return EfficiencyStamp(self.__getSeasonDossier().getStepsEfficiency(), time.time())

    @property
    def currentSeasonEfficiencyDiff(self):
        result = None
        if self.currentSeasonEfficiency.efficiency is not None and self.cachedSeasonEfficiency.efficiency is not None:
            result = self.currentSeasonEfficiency.efficiency - self.cachedSeasonEfficiency.efficiency
        return result

    @property
    def divisionsStats(self):
        return self.itemsCache.items.ranked.divisionsStats

    @property
    def hasSettings(self):
        return self.__settings is not None

    def clear(self):
        self.__settings = None
        self.__currentSeason = None
        return

    def getDivisionEfficiencyPercent(self, divisionsID):
        currentDivisionEfficiency = None
        if self.divisionsStats is not None:
            currentDivisionStats = self.divisionsStats.get(divisionsID)
            if currentDivisionStats:
                rankChanges = currentDivisionStats.get(b'rankChanges', 0)
                battles = currentDivisionStats.get(b'battles', 0)
                if battles:
                    currentDivisionEfficiency = rankChanges / float(battles)
        return currentDivisionEfficiency

    def __getSeasonDossier(self):
        seasonKey = RankedDossierKeys.ARCHIVE
        seasonID = ARCHIVE_SEASON_ID
        if self.__currentSeason is not None:
            seasonKey = RankedDossierKeys.SEASON % self.__currentSeason.getNumber()
            seasonID = self.__currentSeason.getSeasonID()
        return self.itemsCache.items.getAccountDossier().getSeasonRankedStats(seasonKey, seasonID)
