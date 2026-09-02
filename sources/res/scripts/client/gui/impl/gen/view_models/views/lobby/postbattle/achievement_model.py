from frameworks.wulf import ViewModel

class AchievementModel(ViewModel):
    __slots__ = ()
    ACHIEVEMENT_TOOLTIP = b'achievementTooltip'
    ACHIEVEMENT_LEFT_BLOCK = b'left'
    ACHIEVEMENT_RIGHT_BLOCK = b'right'
    MARKS_ON_GUN = b'marksOnGun'

    def __init__(self, properties=6, commands=0):
        super(AchievementModel, self).__init__(properties=properties, commands=commands)
        return

    def getAchievementID(self):
        return self._getNumber(0)

    def setAchievementID(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getIsPersonal(self):
        return self._getBool(2)

    def setIsPersonal(self, value):
        self._setBool(2, value)
        return

    def getGroupID(self):
        return self._getString(3)

    def setGroupID(self, value):
        self._setString(3, value)
        return

    def getIsEpic(self):
        return self._getBool(4)

    def setIsEpic(self, value):
        self._setBool(4, value)
        return

    def getIconName(self):
        return self._getString(5)

    def setIconName(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(AchievementModel, self)._initialize()
        self._addNumberProperty(b'achievementID', 0)
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isPersonal', False)
        self._addStringProperty(b'groupID', b'')
        self._addBoolProperty(b'isEpic', False)
        self._addStringProperty(b'iconName', b'')
        return
