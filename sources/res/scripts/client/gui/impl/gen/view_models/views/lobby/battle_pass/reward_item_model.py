from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RewardItemModel(BonusModel):
    __slots__ = ()
    SIZE_ADAPTIVE = 0
    SIZE_SMALL = 1
    SIZE_BIG = 2

    def __init__(self, properties=15, commands=0):
        super(RewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getItem(self):
        return self._getString(7)

    def setItem(self, value):
        self._setString(7, value)
        return

    def getUserName(self):
        return self._getString(8)

    def setUserName(self, value):
        self._setString(8, value)
        return

    def getIcon(self):
        return self._getString(9)

    def setIcon(self, value):
        self._setString(9, value)
        return

    def getType(self):
        return self._getString(10)

    def setType(self, value):
        self._setString(10, value)
        return

    def getBigIcon(self):
        return self._getString(11)

    def setBigIcon(self, value):
        self._setString(11, value)
        return

    def getOverlayType(self):
        return self._getString(12)

    def setOverlayType(self, value):
        self._setString(12, value)
        return

    def getIsCollectionEntity(self):
        return self._getBool(13)

    def setIsCollectionEntity(self, value):
        self._setBool(13, value)
        return

    def getItemType(self):
        return self._getNumber(14)

    def setItemType(self, value):
        self._setNumber(14, value)
        return

    def _initialize(self):
        super(RewardItemModel, self)._initialize()
        self._addStringProperty(b'item', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'bigIcon', b'')
        self._addStringProperty(b'overlayType', b'')
        self._addBoolProperty(b'isCollectionEntity', False)
        self._addNumberProperty(b'itemType', 0)
        return
