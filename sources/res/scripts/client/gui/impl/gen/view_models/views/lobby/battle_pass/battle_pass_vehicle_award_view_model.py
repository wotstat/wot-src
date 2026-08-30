from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class BattlePassVehicleAwardViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BattlePassVehicleAwardViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getVehicleLevelPoints(self):
        return self._getNumber(1)

    def setVehicleLevelPoints(self, value):
        self._setNumber(1, value)
        return

    def getBattlePassPointsAward(self):
        return self._getNumber(2)

    def setBattlePassPointsAward(self, value):
        self._setNumber(2, value)
        return

    def getTechName(self):
        return self._getString(3)

    def setTechName(self, value):
        self._setString(3, value)
        return

    def getIsPostProgression(self):
        return self._getBool(4)

    def setIsPostProgression(self, value):
        self._setBool(4, value)
        return

    def getChapterID(self):
        return self._getNumber(5)

    def setChapterID(self, value):
        self._setNumber(5, value)
        return

    def getIsBattlePassPurchased(self):
        return self._getBool(6)

    def setIsBattlePassPurchased(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(BattlePassVehicleAwardViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'vehicleLevelPoints', 0)
        self._addNumberProperty(b'battlePassPointsAward', 0)
        self._addStringProperty(b'techName', b'')
        self._addBoolProperty(b'isPostProgression', False)
        self._addNumberProperty(b'chapterID', 0)
        self._addBoolProperty(b'isBattlePassPurchased', False)
        return
