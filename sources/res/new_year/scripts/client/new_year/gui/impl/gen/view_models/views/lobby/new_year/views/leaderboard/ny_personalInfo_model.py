from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class NyPersonalinfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(NyPersonalinfoModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getScore(self):
        return self._getNumber(1)

    def setScore(self, value):
        self._setNumber(1, value)
        return

    def getTop(self):
        return self._getNumber(2)

    def setTop(self, value):
        self._setNumber(2, value)
        return

    def getPosition(self):
        return self._getNumber(3)

    def setPosition(self, value):
        self._setNumber(3, value)
        return

    def getNextTopPoints(self):
        return self._getNumber(4)

    def setNextTopPoints(self, value):
        self._setNumber(4, value)
        return

    def getOpponentPoints(self):
        return self._getNumber(5)

    def setOpponentPoints(self, value):
        self._setNumber(5, value)
        return

    def getFromTimestamp(self):
        return self._getNumber(6)

    def setFromTimestamp(self, value):
        self._setNumber(6, value)
        return

    def getToTimestamp(self):
        return self._getNumber(7)

    def setToTimestamp(self, value):
        self._setNumber(7, value)
        return

    def getIsFinal(self):
        return self._getBool(8)

    def setIsFinal(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(NyPersonalinfoModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addNumberProperty(b'score', 0)
        self._addNumberProperty(b'top', 0)
        self._addNumberProperty(b'position', 0)
        self._addNumberProperty(b'nextTopPoints', 0)
        self._addNumberProperty(b'opponentPoints', 0)
        self._addNumberProperty(b'fromTimestamp', 0)
        self._addNumberProperty(b'toTimestamp', 0)
        self._addBoolProperty(b'isFinal', False)
        return
