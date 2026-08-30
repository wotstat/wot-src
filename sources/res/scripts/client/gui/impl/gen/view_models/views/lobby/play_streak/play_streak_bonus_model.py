from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class PlayStreakBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(PlayStreakBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehCD(self):
        return self._getNumber(7)

    def setVehCD(self, value):
        self._setNumber(7, value)
        return

    def getVehType(self):
        return self._getString(8)

    def setVehType(self, value):
        self._setString(8, value)
        return

    def getLevel(self):
        return self._getNumber(9)

    def setLevel(self, value):
        self._setNumber(9, value)
        return

    def getNation(self):
        return self._getString(10)

    def setNation(self, value):
        self._setString(10, value)
        return

    def getVehName(self):
        return self._getString(11)

    def setVehName(self, value):
        self._setString(11, value)
        return

    def getIsElite(self):
        return self._getBool(12)

    def setIsElite(self, value):
        self._setBool(12, value)
        return

    def _initialize(self):
        super(PlayStreakBonusModel, self)._initialize()
        self._addNumberProperty(b'vehCD', 0)
        self._addStringProperty(b'vehType', b'')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'vehName', b'')
        self._addBoolProperty(b'isElite', False)
        return
