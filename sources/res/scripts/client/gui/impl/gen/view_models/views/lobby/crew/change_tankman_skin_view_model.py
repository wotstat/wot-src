from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_data_card_model import PersonalDataCardModel

class ChangeTankmanSkinViewModel(ViewModel):
    __slots__ = (b'onCardSelected', b'onNewCardViewed', b'onResetFilters', b'onViewClose')

    def __init__(self, properties=3, commands=4):
        super(ChangeTankmanSkinViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCardsLocked(self):
        return self._getBool(0)

    def setIsCardsLocked(self, value):
        self._setBool(0, value)
        return

    def getNation(self):
        return self._getString(1)

    def setNation(self, value):
        self._setString(1, value)
        return

    def getCardList(self):
        return self._getArray(2)

    def setCardList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getCardListType():
        return PersonalDataCardModel

    def _initialize(self):
        super(ChangeTankmanSkinViewModel, self)._initialize()
        self._addBoolProperty(b'isCardsLocked', False)
        self._addStringProperty(b'nation', b'')
        self._addArrayProperty(b'cardList', Array())
        self.onCardSelected = self._addCommand(b'onCardSelected')
        self.onNewCardViewed = self._addCommand(b'onNewCardViewed')
        self.onResetFilters = self._addCommand(b'onResetFilters')
        self.onViewClose = self._addCommand(b'onViewClose')
        return
