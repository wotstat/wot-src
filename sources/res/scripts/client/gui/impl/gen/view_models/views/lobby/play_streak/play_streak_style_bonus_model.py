from gui.impl.gen.view_models.views.lobby.play_streak.play_streak_icon_bonus_model import PlayStreakIconBonusModel

class PlayStreakStyleBonusModel(PlayStreakIconBonusModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(PlayStreakStyleBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getStyleID(self):
        return self._getNumber(11)

    def setStyleID(self, value):
        self._setNumber(11, value)
        return

    def getBranchID(self):
        return self._getNumber(12)

    def setBranchID(self, value):
        self._setNumber(12, value)
        return

    def getProgressLevel(self):
        return self._getNumber(13)

    def setProgressLevel(self, value):
        self._setNumber(13, value)
        return

    def getLabel(self):
        return self._getString(14)

    def setLabel(self, value):
        self._setString(14, value)
        return

    def getStyleCD(self):
        return self._getNumber(15)

    def setStyleCD(self, value):
        self._setNumber(15, value)
        return

    def getIcon(self):
        return self._getString(16)

    def setIcon(self, value):
        self._setString(16, value)
        return

    def _initialize(self):
        super(PlayStreakStyleBonusModel, self)._initialize()
        self._addNumberProperty(b'styleID', 0)
        self._addNumberProperty(b'branchID', 0)
        self._addNumberProperty(b'progressLevel', 0)
        self._addStringProperty(b'label', b'')
        self._addNumberProperty(b'styleCD', 0)
        self._addStringProperty(b'icon', b'')
        return
