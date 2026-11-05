from frameworks.wulf import ViewModel

class MarkerViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MarkerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAvailableDoorsAmount(self):
        return self._getNumber(0)

    def setAvailableDoorsAmount(self, value):
        self._setNumber(0, value)
        return

    def getIsVisible(self):
        return self._getBool(1)

    def setIsVisible(self, value):
        self._setBool(1, value)
        return

    def getIsPostEvent(self):
        return self._getBool(2)

    def setIsPostEvent(self, value):
        self._setBool(2, value)
        return

    def getIsAnimationEnabled(self):
        return self._getBool(3)

    def setIsAnimationEnabled(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(MarkerViewModel, self)._initialize()
        self._addNumberProperty(b'availableDoorsAmount', 0)
        self._addBoolProperty(b'isVisible', True)
        self._addBoolProperty(b'isPostEvent', False)
        self._addBoolProperty(b'isAnimationEnabled', False)
        return
