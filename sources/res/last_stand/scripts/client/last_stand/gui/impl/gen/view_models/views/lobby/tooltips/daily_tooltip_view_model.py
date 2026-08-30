from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class DailyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(DailyTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getResetTime(self):
        return self._getNumber(0)

    def setResetTime(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getCompleted(self):
        return self._getBool(3)

    def setCompleted(self, value):
        self._setBool(3, value)
        return

    def getAllDailyCompleted(self):
        return self._getBool(4)

    def setAllDailyCompleted(self, value):
        self._setBool(4, value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(DailyTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'resetTime', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'completed', False)
        self._addBoolProperty(b'allDailyCompleted', False)
        self._addArrayProperty(b'rewards', Array())
        return
