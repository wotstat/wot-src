from frameworks.wulf import ViewModel

class CustomizationSeasonsItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CustomizationSeasonsItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFull(self):
        return self._getBool(0)

    def setIsFull(self, value):
        self._setBool(0, value)
        return

    def getIsSelected(self):
        return self._getBool(1)

    def setIsSelected(self, value):
        self._setBool(1, value)
        return

    def getSeason(self):
        return self._getString(2)

    def setSeason(self, value):
        self._setString(2, value)
        return

    def getItemNotificationCount(self):
        return self._getNumber(3)

    def setItemNotificationCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(CustomizationSeasonsItemModel, self)._initialize()
        self._addBoolProperty(b'isFull', False)
        self._addBoolProperty(b'isSelected', False)
        self._addStringProperty(b'season', b'')
        self._addNumberProperty(b'itemNotificationCount', 0)
        return
