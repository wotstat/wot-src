from frameworks.wulf import ViewModel

class CrewBannerWidgetModel(ViewModel):
    __slots__ = (b'onReset', b'onFill')

    def __init__(self, properties=3, commands=2):
        super(CrewBannerWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getSecondsLeft(self):
        return self._getNumber(0)

    def setSecondsLeft(self, value):
        self._setNumber(0, value)
        return

    def getIsFillDisabled(self):
        return self._getBool(1)

    def setIsFillDisabled(self, value):
        self._setBool(1, value)
        return

    def getIsResetDisabled(self):
        return self._getBool(2)

    def setIsResetDisabled(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(CrewBannerWidgetModel, self)._initialize()
        self._addNumberProperty(b'secondsLeft', 0)
        self._addBoolProperty(b'isFillDisabled', False)
        self._addBoolProperty(b'isResetDisabled', False)
        self.onReset = self._addCommand(b'onReset')
        self.onFill = self._addCommand(b'onFill')
        return
