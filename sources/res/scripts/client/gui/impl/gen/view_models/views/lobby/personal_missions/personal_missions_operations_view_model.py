from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_operation_model import Pm3OperationModel

class RewardsStatus(Enum):
    AVAILABLE = b'available'
    DISABLE = b'disable'
    HIDDEN = b'hidden'


class PersonalMissionsOperationsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onOpenOperation', b'onTakeRewards', b'onInfo')

    def __init__(self, properties=3, commands=4):
        super(PersonalMissionsOperationsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def lastOperation(self):
        return self._getViewModel(0)

    @staticmethod
    def getLastOperationType():
        return Pm3OperationModel

    def getRewardsStatus(self):
        return RewardsStatus(self._getString(1))

    def setRewardsStatus(self, value):
        self._setString(1, value.value)
        return

    def getOperations(self):
        return self._getArray(2)

    def setOperations(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getOperationsType():
        return Pm3OperationModel

    def _initialize(self):
        super(PersonalMissionsOperationsViewModel, self)._initialize()
        self._addViewModelProperty(b'lastOperation', Pm3OperationModel())
        self._addStringProperty(b'rewardsStatus')
        self._addArrayProperty(b'operations', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onOpenOperation = self._addCommand(b'onOpenOperation')
        self.onTakeRewards = self._addCommand(b'onTakeRewards')
        self.onInfo = self._addCommand(b'onInfo')
        return
