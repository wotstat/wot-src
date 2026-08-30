from frameworks.wulf import ViewModel

class PremiumShopModel(ViewModel):
    __slots__ = (b'onOpenExternalPremiumShop',)

    def __init__(self, properties=1, commands=1):
        super(PremiumShopModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsPremiumShop(self):
        return self._getBool(0)

    def setIsPremiumShop(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(PremiumShopModel, self)._initialize()
        self._addBoolProperty(b'isPremiumShop', False)
        self.onOpenExternalPremiumShop = self._addCommand(b'onOpenExternalPremiumShop')
        return
