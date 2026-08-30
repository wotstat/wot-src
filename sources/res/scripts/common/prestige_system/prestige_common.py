from __future__ import absolute_import
import typing
from constants import IS_CLIENT
from prestige_system import getCache, computePrestigeCache
if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional
PrestigeGrade = typing.NamedTuple(b'_PrestigeGrade', (
 (
  b'level', int),
 (
  b'prestigeMarkID', int),
 (
  b'main', bool)))

class PrestigeConfig(object):

    class GradeKeys(object):
        LEVEL = b'level'
        MARK_ID = b'prestigeMarkID'
        MAIN = b'main'

    def __init__(self, config):
        self._config = config
        if IS_CLIENT:
            self.__cache = {}
            if self._config:
                computePrestigeCache(self._config, self.__cache)
        else:
            self.__cache = getCache()
        return

    @property
    def isEnabled(self):
        return self._config.get(b'enabled', False)

    @property
    def prestigeCoefficient(self):
        return self._config.get(b'prestigeCoefficient', 0)

    @property
    def prestigePoints(self):
        return self.__cache.get(b'prestigePoints', {})

    @property
    def defaultMaxLevel(self):
        return self._config.get(b'default', {}).get(b'maxLevel', 0)

    @property
    def grades(self):
        return self._config.get(b'grades', [])

    def getSortedGrades(self, key=GradeKeys.LEVEL):
        return [PrestigeGrade(**g) for g in sorted(self.grades, key=(lambda v: v.get(key)))]

    def getSortedMainGrades(self, key=GradeKeys.LEVEL):
        return [PrestigeGrade(**g) for g in sorted(self.grades, key=(lambda v: v.get(key))) if g.get(self.GradeKeys.MAIN, False)]

    def getVehiclePoints(self, vehCD):
        return self.prestigePoints.get(vehCD)
