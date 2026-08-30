from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class TokenBonusModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(TokenBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getUserName(self):
        return self._getString(7)

    def setUserName(self, value):
        self._setString(7, value)
        return

    def getIconSmall(self):
        return self._getString(8)

    def setIconSmall(self, value):
        self._setString(8, value)
        return

    def getIconBig(self):
        return self._getString(9)

    def setIconBig(self, value):
        self._setString(9, value)
        return

    def getIcon(self):
        return self._getString(10)

    def setIcon(self, value):
        self._setString(10, value)
        return

    def _initialize(self):
        super(TokenBonusModel, self)._initialize()
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'iconSmall', b'')
        self._addStringProperty(b'iconBig', b'')
        self._addStringProperty(b'icon', b'')
        return
