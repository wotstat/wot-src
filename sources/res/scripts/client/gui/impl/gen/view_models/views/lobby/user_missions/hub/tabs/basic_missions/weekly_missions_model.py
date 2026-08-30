from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.weekly.weekly_mission_model import WeeklyMissionModel

class WeeklyMissionsModel(ViewModel):
    __slots__ = (b'onReroll',)

    def __init__(self, properties=2, commands=1):
        super(WeeklyMissionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionsList(self):
        return self._getArray(0)

    def setMissionsList(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getMissionsListType():
        return WeeklyMissionModel

    def getUpdateWeekDay(self):
        return self._getNumber(1)

    def setUpdateWeekDay(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(WeeklyMissionsModel, self)._initialize()
        self._addArrayProperty(b'missionsList', Array())
        self._addNumberProperty(b'updateWeekDay', 0)
        self.onReroll = self._addCommand(b'onReroll')
        return
