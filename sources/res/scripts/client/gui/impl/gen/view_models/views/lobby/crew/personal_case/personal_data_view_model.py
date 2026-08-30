from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_data_card_model import PersonalDataCardModel

class PersonalDataViewModel(ViewModel):
    __slots__ = (b'onCardSelected', b'onNewCardViewed', b'onResetFilters')

    def __init__(self, properties=2, commands=3):
        super(PersonalDataViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCardsLocked(self):
        return self._getBool(0)

    def setIsCardsLocked(self, value):
        self._setBool(0, value)
        return

    def getCardList(self):
        return self._getArray(1)

    def setCardList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getCardListType():
        return PersonalDataCardModel

    def _initialize(self):
        super(PersonalDataViewModel, self)._initialize()
        self._addBoolProperty(b'isCardsLocked', False)
        self._addArrayProperty(b'cardList', Array())
        self.onCardSelected = self._addCommand(b'onCardSelected')
        self.onNewCardViewed = self._addCommand(b'onNewCardViewed')
        self.onResetFilters = self._addCommand(b'onResetFilters')
        return
