from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.daily.daily_bonus_mission_model import DailyBonusMissionModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.daily.daily_mission_model import DailyMissionModel

class DailyMissionsBlockModel(ViewModel):
    __slots__ = (b'onReroll',)
    BONUS_CARD_DEFAULT_ID = b'BONUS_CARD'

    def __init__(self, properties=5, commands=1):
        super(DailyMissionsBlockModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bonusMission(self):
        return self._getViewModel(0)

    @staticmethod
    def getBonusMissionType():
        return DailyBonusMissionModel

    def getMissionsList(self):
        return self._getArray(1)

    def setMissionsList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getMissionsListType():
        return DailyMissionModel

    def getTimeToNextRerol(self):
        return self._getNumber(2)

    def setTimeToNextRerol(self, value):
        self._setNumber(2, value)
        return

    def getAreAllMissionsCompleted(self):
        return self._getBool(3)

    def setAreAllMissionsCompleted(self, value):
        self._setBool(3, value)
        return

    def getTimeToMissionsUpdate(self):
        return self._getNumber(4)

    def setTimeToMissionsUpdate(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(DailyMissionsBlockModel, self)._initialize()
        self._addViewModelProperty(b'bonusMission', DailyBonusMissionModel())
        self._addArrayProperty(b'missionsList', Array())
        self._addNumberProperty(b'timeToNextRerol', 0)
        self._addBoolProperty(b'areAllMissionsCompleted', False)
        self._addNumberProperty(b'timeToMissionsUpdate', 0)
        self.onReroll = self._addCommand(b'onReroll')
        return
