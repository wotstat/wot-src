import typing
from frameworks.wulf import Array, ViewModel
T = typing.TypeVar(b'T')

class ListModel(ViewModel, typing.Generic[T]):
    __slots__ = (b'onSelectionChanged', b'onItemClicked')

    def __init__(self, properties=2, commands=2):
        super(ListModel, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getItemsType():
        return T

    def getSelectedIndices(self):
        return self._getArray(1)

    def setSelectedIndices(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSelectedIndicesType():
        return int

    def _initialize(self):
        super(ListModel, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self._addArrayProperty(b'selectedIndices', Array())
        self.onSelectionChanged = self._addCommand(b'onSelectionChanged')
        self.onItemClicked = self._addCommand(b'onItemClicked')
        return
