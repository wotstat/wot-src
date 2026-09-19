from frameworks.wulf import ViewModel

class DifficultyDropdownItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DifficultyDropdownItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getShowWarningIcon(self):
        return self._getBool(1)

    def setShowWarningIcon(self, value):
        self._setBool(1, value)
        return

    def getLabel(self):
        return self._getString(2)

    def setLabel(self, value):
        self._setString(2, value)
        return

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(DifficultyDropdownItemModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addBoolProperty(b'showWarningIcon', False)
        self._addStringProperty(b'label', b'')
        self._addBoolProperty(b'isDisabled', False)
        return
