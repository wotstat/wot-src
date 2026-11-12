from gui.impl.gen.view_models.views.lobby.hangar.header_widget_view_model import HeaderWidgetViewModel

class TankAcademyEntryPointViewModel(HeaderWidgetViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=9, commands=2):
        super(TankAcademyEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsSecondaryEntry(self):
        return self._getBool(0)

    def setIsSecondaryEntry(self, value):
        self._setBool(0, value)
        return

    def getIsMainViewVisited(self):
        return self._getBool(1)

    def setIsMainViewVisited(self, value):
        self._setBool(1, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(2)

    def setCurrentProgress(self, value):
        self._setNumber(2, value)
        return

    def getMaxProgress(self):
        return self._getNumber(3)

    def setMaxProgress(self, value):
        self._setNumber(3, value)
        return

    def getQuestNumber(self):
        return self._getNumber(4)

    def setQuestNumber(self, value):
        self._setNumber(4, value)
        return

    def getIsCompleted(self):
        return self._getBool(5)

    def setIsCompleted(self, value):
        self._setBool(5, value)
        return

    def getIsPaused(self):
        return self._getBool(6)

    def setIsPaused(self, value):
        self._setBool(6, value)
        return

    def getUnobtainedVehiclesCount(self):
        return self._getNumber(7)

    def setUnobtainedVehiclesCount(self, value):
        self._setNumber(7, value)
        return

    def getEndDate(self):
        return self._getNumber(8)

    def setEndDate(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(TankAcademyEntryPointViewModel, self)._initialize()
        self._addBoolProperty(b'isSecondaryEntry', False)
        self._addBoolProperty(b'isMainViewVisited', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'maxProgress', 0)
        self._addNumberProperty(b'questNumber', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isPaused', False)
        self._addNumberProperty(b'unobtainedVehiclesCount', 0)
        self._addNumberProperty(b'endDate', 0)
        self.onClick = self._addCommand(b'onClick')
        return
