from abstract import ClassProgressAchievement, getCompletedPersonalMissionsCount
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from nations import Alliances
from personal_missions import PM_BRANCH

class ReadyForBattleAchievement(ClassProgressAchievement):
    __slots__ = (b'__name', b'__classifier', b'__branch', b'__isCurrentUserAchievement')

    def __init__(self, name, classifier, branch, dossier, value=None):
        self.__name = name
        self.__classifier = classifier
        self.__branch = branch
        self.__isCurrentUserAchievement = dossier.isCurrentUser() if dossier is not None else False
        super(ReadyForBattleAchievement, self).__init__(self.__name, _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return (
         b'questsLeft',
         self._lvlUpValue if self.__isCurrentUserAchievement else 0)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, self.__name)

    def _readCurrentProgressValue(self, dossier):
        return getCompletedPersonalMissionsCount(self.__branch, {self.__classifier})


class ReadyForBattleAchievementSeason2(ReadyForBattleAchievement):
    __slots__ = ()
    MIN_LVL = 3
    NO_LVL = 4


class ReadyForBattleALLAchievement(ReadyForBattleAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleALLAchievement, self).__init__(name=b'readyForBattleALL', classifier=b'battleHeroes', branch=0, dossier=dossier, value=value)
        return

    def _readCurrentProgressValue(self, dossier):
        return 0


class ReadyForBattleAllianceFranceAchievement(ReadyForBattleAchievementSeason2):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAllianceFranceAchievement, self).__init__(name=b'readyForBattleAllianceFrance', classifier=Alliances.FRANCE, branch=PM_BRANCH.PERSONAL_MISSION_2, dossier=dossier, value=value)
        return


class ReadyForBattleAllianceGermanyAchievement(ReadyForBattleAchievementSeason2):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAllianceGermanyAchievement, self).__init__(name=b'readyForBattleAllianceGermany', classifier=Alliances.GERMANY, branch=PM_BRANCH.PERSONAL_MISSION_2, dossier=dossier, value=value)
        return


class ReadyForBattleAllianceUSAAchievement(ReadyForBattleAchievementSeason2):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAllianceUSAAchievement, self).__init__(name=b'readyForBattleAllianceUSA', classifier=Alliances.USA, branch=PM_BRANCH.PERSONAL_MISSION_2, dossier=dossier, value=value)
        return


class ReadyForBattleAllianceUSSRAchievement(ReadyForBattleAchievementSeason2):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAllianceUSSRAchievement, self).__init__(name=b'readyForBattleAllianceUSSR', classifier=Alliances.USSR, branch=PM_BRANCH.PERSONAL_MISSION_2, dossier=dossier, value=value)
        return


class ReadyForBattleATSPGAchievement(ReadyForBattleAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleATSPGAchievement, self).__init__(name=b'readyForBattleATSPG', classifier=b'AT-SPG', branch=PM_BRANCH.REGULAR, dossier=dossier, value=value)
        return


class ReadyForBattleHTAchievement(ReadyForBattleAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleHTAchievement, self).__init__(name=b'readyForBattleHT', classifier=b'heavyTank', branch=PM_BRANCH.REGULAR, dossier=dossier, value=value)
        return


class ReadyForBattleLTAchievement(ReadyForBattleAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleLTAchievement, self).__init__(name=b'readyForBattleLT', classifier=b'lightTank', branch=PM_BRANCH.REGULAR, dossier=dossier, value=value)
        return


class ReadyForBattleMTAchievement(ReadyForBattleAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleMTAchievement, self).__init__(name=b'readyForBattleMT', classifier=b'mediumTank', branch=PM_BRANCH.REGULAR, dossier=dossier, value=value)
        return


class ReadyForBattleSPGAchievement(ReadyForBattleAchievement):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleSPGAchievement, self).__init__(name=b'readyForBattleSPG', classifier=b'SPG', branch=PM_BRANCH.REGULAR, dossier=dossier, value=value)
        return
