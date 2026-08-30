from enum import Enum
from frameworks.wulf import Array, ViewModel

class PromoBonus(Enum):
    BONDS = b'bonds'
    COMBAT = b'combat'
    CREDITS = b'credits'
    CREW = b'crew'
    EVENTS = b'events'
    SHOWOFF = b'showoff'


class PromotionModel(ViewModel):
    __slots__ = (b'onChallengeSelect', b'onPurchaseSelect')

    def __init__(self, properties=4, commands=2):
        super(PromotionModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsPromotionEnabled(self):
        return self._getBool(0)

    def setIsPromotionEnabled(self, value):
        self._setBool(0, value)
        return

    def getPromotionBonuses(self):
        return self._getArray(1)

    def setPromotionBonuses(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getPromotionBonusesType():
        return unicode

    def getIsChallengeButtonEnabled(self):
        return self._getBool(2)

    def setIsChallengeButtonEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsPurchaseButtonEnabled(self):
        return self._getBool(3)

    def setIsPurchaseButtonEnabled(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(PromotionModel, self)._initialize()
        self._addBoolProperty(b'isPromotionEnabled', True)
        self._addArrayProperty(b'promotionBonuses', Array())
        self._addBoolProperty(b'isChallengeButtonEnabled', True)
        self._addBoolProperty(b'isPurchaseButtonEnabled', True)
        self.onChallengeSelect = self._addCommand(b'onChallengeSelect')
        self.onPurchaseSelect = self._addCommand(b'onPurchaseSelect')
        return
