from frameworks.wulf import ViewModel

class KeyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(KeyTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getKeyCount(self):
        return self._getNumber(0)

    def setKeyCount(self, value):
        self._setNumber(0, value)
        return

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)
        return

    def getEffective(self):
        return self._getNumber(2)

    def setEffective(self, value):
        self._setNumber(2, value)
        return

    def getBoss(self):
        return self._getNumber(3)

    def setBoss(self, value):
        self._setNumber(3, value)
        return

    def getDaily(self):
        return self._getNumber(4)

    def setDaily(self, value):
        self._setNumber(4, value)
        return

    def getIsPostBatle(self):
        return self._getBool(5)

    def setIsPostBatle(self, value):
        self._setBool(5, value)
        return

    def getSecret(self):
        return self._getNumber(6)

    def setSecret(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(KeyTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'keyCount', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'effective', 0)
        self._addNumberProperty(b'boss', 0)
        self._addNumberProperty(b'daily', 0)
        self._addBoolProperty(b'isPostBatle', False)
        self._addNumberProperty(b'secret', 0)
        return
