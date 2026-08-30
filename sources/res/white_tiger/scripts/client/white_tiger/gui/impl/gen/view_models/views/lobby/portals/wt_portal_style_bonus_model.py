from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class WtPortalStyleBonusModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(WtPortalStyleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCollected(self):
        return self._getBool(8)

    def setIsCollected(self, value):
        self._setBool(8, value)
        return

    def getIsCustom(self):
        return self._getBool(9)

    def setIsCustom(self, value):
        self._setBool(9, value)
        return

    def getName(self):
        return self._getString(10)

    def setName(self, value):
        self._setString(10, value)
        return

    def getLabel(self):
        return self._getString(11)

    def setLabel(self, value):
        self._setString(11, value)
        return

    def getStyleProgressionLvl(self):
        return self._getNumber(12)

    def setStyleProgressionLvl(self, value):
        self._setNumber(12, value)
        return

    def getLockStatus(self):
        return self._getBool(13)

    def setLockStatus(self, value):
        self._setBool(13, value)
        return

    def getStyleCD(self):
        return self._getNumber(14)

    def setStyleCD(self, value):
        self._setNumber(14, value)
        return

    def _initialize(self):
        super(WtPortalStyleBonusModel, self)._initialize()
        self._addBoolProperty(b'isCollected', False)
        self._addBoolProperty(b'isCustom', False)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'label', b'')
        self._addNumberProperty(b'styleProgressionLvl', 0)
        self._addBoolProperty(b'lockStatus', False)
        self._addNumberProperty(b'styleCD', 0)
        return
