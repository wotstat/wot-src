from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class CrewBookRewardOptionModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(CrewBookRewardOptionModel, self).__init__(properties=properties, commands=commands)
        return

    def getExpBonusValue(self):
        return self._getNumber(7)

    def setExpBonusValue(self, value):
        self._setNumber(7, value)
        return

    def getIcon(self):
        return self._getString(8)

    def setIcon(self, value):
        self._setString(8, value)
        return

    def getDescription(self):
        return self._getString(9)

    def setDescription(self, value):
        self._setString(9, value)
        return

    def getItemID(self):
        return self._getNumber(10)

    def setItemID(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(CrewBookRewardOptionModel, self)._initialize()
        self._addNumberProperty(b'expBonusValue', 0)
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'itemID', 0)
        return
