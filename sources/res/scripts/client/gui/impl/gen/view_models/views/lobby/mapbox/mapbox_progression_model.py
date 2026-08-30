from frameworks.wulf import Array, ViewModel

class MapboxProgressionModel(ViewModel):
    __slots__ = (b'onShowInfo', b'onSelectMapboxBattle', b'onShowSurvey', b'onRemoveBubble', b'onClose', b'onAnimationEnded')

    def __init__(self, properties=14, commands=6):
        super(MapboxProgressionModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsOverlapped(self):
        return self._getBool(0)

    def setIsOverlapped(self, value):
        self._setBool(0, value)
        return

    def getIsDataSynced(self):
        return self._getBool(1)

    def setIsDataSynced(self, value):
        self._setBool(1, value)
        return

    def getIsMapboxModeSelected(self):
        return self._getBool(2)

    def setIsMapboxModeSelected(self, value):
        self._setBool(2, value)
        return

    def getIsError(self):
        return self._getBool(3)

    def setIsError(self, value):
        self._setBool(3, value)
        return

    def getHasInfoPage(self):
        return self._getBool(4)

    def setHasInfoPage(self, value):
        self._setBool(4, value)
        return

    def getMaps(self):
        return self._getArray(5)

    def setMaps(self, value):
        self._setArray(5, value)
        return

    def getProgressionRewards(self):
        return self._getArray(6)

    def setProgressionRewards(self, value):
        self._setArray(6, value)
        return

    def getRating(self):
        return self._getNumber(7)

    def setRating(self, value):
        self._setNumber(7, value)
        return

    def getPrevTotalBattlesPlayed(self):
        return self._getNumber(8)

    def setPrevTotalBattlesPlayed(self, value):
        self._setNumber(8, value)
        return

    def getTotalBattlesPlayed(self):
        return self._getNumber(9)

    def setTotalBattlesPlayed(self, value):
        self._setNumber(9, value)
        return

    def getTotalBattles(self):
        return self._getNumber(10)

    def setTotalBattles(self, value):
        self._setNumber(10, value)
        return

    def getStartEvent(self):
        return self._getNumber(11)

    def setStartEvent(self, value):
        self._setNumber(11, value)
        return

    def getEndEvent(self):
        return self._getNumber(12)

    def setEndEvent(self, value):
        self._setNumber(12, value)
        return

    def getTimeTillProgressionRestart(self):
        return self._getString(13)

    def setTimeTillProgressionRestart(self, value):
        self._setString(13, value)
        return

    def _initialize(self):
        super(MapboxProgressionModel, self)._initialize()
        self._addBoolProperty(b'isOverlapped', False)
        self._addBoolProperty(b'isDataSynced', False)
        self._addBoolProperty(b'isMapboxModeSelected', False)
        self._addBoolProperty(b'isError', False)
        self._addBoolProperty(b'hasInfoPage', False)
        self._addArrayProperty(b'maps', Array())
        self._addArrayProperty(b'progressionRewards', Array())
        self._addNumberProperty(b'rating', 0)
        self._addNumberProperty(b'prevTotalBattlesPlayed', 0)
        self._addNumberProperty(b'totalBattlesPlayed', 0)
        self._addNumberProperty(b'totalBattles', 0)
        self._addNumberProperty(b'startEvent', 0)
        self._addNumberProperty(b'endEvent', 0)
        self._addStringProperty(b'timeTillProgressionRestart', b'')
        self.onShowInfo = self._addCommand(b'onShowInfo')
        self.onSelectMapboxBattle = self._addCommand(b'onSelectMapboxBattle')
        self.onShowSurvey = self._addCommand(b'onShowSurvey')
        self.onRemoveBubble = self._addCommand(b'onRemoveBubble')
        self.onClose = self._addCommand(b'onClose')
        self.onAnimationEnded = self._addCommand(b'onAnimationEnded')
        return
