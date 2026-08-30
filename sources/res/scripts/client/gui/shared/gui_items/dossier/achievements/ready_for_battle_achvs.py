from __future__ import absolute_import
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui.shared.gui_items.dossier.achievements.abstract import ClassProgressAchievement, getCompletedPersonalMissionsCount
from nations import Alliances
from personal_missions import PM_BRANCH, PM3QType

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


class ReadyForBattleAchievement3Steps(ReadyForBattleAchievement):
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


class ReadyForBattleAllianceFranceAchievement(ReadyForBattleAchievement3Steps):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAllianceFranceAchievement, self).__init__(name=b'readyForBattleAllianceFrance', classifier=Alliances.FRANCE, branch=PM_BRANCH.PERSONAL_MISSION_2, dossier=dossier, value=value)
        return


class ReadyForBattleAllianceGermanyAchievement(ReadyForBattleAchievement3Steps):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAllianceGermanyAchievement, self).__init__(name=b'readyForBattleAllianceGermany', classifier=Alliances.GERMANY, branch=PM_BRANCH.PERSONAL_MISSION_2, dossier=dossier, value=value)
        return


class ReadyForBattleAllianceUSAAchievement(ReadyForBattleAchievement3Steps):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAllianceUSAAchievement, self).__init__(name=b'readyForBattleAllianceUSA', classifier=Alliances.USA, branch=PM_BRANCH.PERSONAL_MISSION_2, dossier=dossier, value=value)
        return


class ReadyForBattleAllianceUSSRAchievement(ReadyForBattleAchievement3Steps):
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


class ReadyForBattleAssault(ReadyForBattleAchievement3Steps):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleAssault, self).__init__(name=b'readyForBattleAssault', classifier=PM3QType.ASSAULT, branch=PM_BRANCH.PERSONAL_MISSION_3, dossier=dossier, value=value)
        return


class ReadyForBattleSniper(ReadyForBattleAchievement3Steps):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleSniper, self).__init__(name=b'readyForBattleSniper', classifier=PM3QType.SNIPER, branch=PM_BRANCH.PERSONAL_MISSION_3, dossier=dossier, value=value)
        return


class ReadyForBattleSupport(ReadyForBattleAchievement3Steps):
    __slots__ = ()

    def __init__(self, dossier, value=None):
        super(ReadyForBattleSupport, self).__init__(name=b'readyForBattleSupport', classifier=PM3QType.SUPPORT, branch=PM_BRANCH.PERSONAL_MISSION_3, dossier=dossier, value=value)
        return
