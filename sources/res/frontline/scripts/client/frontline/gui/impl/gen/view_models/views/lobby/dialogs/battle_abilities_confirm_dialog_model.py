from frameworks.wulf import Array, ViewModel

class BattleAbilitiesConfirmDialogModel(ViewModel):
    __slots__ = (b'onCheckBoxClick', b'onSubmitClick', b'onCancelClick', b'onCloseClick')

    def __init__(self, properties=10, commands=4):
        super(BattleAbilitiesConfirmDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getPrice(self):
        return self._getNumber(0)

    def setPrice(self, value):
        self._setNumber(0, value)
        return

    def getBonus(self):
        return self._getNumber(1)

    def setBonus(self, value):
        self._setNumber(1, value)
        return

    def getIsBuy(self):
        return self._getBool(2)

    def setIsBuy(self, value):
        self._setBool(2, value)
        return

    def getIsMultipleAbilities(self):
        return self._getBool(3)

    def setIsMultipleAbilities(self, value):
        self._setBool(3, value)
        return

    def getIsTypeSelected(self):
        return self._getBool(4)

    def setIsTypeSelected(self, value):
        self._setBool(4, value)
        return

    def getIsEnoughMoney(self):
        return self._getBool(5)

    def setIsEnoughMoney(self, value):
        self._setBool(5, value)
        return

    def getSelectedSkillName(self):
        return self._getString(6)

    def setSelectedSkillName(self, value):
        self._setString(6, value)
        return

    def getVehicleType(self):
        return self._getString(7)

    def setVehicleType(self, value):
        self._setString(7, value)
        return

    def getIcons(self):
        return self._getArray(8)

    def setIcons(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getIconsType():
        return unicode

    def getNames(self):
        return self._getArray(9)

    def setNames(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getNamesType():
        return unicode

    def _initialize(self):
        super(BattleAbilitiesConfirmDialogModel, self)._initialize()
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'bonus', 0)
        self._addBoolProperty(b'isBuy', False)
        self._addBoolProperty(b'isMultipleAbilities', False)
        self._addBoolProperty(b'isTypeSelected', False)
        self._addBoolProperty(b'isEnoughMoney', False)
        self._addStringProperty(b'selectedSkillName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addArrayProperty(b'icons', Array())
        self._addArrayProperty(b'names', Array())
        self.onCheckBoxClick = self._addCommand(b'onCheckBoxClick')
        self.onSubmitClick = self._addCommand(b'onSubmitClick')
        self.onCancelClick = self._addCommand(b'onCancelClick')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        return
