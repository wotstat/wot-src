from enum import Enum
from frameworks.wulf import ViewModel

class BoostState(Enum):
    UNAVAILABLE = b'unavailable'
    INAPPLICABLE = b'inapplicable'
    WAITINGFORSTART = b'waitingForStart'
    CHARGING = b'charging'
    CHARGED = b'charged'


class AutoLoaderClipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(AutoLoaderClipModel, self).__init__(properties=properties, commands=commands)
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

    def getShellLoadingTimeLeft(self):
        return self._getReal(2)

    def setShellLoadingTimeLeft(self, value):
        self._setReal(2, value)
        return

    def getShellLoadingBaseDuration(self):
        return self._getReal(3)

    def setShellLoadingBaseDuration(self, value):
        self._setReal(3, value)
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

    def getIsTimerRed(self):
        return self._getBool(8)

    def setIsTimerRed(self, value):
        self._setBool(8, value)
        return

    def getBoostState(self):
        return BoostState(self._getString(9))

    def setBoostState(self, value):
        self._setString(9, value.value)
        return

    def getBoostTimeLeft(self):
        return self._getReal(10)

    def setBoostTimeLeft(self, value):
        self._setReal(10, value)
        return

    def getBoostTotalTime(self):
        return self._getReal(11)

    def setBoostTotalTime(self, value):
        self._setReal(11, value)
        return

    def getIsBoostApplicable(self):
        return self._getBool(12)

    def setIsBoostApplicable(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(AutoLoaderClipModel, self)._initialize()
        self._addNumberProperty(b'clipCapacity', -1)
        self._addNumberProperty(b'quantityInClip', -1)
        self._addRealProperty(b'shellLoadingTimeLeft', -1.0)
        self._addRealProperty(b'shellLoadingBaseDuration', -1.0)
        self._addRealProperty(b'autoloadTimeLeft', -1.0)
        self._addRealProperty(b'autoloadBaseDuration', -1.0)
        self._addBoolProperty(b'isAutoloadCritical', False)
        self._addBoolProperty(b'isAutoloadTimerOn', False)
        self._addBoolProperty(b'isTimerRed', False)
        self._addStringProperty(b'boostState', BoostState.UNAVAILABLE.value)
        self._addRealProperty(b'boostTimeLeft', 0.0)
        self._addRealProperty(b'boostTotalTime', 0.0)
        self._addBoolProperty(b'isBoostApplicable', False)
        return
