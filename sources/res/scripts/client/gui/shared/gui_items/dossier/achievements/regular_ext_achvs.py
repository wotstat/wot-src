from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import RegularExtAchievement
from abstract.mixins import NoProgressBar
from arena_achievements import ACHIEVEMENT_CONDITIONS, ACHIEVEMENT_CONDITIONS_EXT

class HeroesOfRassenayAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, b'heroesOfRassenay', _AB.TOTAL, dossier, value)
        return

    def _getStandardValues(self):
        return ACHIEVEMENT_CONDITIONS[self._getActualName()][b'minKills']

    def _getExtValues(self):
        return ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()][b'minKills']


class MedalLafayettePoolAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, b'medalLafayettePool', _AB.TOTAL, dossier, value)
        return

    def _getStandardValues(self):
        return str(ACHIEVEMENT_CONDITIONS[self._getActualName()][b'minKills']) + b'-' + str(ACHIEVEMENT_CONDITIONS[self._getActualName()][b'maxKills'])

    def _getExtValues(self):
        return str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()][b'minKills']) + b'-' + str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()][b'maxKills'])


class MedalRadleyWaltersAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, b'medalRadleyWalters', _AB.TOTAL, dossier, value)
        return

    def _getStandardValues(self):
        return str(ACHIEVEMENT_CONDITIONS[self._getActualName()][b'minKills']) + b'-' + str(ACHIEVEMENT_CONDITIONS[self._getActualName()][b'maxKills'])

    def _getExtValues(self):
        return str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()][b'minKills']) + b'-' + str(ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()][b'maxKills'])


class WarriorAchievement(NoProgressBar, RegularExtAchievement):

    def __init__(self, dossier, value=None):
        RegularExtAchievement.__init__(self, b'warrior', _AB.TOTAL, dossier, value)
        return

    def _getStandardValues(self):
        return ACHIEVEMENT_CONDITIONS[self._getActualName()][b'minFrags']

    def _getExtValues(self):
        return ACHIEVEMENT_CONDITIONS_EXT[self._getActualName()][b'minFrags']
