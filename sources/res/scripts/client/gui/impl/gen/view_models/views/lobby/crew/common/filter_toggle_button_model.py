from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.common.dynamic_tooltip_model import DynamicTooltipModel

class FilterToggleButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FilterToggleButtonModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tooltip(self):
        return self._getViewModel(0)

    @staticmethod
    def getTooltipType():
        return DynamicTooltipModel

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getIsSelected(self):
        return self._getBool(3)

    def setIsSelected(self, value):
        self._setBool(3, value)
        return

    def getCounter(self):
        return self._getNumber(4)

    def setCounter(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(FilterToggleButtonModel, self)._initialize()
        self._addViewModelProperty(b'tooltip', DynamicTooltipModel())
        self._addStringProperty(b'id', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'isSelected', False)
        self._addNumberProperty(b'counter', 0)
        return
