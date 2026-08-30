from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.customization_cart.cart_season_model import CartSeasonModel

class CartSeasonsModel(ViewModel):
    __slots__ = (b'onSelectItem',)

    def __init__(self, properties=3, commands=1):
        super(CartSeasonsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def winter(self):
        return self._getViewModel(0)

    @staticmethod
    def getWinterType():
        return CartSeasonModel

    @property
    def summer(self):
        return self._getViewModel(1)

    @staticmethod
    def getSummerType():
        return CartSeasonModel

    @property
    def desert(self):
        return self._getViewModel(2)

    @staticmethod
    def getDesertType():
        return CartSeasonModel

    def _initialize(self):
        super(CartSeasonsModel, self)._initialize()
        self._addViewModelProperty(b'winter', CartSeasonModel())
        self._addViewModelProperty(b'summer', CartSeasonModel())
        self._addViewModelProperty(b'desert', CartSeasonModel())
        self.onSelectItem = self._addCommand(b'onSelectItem')
        return
