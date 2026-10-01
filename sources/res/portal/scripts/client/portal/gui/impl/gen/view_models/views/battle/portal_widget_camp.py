from enum import Enum
from frameworks.wulf import ViewModel

class CampState(Enum):
    CANBECAPTURED = b'canBeCaptured'
    CAPTURED = b'captured'
    DEFAULT = b'default'


class PortalWidgetCamp(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PortalWidgetCamp, self).__init__(properties=properties, commands=commands)
        return

    def getAllDefenders(self):
        return self._getNumber(0)

    def setAllDefenders(self, value):
        self._setNumber(0, value)
        return

    def getKilledDefenders(self):
        return self._getNumber(1)

    def setKilledDefenders(self, value):
        self._setNumber(1, value)
        return

    def getState(self):
        return CampState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(PortalWidgetCamp, self)._initialize()
        self._addNumberProperty(b'allDefenders', 0)
        self._addNumberProperty(b'killedDefenders', 0)
        self._addStringProperty(b'state')
        return
