from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.select_option_base_item_view_model import SelectOptionBaseItemViewModel

class SelectOptionViewModel(ViewModel):
    __slots__ = (b'onClicked',)

    def __init__(self, properties=3, commands=1):
        super(SelectOptionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getItemsType():
        return SelectOptionBaseItemViewModel

    def getSelectedIndexes(self):
        return self._getArray(1)

    def setSelectedIndexes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSelectedIndexesType():
        return int

    def getMessage(self):
        return self._getString(2)

    def setMessage(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(SelectOptionViewModel, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self._addArrayProperty(b'selectedIndexes', Array())
        self._addStringProperty(b'message', b'')
        self.onClicked = self._addCommand(b'onClicked')
        return
