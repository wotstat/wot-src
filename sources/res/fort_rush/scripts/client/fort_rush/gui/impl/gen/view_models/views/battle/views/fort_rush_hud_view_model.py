from enum import Enum
from frameworks.wulf import Array, Map, ViewModel
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_base_capture_indicator_model import FortRushHudBaseCaptureIndicatorModel
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_base_marker_model import FortRushHudBaseMarkerModel
from fort_rush.gui.impl.gen.view_models.views.battle.views.fort_rush_hud_team_unit_model import FortRushHudTeamUnitModel

class AnnouncementTypeEnum(Enum):
    NONE = b'none'
    TEXT = b'text'
    RESPAWN = b'respawn'


class FortRushHudViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(FortRushHudViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAllyScore(self):
        return self._getNumber(0)

    def setAllyScore(self, value):
        self._setNumber(0, value)
        return

    def getEnemyScore(self):
        return self._getNumber(1)

    def setEnemyScore(self, value):
        self._setNumber(1, value)
        return

    def getScoreCap(self):
        return self._getNumber(2)

    def setScoreCap(self, value):
        self._setNumber(2, value)
        return

    def getTimerSeconds(self):
        return self._getNumber(3)

    def setTimerSeconds(self, value):
        self._setNumber(3, value)
        return

    def getBaseCount(self):
        return self._getNumber(4)

    def setBaseCount(self, value):
        self._setNumber(4, value)
        return

    def getAllyCapturedBases(self):
        return self._getNumber(5)

    def setAllyCapturedBases(self, value):
        self._setNumber(5, value)
        return

    def getEnemyCapturedBases(self):
        return self._getNumber(6)

    def setEnemyCapturedBases(self, value):
        self._setNumber(6, value)
        return

    def getPendingAllyScore(self):
        return self._getNumber(7)

    def setPendingAllyScore(self, value):
        self._setNumber(7, value)
        return

    def getPendingEnemyScore(self):
        return self._getNumber(8)

    def setPendingEnemyScore(self, value):
        self._setNumber(8, value)
        return

    def getIsSniperModeOn(self):
        return self._getBool(9)

    def setIsSniperModeOn(self, value):
        self._setBool(9, value)
        return

    def getAllyUnits(self):
        return self._getArray(10)

    def setAllyUnits(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getAllyUnitsType():
        return FortRushHudTeamUnitModel

    def getEnemyUnits(self):
        return self._getArray(11)

    def setEnemyUnits(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getEnemyUnitsType():
        return FortRushHudTeamUnitModel

    def getCapturePointsMarker(self):
        return self._getArray(12)

    def setCapturePointsMarker(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getCapturePointsMarkerType():
        return FortRushHudBaseMarkerModel

    def getCapturingPointUid(self):
        return self._getNumber(13)

    def setCapturingPointUid(self, value):
        self._setNumber(13, value)
        return

    def getCaptureIndicatorsByUid(self):
        return self._getMap(14)

    def setCaptureIndicatorsByUid(self, value):
        self._setMap(14, value)
        return

    @staticmethod
    def getCaptureIndicatorsByUidType():
        return (int, FortRushHudBaseCaptureIndicatorModel)

    def getIsAnnouncementVisible(self):
        return self._getBool(15)

    def setIsAnnouncementVisible(self, value):
        self._setBool(15, value)
        return

    def getAnnouncementCountdownTargetTime(self):
        return self._getReal(16)

    def setAnnouncementCountdownTargetTime(self, value):
        self._setReal(16, value)
        return

    def getAnnouncementHeading(self):
        return self._getString(17)

    def setAnnouncementHeading(self, value):
        self._setString(17, value)
        return

    def getAnnouncementDescription(self):
        return self._getString(18)

    def setAnnouncementDescription(self, value):
        self._setString(18, value)
        return

    def getAnnouncementType(self):
        return AnnouncementTypeEnum(self._getString(19))

    def setAnnouncementType(self, value):
        self._setString(19, value.value)
        return

    def getHudVisibility(self):
        return self._getMap(20)

    def setHudVisibility(self, value):
        self._setMap(20, value)
        return

    @staticmethod
    def getHudVisibilityType():
        return (unicode, bool)

    def _initialize(self):
        super(FortRushHudViewModel, self)._initialize()
        self._addNumberProperty(b'allyScore', 0)
        self._addNumberProperty(b'enemyScore', 0)
        self._addNumberProperty(b'scoreCap', 0)
        self._addNumberProperty(b'timerSeconds', 0)
        self._addNumberProperty(b'baseCount', 0)
        self._addNumberProperty(b'allyCapturedBases', 0)
        self._addNumberProperty(b'enemyCapturedBases', 0)
        self._addNumberProperty(b'pendingAllyScore', 0)
        self._addNumberProperty(b'pendingEnemyScore', 0)
        self._addBoolProperty(b'isSniperModeOn', False)
        self._addArrayProperty(b'allyUnits', Array())
        self._addArrayProperty(b'enemyUnits', Array())
        self._addArrayProperty(b'capturePointsMarker', Array())
        self._addNumberProperty(b'capturingPointUid', -1)
        self._addMapProperty(b'captureIndicatorsByUid', Map(int, FortRushHudBaseCaptureIndicatorModel))
        self._addBoolProperty(b'isAnnouncementVisible', False)
        self._addRealProperty(b'announcementCountdownTargetTime', -1)
        self._addStringProperty(b'announcementHeading', b'')
        self._addStringProperty(b'announcementDescription', b'')
        self._addStringProperty(b'announcementType', AnnouncementTypeEnum.NONE.value)
        self._addMapProperty(b'hudVisibility', Map(unicode, bool))
        return
