from frameworks.wulf import ViewModel

class IntroScreenModel(ViewModel):
    __slots__ = (b'onClose', b'onCloseAnimationStarted')

    def __init__(self, properties=5, commands=2):
        super(IntroScreenModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartDate(self):
        return self._getNumber(0)

    def setStartDate(self, value):
        self._setNumber(0, value)
        return

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)
        return

    def getDoorsCount(self):
        return self._getNumber(2)

    def setDoorsCount(self, value):
        self._setNumber(2, value)
        return

    def getIsOpenedFirstTime(self):
        return self._getBool(3)

    def setIsOpenedFirstTime(self, value):
        self._setBool(3, value)
        return

    def getIsAnimationEnabled(self):
        return self._getBool(4)

    def setIsAnimationEnabled(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(IntroScreenModel, self)._initialize()
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'doorsCount', 0)
        self._addBoolProperty(b'isOpenedFirstTime', False)
        self._addBoolProperty(b'isAnimationEnabled', False)
        self.onClose = self._addCommand(b'onClose')
        self.onCloseAnimationStarted = self._addCommand(b'onCloseAnimationStarted')
        return
