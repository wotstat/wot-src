from frameworks.wulf import ViewModel

class ModeSelectorCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(ModeSelectorCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getIndex(self):
        return self._getNumber(0)

    def setIndex(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return self._getNumber(1)

    def setType(self, value):
        self._setNumber(1, value)
        return

    def getResourcesFolderName(self):
        return self._getString(2)

    def setResourcesFolderName(self, value):
        self._setString(2, value)
        return

    def getIsNew(self):
        return self._getBool(3)

    def setIsNew(self, value):
        self._setBool(3, value)
        return

    def getIsSelected(self):
        return self._getBool(4)

    def setIsSelected(self, value):
        self._setBool(4, value)
        return

    def getIsDisabled(self):
        return self._getBool(5)

    def setIsDisabled(self, value):
        self._setBool(5, value)
        return

    def getIsInfoIconVisible(self):
        return self._getBool(6)

    def setIsInfoIconVisible(self, value):
        self._setBool(6, value)
        return

    def getPriority(self):
        return self._getNumber(7)

    def setPriority(self, value):
        self._setNumber(7, value)
        return

    def getColumn(self):
        return self._getNumber(8)

    def setColumn(self, value):
        self._setNumber(8, value)
        return

    def getModeName(self):
        return self._getString(9)

    def setModeName(self, value):
        self._setString(9, value)
        return

    def getIsLocked(self):
        return self._getBool(10)

    def setIsLocked(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(ModeSelectorCardModel, self)._initialize()
        self._addNumberProperty(b'index', 0)
        self._addNumberProperty(b'type', 0)
        self._addStringProperty(b'resourcesFolderName', b'')
        self._addBoolProperty(b'isNew', False)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isInfoIconVisible', False)
        self._addNumberProperty(b'priority', 0)
        self._addNumberProperty(b'column', -1)
        self._addStringProperty(b'modeName', b'')
        self._addBoolProperty(b'isLocked', False)
        return
