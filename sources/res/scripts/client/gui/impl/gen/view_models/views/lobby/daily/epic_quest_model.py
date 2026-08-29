from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class EpicQuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(EpicQuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def getCurrent(self):
        return self._getNumber(2)

    def setCurrent(self, value):
        self._setNumber(2, value)
        return

    def getTotal(self):
        return self._getNumber(3)

    def setTotal(self, value):
        self._setNumber(3, value)
        return

    def getEarned(self):
        return self._getNumber(4)

    def setEarned(self, value):
        self._setNumber(4, value)
        return

    def getCountDown(self):
        return self._getNumber(5)

    def setCountDown(self, value):
        self._setNumber(5, value)
        return

    def getBonuses(self):
        return self._getArray(6)

    def setBonuses(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getIsEnabled(self):
        return self._getBool(7)

    def setIsEnabled(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(EpicQuestModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'current', 0)
        self._addNumberProperty(b'total', 0)
        self._addNumberProperty(b'earned', 0)
        self._addNumberProperty(b'countDown', 0)
        self._addArrayProperty(b'bonuses', Array())
        self._addBoolProperty(b'isEnabled', False)
        return
