from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel

class PreBattleQueueViewModel(SelectableViewModel):
    __slots__ = (b'onExitBattle', b'onEscape')

    def __init__(self, properties=7, commands=4):
        super(PreBattleQueueViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedDifficultyLevel(self):
        return self._getNumber(0)

    def setSelectedDifficultyLevel(self, value):
        self._setNumber(0, value)
        return

    def getIsExitButtonAvailable(self):
        return self._getBool(1)

    def setIsExitButtonAvailable(self, value):
        self._setBool(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getVehicleName(self):
        return self._getString(3)

    def setVehicleName(self, value):
        self._setString(3, value)
        return

    def getTip(self):
        return self._getString(4)

    def setTip(self, value):
        self._setString(4, value)
        return

    def getIsFirstTip(self):
        return self._getBool(5)

    def setIsFirstTip(self, value):
        self._setBool(5, value)
        return

    def getTimerStartTime(self):
        return self._getNumber(6)

    def setTimerStartTime(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(PreBattleQueueViewModel, self)._initialize()
        self._addNumberProperty(b'selectedDifficultyLevel', 0)
        self._addBoolProperty(b'isExitButtonAvailable', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'tip', b'')
        self._addBoolProperty(b'isFirstTip', False)
        self._addNumberProperty(b'timerStartTime', 0)
        self.onExitBattle = self._addCommand(b'onExitBattle')
        self.onEscape = self._addCommand(b'onEscape')
        return
