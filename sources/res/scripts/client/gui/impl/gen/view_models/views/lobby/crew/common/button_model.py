from enum import Enum
from frameworks.wulf import ViewModel

class ButtonType(Enum):
    CREWOPERATIONS = b'crewOperations'
    CREWBOOKS = b'crewBooks'
    ACCELERATEDTRAINING = b'acceleratedTraining'
    WOTPLUS = b'wotPlus'


class ButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return ButtonType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(ButtonModel, self)._initialize()
        self._addStringProperty(b'type')
        return
