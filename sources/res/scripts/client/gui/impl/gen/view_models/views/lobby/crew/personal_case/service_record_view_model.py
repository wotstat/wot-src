from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.tankman_info_model import TankmanInfoModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.achievement_model import AchievementModel

class ServiceRecordViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ServiceRecordViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tankmanInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getTankmanInfoType():
        return TankmanInfoModel

    def getIsTankmanInVehicle(self):
        return self._getBool(1)

    def setIsTankmanInVehicle(self, value):
        self._setBool(1, value)
        return

    def getRankName(self):
        return self._getString(2)

    def setRankName(self, value):
        self._setString(2, value)
        return

    def getRankIcon(self):
        return self._getString(3)

    def setRankIcon(self, value):
        self._setString(3, value)
        return

    def getBattlesCount(self):
        return self._getNumber(4)

    def setBattlesCount(self, value):
        self._setNumber(4, value)
        return

    def getAverageXP(self):
        return self._getNumber(5)

    def setAverageXP(self, value):
        self._setNumber(5, value)
        return

    def getAchievementsList(self):
        return self._getArray(6)

    def setAchievementsList(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getAchievementsListType():
        return AchievementModel

    def _initialize(self):
        super(ServiceRecordViewModel, self)._initialize()
        self._addViewModelProperty(b'tankmanInfo', TankmanInfoModel())
        self._addBoolProperty(b'isTankmanInVehicle', False)
        self._addStringProperty(b'rankName', b'')
        self._addStringProperty(b'rankIcon', b'')
        self._addNumberProperty(b'battlesCount', 0)
        self._addNumberProperty(b'averageXP', 0)
        self._addArrayProperty(b'achievementsList', Array())
        return
