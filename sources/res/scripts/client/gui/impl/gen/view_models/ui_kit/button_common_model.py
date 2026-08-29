from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.counter_model import CounterModel

class ButtonCommonModel(ViewModel):
    __slots__ = (b'onClicked', b'onSelected')

    def __init__(self, properties=6, commands=2):
        super(ButtonCommonModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def Counter(self):
        return self._getViewModel(0)

    @staticmethod
    def getCounterType():
        return CounterModel

    def getLabel(self):
        return self._getResource(1)

    def setLabel(self, value):
        self._setResource(1, value)
        return

    def getLabelString(self):
        return self._getString(2)

    def setLabelString(self, value):
        self._setString(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsSelected(self):
        return self._getBool(4)

    def setIsSelected(self, value):
        self._setBool(4, value)
        return

    def getIsVisible(self):
        return self._getBool(5)

    def setIsVisible(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(ButtonCommonModel, self)._initialize()
        self._addViewModelProperty(b'Counter', CounterModel())
        self._addResourceProperty(b'label', R.invalid())
        self._addStringProperty(b'labelString', b'')
        self._addBoolProperty(b'isEnabled', True)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isVisible', True)
        self.onClicked = self._addCommand(b'onClicked')
        self.onSelected = self._addCommand(b'onSelected')
        return
