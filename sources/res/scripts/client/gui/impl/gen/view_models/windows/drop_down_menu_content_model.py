from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class DropDownMenuContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DropDownMenuContentModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def dropDownList(self):
        return self._getViewModel(0)

    @staticmethod
    def getDropDownListType():
        return ListModel

    def getListItemRenderer(self):
        return self._getString(1)

    def setListItemRenderer(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(DropDownMenuContentModel, self)._initialize()
        self._addViewModelProperty(b'dropDownList', ListModel())
        self._addStringProperty(b'listItemRenderer', b'')
        return
