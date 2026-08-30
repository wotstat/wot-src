from frameworks.wulf import ViewModel

class TierButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TierButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getTier(self):
        return self._getNumber(0)

    def setTier(self, value):
        self._setNumber(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(TierButtonModel, self)._initialize()
        self._addNumberProperty(b'tier', 0)
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'isSelected', False)
        return
