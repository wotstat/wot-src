from __future__ import absolute_import
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui.shared.gui_items.dossier.achievements import validators
from gui.shared.gui_items.dossier.achievements.abstract import ClassProgressAchievement
from gui.shared.gui_items.dossier.achievements.abstract.mixins import Deprecated, Fortification, NoProgressBar

class BattleTestedAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(BattleTestedAchievement, self).__init__(b'battleTested', _AB.TEAM_7X7, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'achievesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'battleTested')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'awardCount')


class GuardsmanAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value=None):
        ClassProgressAchievement.__init__(self, b'guardsman', _AB.HISTORICAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.HISTORICAL, b'guardsman')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.HISTORICAL, b'weakVehiclesWins')


class ForTacticalOperationsAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ForTacticalOperationsAchievement, self).__init__(b'forTacticalOperations', _AB.TEAM_7X7, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, b'forTacticalOperations')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getTeam7x7Stats().getWinsCount()


class MarkI100Years(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MarkI100Years, self).__init__(b'markI100Years', _AB.TOTAL, dossier, value)
        return

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)


class MakerOfHistoryAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value=None):
        ClassProgressAchievement.__init__(self, b'makerOfHistory', _AB.HISTORICAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'pairWinsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.HISTORICAL, b'makerOfHistory')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.HISTORICAL, b'bothSidesWins')


class MedalAbramsAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalAbramsAchievement, self).__init__(b'medalAbrams', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'battlesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalAbrams')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getWinAndSurvived() + dossier.getTeam7x7Stats().getWinAndSurvived() + dossier.getFortBattlesStats().getWinAndSurvived() + dossier.getFortSortiesStats().getWinAndSurvived() + dossier.getGlobalMapStats().getWinAndSurvived()


class MedalCariusAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalCariusAchievement, self).__init__(b'medalCarius', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalCarius')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getFragsCount() - dossier.getClanStats().getFragsCount() + dossier.getTeam7x7Stats().getFragsCount() + dossier.getFortBattlesStats().getFragsCount() + dossier.getFortSortiesStats().getFragsCount() + dossier.getGlobalMapStats().getFragsCount()


class MedalEkinsAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalEkinsAchievement, self).__init__(b'medalEkins', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalEkins')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getFrags8p() + dossier.getTeam7x7Stats().getFrags8p() + dossier.getFortBattlesStats().getFrags8p() + dossier.getFortSortiesStats().getFrags8p() + dossier.getGlobalMapStats().getFrags8p()


class MedalKayAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalKayAchievement, self).__init__(b'medalKay', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'heroesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalKay')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'battleHeroes')


class MedalKnispelAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalKnispelAchievement, self).__init__(b'medalKnispel', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'damageLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalKnispel')

    def _readCurrentProgressValue(self, dossier):
        random = dossier.getRandomStats()
        clans = dossier.getClanStats()
        fortBattles = dossier.getFortBattlesStats()
        fortSorties = dossier.getFortSortiesStats()
        globalMap = dossier.getGlobalMapStats()
        return random.getDamageDealt() + random.getDamageReceived() - (clans.getDamageDealt() + clans.getDamageReceived()) + dossier.getTeam7x7Stats().getDamageDealt() + dossier.getTeam7x7Stats().getDamageReceived() + fortBattles.getDamageDealt() + fortBattles.getDamageReceived() + fortSorties.getDamageDealt() + fortSorties.getDamageReceived() + globalMap.getDamageDealt() + globalMap.getDamageReceived()


class MedalLavrinenkoAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalLavrinenkoAchievement, self).__init__(b'medalLavrinenko', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'dropPointsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalLavrinenko')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getDroppedCapturePoints() - dossier.getClanStats().getDroppedCapturePoints() + dossier.getTeam7x7Stats().getDroppedCapturePoints() + dossier.getFortBattlesStats().getDroppedCapturePoints() + dossier.getFortSortiesStats().getDroppedCapturePoints() + dossier.getGlobalMapStats().getDroppedCapturePoints()


class MedalLeClercAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalLeClercAchievement, self).__init__(b'medalLeClerc', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'capturePointsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalLeClerc')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getCapturePoints() - dossier.getClanStats().getCapturePoints() + dossier.getTeam7x7Stats().getCapturePoints() + dossier.getFortBattlesStats().getCapturePoints() + dossier.getFortSortiesStats().getCapturePoints() + dossier.getGlobalMapStats().getCapturePoints()


class MedalPoppelAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalPoppelAchievement, self).__init__(b'medalPoppel', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'medalPoppel')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRandomStats().getSpottedEnemiesCount() - dossier.getClanStats().getSpottedEnemiesCount() + dossier.getTeam7x7Stats().getSpottedEnemiesCount() + dossier.getFortBattlesStats().getSpottedEnemiesCount() + dossier.getFortSortiesStats().getSpottedEnemiesCount() + dossier.getGlobalMapStats().getSpottedEnemiesCount()


class MedalRotmistrovAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(MedalRotmistrovAchievement, self).__init__(b'medalRotmistrov', _AB.CLAN, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'battlesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.CLAN, b'medalRotmistrov')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getGlobalMapStats().getBattlesCount()


class RankedStayingPowerAchievement(ClassProgressAchievement):
    __slots__ = ()
    __ACHIEVEMENT_NAME = b'rankedStayingPower'
    __ACHIEVEMENT_COUNTER = b'rankedStayingCounter'
    __DEFAULT_LEVEL = 0

    def __init__(self, dossier, value=None):
        ClassProgressAchievement.__init__(self, self.__ACHIEVEMENT_NAME, _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'stepsLeft', self._lvlUpValue)

    def _readValue(self, dossier):
        return self.__getLvlValue(dossier)

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, self.__ACHIEVEMENT_COUNTER)

    @classmethod
    def checkIsInDossier(cls, block, name, dossier):
        if dossier is not None:
            return cls.__getLvlValue(dossier) > cls.__DEFAULT_LEVEL
        else:
            return False

    def _readProgressValue(self, dossier):
        return self.__getLvlValue(dossier)

    @classmethod
    def __getLvlValue(cls, dossier):
        return dossier.getRecordValue(_AB.TOTAL, cls.__ACHIEVEMENT_NAME)


class RankedDivisionFighterAchievement(ClassProgressAchievement):
    __slots__ = ()
    __ACHIEVEMENT_NAME = b'rankedDivisionFighter'
    __ACHIEVEMENT_COUNTER = b'rankedDivisionCounter'
    __DEFAULT_LEVEL = 0

    def __init__(self, dossier, value=None):
        ClassProgressAchievement.__init__(self, self.__ACHIEVEMENT_NAME, _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'battlesLeft', self._lvlUpValue)

    def _readValue(self, dossier):
        return self.__getLvlValue(dossier)

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, self.__ACHIEVEMENT_COUNTER)

    @classmethod
    def checkIsInDossier(cls, block, name, dossier):
        if dossier is not None:
            return cls.__getLvlValue(dossier) > cls.__DEFAULT_LEVEL
        else:
            return False

    def _readProgressValue(self, dossier):
        return self.__getLvlValue(dossier)

    @classmethod
    def __getLvlValue(cls, dossier):
        return dossier.getRecordValue(_AB.TOTAL, cls.__ACHIEVEMENT_NAME)


class ReferralProgramClassAchievement(ClassProgressAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReferralProgramClassAchievement, self).__init__(b'RP2018sergeant', _AB.TOTAL, dossier, value)
        return

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.requiresReferralProgram() or validators.alreadyAchieved(cls, name, block, dossier)

    def getNextLevelInfo(self):
        return (
         b'recruitsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'RP2018sergeant')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, b'RP2018sergeantCounter')


class SoldierOfFortuneAchievement(Fortification, ClassProgressAchievement):

    def __init__(self, dossier, value=None):
        ClassProgressAchievement.__init__(self, b'soldierOfFortune', _AB.FORT, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FORT, b'soldierOfFortune')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFortSortiesStats().getWinsCount()


class StormLordAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value=None):
        super(StormLordAchievement, self).__init__(b'stormLord', _AB.FALLOUT, dossier, value)
        return

    def getNextLevelInfo(self):
        return (
         b'vehiclesLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FALLOUT, b'stormLord')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFalloutStats().getConsumablesFragsCount()


class StrategicOperationsAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value=None):
        super(StrategicOperationsAchievement, self).__init__(b'strategicOperations', _AB.RATED_7X7, dossier, value)
        return

    def getNextLevelInfo(self):
        return (b'winsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.RATED_7X7, b'strategicOperations')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getTotalStats().getWinsCount()


class WinnerLaurelsAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value=None):
        super(WinnerLaurelsAchievement, self).__init__(b'winnerLaurels', _AB.FALLOUT, dossier, value)
        return

    def getNextLevelInfo(self):
        return (
         b'winPointsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FALLOUT, b'winnerLaurels')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFalloutStats().getVictoryPoints()
