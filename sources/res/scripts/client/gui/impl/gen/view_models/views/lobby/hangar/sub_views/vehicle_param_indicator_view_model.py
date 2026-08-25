from frameworks.wulf import ViewModel

class VehicleParamIndicatorViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(VehicleParamIndicatorViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsUseAnim(self):
        return self._getBool(0)

    def setIsUseAnim(self, value):
        self._setBool(0, value)
        return

    def getDelta(self):
        return self._getNumber(1)

    def setDelta(self, value):
        self._setNumber(1, value)
        return

    def getMarkerValue(self):
        return self._getNumber(2)

    def setMarkerValue(self, value):
        self._setNumber(2, value)
        return

    def getMaxValue(self):
        return self._getNumber(3)

    def setMaxValue(self, value):
        self._setNumber(3, value)
        return

    def getValue(self):
        return self._getNumber(4)

    def setValue(self, value):
        self._setNumber(4, value)
        return

    def getMinValue(self):
        return self._getNumber(5)

    def setMinValue(self, value):
        self._setNumber(5, value)
        return

    def getCurrentPercent(self):
        return self._getNumber(6)

    def setCurrentPercent(self, value):
        self._setNumber(6, value)
        return

    def getModifiedPercent(self):
        return self._getNumber(7)

    def setModifiedPercent(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(VehicleParamIndicatorViewModel, self)._initialize()
        self._addBoolProperty(b'isUseAnim', False)
        self._addNumberProperty(b'delta', 0)
        self._addNumberProperty(b'markerValue', 0)
        self._addNumberProperty(b'maxValue', 0)
        self._addNumberProperty(b'value', 0)
        self._addNumberProperty(b'minValue', 0)
        self._addNumberProperty(b'currentPercent', 0)
        self._addNumberProperty(b'modifiedPercent', 0)
        return
