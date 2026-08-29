from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_compound_price_model import UserCompoundPriceModel

class BattlePassBuyConfirmViewModel(ViewModel):
    __slots__ = (b'onCloseClick', b'onBuyClick', b'onShowRewardsClick')

    def __init__(self, properties=5, commands=3):
        super(BattlePassBuyConfirmViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def compoundPrice(self):
        return self._getViewModel(0)

    @staticmethod
    def getCompoundPriceType():
        return UserCompoundPriceModel

    def getPrice(self):
        return self._getNumber(1)

    def setPrice(self, value):
        self._setNumber(1, value)
        return

    def getChapterID(self):
        return self._getNumber(2)

    def setChapterID(self, value):
        self._setNumber(2, value)
        return

    def getIsActive(self):
        return self._getBool(3)

    def setIsActive(self, value):
        self._setBool(3, value)
        return

    def getCompoundPriceDefaultID(self):
        return self._getString(4)

    def setCompoundPriceDefaultID(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(BattlePassBuyConfirmViewModel, self)._initialize()
        self._addViewModelProperty(b'compoundPrice', UserCompoundPriceModel())
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'chapterID', 0)
        self._addBoolProperty(b'isActive', False)
        self._addStringProperty(b'compoundPriceDefaultID', b'')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        self.onBuyClick = self._addCommand(b'onBuyClick')
        self.onShowRewardsClick = self._addCommand(b'onShowRewardsClick')
        return
