from frameworks.wulf import ViewModel

class BattleRoyaleEquipmentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BattleRoyaleEquipmentModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)
        return

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)
        return

    def getQuantity(self):
        return self._getNumber(2)

    def setQuantity(self, value):
        self._setNumber(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getCooldownSeconds(self):
        return self._getNumber(4)

    def setCooldownSeconds(self, value):
        self._setNumber(4, value)
        return

    def getTitle(self):
        return self._getString(5)

    def setTitle(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(BattleRoyaleEquipmentModel, self)._initialize()
        self._addStringProperty(b'iconName', b'')
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'quantity', 0)
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'cooldownSeconds', 0)
        self._addStringProperty(b'title', b'')
        return
