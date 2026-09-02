from frameworks.wulf import ViewModel

class BenefitValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BenefitValueModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getReal(0)

    def setValue(self, value):
        self._setReal(0, value)
        return

    def getSubstitutionID(self):
        return self._getString(1)

    def setSubstitutionID(self, value):
        self._setString(1, value)
        return

    def getValueType(self):
        return self._getString(2)

    def setValueType(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(BenefitValueModel, self)._initialize()
        self._addRealProperty(b'value', 0.0)
        self._addStringProperty(b'substitutionID', b'')
        self._addStringProperty(b'valueType', b'')
        return
