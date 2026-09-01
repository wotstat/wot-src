from __future__ import absolute_import
from gui.shared.utils.decorators import ReprInjector
from fall_tanks.gui.battle_control.arena_info.interfaces import IFallTanksVehicleInfo
_DEFAULT_CHECKPOINT = -1
_DEFAULT_RACE_POSITION = 0
_DEFAULT_FINISH_TIME = 0.0
_DEFAULT_FRAGS_COUNT = 0
_DEFAULT_IS_LEAVER = False

class FallTanksKeys(object):
    CHECKPOINT = b'checkpoint'
    RACE_POSITION = b'racePosition'
    FINISH_TIME = b'finishTime'
    IS_LEAVER = b'isLeaver'

    @classmethod
    def getSortingKeys(cls, static=True):
        if static:
            return cls._getStaticSortingKeys()
        return cls._getDynamicSortingKeys()

    @classmethod
    def getKeys(cls, static=True):
        if static:
            return cls._getStaticKeys()
        return cls._getDynamicKeys()

    @classmethod
    def _getDynamicKeys(cls):
        return [
         (
          cls.CHECKPOINT, _DEFAULT_CHECKPOINT),
         (
          cls.RACE_POSITION, _DEFAULT_RACE_POSITION),
         (
          cls.FINISH_TIME, _DEFAULT_FINISH_TIME),
         (
          cls.IS_LEAVER, _DEFAULT_IS_LEAVER)]

    @classmethod
    def _getDynamicSortingKeys(cls):
        return [cls.RACE_POSITION]

    @classmethod
    def _getStaticKeys(cls):
        return []

    @classmethod
    def _getStaticSortingKeys(cls):
        return []


@ReprInjector.simple(b'isPlayerVehicle', b'frags', b'racePosition', b'checkpoint', b'isFinished', b'finishTime')
class FallTanksVehicleInfo(IFallTanksVehicleInfo):
    __slots__ = (b'__isPlayerVehicle', b'__checkpoint', b'__finishTime', b'__racePosition', b'__frags')

    def __init__(self, isPlayerVehicle=True, checkpoint=_DEFAULT_CHECKPOINT, finishTime=_DEFAULT_FINISH_TIME, racePosition=_DEFAULT_RACE_POSITION, frags=_DEFAULT_FRAGS_COUNT):
        self.__isPlayerVehicle = isPlayerVehicle
        self.__checkpoint = checkpoint
        self.__finishTime = finishTime
        self.__racePosition = racePosition
        self.__frags = frags
        return

    @property
    def isFinished(self):
        return self.__finishTime > 0.0

    @property
    def isPlayerVehicle(self):
        return self.__isPlayerVehicle

    @property
    def isPlayerVehicleInRace(self):
        return self.isPlayerVehicle and self.__racePosition and not self.isFinished

    @property
    def checkpoint(self):
        return self.__checkpoint

    @property
    def finishTime(self):
        return self.__finishTime

    @property
    def frags(self):
        return self.__frags

    @property
    def racePosition(self):
        return self.__racePosition
