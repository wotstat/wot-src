from gui.impl.gen import R
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.common.customization_zone_type_model import CustomizationZoneTypeModel

class NyDecorationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(NyDecorationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def customizationZone(self):
        return self._getViewModel(0)

    @staticmethod
    def getCustomizationZoneType():
        return CustomizationZoneTypeModel

    def getName(self):
        return self._getResource(1)

    def setName(self, value):
        self._setResource(1, value)
        return

    def getDecorationTypeIcon(self):
        return self._getResource(2)

    def setDecorationTypeIcon(self, value):
        self._setResource(2, value)
        return

    def getDescription(self):
        return self._getResource(3)

    def setDescription(self, value):
        self._setResource(3, value)
        return

    def getIcon(self):
        return self._getResource(4)

    def setIcon(self, value):
        self._setResource(4, value)
        return

    def getIsPremium(self):
        return self._getBool(5)

    def setIsPremium(self, value):
        self._setBool(5, value)
        return

    def getIsLocked(self):
        return self._getBool(6)

    def setIsLocked(self, value):
        self._setBool(6, value)
        return

    def getUnlockLevel(self):
        return self._getNumber(7)

    def setUnlockLevel(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(NyDecorationTooltipModel, self)._initialize()
        self._addViewModelProperty(b'customizationZone', CustomizationZoneTypeModel())
        self._addResourceProperty(b'name', R.invalid())
        self._addResourceProperty(b'decorationTypeIcon', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'isPremium', False)
        self._addBoolProperty(b'isLocked', True)
        self._addNumberProperty(b'unlockLevel', 0)
        return
