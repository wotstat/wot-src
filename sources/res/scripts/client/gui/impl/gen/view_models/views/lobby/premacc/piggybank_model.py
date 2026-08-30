from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.premacc.piggybank_base_model import PiggybankBaseModel

class PiggybankModel(PiggybankBaseModel):
    __slots__ = (b'onPremAccProlong', b'onGoToContentPage', b'onBackBtnClicked')

    def __init__(self, properties=11, commands=3):
        super(PiggybankModel, self).__init__(properties=properties, commands=commands)
        return

    def getPeriodInDays(self):
        return self._getNumber(6)

    def setPeriodInDays(self, value):
        self._setNumber(6, value)
        return

    def getPiggyIsFull(self):
        return self._getBool(7)

    def setPiggyIsFull(self, value):
        self._setBool(7, value)
        return

    def getIsPremUsed(self):
        return self._getBool(8)

    def setIsPremUsed(self, value):
        self._setBool(8, value)
        return

    def getBackBtnLabel(self):
        return self._getResource(9)

    def setBackBtnLabel(self, value):
        self._setResource(9, value)
        return

    def getPercentDiscount(self):
        return self._getNumber(10)

    def setPercentDiscount(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(PiggybankModel, self)._initialize()
        self._addNumberProperty(b'periodInDays', 0)
        self._addBoolProperty(b'piggyIsFull', False)
        self._addBoolProperty(b'isPremUsed', False)
        self._addResourceProperty(b'backBtnLabel', R.invalid())
        self._addNumberProperty(b'percentDiscount', 0)
        self.onPremAccProlong = self._addCommand(b'onPremAccProlong')
        self.onGoToContentPage = self._addCommand(b'onGoToContentPage')
        self.onBackBtnClicked = self._addCommand(b'onBackBtnClicked')
        return
