from frameworks.wulf import ViewModel

class ArmorLayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ArmorLayerModel, self).__init__(properties=properties, commands=commands)
        return

    def getLayerName(self):
        return self._getString(0)

    def setLayerName(self, value):
        self._setString(0, value)
        return

    def getNominalArmor(self):
        return self._getNumber(1)

    def setNominalArmor(self, value):
        self._setNumber(1, value)
        return

    def getImpactAngle(self):
        return self._getNumber(2)

    def setImpactAngle(self, value):
        self._setNumber(2, value)
        return

    def getResultArmor(self):
        return self._getReal(3)

    def setResultArmor(self, value):
        self._setReal(3, value)
        return

    def getColor(self):
        return self._getString(4)

    def setColor(self, value):
        self._setString(4, value)
        return

    def getCount(self):
        return self._getNumber(5)

    def setCount(self, value):
        self._setNumber(5, value)
        return

    def getReductionFactor(self):
        return self._getNumber(6)

    def setReductionFactor(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(ArmorLayerModel, self)._initialize()
        self._addStringProperty(b'layerName', b'')
        self._addNumberProperty(b'nominalArmor', 0)
        self._addNumberProperty(b'impactAngle', 0)
        self._addRealProperty(b'resultArmor', 0.0)
        self._addStringProperty(b'color', b'')
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'reductionFactor', 0)
        return
