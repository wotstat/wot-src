from frameworks.wulf import Array, ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_quest_card_model import FunRandomQuestCardModel

class FunRandomProgressionCondition(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(FunRandomProgressionCondition, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentPoints(self):
        return self._getNumber(0)

    def setCurrentPoints(self, value):
        self._setNumber(0, value)
        return

    def getPrevPoints(self):
        return self._getNumber(1)

    def setPrevPoints(self, value):
        self._setNumber(1, value)
        return

    def getMaximumPoints(self):
        return self._getNumber(2)

    def setMaximumPoints(self, value):
        self._setNumber(2, value)
        return

    def getTitle(self):
        return self._getString(3)

    def setTitle(self, value):
        self._setString(3, value)
        return

    def getText(self):
        return self._getString(4)

    def setText(self, value):
        self._setString(4, value)
        return

    def getConditionIcon(self):
        return self._getString(5)

    def setConditionIcon(self, value):
        self._setString(5, value)
        return

    def getStatusTimer(self):
        return self._getNumber(6)

    def setStatusTimer(self, value):
        self._setNumber(6, value)
        return

    def getConditions(self):
        return self._getArray(7)

    def setConditions(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getConditionsType():
        return FunRandomQuestCardModel

    def _initialize(self):
        super(FunRandomProgressionCondition, self)._initialize()
        self._addNumberProperty(b'currentPoints', -1)
        self._addNumberProperty(b'prevPoints', -1)
        self._addNumberProperty(b'maximumPoints', -1)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'conditionIcon', b'')
        self._addNumberProperty(b'statusTimer', -1)
        self._addArrayProperty(b'conditions', Array())
        return
