from frameworks.wulf import ViewModel

class FeatureTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FeatureTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsUnlocked(self):
        return self._getBool(0)

    def setIsUnlocked(self, value):
        self._setBool(0, value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(FeatureTooltipViewModel, self)._initialize()
        self._addBoolProperty(b'isUnlocked', False)
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isDisabled', False)
        return
