from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.postbattle.events.base_event_model import BaseEventModel

class EventModel(BaseEventModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=1):
        super(EventModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(2)

    def setState(self, value):
        self._setString(2, value)
        return

    def getStateTitle(self):
        return self._getResource(3)

    def setStateTitle(self, value):
        self._setResource(3, value)
        return

    def getSeparatedStateTitle(self):
        return self._getResource(4)

    def setSeparatedStateTitle(self, value):
        self._setResource(4, value)
        return

    def getDescription(self):
        return self._getString(5)

    def setDescription(self, value):
        self._setString(5, value)
        return

    def getDescriptionIcon(self):
        return self._getResource(6)

    def setDescriptionIcon(self, value):
        self._setResource(6, value)
        return

    def getStageState(self):
        return self._getString(7)

    def setStageState(self, value):
        self._setString(7, value)
        return

    def getRankID(self):
        return self._getNumber(8)

    def setRankID(self, value):
        self._setNumber(8, value)
        return

    def getShieldHP(self):
        return self._getNumber(9)

    def setShieldHP(self, value):
        self._setNumber(9, value)
        return

    def getIsUnburnable(self):
        return self._getBool(10)

    def setIsUnburnable(self, value):
        self._setBool(10, value)
        return

    def getDivisionID(self):
        return self._getNumber(11)

    def setDivisionID(self, value):
        self._setNumber(11, value)
        return

    def getStepsBonusBattles(self):
        return self._getNumber(12)

    def setStepsBonusBattles(self, value):
        self._setNumber(12, value)
        return

    def getEfficiencyBonusBattles(self):
        return self._getNumber(13)

    def setEfficiencyBonusBattles(self, value):
        self._setNumber(13, value)
        return

    def _initialize(self):
        super(EventModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addResourceProperty(b'stateTitle', R.invalid())
        self._addResourceProperty(b'separatedStateTitle', R.invalid())
        self._addStringProperty(b'description', b'')
        self._addResourceProperty(b'descriptionIcon', R.invalid())
        self._addStringProperty(b'stageState', b'')
        self._addNumberProperty(b'rankID', 0)
        self._addNumberProperty(b'shieldHP', 0)
        self._addBoolProperty(b'isUnburnable', False)
        self._addNumberProperty(b'divisionID', 0)
        self._addNumberProperty(b'stepsBonusBattles', 0)
        self._addNumberProperty(b'efficiencyBonusBattles', 0)
        return
