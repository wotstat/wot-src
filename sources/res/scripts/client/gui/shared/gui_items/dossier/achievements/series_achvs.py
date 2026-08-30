from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import Deprecated, Quest, NoProgressBar

class AimerAchievement(NoProgressBar, SeriesAchievement):

    def __init__(self, dossier, value=None):
        SeriesAchievement.__init__(self, b'aimer', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, b'maxAimerSeries'), (_AB.TOTAL, b'maxAimerSeries'))


class ArmorPiercerAchievement(SeriesAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ArmorPiercerAchievement, self).__init__(b'armorPiercer', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.TOTAL, b'piercingSeries'), (_AB.TOTAL, b'maxPiercingSeries'))


class DeathTrackAchievement(NoProgressBar, Quest, SeriesAchievement):

    def __init__(self, dossier, value=None):
        SeriesAchievement.__init__(self, b'deathTrack', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, b'deathTrackWinSeries'),
         (
          _AB.TOTAL, b'maxDeathTrackWinSeries'))


class DiehardAchievement(SeriesAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(DiehardAchievement, self).__init__(b'diehard', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.TOTAL, b'diehardSeries'), (_AB.TOTAL, b'maxDiehardSeries'))


class EFC2016Achievement(Quest, SeriesAchievement):

    def __init__(self, dossier, value=None):
        SeriesAchievement.__init__(self, b'EFC2016', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, b'EFC2016WinSeries'),
         (
          _AB.TOTAL, b'maxEFC2016WinSeries'))


class InvincibleAchievement(SeriesAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(InvincibleAchievement, self).__init__(b'invincible', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.TOTAL, b'invincibleSeries'), (_AB.TOTAL, b'maxInvincibleSeries'))


class HandOfDeathAchievement(SeriesAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(HandOfDeathAchievement, self).__init__(b'handOfDeath', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.TOTAL, b'killingSeries'), (_AB.TOTAL, b'maxKillingSeries'))


class RankedBattlesHeroAchievement(Quest, SeriesAchievement):

    def __init__(self, dossier, value=None):
        SeriesAchievement.__init__(self, b'rankedBattlesHero', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, b'rankedBattlesHeroProgress'), (_AB.TOTAL, b'rankedBattlesHeroProgress'))


class TacticalBreakthroughAchievement(Deprecated, SeriesAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(TacticalBreakthroughAchievement, self).__init__(b'tacticalBreakthrough', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.TEAM_7X7, b'tacticalBreakthroughSeries'),
         (
          _AB.TEAM_7X7, b'maxTacticalBreakthroughSeries'))


class TitleSniperAchievement(SeriesAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(TitleSniperAchievement, self).__init__(b'titleSniper', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.TOTAL, b'sniperSeries'), (_AB.TOTAL, b'maxSniperSeries'))


class VictoryMarchAchievement(Deprecated, NoProgressBar, SeriesAchievement):

    def __init__(self, dossier, value=None):
        super(VictoryMarchAchievement, self).__init__(b'victoryMarch', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.RATED_7X7, b'victoryMarchSeries'),
         (
          _AB.RATED_7X7, b'maxVictoryMarchSeries'))


class VictoryMarchClubAchievement(Deprecated, NoProgressBar, SeriesAchievement):

    def __init__(self, dossier, value=None):
        super(VictoryMarchClubAchievement, self).__init__(b'victoryMarch', _AB.SINGLE_7X7, dossier, value)
        return

    def _getCounterRecordNames(self):
        return (
         (
          _AB.RATED_7X7, b'victoryMarchSeries'),
         (
          _AB.RATED_7X7, b'maxVictoryMarchSeries'))


class WFC2014Achievement(Quest, SeriesAchievement):

    def __init__(self, dossier, value=None):
        SeriesAchievement.__init__(self, b'WFC2014', _AB.SINGLE, dossier, value)
        return

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, b'WFC2014WinSeries'),
         (
          _AB.TOTAL, b'maxWFC2014WinSeries'))
