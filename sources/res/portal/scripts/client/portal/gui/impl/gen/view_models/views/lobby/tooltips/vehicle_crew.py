from enum import Enum
from frameworks.wulf import ViewModel

class CrewId(Enum):
    KOSHCHEYEV = b'koshcheyev'
    TSAREV = b'tsarev'
    YAGINSKAYA = b'yaginskaya'
    VASILIEVA = b'vasilieva'


class VehicleCrew(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(VehicleCrew, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return CrewId(self._getString(0))

    def setId(self, value):
        self._setString(0, value.value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getRole(self):
        return self._getString(2)

    def setRole(self, value):
        self._setString(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(VehicleCrew, self)._initialize()
        self._addStringProperty(b'id')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'role', b'')
        self._addStringProperty(b'description', b'')
        return
