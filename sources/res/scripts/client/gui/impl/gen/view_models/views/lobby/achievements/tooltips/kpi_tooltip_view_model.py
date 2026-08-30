from frameworks.wulf import ViewModel

class KpiTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(KpiTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getKpiType(self):
        return self._getString(0)

    def setKpiType(self, value):
        self._setString(0, value)
        return

    def getAvgValue(self):
        return self._getString(1)

    def setAvgValue(self, value):
        self._setString(1, value)
        return

    def getMaxValue(self):
        return self._getString(2)

    def setMaxValue(self, value):
        self._setString(2, value)
        return

    def getTankName(self):
        return self._getString(3)

    def setTankName(self, value):
        self._setString(3, value)
        return

    def getIsPremiumIGR(self):
        return self._getBool(4)

    def setIsPremiumIGR(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(KpiTooltipViewModel, self)._initialize()
        self._addStringProperty(b'kpiType', b'damage')
        self._addStringProperty(b'avgValue', b'')
        self._addStringProperty(b'maxValue', b'')
        self._addStringProperty(b'tankName', b'')
        self._addBoolProperty(b'isPremiumIGR', False)
        return
