from enum import Enum
from frameworks.wulf import ViewModel

class MechanicState(Enum):
    DEFAULT = b''
    ON = b'on'
    OFF = b'off'


class ParamValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ParamValueModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getMechanic(self):
        return self._getString(1)

    def setMechanic(self, value):
        self._setString(1, value)
        return

    def getState(self):
        return MechanicState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(ParamValueModel, self)._initialize()
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'mechanic', b'')
        self._addStringProperty(b'state')
        return
