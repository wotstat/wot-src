from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.missions.epic_quests_bonus_model import EpicQuestsBonusModel

class EpicQuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(EpicQuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getCurrent(self):
        return self._getNumber(1)

    def setCurrent(self, value):
        self._setNumber(1, value)
        return

    def getTotal(self):
        return self._getNumber(2)

    def setTotal(self, value):
        self._setNumber(2, value)
        return

    def getEarned(self):
        return self._getNumber(3)

    def setEarned(self, value):
        self._setNumber(3, value)
        return

    def getBonuses(self):
        return self._getArray(4)

    def setBonuses(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getBonusesType():
        return EpicQuestsBonusModel

    def getIsEnabled(self):
        return self._getBool(5)

    def setIsEnabled(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(EpicQuestModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'current', 0)
        self._addNumberProperty(b'total', 0)
        self._addNumberProperty(b'earned', 0)
        self._addArrayProperty(b'bonuses', Array())
        self._addBoolProperty(b'isEnabled', False)
        return
