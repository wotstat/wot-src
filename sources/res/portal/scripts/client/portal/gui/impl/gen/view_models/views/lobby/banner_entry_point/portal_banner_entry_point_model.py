from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    ACTIVE = b'active'
    DISABLED = b'disabled'


class PortalBannerEntryPointModel(ViewModel):
    __slots__ = (b'onOpen', b'onShowingAnimationFinish')

    def __init__(self, properties=4, commands=2):
        super(PortalBannerEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getPerformance(self):
        return self._getNumber(1)

    def setPerformance(self, value):
        self._setNumber(1, value)
        return

    def getIsAnimated(self):
        return self._getBool(2)

    def setIsAnimated(self, value):
        self._setBool(2, value)
        return

    def getTimestamp(self):
        return self._getNumber(3)

    def setTimestamp(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(PortalBannerEntryPointModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'performance', 0)
        self._addBoolProperty(b'isAnimated', False)
        self._addNumberProperty(b'timestamp', 0)
        self.onOpen = self._addCommand(b'onOpen')
        self.onShowingAnimationFinish = self._addCommand(b'onShowingAnimationFinish')
        return
