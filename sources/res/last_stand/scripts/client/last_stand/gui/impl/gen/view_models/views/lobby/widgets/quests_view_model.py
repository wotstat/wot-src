from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class QuestsViewModel(ViewModel):
    __slots__ = (b'onClick', b'onMarkAsViewed')

    def __init__(self, properties=13, commands=2):
        super(QuestsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getConditionName(self):
        return self._getString(1)

    def setConditionName(self, value):
        self._setString(1, value)
        return

    def getResetTime(self):
        return self._getNumber(2)

    def setResetTime(self, value):
        self._setNumber(2, value)
        return

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)
        return

    def getDescription(self):
        return self._getString(4)

    def setDescription(self, value):
        self._setString(4, value)
        return

    def getIsCompleted(self):
        return self._getBool(5)

    def setIsCompleted(self, value):
        self._setBool(5, value)
        return

    def getIsHidden(self):
        return self._getBool(6)

    def setIsHidden(self, value):
        self._setBool(6, value)
        return

    def getAllDailyCompleted(self):
        return self._getBool(7)

    def setAllDailyCompleted(self, value):
        self._setBool(7, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(8)

    def setCurrentProgress(self, value):
        self._setNumber(8, value)
        return

    def getMaximumProgress(self):
        return self._getNumber(9)

    def setMaximumProgress(self, value):
        self._setNumber(9, value)
        return

    def getEarned(self):
        return self._getNumber(10)

    def setEarned(self, value):
        self._setNumber(10, value)
        return

    def getAnimateCompletion(self):
        return self._getBool(11)

    def setAnimateCompletion(self, value):
        self._setBool(11, value)
        return

    def getBonuses(self):
        return self._getArray(12)

    def setBonuses(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusItemViewModel

    def _initialize(self):
        super(QuestsViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'conditionName', b'')
        self._addNumberProperty(b'resetTime', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isHidden', False)
        self._addBoolProperty(b'allDailyCompleted', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'maximumProgress', 0)
        self._addNumberProperty(b'earned', 0)
        self._addBoolProperty(b'animateCompletion', False)
        self._addArrayProperty(b'bonuses', Array())
        self.onClick = self._addCommand(b'onClick')
        self.onMarkAsViewed = self._addCommand(b'onMarkAsViewed')
        return
