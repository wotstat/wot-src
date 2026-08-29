from frameworks.wulf import ViewModel

class RetrainTankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RetrainTankmanModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)
        return

    def getIsInSkin(self):
        return self._getBool(1)

    def setIsInSkin(self, value):
        self._setBool(1, value)
        return

    def getIsFemale(self):
        return self._getBool(2)

    def setIsFemale(self, value):
        self._setBool(2, value)
        return

    def getRole(self):
        return self._getString(3)

    def setRole(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(RetrainTankmanModel, self)._initialize()
        self._addStringProperty(b'iconName', b'')
        self._addBoolProperty(b'isInSkin', False)
        self._addBoolProperty(b'isFemale', False)
        self._addStringProperty(b'role', b'')
        return
