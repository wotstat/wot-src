from frameworks.wulf import ViewModel

class WidgetRankModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(WidgetRankModel, self).__init__(properties=properties, commands=commands)
        return

    def getDivisionID(self):
        return self._getNumber(0)

    def setDivisionID(self, value):
        self._setNumber(0, value)
        return

    def getRankID(self):
        return self._getNumber(1)

    def setRankID(self, value):
        self._setNumber(1, value)
        return

    def getRankName(self):
        return self._getNumber(2)

    def setRankName(self, value):
        self._setNumber(2, value)
        return

    def getIsUnburnable(self):
        return self._getBool(3)

    def setIsUnburnable(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(WidgetRankModel, self)._initialize()
        self._addNumberProperty(b'divisionID', 0)
        self._addNumberProperty(b'rankID', 0)
        self._addNumberProperty(b'rankName', 0)
        self._addBoolProperty(b'isUnburnable', False)
        return
