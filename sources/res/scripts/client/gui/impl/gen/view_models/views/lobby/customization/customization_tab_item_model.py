from frameworks.wulf import ViewModel

class CustomizationTabItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CustomizationTabItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getGroupId(self):
        return self._getNumber(0)

    def setGroupId(self, value):
        self._setNumber(0, value)
        return

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getItemType(self):
        return self._getString(2)

    def setItemType(self, value):
        self._setString(2, value)
        return

    def getIsPlus(self):
        return self._getBool(3)

    def setIsPlus(self, value):
        self._setBool(3, value)
        return

    def getNoveltyCounter(self):
        return self._getNumber(4)

    def setNoveltyCounter(self, value):
        self._setNumber(4, value)
        return

    def getIsSelected(self):
        return self._getBool(5)

    def setIsSelected(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(CustomizationTabItemModel, self)._initialize()
        self._addNumberProperty(b'groupId', 0)
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'itemType', b'')
        self._addBoolProperty(b'isPlus', False)
        self._addNumberProperty(b'noveltyCounter', 0)
        self._addBoolProperty(b'isSelected', False)
        return
