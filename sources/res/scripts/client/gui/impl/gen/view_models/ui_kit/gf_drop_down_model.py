from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.gf_drop_down_item import GfDropDownItem

class GfDropDownModel(ViewModel):
    __slots__ = (b'onChange',)

    def __init__(self, properties=3, commands=1):
        super(GfDropDownModel, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getItemsType():
        return GfDropDownItem

    def getSelected(self):
        return self._getArray(1)

    def setSelected(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSelectedType():
        return unicode

    def getMultiple(self):
        return self._getBool(2)

    def setMultiple(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(GfDropDownModel, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self._addArrayProperty(b'selected', Array())
        self._addBoolProperty(b'multiple', False)
        self.onChange = self._addCommand(b'onChange')
        return
