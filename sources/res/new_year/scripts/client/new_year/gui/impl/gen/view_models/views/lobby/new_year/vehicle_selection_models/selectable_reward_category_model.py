from frameworks.wulf import ViewModel

class SelectableRewardCategoryModel(ViewModel):
    __slots__ = ()
    UNDEFIEND_REVARD_INDEX = -1

    def __init__(self, properties=9, commands=0):
        super(SelectableRewardCategoryModel, self).__init__(properties=properties, commands=commands)
        return

    def getVariadicID(self):
        return self._getString(0)

    def setVariadicID(self, value):
        self._setString(0, value)
        return

    def getTabIndex(self):
        return self._getNumber(1)

    def setTabIndex(self, value):
        self._setNumber(1, value)
        return

    def getDiscount(self):
        return self._getNumber(2)

    def setDiscount(self, value):
        self._setNumber(2, value)
        return

    def getIsSelected(self):
        return self._getBool(3)

    def setIsSelected(self, value):
        self._setBool(3, value)
        return

    def getLevel(self):
        return self._getNumber(4)

    def setLevel(self, value):
        self._setNumber(4, value)
        return

    def getSelectedRewardIndex(self):
        return self._getNumber(5)

    def setSelectedRewardIndex(self, value):
        self._setNumber(5, value)
        return

    def getTooltipContentId(self):
        return self._getString(6)

    def setTooltipContentId(self, value):
        self._setString(6, value)
        return

    def getTooltipId(self):
        return self._getString(7)

    def setTooltipId(self, value):
        self._setString(7, value)
        return

    def getSelectedVehicle(self):
        return self._getString(8)

    def setSelectedVehicle(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(SelectableRewardCategoryModel, self)._initialize()
        self._addStringProperty(b'variadicID', b'')
        self._addNumberProperty(b'tabIndex', 0)
        self._addNumberProperty(b'discount', 0)
        self._addBoolProperty(b'isSelected', False)
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'selectedRewardIndex', -1)
        self._addStringProperty(b'tooltipContentId', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'selectedVehicle', b'')
        return
