from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ProgressiveItemsRewardViewModel(ViewModel):
    __slots__ = (b'onOkClick', b'onSecondaryClick')

    def __init__(self, properties=15, commands=2):
        super(ProgressiveItemsRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsNewItem(self):
        return self._getBool(0)

    def setIsNewItem(self, value):
        self._setBool(0, value)
        return

    def getTankLevel(self):
        return self._getString(1)

    def setTankLevel(self, value):
        self._setString(1, value)
        return

    def getShowTankLevel(self):
        return self._getBool(2)

    def setShowTankLevel(self, value):
        self._setBool(2, value)
        return

    def getTankTypeIcon(self):
        return self._getResource(3)

    def setTankTypeIcon(self, value):
        self._setResource(3, value)
        return

    def getTankName(self):
        return self._getString(4)

    def setTankName(self, value):
        self._setString(4, value)
        return

    def getCongratsText(self):
        return self._getString(5)

    def setCongratsText(self, value):
        self._setString(5, value)
        return

    def getItemName(self):
        return self._getString(6)

    def setItemName(self, value):
        self._setString(6, value)
        return

    def getFormFactor(self):
        return self._getString(7)

    def setFormFactor(self, value):
        self._setString(7, value)
        return

    def getItemIcons(self):
        return self._getArray(8)

    def setItemIcons(self, value):
        self._setArray(8, value)
        return

    def getOkButtonLabel(self):
        return self._getString(9)

    def setOkButtonLabel(self, value):
        self._setString(9, value)
        return

    def getOkButtonTooltip(self):
        return self._getString(10)

    def setOkButtonTooltip(self, value):
        self._setString(10, value)
        return

    def getIsOkButtonEnabled(self):
        return self._getBool(11)

    def setIsOkButtonEnabled(self, value):
        self._setBool(11, value)
        return

    def getSecondaryButtonLabel(self):
        return self._getString(12)

    def setSecondaryButtonLabel(self, value):
        self._setString(12, value)
        return

    def getSecondaryButtonTooltip(self):
        return self._getString(13)

    def setSecondaryButtonTooltip(self, value):
        self._setString(13, value)
        return

    def getIsSecondaryButtonEnabled(self):
        return self._getBool(14)

    def setIsSecondaryButtonEnabled(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(ProgressiveItemsRewardViewModel, self)._initialize()
        self._addBoolProperty(b'isNewItem', False)
        self._addStringProperty(b'tankLevel', b'')
        self._addBoolProperty(b'showTankLevel', False)
        self._addResourceProperty(b'tankTypeIcon', R.invalid())
        self._addStringProperty(b'tankName', b'')
        self._addStringProperty(b'congratsText', b'')
        self._addStringProperty(b'itemName', b'')
        self._addStringProperty(b'formFactor', b'')
        self._addArrayProperty(b'itemIcons', Array())
        self._addStringProperty(b'okButtonLabel', b'')
        self._addStringProperty(b'okButtonTooltip', b'')
        self._addBoolProperty(b'isOkButtonEnabled', False)
        self._addStringProperty(b'secondaryButtonLabel', b'')
        self._addStringProperty(b'secondaryButtonTooltip', b'')
        self._addBoolProperty(b'isSecondaryButtonEnabled', False)
        self.onOkClick = self._addCommand(b'onOkClick')
        self.onSecondaryClick = self._addCommand(b'onSecondaryClick')
        return
