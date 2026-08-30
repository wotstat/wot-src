from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class BattleMattersEntryTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(BattleMattersEntryTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getCondition(self):
        return self._getString(1)

    def setCondition(self, value):
        self._setString(1, value)
        return

    def getHasToken(self):
        return self._getBool(2)

    def setHasToken(self, value):
        self._setBool(2, value)
        return

    def getIsPaused(self):
        return self._getBool(3)

    def setIsPaused(self, value):
        self._setBool(3, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(4)

    def setCurrentProgress(self, value):
        self._setNumber(4, value)
        return

    def getMaxProgress(self):
        return self._getNumber(5)

    def setMaxProgress(self, value):
        self._setNumber(5, value)
        return

    def getCurrentQuest(self):
        return self._getNumber(6)

    def setCurrentQuest(self, value):
        self._setNumber(6, value)
        return

    def getQuestsCount(self):
        return self._getNumber(7)

    def setQuestsCount(self, value):
        self._setNumber(7, value)
        return

    def getEndDate(self):
        return self._getNumber(8)

    def setEndDate(self, value):
        self._setNumber(8, value)
        return

    def getRewards(self):
        return self._getArray(9)

    def setRewards(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(BattleMattersEntryTooltipViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'condition', b'')
        self._addBoolProperty(b'hasToken', False)
        self._addBoolProperty(b'isPaused', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'maxProgress', 0)
        self._addNumberProperty(b'currentQuest', 0)
        self._addNumberProperty(b'questsCount', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addArrayProperty(b'rewards', Array())
        return
