from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class AdditionalEquipmentSlotModel(ViewModel):
    __slots__ = (b'onSelectedChange',)

    def __init__(self, properties=4, commands=1):
        super(AdditionalEquipmentSlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def actionPrices(self):
        return self._getViewModel(0)

    @staticmethod
    def getActionPricesType():
        return ListModel

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)
        return

    def getIsDisabledTooltip(self):
        return self._getBool(3)

    def setIsDisabledTooltip(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(AdditionalEquipmentSlotModel, self)._initialize()
        self._addViewModelProperty(b'actionPrices', ListModel())
        self._addBoolProperty(b'isEnabled', False)
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isDisabledTooltip', False)
        self.onSelectedChange = self._addCommand(b'onSelectedChange')
        return
