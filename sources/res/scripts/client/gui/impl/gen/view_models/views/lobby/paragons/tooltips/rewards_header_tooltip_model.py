from frameworks.wulf import ViewModel

class RewardsHeaderTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RewardsHeaderTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsLevelAchieved(self):
        return self._getBool(0)

    def setIsLevelAchieved(self, value):
        self._setBool(0, value)
        return

    def getIsCurrentLevel(self):
        return self._getBool(1)

    def setIsCurrentLevel(self, value):
        self._setBool(1, value)
        return

    def getIsParagonsPoints(self):
        return self._getBool(2)

    def setIsParagonsPoints(self, value):
        self._setBool(2, value)
        return

    def getHasSelectableRewards(self):
        return self._getBool(3)

    def setHasSelectableRewards(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(RewardsHeaderTooltipModel, self)._initialize()
        self._addBoolProperty(b'isLevelAchieved', False)
        self._addBoolProperty(b'isCurrentLevel', False)
        self._addBoolProperty(b'isParagonsPoints', False)
        self._addBoolProperty(b'hasSelectableRewards', False)
        return
