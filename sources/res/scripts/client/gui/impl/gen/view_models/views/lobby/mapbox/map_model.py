from frameworks.wulf import ViewModel

class MapModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MapModel, self).__init__(properties=properties, commands=commands)
        return

    def getMapName(self):
        return self._getString(0)

    def setMapName(self, value):
        self._setString(0, value)
        return

    def getMapBattles(self):
        return self._getNumber(1)

    def setMapBattles(self, value):
        self._setNumber(1, value)
        return

    def getMapBattlesPlayed(self):
        return self._getNumber(2)

    def setMapBattlesPlayed(self, value):
        self._setNumber(2, value)
        return

    def getMapSurveyPassed(self):
        return self._getBool(3)

    def setMapSurveyPassed(self, value):
        self._setBool(3, value)
        return

    def getIsSurveyAvailable(self):
        return self._getBool(4)

    def setIsSurveyAvailable(self, value):
        self._setBool(4, value)
        return

    def getRating(self):
        return self._getNumber(5)

    def setRating(self, value):
        self._setNumber(5, value)
        return

    def getIsBubble(self):
        return self._getBool(6)

    def setIsBubble(self, value):
        self._setBool(6, value)
        return

    def getIsSpecial(self):
        return self._getBool(7)

    def setIsSpecial(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(MapModel, self)._initialize()
        self._addStringProperty(b'mapName', b'')
        self._addNumberProperty(b'mapBattles', 0)
        self._addNumberProperty(b'mapBattlesPlayed', 0)
        self._addBoolProperty(b'mapSurveyPassed', False)
        self._addBoolProperty(b'isSurveyAvailable', False)
        self._addNumberProperty(b'rating', 0)
        self._addBoolProperty(b'isBubble', False)
        self._addBoolProperty(b'isSpecial', False)
        return
