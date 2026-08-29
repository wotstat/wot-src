from frameworks.wulf import ViewModel

class PrebattleWindowViewModel(ViewModel):
    __slots__ = (b'onGotoBattle', b'onSkip', b'onLoaded')

    def __init__(self, properties=3, commands=3):
        super(PrebattleWindowViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsLoading(self):
        return self._getBool(0)

    def setIsLoading(self, value):
        self._setBool(0, value)
        return

    def getMissionNumber(self):
        return self._getNumber(1)

    def setMissionNumber(self, value):
        self._setNumber(1, value)
        return

    def getShowSkipButton(self):
        return self._getBool(2)

    def setShowSkipButton(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(PrebattleWindowViewModel, self)._initialize()
        self._addBoolProperty(b'isLoading', False)
        self._addNumberProperty(b'missionNumber', 0)
        self._addBoolProperty(b'showSkipButton', False)
        self.onGotoBattle = self._addCommand(b'onGotoBattle')
        self.onSkip = self._addCommand(b'onSkip')
        self.onLoaded = self._addCommand(b'onLoaded')
        return
