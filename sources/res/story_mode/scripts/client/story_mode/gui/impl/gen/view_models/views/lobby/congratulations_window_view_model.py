from frameworks.wulf import ViewModel

class CongratulationsWindowViewModel(ViewModel):
    __slots__ = (b'onClose', b'onLoaded')

    def __init__(self, properties=5, commands=2):
        super(CongratulationsWindowViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCloseVisible(self):
        return self._getBool(0)

    def setIsCloseVisible(self, value):
        self._setBool(0, value)
        return

    def getIsOnboarding(self):
        return self._getBool(1)

    def setIsOnboarding(self, value):
        self._setBool(1, value)
        return

    def getMedalName(self):
        return self._getString(2)

    def setMedalName(self, value):
        self._setString(2, value)
        return

    def getBadgeId(self):
        return self._getNumber(3)

    def setBadgeId(self, value):
        self._setNumber(3, value)
        return

    def getMissionId(self):
        return self._getNumber(4)

    def setMissionId(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(CongratulationsWindowViewModel, self)._initialize()
        self._addBoolProperty(b'isCloseVisible', False)
        self._addBoolProperty(b'isOnboarding', False)
        self._addStringProperty(b'medalName', b'')
        self._addNumberProperty(b'badgeId', 0)
        self._addNumberProperty(b'missionId', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onLoaded = self._addCommand(b'onLoaded')
        return
