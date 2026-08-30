from frameworks.wulf import ViewModel

class CollectiveGoalEntryTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(CollectiveGoalEntryTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getStage(self):
        return self._getNumber(1)

    def setStage(self, value):
        self._setNumber(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(4)

    def setCurrentPoints(self, value):
        self._setNumber(4, value)
        return

    def getTotalPoints(self):
        return self._getNumber(5)

    def setTotalPoints(self, value):
        self._setNumber(5, value)
        return

    def getCaption(self):
        return self._getString(6)

    def setCaption(self, value):
        self._setString(6, value)
        return

    def getEndDate(self):
        return self._getNumber(7)

    def setEndDate(self, value):
        self._setNumber(7, value)
        return

    def getIsFinished(self):
        return self._getBool(8)

    def setIsFinished(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(CollectiveGoalEntryTooltipModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addNumberProperty(b'stage', 0)
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'totalPoints', 0)
        self._addStringProperty(b'caption', b'')
        self._addNumberProperty(b'endDate', 0)
        self._addBoolProperty(b'isFinished', False)
        return
