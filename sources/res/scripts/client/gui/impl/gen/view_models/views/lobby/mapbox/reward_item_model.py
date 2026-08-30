from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RewardItemModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(7)

    def setIcon(self, value):
        self._setString(7, value)
        return

    def getIsOpenable(self):
        return self._getBool(8)

    def setIsOpenable(self, value):
        self._setBool(8, value)
        return

    def getPreviousIcon(self):
        return self._getString(9)

    def setPreviousIcon(self, value):
        self._setString(9, value)
        return

    def getIsSelected(self):
        return self._getBool(10)

    def setIsSelected(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addBoolProperty(b'isOpenable', False)
        self._addStringProperty(b'previousIcon', b'')
        self._addBoolProperty(b'isSelected', False)
        return
