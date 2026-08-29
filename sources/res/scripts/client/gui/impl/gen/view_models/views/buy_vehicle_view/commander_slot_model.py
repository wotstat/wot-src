from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class CommanderSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(CommanderSlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def actionPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getActionPriceType():
        return ListModel

    def getIdx(self):
        return self._getNumber(1)

    def setIdx(self, value):
        self._setNumber(1, value)
        return

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)
        return

    def getPercents(self):
        return self._getNumber(3)

    def setPercents(self, value):
        self._setNumber(3, value)
        return

    def getTitle(self):
        return self._getString(4)

    def setTitle(self, value):
        self._setString(4, value)
        return

    def getDefPrice(self):
        return self._getString(5)

    def setDefPrice(self, value):
        self._setString(5, value)
        return

    def getIsFree(self):
        return self._getBool(6)

    def setIsFree(self, value):
        self._setBool(6, value)
        return

    def getDiscount(self):
        return self._getNumber(7)

    def setDiscount(self, value):
        self._setNumber(7, value)
        return

    def getSlotIsEnabled(self):
        return self._getBool(8)

    def setSlotIsEnabled(self, value):
        self._setBool(8, value)
        return

    def getIsBootcamp(self):
        return self._getBool(9)

    def setIsBootcamp(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(CommanderSlotModel, self)._initialize()
        self._addViewModelProperty(b'actionPrice', ListModel())
        self._addNumberProperty(b'idx', 0)
        self._addBoolProperty(b'isSelected', False)
        self._addNumberProperty(b'percents', 0)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'defPrice', b'')
        self._addBoolProperty(b'isFree', False)
        self._addNumberProperty(b'discount', -1)
        self._addBoolProperty(b'slotIsEnabled', True)
        self._addBoolProperty(b'isBootcamp', False)
        return
