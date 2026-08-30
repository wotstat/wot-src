from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.meta_view.pages.yearly_rewards_card_model import YearlyRewardsCardModel

class Rank(IntEnum):
    FIRST = 6
    SECOND = 5
    THIRD = 4
    FOURTH = 3
    FIFTH = 2
    SIXTH = 1


class YearlyRewardsModel(ViewModel):
    __slots__ = ()
    DEFAULT_CARD_INDEX = -1

    def __init__(self, properties=4, commands=0):
        super(YearlyRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getCards(self):
        return self._getArray(0)

    def setCards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCardsType():
        return YearlyRewardsCardModel

    def getCurrentRank(self):
        return Rank(self._getNumber(1))

    def setCurrentRank(self, value):
        self._setNumber(1, value.value)
        return

    def getSeasonPointsReceived(self):
        return self._getBool(2)

    def setSeasonPointsReceived(self, value):
        self._setBool(2, value)
        return

    def getHasDataError(self):
        return self._getBool(3)

    def setHasDataError(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(YearlyRewardsModel, self)._initialize()
        self._addArrayProperty(b'cards', Array())
        self._addNumberProperty(b'currentRank')
        self._addBoolProperty(b'seasonPointsReceived', False)
        self._addBoolProperty(b'hasDataError', False)
        return
