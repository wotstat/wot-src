from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.achievement_model import AchievementModel

class ServiceRecordViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ServiceRecordViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsTankmanInVehicle(self):
        return self._getBool(0)

    def setIsTankmanInVehicle(self, value):
        self._setBool(0, value)
        return

    def getRankName(self):
        return self._getString(1)

    def setRankName(self, value):
        self._setString(1, value)
        return

    def getRankIcon(self):
        return self._getString(2)

    def setRankIcon(self, value):
        self._setString(2, value)
        return

    def getBattlesCount(self):
        return self._getNumber(3)

    def setBattlesCount(self, value):
        self._setNumber(3, value)
        return

    def getAverageXP(self):
        return self._getNumber(4)

    def setAverageXP(self, value):
        self._setNumber(4, value)
        return

    def getAchievementsList(self):
        return self._getArray(5)

    def setAchievementsList(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getAchievementsListType():
        return AchievementModel

    def _initialize(self):
        super(ServiceRecordViewModel, self)._initialize()
        self._addBoolProperty(b'isTankmanInVehicle', False)
        self._addStringProperty(b'rankName', b'')
        self._addStringProperty(b'rankIcon', b'')
        self._addNumberProperty(b'battlesCount', 0)
        self._addNumberProperty(b'averageXP', 0)
        self._addArrayProperty(b'achievementsList', Array())
        return
