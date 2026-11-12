from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.common.customization_zone_type_model import CustomizationZoneTypeModel
from new_year.gui.impl.gen.view_models.common.ny_currency_type_model import NyCurrencyTypeModel

class CustomizationZoneModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(CustomizationZoneModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def customizationZone(self):
        return self._getViewModel(0)

    @staticmethod
    def getCustomizationZoneType():
        return CustomizationZoneTypeModel

    @property
    def currencyType(self):
        return self._getViewModel(1)

    @staticmethod
    def getCurrencyTypeType():
        return NyCurrencyTypeModel

    def getCurrentLevel(self):
        return self._getNumber(2)

    def setCurrentLevel(self, value):
        self._setNumber(2, value)
        return

    def getCurrencyCount(self):
        return self._getNumber(3)

    def setCurrencyCount(self, value):
        self._setNumber(3, value)
        return

    def getLevelUpCurrencyNeed(self):
        return self._getNumber(4)

    def setLevelUpCurrencyNeed(self, value):
        self._setNumber(4, value)
        return

    def getMaxLevel(self):
        return self._getNumber(5)

    def setMaxLevel(self, value):
        self._setNumber(5, value)
        return

    def getAtmospherePoints(self):
        return self._getNumber(6)

    def setAtmospherePoints(self, value):
        self._setNumber(6, value)
        return

    def getToysCount(self):
        return self._getNumber(7)

    def setToysCount(self, value):
        self._setNumber(7, value)
        return

    def getCanUpgrade(self):
        return self._getBool(8)

    def setCanUpgrade(self, value):
        self._setBool(8, value)
        return

    def getHasNewToys(self):
        return self._getBool(9)

    def setHasNewToys(self, value):
        self._setBool(9, value)
        return

    def getIsZoneHovered(self):
        return self._getBool(10)

    def setIsZoneHovered(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(CustomizationZoneModel, self)._initialize()
        self._addViewModelProperty(b'customizationZone', CustomizationZoneTypeModel())
        self._addViewModelProperty(b'currencyType', NyCurrencyTypeModel())
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'currencyCount', 0)
        self._addNumberProperty(b'levelUpCurrencyNeed', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addNumberProperty(b'atmospherePoints', 0)
        self._addNumberProperty(b'toysCount', 0)
        self._addBoolProperty(b'canUpgrade', True)
        self._addBoolProperty(b'hasNewToys', True)
        self._addBoolProperty(b'isZoneHovered', False)
        return
