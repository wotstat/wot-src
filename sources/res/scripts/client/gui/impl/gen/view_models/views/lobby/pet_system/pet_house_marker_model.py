from frameworks.wulf import ViewModel

class PetHouseMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PetHouseMarkerModel, self).__init__(properties=properties, commands=commands)
        return

    def getPetNameID(self):
        return self._getNumber(0)

    def setPetNameID(self, value):
        self._setNumber(0, value)
        return

    def getHasUpdate(self):
        return self._getBool(1)

    def setHasUpdate(self, value):
        self._setBool(1, value)
        return

    def getIsVisible(self):
        return self._getBool(2)

    def setIsVisible(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(PetHouseMarkerModel, self)._initialize()
        self._addNumberProperty(b'petNameID', 0)
        self._addBoolProperty(b'hasUpdate', False)
        self._addBoolProperty(b'isVisible', True)
        return
