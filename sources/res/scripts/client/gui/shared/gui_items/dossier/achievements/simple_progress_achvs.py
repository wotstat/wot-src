from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from dossiers2.custom.cache import getCache as getDossiersCache
from abstract import SimpleProgressAchievement
from abstract.mixins import Deprecated, HasVehiclesList
from collections import namedtuple
from supply_shared import Supply
from items import vehicles

class BeasthunterAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(BeasthunterAchievement, self).__init__(b'beasthunter', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'fragsBeast')


class BruteForceAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(BruteForceAchievement, self).__init__(b'bruteForceMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'bruteForce')


class CrucialShotAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(CrucialShotAchievement, self).__init__(b'crucialShotMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'crucialShot')


class InfiltratorAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(InfiltratorAchievement, self).__init__(b'infiltratorMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'infiltrator')


class GeniusForWarAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(GeniusForWarAchievement, self).__init__(b'geniusForWarMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'geniusForWar')


class GuerrillaAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(GuerrillaAchievement, self).__init__(b'guerrillaMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'guerrilla')


class HeavyFireAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(HeavyFireAchievement, self).__init__(b'heavyFireMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'heavyFire')


class FightingReconnaissanceAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(FightingReconnaissanceAchievement, self).__init__(b'fightingReconnaissanceMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'fightingReconnaissance')


class FireAndSteelAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(FireAndSteelAchievement, self).__init__(b'fireAndSteelMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'fireAndSteel')


class MousebaneAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MousebaneAchievement, self).__init__(b'mousebane', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getBlock(b'vehTypeFrags').get(getDossiersCache()[b'mausTypeCompDescr'], 0)


class ReliableComradeAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReliableComradeAchievement, self).__init__(b'reliableComrade', _AB.TOTAL, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'reliableComradeSeries')


class RangerAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(RangerAchievement, self).__init__(b'rangerMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'ranger')


class PrematureDetonationAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(PrematureDetonationAchievement, self).__init__(b'prematureDetonationMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'prematureDetonation')


class PromisingFighterAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(PromisingFighterAchievement, self).__init__(b'promisingFighterMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'promisingFighter')


class PattonValleyAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(PattonValleyAchievement, self).__init__(b'pattonValley', _AB.TOTAL, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'fragsPatton')


class PyromaniacAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(PyromaniacAchievement, self).__init__(b'pyromaniacMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'pyromaniac')


class SentinelAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(SentinelAchievement, self).__init__(b'sentinelMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'sentinel')


class SinaiAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(SinaiAchievement, self).__init__(b'sinai', _AB.TOTAL, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'fragsSinai')


class TankwomenAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(TankwomenAchievement, self).__init__(b'tankwomen', _AB.SINGLE, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'tankwomenProgress')


class WolfAmongSheepAchievement(Deprecated, SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(WolfAmongSheepAchievement, self).__init__(b'wolfAmongSheepMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'wolfAmongSheep')


class SaboteurAchievement(HasVehiclesList, SimpleProgressAchievement):
    __slots__ = ()
    VehicleData = namedtuple(b'VehicleData', b'name icon')
    _LIST_NAME = b'vehiclesToKill'

    def __init__(self, dossier, value=None):
        self.__vehTypeCompDescrs = self._getSuppliesList(dossier)
        SimpleProgressAchievement.__init__(self, b'saboteur', _AB.EPIC_BATTLE, dossier, value)
        HasVehiclesList.__init__(self)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.EPIC_BATTLE, b'saboteurProgress')

    def _getVehiclesDescrsList(self):
        return self.__vehTypeCompDescrs

    def _getSuppliesList(self, dossier):
        suppliesList = []
        displayOrderSupplies = [
         Supply.PILLBOX, Supply.FLAMER, Supply.MORTAR, Supply.AIRSHIP]
        allSupplies = getDossiersCache()[b'vehiclesByTag'].get(b'supply', set())
        killedSupplies = set()
        if dossier:
            killedSupplies = set(dossier.getBlock(b'vehTypeFrags').iterkeys())
        leftKilledSupplies = allSupplies - killedSupplies
        for supplyID in displayOrderSupplies:
            for supply in leftKilledSupplies:
                if Supply.SUPPLY_ID_TO_TAG[supplyID] in vehicles.getItemByCompactDescr(supply).tags:
                    suppliesList.append(supply)
                    break

        return suppliesList

    def getVehiclesData(self):
        result = []
        for vCD in self._getVehiclesDescrsList():
            vehicle = self.itemsCache.items.getItemByCD(vCD)
            result.append(self.VehicleData(vehicle.userName, vehicle.iconSmall))

        return [i._asdict() for i in result]
