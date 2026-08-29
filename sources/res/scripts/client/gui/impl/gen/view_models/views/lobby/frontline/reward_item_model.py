from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RewardItemModel(BonusModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getBigIcon(self):
        return self._getString(7)

    def setBigIcon(self, value):
        self._setString(7, value)
        return

    def getItem(self):
        return self._getString(8)

    def setItem(self, value):
        self._setString(8, value)
        return

    def getUserName(self):
        return self._getString(9)

    def setUserName(self, value):
        self._setString(9, value)
        return

    def getName(self):
        return self._getString(10)

    def setName(self, value):
        self._setString(10, value)
        return

    def getTooltipId(self):
        return self._getString(11)

    def setTooltipId(self, value):
        self._setString(11, value)
        return

    def getTooltipContentId(self):
        return self._getString(12)

    def setTooltipContentId(self, value):
        self._setString(12, value)
        return

    def getValue(self):
        return self._getString(13)

    def setValue(self, value):
        self._setString(13, value)
        return

    def getOverlayType(self):
        return self._getString(14)

    def setOverlayType(self, value):
        self._setString(14, value)
        return

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty(b'bigIcon', b'')
        self._addStringProperty(b'item', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipContentId', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'overlayType', b'')
        return
