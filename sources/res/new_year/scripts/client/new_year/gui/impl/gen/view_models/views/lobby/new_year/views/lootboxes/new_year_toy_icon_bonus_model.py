from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class NewYearToyIconBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(NewYearToyIconBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getRankIcon(self):
        return self._getString(8)

    def setRankIcon(self, value):
        self._setString(8, value)
        return

    def getRankValue(self):
        return self._getNumber(9)

    def setRankValue(self, value):
        self._setNumber(9, value)
        return

    def getIsMega(self):
        return self._getBool(10)

    def setIsMega(self, value):
        self._setBool(10, value)
        return

    def getToyID(self):
        return self._getNumber(11)

    def setToyID(self, value):
        self._setNumber(11, value)
        return

    def getIsNew(self):
        return self._getBool(12)

    def setIsNew(self, value):
        self._setBool(12, value)
        return

    def getAtmosphereBonus(self):
        return self._getNumber(13)

    def setAtmosphereBonus(self, value):
        self._setNumber(13, value)
        return

    def _initialize(self):
        super(NewYearToyIconBonusModel, self)._initialize()
        self._addStringProperty(b'rankIcon', b'')
        self._addNumberProperty(b'rankValue', 0)
        self._addBoolProperty(b'isMega', False)
        self._addNumberProperty(b'toyID', 0)
        self._addBoolProperty(b'isNew', False)
        self._addNumberProperty(b'atmosphereBonus', 0)
        return
