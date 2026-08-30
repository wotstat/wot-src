from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel

class StatisticsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(StatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getElite(self):
        return self._getBool(0)

    def setElite(self, value):
        self._setBool(0, value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)
        return

    def getPremium(self):
        return self._getBool(3)

    def setPremium(self, value):
        self._setBool(3, value)
        return

    def getName(self):
        return self._getString(4)

    def setName(self, value):
        self._setString(4, value)
        return

    def getNationId(self):
        return self._getNumber(5)

    def setNationId(self, value):
        self._setNumber(5, value)
        return

    def getRole(self):
        return self._getNumber(6)

    def setRole(self, value):
        self._setNumber(6, value)
        return

    def getRentLeftTime(self):
        return self._getNumber(7)

    def setRentLeftTime(self, value):
        self._setNumber(7, value)
        return

    def getRentLeftBattles(self):
        return self._getNumber(8)

    def setRentLeftBattles(self, value):
        self._setNumber(8, value)
        return

    def getRentLeftWins(self):
        return self._getNumber(9)

    def setRentLeftWins(self, value):
        self._setNumber(9, value)
        return

    def getSlots(self):
        return self._getArray(10)

    def setSlots(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getSlotsType():
        return SlotModel

    def _initialize(self):
        super(StatisticsModel, self)._initialize()
        self._addBoolProperty(b'elite', False)
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'type', b'')
        self._addBoolProperty(b'premium', False)
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'nationId', 0)
        self._addNumberProperty(b'role', 0)
        self._addNumberProperty(b'rentLeftTime', 0)
        self._addNumberProperty(b'rentLeftBattles', 0)
        self._addNumberProperty(b'rentLeftWins', 0)
        self._addArrayProperty(b'slots', Array())
        return
