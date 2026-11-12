from frameworks.wulf import ViewModel

class CustomizationResourceExchangeTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CustomizationResourceExchangeTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getTabId(self):
        return self._getNumber(0)

    def setTabId(self, value):
        self._setNumber(0, value)
        return

    def getItemType(self):
        return self._getString(1)

    def setItemType(self, value):
        self._setString(1, value)
        return

    def getAvailableCount(self):
        return self._getNumber(2)

    def setAvailableCount(self, value):
        self._setNumber(2, value)
        return

    def getSelectedCount(self):
        return self._getNumber(3)

    def setSelectedCount(self, value):
        self._setNumber(3, value)
        return

    def getIsDone(self):
        return self._getBool(4)

    def setIsDone(self, value):
        self._setBool(4, value)
        return

    def getIsSelected(self):
        return self._getBool(5)

    def setIsSelected(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(CustomizationResourceExchangeTabModel, self)._initialize()
        self._addNumberProperty(b'tabId', 0)
        self._addStringProperty(b'itemType', b'')
        self._addNumberProperty(b'availableCount', 0)
        self._addNumberProperty(b'selectedCount', 0)
        self._addBoolProperty(b'isDone', False)
        self._addBoolProperty(b'isSelected', False)
        return
