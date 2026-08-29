from frameworks.wulf import ViewModel

class StrongholdMainWidgetTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(StrongholdMainWidgetTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getSprintType(self):
        return self._getString(0)

    def setSprintType(self, value):
        self._setString(0, value)
        return

    def getSprintNumber(self):
        return self._getNumber(1)

    def setSprintNumber(self, value):
        self._setNumber(1, value)
        return

    def getSprintStartDate(self):
        return self._getString(2)

    def setSprintStartDate(self, value):
        self._setString(2, value)
        return

    def getSprintEndDate(self):
        return self._getString(3)

    def setSprintEndDate(self, value):
        self._setString(3, value)
        return

    def getIsEventActive(self):
        return self._getBool(4)

    def setIsEventActive(self, value):
        self._setBool(4, value)
        return

    def getIsDataAvailable(self):
        return self._getBool(5)

    def setIsDataAvailable(self, value):
        self._setBool(5, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(6)

    def setProgressionLevel(self, value):
        self._setNumber(6, value)
        return

    def getIsInClan(self):
        return self._getBool(7)

    def setIsInClan(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(StrongholdMainWidgetTooltipModel, self)._initialize()
        self._addStringProperty(b'sprintType', b'')
        self._addNumberProperty(b'sprintNumber', 0)
        self._addStringProperty(b'sprintStartDate', b'')
        self._addStringProperty(b'sprintEndDate', b'')
        self._addBoolProperty(b'isEventActive', False)
        self._addBoolProperty(b'isDataAvailable', False)
        self._addNumberProperty(b'progressionLevel', 0)
        self._addBoolProperty(b'isInClan', False)
        return
