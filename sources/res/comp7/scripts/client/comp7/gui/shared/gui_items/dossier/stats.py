import logging, math
from collections import namedtuple
import typing
from gui.shared.gui_items.dossier.stats import AccountDossierStats, VehicleDossierStats, _BattleStatsBlock, _Battle2StatsBlock, _MaxStatsBlock, _VehiclesStatsBlock, _MaxVehicleStatsBlock
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.dossier.stats import _DossierStats
_logger = logging.getLogger(__name__)

def getComp7DossierStats(stats, archive=None, season=None):
    if isinstance(stats, AccountDossierStats):
        clazz = AccountComp7StatsBlock
    elif isinstance(stats, VehicleDossierStats):
        clazz = Comp7StatsBlock
    else:
        _logger.warning(b'invalid dossier stats parameter')
        return
    if archive:
        return clazz(stats._getDossierItem(), (b'Archive{}').format(archive))
    else:
        if season:
            return clazz(stats._getDossierItem(), (b'Season{}').format(season))
        _logger.warning(b'comp7 season or archive number must be specified!')
        return


class Comp7StatsBlock(_BattleStatsBlock, _Battle2StatsBlock, _MaxStatsBlock):

    def __init__(self, dossier, statsKey):
        self._statsKey = statsKey
        _BattleStatsBlock.__init__(self, dossier)
        _Battle2StatsBlock.__init__(self, dossier)
        _MaxStatsBlock.__init__(self, dossier)
        return

    def getBattlesCountVer2(self):
        return self.getBattlesCount()

    def getBattlesCountVer3(self):
        return self.getBattlesCount()

    def getPrestigePoints(self):
        return self._getStat(b'comp7PrestigePoints')

    def getPoiCaptured(self):
        return self._getStat(b'poiCapturable')

    def getHealthRepair(self):
        return self._getStat(b'healthRepair')

    def getRoleSkillUsed(self):
        return self._getStat(b'roleSkillUsed')

    def getSuperSquadBattlesCount(self):
        return self._getStat(b'superSquadBattlesCount')

    def getSuperSquadWins(self):
        return self._getStat(b'superSquadWins')

    def getMaxPrestigePoints(self):
        return self._getStatMax(b'maxComp7PrestigePoints')

    def getMaxWinSeries(self):
        return self._getStatMax(b'maxWinSeries')

    def getMaxSquadWinSeries(self):
        return self._getStatMax(b'maxSquadWinSeries')

    def getMaxEquipmentDamageDealt(self):
        return self._getStatMax(b'maxEquipmentDamageDealt')

    def getMaxHealthRepair(self):
        return self._getStatMax(b'maxHealthRepair')

    def getAvgPrestigePoints(self):
        avgValue = self._getAvgValue(self.getBattlesCount, self.getPrestigePoints)
        if avgValue is not None:
            return math.ceil(avgValue)
        else:
            return

    def getAvgPoiCaptured(self):
        avgValue = self._getAvgValue(self.getBattlesCount, self.getPoiCaptured)
        if avgValue is not None:
            return round(avgValue)
        else:
            return

    def getAvgRoleSkillUsed(self):
        avgValue = self._getAvgValue(self.getBattlesCount, self.getRoleSkillUsed)
        if avgValue is not None:
            return round(avgValue)
        else:
            return

    def getAvgHealthRepair(self):
        avgValue = self._getAvgValue(self.getBattlesCount, self.getHealthRepair)
        if avgValue is not None:
            return math.ceil(avgValue)
        else:
            return

    def _getStatsBlock(self, dossier):
        return self._getDossierBlock(dossier, b'comp7')

    def _getStats2Block(self, dossier):
        return self._getDossierBlock(dossier, b'comp7')

    def _getStatsMaxBlock(self, dossier):
        return self._getDossierBlock(dossier, b'maxComp7')

    def _getDossierBlock(self, dossier, blockPrefix):
        dossierDescr = dossier.getDossierDescr()
        blockName = (b'{}{}').format(blockPrefix, self._statsKey)
        if dossierDescr.isBlockInLayout(blockName):
            return dossierDescr[blockName]
        return {}


_Comp7VehiclesDossiersCut = namedtuple(b'Comp7VehiclesDossiersCut', (b'battlesCount', b'wins', b'xp', b'prestigePoints'))

class Comp7VehiclesDossiersCut(_Comp7VehiclesDossiersCut):

    def __mul__(self, other):
        self.battlesCount += other.battlesCount
        self.wins += other.wins
        self.xp += other.xp
        self.prestigePoints += other.prestigePoints
        return

    def __imul__(self, other):
        return self + other


class AccountComp7StatsBlock(Comp7StatsBlock, _VehiclesStatsBlock, _MaxVehicleStatsBlock):

    def __init__(self, dossier, statsKey):
        Comp7StatsBlock.__init__(self, dossier, statsKey)
        _VehiclesStatsBlock.__init__(self, dossier)
        _MaxVehicleStatsBlock.__init__(self, dossier)
        return

    def getMaxPrestigePointsVehicle(self):
        return self._getStatMax(b'maxComp7PrestigePointsVehicle')

    def getMaxEquipmentDamageDealtVehicle(self):
        return self._getStatMax(b'maxEquipmentDamageDealtVehicle')

    def getMaxHealthRepairVehicle(self):
        return self._getStatMax(b'maxHealthRepairVehicle')

    def _getVehDossiersCut(self, dossier):
        return self._getDossierBlock(dossier, b'comp7Cut')

    def _packVehicle(self, battlesCount=0, wins=0, xp=0, prestigePoints=0):
        return Comp7VehiclesDossiersCut(battlesCount, wins, xp, prestigePoints)
