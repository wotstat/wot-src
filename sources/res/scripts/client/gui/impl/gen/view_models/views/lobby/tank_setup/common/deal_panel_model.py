from gui.impl.gen.view_models.common.price_model import PriceModel

class DealPanelModel(PriceModel):
    __slots__ = (b'onDealConfirmed', b'onDealCancelled', b'onAutoRenewalChanged')
    GENERAL = b'general'
    REPAIR = b'repair'

    def __init__(self, properties=13, commands=3):
        super(DealPanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getDealType(self):
        return self._getString(4)

    def setDealType(self, value):
        self._setString(4, value)
        return

    def getCanAccept(self):
        return self._getBool(5)

    def setCanAccept(self, value):
        self._setBool(5, value)
        return

    def getCanCancel(self):
        return self._getBool(6)

    def setCanCancel(self, value):
        self._setBool(6, value)
        return

    def getIsAutoRenewalEnabled(self):
        return self._getBool(7)

    def setIsAutoRenewalEnabled(self, value):
        self._setBool(7, value)
        return

    def getIsDisabled(self):
        return self._getBool(8)

    def setIsDisabled(self, value):
        self._setBool(8, value)
        return

    def getTotalItemsInStorage(self):
        return self._getNumber(9)

    def setTotalItemsInStorage(self, value):
        self._setNumber(9, value)
        return

    def getShowEliteXp(self):
        return self._getBool(10)

    def setShowEliteXp(self, value):
        self._setBool(10, value)
        return

    def getDemountKitsCount(self):
        return self._getNumber(11)

    def setDemountKitsCount(self, value):
        self._setNumber(11, value)
        return

    def getTotalItemsInstalled(self):
        return self._getNumber(12)

    def setTotalItemsInstalled(self, value):
        self._setNumber(12, value)
        return

    def _initialize(self):
        super(DealPanelModel, self)._initialize()
        self._addStringProperty(b'dealType', b'')
        self._addBoolProperty(b'canAccept', False)
        self._addBoolProperty(b'canCancel', True)
        self._addBoolProperty(b'isAutoRenewalEnabled', False)
        self._addBoolProperty(b'isDisabled', False)
        self._addNumberProperty(b'totalItemsInStorage', 0)
        self._addBoolProperty(b'showEliteXp', False)
        self._addNumberProperty(b'demountKitsCount', 0)
        self._addNumberProperty(b'totalItemsInstalled', 0)
        self.onDealConfirmed = self._addCommand(b'onDealConfirmed')
        self.onDealCancelled = self._addCommand(b'onDealCancelled')
        self.onAutoRenewalChanged = self._addCommand(b'onAutoRenewalChanged')
        return
