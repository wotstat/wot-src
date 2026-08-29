from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class ContextMenuItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ContextMenuItemModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def subItemsList(self):
        return self._getViewModel(0)

    @staticmethod
    def getSubItemsListType():
        return int

    def getLabel(self):
        return self._getResource(1)

    def setLabel(self, value):
        self._setResource(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsSeparator(self):
        return self._getBool(4)

    def setIsSeparator(self, value):
        self._setBool(4, value)
        return

    def getId(self):
        return self._getNumber(5)

    def setId(self, value):
        self._setNumber(5, value)
        return

    def getSubItemsCount(self):
        return self._getNumber(6)

    def setSubItemsCount(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(ContextMenuItemModel, self)._initialize()
        self._addViewModelProperty(b'subItemsList', ListModel())
        self._addResourceProperty(b'label', R.invalid())
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'isEnabled', True)
        self._addBoolProperty(b'isSeparator', False)
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'subItemsCount', 0)
        return
