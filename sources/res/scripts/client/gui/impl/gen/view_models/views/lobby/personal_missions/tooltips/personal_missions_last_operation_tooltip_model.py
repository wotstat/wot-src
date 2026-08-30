from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.tooltips.pm3_last_operation_tooltip_rewards_model import Pm3LastOperationTooltipRewardsModel

class LastMissionStatus(Enum):
    DEVELOPMENT = b'development'
    ACTIVE = b'active'
    COMPLETED = b'completed'


class PersonalMissionsLastOperationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(PersonalMissionsLastOperationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionStatus(self):
        return LastMissionStatus(self._getString(0))

    def setMissionStatus(self, value):
        self._setString(0, value.value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getCompleted(self):
        return self._getNumber(2)

    def setCompleted(self, value):
        self._setNumber(2, value)
        return

    def getAll(self):
        return self._getNumber(3)

    def setAll(self, value):
        self._setNumber(3, value)
        return

    def getVehicleName(self):
        return self._getString(4)

    def setVehicleName(self, value):
        self._setString(4, value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return Pm3LastOperationTooltipRewardsModel

    def _initialize(self):
        super(PersonalMissionsLastOperationTooltipModel, self)._initialize()
        self._addStringProperty(b'missionStatus')
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'completed', 0)
        self._addNumberProperty(b'all', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addArrayProperty(b'rewards', Array())
        return
