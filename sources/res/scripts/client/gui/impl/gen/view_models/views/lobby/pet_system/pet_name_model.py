from frameworks.wulf import ViewModel

class PetNameModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PetNameModel, self).__init__(properties=properties, commands=commands)
        return

    def getPetNameID(self):
        return self._getNumber(0)

    def setPetNameID(self, value):
        self._setNumber(0, value)
        return

    def getIsNew(self):
        return self._getBool(1)

    def setIsNew(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(PetNameModel, self)._initialize()
        self._addNumberProperty(b'petNameID', 0)
        self._addBoolProperty(b'isNew', False)
        return
