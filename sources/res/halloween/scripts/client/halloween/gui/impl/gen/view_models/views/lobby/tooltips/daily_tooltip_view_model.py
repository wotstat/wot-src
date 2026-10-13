from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class DailyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DailyTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEpicMedal(self):
        return self._getBool(0)

    def setIsEpicMedal(self, value):
        self._setBool(0, value)
        return

    def getResetTime(self):
        return self._getNumber(1)

    def setResetTime(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(DailyTooltipViewModel, self)._initialize()
        self._addBoolProperty(b'isEpicMedal', False)
        self._addNumberProperty(b'resetTime', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addArrayProperty(b'rewards', Array())
        return
