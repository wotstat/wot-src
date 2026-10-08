from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel

class AbilityTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(AbilityTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bonuses(self):
        return self._getViewModel(0)

    @staticmethod
    def getBonusesType():
        return BonusesModel

    def getVehicleIntCD(self):
        return self._getNumber(1)

    def setVehicleIntCD(self, value):
        self._setNumber(1, value)
        return

    def getReuseCount(self):
        return self._getNumber(2)

    def setReuseCount(self, value):
        self._setNumber(2, value)
        return

    def getDuration(self):
        return self._getNumber(3)

    def setDuration(self, value):
        self._setNumber(3, value)
        return

    def getCooldown(self):
        return self._getNumber(4)

    def setCooldown(self, value):
        self._setNumber(4, value)
        return

    def getIconName(self):
        return self._getString(5)

    def setIconName(self, value):
        self._setString(5, value)
        return

    def getUserString(self):
        return self._getString(6)

    def setUserString(self, value):
        self._setString(6, value)
        return

    def getDescription(self):
        return self._getString(7)

    def setDescription(self, value):
        self._setString(7, value)
        return

    def getLightAdditional(self):
        return self._getBool(8)

    def setLightAdditional(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(AbilityTooltipModel, self)._initialize()
        self._addViewModelProperty(b'bonuses', BonusesModel())
        self._addNumberProperty(b'vehicleIntCD', 0)
        self._addNumberProperty(b'reuseCount', 0)
        self._addNumberProperty(b'duration', 0)
        self._addNumberProperty(b'cooldown', 0)
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'userString', b'')
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'lightAdditional', True)
        return
