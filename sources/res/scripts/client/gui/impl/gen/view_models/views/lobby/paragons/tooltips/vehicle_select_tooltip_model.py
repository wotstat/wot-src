from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.paragons.common.paragons_vehicle_model import ParagonsVehicleModel

class VehicleSelectTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleSelectTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def reward(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardType():
        return IconBonusModel

    def getIsAchieved(self):
        return self._getBool(1)

    def setIsAchieved(self, value):
        self._setBool(1, value)
        return

    def getVehicles(self):
        return self._getArray(2)

    def setVehicles(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getVehiclesType():
        return ParagonsVehicleModel

    def _initialize(self):
        super(VehicleSelectTooltipModel, self)._initialize()
        self._addViewModelProperty(b'reward', IconBonusModel())
        self._addBoolProperty(b'isAchieved', False)
        self._addArrayProperty(b'vehicles', Array())
        return
