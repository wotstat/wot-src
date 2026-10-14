from enum import Enum
from frameworks.wulf import ViewModel

class ClipState(Enum):
    NONE = b'none'
    NORMAL = b'normal'
    CRITICAL = b'critical'


class ControllableReloadModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(ControllableReloadModel, self).__init__(properties=properties, commands=commands)
        return

    def getClipCapacity(self):
        return self._getNumber(0)

    def setClipCapacity(self, value):
        self._setNumber(0, value)
        return

    def getQuantityInClip(self):
        return self._getNumber(1)

    def setQuantityInClip(self, value):
        self._setNumber(1, value)
        return

    def getClipState(self):
        return ClipState(self._getString(2))

    def setClipState(self, value):
        self._setString(2, value.value)
        return

    def getIsInControllableReload(self):
        return self._getBool(3)

    def setIsInControllableReload(self, value):
        self._setBool(3, value)
        return

    def getAutoloadTimeLeft(self):
        return self._getReal(4)

    def setAutoloadTimeLeft(self, value):
        self._setReal(4, value)
        return

    def getAutoloadBaseDuration(self):
        return self._getReal(5)

    def setAutoloadBaseDuration(self, value):
        self._setReal(5, value)
        return

    def getIsAutoloadCritical(self):
        return self._getBool(6)

    def setIsAutoloadCritical(self, value):
        self._setBool(6, value)
        return

    def getIsAutoloadTimerOn(self):
        return self._getBool(7)

    def setIsAutoloadTimerOn(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(ControllableReloadModel, self)._initialize()
        self._addNumberProperty(b'clipCapacity', -1)
        self._addNumberProperty(b'quantityInClip', -1)
        self._addStringProperty(b'clipState', ClipState.NONE.value)
        self._addBoolProperty(b'isInControllableReload', False)
        self._addRealProperty(b'autoloadTimeLeft', -1.0)
        self._addRealProperty(b'autoloadBaseDuration', -1.0)
        self._addBoolProperty(b'isAutoloadCritical', False)
        self._addBoolProperty(b'isAutoloadTimerOn', False)
        return
