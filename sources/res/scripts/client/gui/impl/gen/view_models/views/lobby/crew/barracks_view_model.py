from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.range_model import RangeModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class BarracksViewModel(ViewModel):
    __slots__ = (b'onResetFilters', b'onRetireUndertrained', b'onBuyBerth', b'onTankmanSelected', b'onTankmanRecruit', b'onTankmanDismiss', b'onPlayTankmanVoiceover', b'onTankmanRestore', b'onLoadCards', b'showHangar', b'onNewTankmanHovered')

    def __init__(self, properties=9, commands=11):
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

    def getIsBerthsOnSale(self):
        return self._getBool(4)

    def setIsBerthsOnSale(self, value):
        self._setBool(4, value)
        return

    def getIsBannerVisible(self):
        return self._getBool(5)

    def setIsBannerVisible(self, value):
        self._setBool(5, value)
        return

    def getHasFilters(self):
        return self._getBool(6)

    def setHasFilters(self, value):
        self._setBool(6, value)
        return

    def getHasUndertrainedCrewMembers(self):
        return self._getBool(7)

    def setHasUndertrainedCrewMembers(self, value):
        self._setBool(7, value)
        return

    def getIsCleanButtonEnabled(self):
        return self._getBool(8)

    def setIsCleanButtonEnabled(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(BarracksViewModel, self)._initialize()
        self._addViewModelProperty(b'berthsAmount', RangeModel())
        self._addNumberProperty(b'itemsAmount', 0)
        self._addNumberProperty(b'itemsOffset', 0)
        self._addArrayProperty(b'tankmanList', Array())
        self._addBoolProperty(b'isBerthsOnSale', False)
        self._addBoolProperty(b'isBannerVisible', False)
        self._addBoolProperty(b'hasFilters', False)
        self._addBoolProperty(b'hasUndertrainedCrewMembers', False)
        self._addBoolProperty(b'isCleanButtonEnabled', False)
        self.onResetFilters = self._addCommand(b'onResetFilters')
        self.onRetireUndertrained = self._addCommand(b'onRetireUndertrained')
        self.onBuyBerth = self._addCommand(b'onBuyBerth')
        self.onTankmanSelected = self._addCommand(b'onTankmanSelected')
        self.onTankmanRecruit = self._addCommand(b'onTankmanRecruit')
        self.onTankmanDismiss = self._addCommand(b'onTankmanDismiss')
        self.onPlayTankmanVoiceover = self._addCommand(b'onPlayTankmanVoiceover')
        self.onTankmanRestore = self._addCommand(b'onTankmanRestore')
        self.onLoadCards = self._addCommand(b'onLoadCards')
        self.showHangar = self._addCommand(b'showHangar')
        self.onNewTankmanHovered = self._addCommand(b'onNewTankmanHovered')
        return
