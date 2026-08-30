from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ContextMenuSubItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ContextMenuSubItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getResource(0)

    def setLabel(self, value):
        self._setResource(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getId(self):
        return self._getNumber(3)

    def setId(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(ContextMenuSubItemModel, self)._initialize()
        self._addResourceProperty(b'label', R.invalid())
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'isEnabled', True)
        self._addNumberProperty(b'id', 0)
        return
