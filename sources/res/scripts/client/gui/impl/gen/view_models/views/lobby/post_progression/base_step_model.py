from enum import Enum
from frameworks.wulf import ViewModel

class ActionType(Enum):
    MODIFICATION = b'modification'
    PAIRMODIFICATION = b'pairModification'
    MODIFICATIONWITHFEATURE = b'modificationWithFeature'


class BaseStepModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BaseStepModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getActionType(self):
        return ActionType(self._getString(1))

    def setActionType(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(BaseStepModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'actionType')
        return
