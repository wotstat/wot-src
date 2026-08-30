from frameworks.wulf import ViewModel

class BattleMattersVehicleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(BattleMattersVehicleModel, self).__init__(properties=properties, commands=commands)
        return

    def getIndex(self):
        return self._getNumber(0)

    def setIndex(self, value):
        self._setNumber(0, value)
        return

    def getIsElite(self):
        return self._getBool(1)

    def setIsElite(self, value):
        self._setBool(1, value)
        return

    def getIsInHangar(self):
        return self._getBool(2)

    def setIsInHangar(self, value):
        self._setBool(2, value)
        return

    def getVehCD(self):
        return self._getNumber(3)

    def setVehCD(self, value):
        self._setNumber(3, value)
        return

    def getRentLength(self):
        return self._getNumber(4)

    def setRentLength(self, value):
        self._setNumber(4, value)
        return

    def getLevel(self):
        return self._getNumber(5)

    def setLevel(self, value):
        self._setNumber(5, value)
        return

    def getVehType(self):
        return self._getString(6)

    def setVehType(self, value):
        self._setString(6, value)
        return

    def getVehName(self):
        return self._getString(7)

    def setVehName(self, value):
        self._setString(7, value)
        return

    def getUserName(self):
        return self._getString(8)

    def setUserName(self, value):
        self._setString(8, value)
        return

    def getNation(self):
        return self._getString(9)

    def setNation(self, value):
        self._setString(9, value)
        return

    def getTooltipId(self):
        return self._getString(10)

    def setTooltipId(self, value):
        self._setString(10, value)
        return

    def getTooltipContentId(self):
        return self._getString(11)

    def setTooltipContentId(self, value):
        self._setString(11, value)
        return

    def _initialize(self):
        super(BattleMattersVehicleModel, self)._initialize()
        self._addNumberProperty(b'index', 0)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isInHangar', False)
        self._addNumberProperty(b'vehCD', 0)
        self._addNumberProperty(b'rentLength', 0)
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'vehType', b'')
        self._addStringProperty(b'vehName', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipContentId', b'')
        return
