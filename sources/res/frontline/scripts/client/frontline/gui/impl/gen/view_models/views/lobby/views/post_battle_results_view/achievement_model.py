from frameworks.wulf import ViewModel

class AchievementModel(ViewModel):
    __slots__ = ()
    ACHIEVEMENT_LEFT_BLOCK = b'left'
    ACHIEVEMENT_RIGHT_BLOCK = b'right'
    RANK = b'rank'

    def __init__(self, properties=5, commands=0):
        super(AchievementModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getGroupID(self):
        return self._getString(1)

    def setGroupID(self, value):
        self._setString(1, value)
        return

    def getIconName(self):
        return self._getString(2)

    def setIconName(self, value):
        self._setString(2, value)
        return

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)
        return

    def getTooltipArgs(self):
        return self._getString(4)

    def setTooltipArgs(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(AchievementModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'groupID', b'')
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'tooltipArgs', b'')
        return
