from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class PortalAmmunitionPanel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PortalAmmunitionPanel, self).__init__(properties=properties, commands=commands)
        return

    def getShellType(self):
        return self._getString(0)

    def setShellType(self, value):
        self._setString(0, value)
        return

    def getAbilities(self):
        return self._getArray(1)

    def setAbilities(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getAbilitiesType():
        return unicode

    def getHasNewUpgrade(self):
        return self._getBool(2)

    def setHasNewUpgrade(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(PortalAmmunitionPanel, self)._initialize()
        self._addStringProperty(b'shellType', b'')
        self._addArrayProperty(b'abilities', Array())
        self._addBoolProperty(b'hasNewUpgrade', False)
        return
