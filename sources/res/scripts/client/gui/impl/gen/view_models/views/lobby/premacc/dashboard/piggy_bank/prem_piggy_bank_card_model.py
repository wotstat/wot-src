from gui.impl.gen.view_models.views.lobby.premacc.piggybank_base_model import PiggybankBaseModel

class PremPiggyBankCardModel(PiggybankBaseModel):
    __slots__ = (b'onGoToPiggyView',)

    def __init__(self, properties=8, commands=1):
        super(PremPiggyBankCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAvailable(self):
        return self._getBool(6)

    def setIsAvailable(self, value):
        self._setBool(6, value)
        return

    def getIsGoldReserveAvailable(self):
        return self._getBool(7)

    def setIsGoldReserveAvailable(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(PremPiggyBankCardModel, self)._initialize()
        self._addBoolProperty(b'isAvailable', True)
        self._addBoolProperty(b'isGoldReserveAvailable', True)
        self.onGoToPiggyView = self._addCommand(b'onGoToPiggyView')
        return
