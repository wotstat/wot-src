from enum import Enum
from frameworks.wulf import ViewModel

class ModeStatus(Enum):
    ALERT = b'alert'
    BATTLESELECTOR = b'battleSelector'


class HeaderModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(HeaderModel, self).__init__(properties=properties, commands=commands)
        return

    def getModeStatus(self):
        return ModeStatus(self._getString(0))

    def setModeStatus(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(HeaderModel, self)._initialize()
        self._addStringProperty(b'modeStatus', ModeStatus.BATTLESELECTOR.value)
        return
