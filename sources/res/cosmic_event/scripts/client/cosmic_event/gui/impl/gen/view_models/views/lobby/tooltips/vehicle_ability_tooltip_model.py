from frameworks.wulf import ViewModel

class VehicleAbilityTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(VehicleAbilityTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getAbilityName(self):
        return self._getString(0)

    def setAbilityName(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getCooldown(self):
        return self._getNumber(3)

    def setCooldown(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(VehicleAbilityTooltipModel, self)._initialize()
        self._addStringProperty(b'abilityName', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'cooldown', 0)
        return
