from enum import Enum
from frameworks.wulf import ViewModel

class CardState(Enum):
    ACTIVE = b'active'
    COMPLETED = b'completed'


class FunRandomQuestCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(FunRandomQuestCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return CardState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getCurrentProgress(self):
        return self._getNumber(1)

    def setCurrentProgress(self, value):
        self._setNumber(1, value)
        return

    def getTotalProgress(self):
        return self._getNumber(2)

    def setTotalProgress(self, value):
        self._setNumber(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getQuestCondition(self):
        return self._getString(4)

    def setQuestCondition(self, value):
        self._setString(4, value)
        return

    def getTotalPoints(self):
        return self._getNumber(5)

    def setTotalPoints(self, value):
        self._setNumber(5, value)
        return

    def getMainBonusCount(self):
        return self._getNumber(6)

    def setMainBonusCount(self, value):
        self._setNumber(6, value)
        return

    def getAltBonusCount(self):
        return self._getNumber(7)

    def setAltBonusCount(self, value):
        self._setNumber(7, value)
        return

    def getTriggerId(self):
        return self._getString(8)

    def setTriggerId(self, value):
        self._setString(8, value)
        return

    def getAnimateCompletion(self):
        return self._getBool(9)

    def setAnimateCompletion(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(FunRandomQuestCardModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'questCondition', b'')
        self._addNumberProperty(b'totalPoints', 0)
        self._addNumberProperty(b'mainBonusCount', 0)
        self._addNumberProperty(b'altBonusCount', 0)
        self._addStringProperty(b'triggerId', b'')
        self._addBoolProperty(b'animateCompletion', False)
        return
