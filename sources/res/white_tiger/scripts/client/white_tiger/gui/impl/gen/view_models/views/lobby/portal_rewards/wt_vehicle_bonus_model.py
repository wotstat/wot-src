from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class WtVehicleBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(WtVehicleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(7)

    def setType(self, value):
        self._setString(7, value)
        return

    def getLevel(self):
        return self._getNumber(8)

    def setLevel(self, value):
        self._setNumber(8, value)
        return

    def getSpecName(self):
        return self._getString(9)

    def setSpecName(self, value):
        self._setString(9, value)
        return

    def getNation(self):
        return self._getString(10)

    def setNation(self, value):
        self._setString(10, value)
        return

    def getIsElite(self):
        return self._getBool(11)

    def setIsElite(self, value):
        self._setBool(11, value)
        return

    def getIntCD(self):
        return self._getNumber(12)

    def setIntCD(self, value):
        self._setNumber(12, value)
        return

    def getRentBattles(self):
        return self._getNumber(13)

    def setRentBattles(self, value):
        self._setNumber(13, value)
        return

    def _initialize(self):
        super(WtVehicleBonusModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'specName', b'')
        self._addStringProperty(b'nation', b'')
        self._addBoolProperty(b'isElite', False)
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'rentBattles', 0)
        return
