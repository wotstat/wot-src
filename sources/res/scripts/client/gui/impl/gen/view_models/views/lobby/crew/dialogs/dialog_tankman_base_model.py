from frameworks.wulf import ViewModel

class DialogTankmanBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(DialogTankmanBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getInvId(self):
        return self._getReal(0)

    def setInvId(self, value):
        self._setReal(0, value)
        return

    def getIconName(self):
        return self._getString(1)

    def setIconName(self, value):
        self._setString(1, value)
        return

    def getIsInSkin(self):
        return self._getBool(2)

    def setIsInSkin(self, value):
        self._setBool(2, value)
        return

    def getIsFemale(self):
        return self._getBool(3)

    def setIsFemale(self, value):
        self._setBool(3, value)
        return

    def getIsSelected(self):
        return self._getBool(4)

    def setIsSelected(self, value):
        self._setBool(4, value)
        return

    def getRole(self):
        return self._getString(5)

    def setRole(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(DialogTankmanBaseModel, self)._initialize()
        self._addRealProperty(b'invId', 0.0)
        self._addStringProperty(b'iconName', b'')
        self._addBoolProperty(b'isInSkin', False)
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isSelected', False)
        self._addStringProperty(b'role', b'')
        return
