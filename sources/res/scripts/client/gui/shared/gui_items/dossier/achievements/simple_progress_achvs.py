from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from gui.shared.utils.requesters import REQ_CRITERIA
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from dossiers2.custom.cache import getCache as getDossiersCache
from dossiers2.custom.collector20 import getCollector20Config
from dossiers2.custom.helpers import getCollector20Requirements
from gui.shared.gui_items.dossier.achievements.abstract import SimpleProgressAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import Deprecated, HasVehiclesList

class BeasthunterAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(BeasthunterAchievement, self).__init__(b'beasthunter', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'fragsBeast')


class BruteForceAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(BruteForceAchievement, self).__init__(b'bruteForceMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'bruteForce')


class CrucialShotAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(CrucialShotAchievement, self).__init__(b'crucialShotMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'crucialShot')


class InfiltratorAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(InfiltratorAchievement, self).__init__(b'infiltratorMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'infiltrator')


class GeniusForWarAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(GeniusForWarAchievement, self).__init__(b'geniusForWarMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'geniusForWar')


class GuerrillaAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(GuerrillaAchievement, self).__init__(b'guerrillaMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'guerrilla')


class HeavyFireAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(HeavyFireAchievement, self).__init__(b'heavyFireMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'heavyFire')


class FightingReconnaissanceAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(FightingReconnaissanceAchievement, self).__init__(b'fightingReconnaissanceMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'fightingReconnaissance')


class FireAndSteelAchievement(SimpleProgressAchievement):
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


class RangerAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(RangerAchievement, self).__init__(b'rangerMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'ranger')


class PrematureDetonationAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(PrematureDetonationAchievement, self).__init__(b'prematureDetonationMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'prematureDetonation')


class PromisingFighterAchievement(SimpleProgressAchievement):
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


class PyromaniacAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(PyromaniacAchievement, self).__init__(b'pyromaniacMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'pyromaniac')


class SentinelAchievement(SimpleProgressAchievement):
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


class WolfAmongSheepAchievement(SimpleProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(WolfAmongSheepAchievement, self).__init__(b'wolfAmongSheepMedal', _AB.TEAM_7X7, dossier, value)
        return

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'wolfAmongSheep')


class Collector20Achievement(HasVehiclesList, SimpleProgressAchievement):
    __itemsCache = dependency.descriptor(IItemsCache)
    _LIST_NAME = b'vehiclesToHaveInGarage'

    def __init__(self, name, block, dossier, value=None):
        if not self.checkIsInDossier(block, name, dossier):
            inventoryVehsCDs = set(self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | ~REQ_CRITERIA.SECRET | ~REQ_CRITERIA.HIDDEN))
            self._vehTypeCompDescrs = getCollector20Requirements(inventoryVehsCDs)
        else:
            self._vehTypeCompDescrs = set()
        SimpleProgressAchievement.__init__(self, name, block, dossier, value)
        HasVehiclesList.__init__(self)
        return

    def _getVehiclesDescrsList(self):
        return self._vehTypeCompDescrs

    def _readLevelUpTotalValue(self, dossier):
        return len(getCollector20Config())

    def _readLevelUpValue(self, dossier):
        return len(self._vehTypeCompDescrs)

    @classmethod
    def _sortKey(cls, v):
        return (v.level, v.innationID, v.nation)
