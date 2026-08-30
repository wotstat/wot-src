from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel

class WindowType(Enum):
    STANDARD = b'standard'
    POST_PROGRESSION = b'postProgression'
    VEH_SKILL_TREE = b'vehSkillTree'


class EliteViewModel(ViewModel):
    __slots__ = (b'onGoToProgression', b'onClose')

    def __init__(self, properties=4, commands=2):
        super(EliteViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    @property
    def prestigeEmblem(self):
        return self._getViewModel(1)

    @staticmethod
    def getPrestigeEmblemType():
        return PrestigeEmblemModel

    def getType(self):
        return WindowType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def getIsPrestigeAvailable(self):
        return self._getBool(3)

    def setIsPrestigeAvailable(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(EliteViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addViewModelProperty(b'prestigeEmblem', PrestigeEmblemModel())
        self._addStringProperty(b'type')
        self._addBoolProperty(b'isPrestigeAvailable', False)
        self.onGoToProgression = self._addCommand(b'onGoToProgression')
        self.onClose = self._addCommand(b'onClose')
        return
