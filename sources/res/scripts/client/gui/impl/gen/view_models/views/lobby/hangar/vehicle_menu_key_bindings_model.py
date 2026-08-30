from frameworks.wulf import ViewModel

class VehicleMenuKeyBindingsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(VehicleMenuKeyBindingsModel, self).__init__(properties=properties, commands=commands)
        return

    def getRetrainCrew(self):
        return self._getNumber(0)

    def setRetrainCrew(self, value):
        self._setNumber(0, value)
        return

    def getQuickTraining(self):
        return self._getNumber(1)

    def setQuickTraining(self, value):
        self._setNumber(1, value)
        return

    def getReturnCrew(self):
        return self._getNumber(2)

    def setReturnCrew(self, value):
        self._setNumber(2, value)
        return

    def getAboutVehicle(self):
        return self._getNumber(3)

    def setAboutVehicle(self, value):
        self._setNumber(3, value)
        return

    def getUpgrades(self):
        return self._getNumber(4)

    def setUpgrades(self, value):
        self._setNumber(4, value)
        return

    def getCompare(self):
        return self._getNumber(5)

    def setCompare(self, value):
        self._setNumber(5, value)
        return

    def getResearch(self):
        return self._getNumber(6)

    def setResearch(self, value):
        self._setNumber(6, value)
        return

    def getArmor(self):
        return self._getNumber(7)

    def setArmor(self, value):
        self._setNumber(7, value)
        return

    def getQuickService(self):
        return self._getNumber(8)

    def setQuickService(self, value):
        self._setNumber(8, value)
        return

    def getCustomization(self):
        return self._getNumber(9)

    def setCustomization(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(VehicleMenuKeyBindingsModel, self)._initialize()
        self._addNumberProperty(b'retrainCrew', 0)
        self._addNumberProperty(b'quickTraining', 0)
        self._addNumberProperty(b'returnCrew', 0)
        self._addNumberProperty(b'aboutVehicle', 0)
        self._addNumberProperty(b'upgrades', 0)
        self._addNumberProperty(b'compare', 0)
        self._addNumberProperty(b'research', 0)
        self._addNumberProperty(b'armor', 0)
        self._addNumberProperty(b'quickService', 0)
        self._addNumberProperty(b'customization', 0)
        return
