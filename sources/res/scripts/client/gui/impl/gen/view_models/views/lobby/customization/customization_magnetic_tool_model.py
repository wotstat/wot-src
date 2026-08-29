from frameworks.wulf import ViewModel

class CustomizationMagneticToolModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CustomizationMagneticToolModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getIsWide(self):
        return self._getBool(2)

    def setIsWide(self, value):
        self._setBool(2, value)
        return

    def getIsDim(self):
        return self._getBool(3)

    def setIsDim(self, value):
        self._setBool(3, value)
        return

    def getFormFactor(self):
        return self._getNumber(4)

    def setFormFactor(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(CustomizationMagneticToolModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', False)
        self._addStringProperty(b'icon', b'')
        self._addBoolProperty(b'isWide', False)
        self._addBoolProperty(b'isDim', False)
        self._addNumberProperty(b'formFactor', 0)
        return
