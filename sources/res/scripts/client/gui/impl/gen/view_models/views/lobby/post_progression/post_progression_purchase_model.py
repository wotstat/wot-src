from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel
from gui.impl.gen.view_models.common.price_model import PriceModel

class PostProgressionPurchaseModel(ViewModel):
    __slots__ = (b'onPurchaseClick',)

    def __init__(self, properties=6, commands=1):
        super(PostProgressionPurchaseModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def modificationBonuses(self):
        return self._getViewModel(0)

    @staticmethod
    def getModificationBonusesType():
        return BonusesModel

    @property
    def price(self):
        return self._getViewModel(1)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getCanPurchase(self):
        return self._getBool(2)

    def setCanPurchase(self, value):
        self._setBool(2, value)
        return

    def getPurchasedSingleStepIds(self):
        return self._getArray(3)

    def setPurchasedSingleStepIds(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getPurchasedSingleStepIdsType():
        return int

    def getPurchasedFeatureStepIds(self):
        return self._getArray(4)

    def setPurchasedFeatureStepIds(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getPurchasedFeatureStepIdsType():
        return int

    def getUnlockedMultiStepIds(self):
        return self._getArray(5)

    def setUnlockedMultiStepIds(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getUnlockedMultiStepIdsType():
        return int

    def _initialize(self):
        super(PostProgressionPurchaseModel, self)._initialize()
        self._addViewModelProperty(b'modificationBonuses', BonusesModel())
        self._addViewModelProperty(b'price', PriceModel())
        self._addBoolProperty(b'canPurchase', True)
        self._addArrayProperty(b'purchasedSingleStepIds', Array())
        self._addArrayProperty(b'purchasedFeatureStepIds', Array())
        self._addArrayProperty(b'unlockedMultiStepIds', Array())
        self.onPurchaseClick = self._addCommand(b'onPurchaseClick')
        return
