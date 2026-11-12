from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.common.customization_zone_type_model import CustomizationZoneTypeModel

class CustomizationZoneTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(CustomizationZoneTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def customizationZone(self):
        return self._getViewModel(0)

    @staticmethod
    def getCustomizationZoneType():
        return CustomizationZoneTypeModel

    def getCurrentLevel(self):
        return self._getNumber(1)

    def setCurrentLevel(self, value):
        self._setNumber(1, value)
        return

    def getMaxLevel(self):
        return self._getNumber(2)

    def setMaxLevel(self, value):
        self._setNumber(2, value)
        return

    def getNextLevelDecorations(self):
        return self._getNumber(3)

    def setNextLevelDecorations(self, value):
        self._setNumber(3, value)
        return

    def getUpgradeCost(self):
        return self._getNumber(4)

    def setUpgradeCost(self, value):
        self._setNumber(4, value)
        return

    def getIsEnoughValue(self):
        return self._getBool(5)

    def setIsEnoughValue(self, value):
        self._setBool(5, value)
        return

    def getAtmosphereCount(self):
        return self._getNumber(6)

    def setAtmosphereCount(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(CustomizationZoneTooltipModel, self)._initialize()
        self._addViewModelProperty(b'customizationZone', CustomizationZoneTypeModel())
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addNumberProperty(b'nextLevelDecorations', 0)
        self._addNumberProperty(b'upgradeCost', 0)
        self._addBoolProperty(b'isEnoughValue', False)
        self._addNumberProperty(b'atmosphereCount', 0)
        return
