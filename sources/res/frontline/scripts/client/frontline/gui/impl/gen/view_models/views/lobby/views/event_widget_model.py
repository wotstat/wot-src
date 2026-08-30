from frameworks.wulf import ViewModel

class EventWidgetModel(ViewModel):
    __slots__ = (b'goToProgressionScreen', b'goToCombatReservesScreen', b'goToSpecialVehicleRentScreen')

    def __init__(self, properties=12, commands=3):
        super(EventWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getTotalProgress(self):
        return self._getNumber(0)

    def setTotalProgress(self, value):
        self._setNumber(0, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(1)

    def setCurrentProgress(self, value):
        self._setNumber(1, value)
        return

    def getCurrentTier(self):
        return self._getNumber(2)

    def setCurrentTier(self, value):
        self._setNumber(2, value)
        return

    def getRewardsHash(self):
        return self._getNumber(3)

    def setRewardsHash(self, value):
        self._setNumber(3, value)
        return

    def getLastSeenRewardsHash(self):
        return self._getNumber(4)

    def setLastSeenRewardsHash(self, value):
        self._setNumber(4, value)
        return

    def getIsRentHighlighted(self):
        return self._getBool(5)

    def setIsRentHighlighted(self, value):
        self._setBool(5, value)
        return

    def getIsCurrentCycleActive(self):
        return self._getBool(6)

    def setIsCurrentCycleActive(self, value):
        self._setBool(6, value)
        return

    def getModeState(self):
        return self._getString(7)

    def setModeState(self, value):
        self._setString(7, value)
        return

    def getRentalVehicleLevel(self):
        return self._getString(8)

    def setRentalVehicleLevel(self, value):
        self._setString(8, value)
        return

    def getCombatReservesPoints(self):
        return self._getNumber(9)

    def setCombatReservesPoints(self, value):
        self._setNumber(9, value)
        return

    def getIsMaxLevel(self):
        return self._getBool(10)

    def setIsMaxLevel(self, value):
        self._setBool(10, value)
        return

    def getIsSelectedSuitableVehicle(self):
        return self._getBool(11)

    def setIsSelectedSuitableVehicle(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(EventWidgetModel, self)._initialize()
        self._addNumberProperty(b'totalProgress', 0)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'currentTier', 0)
        self._addNumberProperty(b'rewardsHash', 0)
        self._addNumberProperty(b'lastSeenRewardsHash', 0)
        self._addBoolProperty(b'isRentHighlighted', False)
        self._addBoolProperty(b'isCurrentCycleActive', False)
        self._addStringProperty(b'modeState', b'')
        self._addStringProperty(b'rentalVehicleLevel', b'')
        self._addNumberProperty(b'combatReservesPoints', 0)
        self._addBoolProperty(b'isMaxLevel', False)
        self._addBoolProperty(b'isSelectedSuitableVehicle', False)
        self.goToProgressionScreen = self._addCommand(b'goToProgressionScreen')
        self.goToCombatReservesScreen = self._addCommand(b'goToCombatReservesScreen')
        self.goToSpecialVehicleRentScreen = self._addCommand(b'goToSpecialVehicleRentScreen')
        return
