from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.range_model import RangeModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class BarracksViewModel(ViewModel):
    __slots__ = (b'onResetFilters', b'onBuyBerth', b'onTankmanSelected', b'onTankmanRecruit', b'onTankmanDismiss', b'onPlayTankmanVoiceover', b'onTankmanRestore', b'onLoadCards', b'showHangar', b'onTankmanSelectedChange')

    def __init__(self, properties=12, commands=10):
        super(BarracksViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def berthsAmount(self):
        return self._getViewModel(0)

    @staticmethod
    def getBerthsAmountType():
        return RangeModel

    def getItemsAmount(self):
        return self._getNumber(1)

    def setItemsAmount(self, value):
        self._setNumber(1, value)
        return

    def getItemsOffset(self):
        return self._getNumber(2)

    def setItemsOffset(self, value):
        self._setNumber(2, value)
        return

    def getTankmanList(self):
        return self._getArray(3)

    def setTankmanList(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getTankmanListType():
        return TankmanModel

    def getSelectedTankmanList(self):
        return self._getArray(4)

    def setSelectedTankmanList(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getSelectedTankmanListType():
        return int

    def getIsSelectedLimitReached(self):
        return self._getBool(5)

    def setIsSelectedLimitReached(self, value):
        self._setBool(5, value)
        return

    def getIsBerthsOnSale(self):
        return self._getBool(6)

    def setIsBerthsOnSale(self, value):
        self._setBool(6, value)
        return

    def getHasFilters(self):
        return self._getBool(7)

    def setHasFilters(self, value):
        self._setBool(7, value)
        return

    def getHeaderTitle(self):
        return self._getString(8)

    def setHeaderTitle(self, value):
        self._setString(8, value)
        return

    def getIsSelectedMode(self):
        return self._getBool(9)

    def setIsSelectedMode(self, value):
        self._setBool(9, value)
        return

    def getHeadersIndexes(self):
        return self._getArray(10)

    def setHeadersIndexes(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getHeadersIndexesType():
        return int

    def getIsAllTankmanFilter(self):
        return self._getBool(11)

    def setIsAllTankmanFilter(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(BarracksViewModel, self)._initialize()
        self._addViewModelProperty(b'berthsAmount', RangeModel())
        self._addNumberProperty(b'itemsAmount', 0)
        self._addNumberProperty(b'itemsOffset', 0)
        self._addArrayProperty(b'tankmanList', Array())
        self._addArrayProperty(b'selectedTankmanList', Array())
        self._addBoolProperty(b'isSelectedLimitReached', False)
        self._addBoolProperty(b'isBerthsOnSale', False)
        self._addBoolProperty(b'hasFilters', False)
        self._addStringProperty(b'headerTitle', b'')
        self._addBoolProperty(b'isSelectedMode', False)
        self._addArrayProperty(b'headersIndexes', Array())
        self._addBoolProperty(b'isAllTankmanFilter', True)
        self.onResetFilters = self._addCommand(b'onResetFilters')
        self.onBuyBerth = self._addCommand(b'onBuyBerth')
        self.onTankmanSelected = self._addCommand(b'onTankmanSelected')
        self.onTankmanRecruit = self._addCommand(b'onTankmanRecruit')
        self.onTankmanDismiss = self._addCommand(b'onTankmanDismiss')
        self.onPlayTankmanVoiceover = self._addCommand(b'onPlayTankmanVoiceover')
        self.onTankmanRestore = self._addCommand(b'onTankmanRestore')
        self.onLoadCards = self._addCommand(b'onLoadCards')
        self.showHangar = self._addCommand(b'showHangar')
        self.onTankmanSelectedChange = self._addCommand(b'onTankmanSelectedChange')
        return
